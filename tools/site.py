"""Construit et contrôle les deux sites Zensical sans outillage d’extraction."""

import argparse
from hashlib import file_digest
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urljoin, urlsplit

LANGS = ("fr", "en")
STAT_PAGES = {"fr": ("Caractéristiques", "caracteristiques"), "en": ("Stats", "stats")}
WIKI_ROUTE = re.compile(r'href="@(wiki|alternate)/(cards/[a-z0-9-]+/|stats/|caracteristiques/)?(?=[#"])')
PAGE = re.compile(r"(fr|en)/(?:(?:skills|cards|constellations)/[a-z0-9][a-z0-9-]*|(?:stats|caracteristiques)/index)\.md")
IMAGE_NAME = r"(constellations|stats|skills|cards)/([0-9a-f]{64})\.png"
ASSET = re.compile(r"public-assets/" + IMAGE_NAME)
GAME_IMAGE = re.compile(r"assets/game/" + IMAGE_NAME)
MARKDOWN_IMAGE = re.compile(r'(!\[[^\]\n]*\]\(|src=")\.\./(public-assets/' + IMAGE_NAME + r')(\)|")')
ASSET_BUDGET = 2 * 1024 * 1024
SKILL_LINK = re.compile(
    r"^- (?:!\[\]\([^\n]+?\) )?\[(.+?)\]\(([a-z0-9-]+\.md)\)(?: · [^\n]+)?$", re.MULTILINE
)
GROUP_LINK = re.compile(r"## !\[\]\(([^)]+)\) \[(.+?)\]\(\.\./(constellations/[a-z]+\.md)\)")
NATIVE_LINK = re.compile(r"### (?:!\[\]\(([^)]+)\) )?\[(.+?)\]\(([a-z0-9-]+\.md)\)")
EDITORIAL = re.compile(r"(fr|en)/(?:index\.md|about\.md|history\.md|notes/[\w-]+\.md)", re.UNICODE)

LABELS = {
    "fr": ("Accueil", "Compétences", "Index des compétences", "Cartes", "À propos", "Historique", "Notes communautaires"),
    "en": ("Home", "Skills", "Skill index", "Cards", "About", "History", "Community notes"),
}


def stamp(path):
    with path.open("rb") as file:
        return {"sha256": file_digest(file, "sha256").hexdigest(), "size": path.stat().st_size}


def files_in(root):
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"Dossier source invalide · {root}")
    files = {}
    for node in root.rglob("*"):
        if node.is_symlink():
            raise ValueError(f"Lien symbolique interdit · {node}")
        if node.is_file():
            files[node.relative_to(root).as_posix()] = node
    return files


def publication(root):
    source = files_in(root / "generated")
    marker = source.pop("publication.json", None)
    if marker is None:
        raise ValueError("Manifeste generated/publication.json absent")
    manifest = json.loads(marker.read_text(encoding="utf-8"))
    expected = manifest["files"]
    if (manifest["schema_version"] != 1 or not re.fullmatch(r"[0-9]+", manifest["steam_build_id"])
            or any(not re.fullmatch(r"[0-9a-f]{64}", manifest[k]) for k in ("snapshot_id", "source_export_id"))
            or set(source) != set(expected) or any(not (PAGE.fullmatch(name) or ASSET.fullmatch(name)) for name in expected)
            or any(f"{lang}/{kind}/index.md" not in source for lang in LANGS for kind in ("skills", "cards"))):
        raise ValueError("Périmètre generated/ incohérent")
    images = {name: expected[name] for name in expected if ASSET.fullmatch(name)}
    if (any(stamp["sha256"] != ASSET.fullmatch(name)[2] for name, stamp in images.items())
            or sum(stamp["size"] for stamp in images.values()) > ASSET_BUDGET
            or len({stamp["sha256"] for stamp in images.values()}) != len(images)):
        raise ValueError("Budget ou empreinte des images publiques incohérents")
    for name, path in source.items():
        if stamp(path) != expected[name]:
            raise ValueError(f"Fichier public altéré · {name}")
    return manifest, source


def shared_path(name):
    return "assets/game/" + name.removeprefix("public-assets/")


def assemble(root, docs, base_url):
    manifest, generated = publication(root)
    community = files_in(root / "editorial")
    overlap = generated.keys() & community.keys()
    if overlap:
        raise ValueError(f"Collision entre generated et editorial · {min(overlap)}")
    if any(not EDITORIAL.fullmatch(name) for name in community):
        raise ValueError("Chemin éditorial inattendu")
    for lang in LANGS:
        for page in ("index", "about", "history"):
            if f"{lang}/{page}.md" not in community:
                raise ValueError(f"Page éditoriale requise · {lang}/{page}.md")
    for name, source in sorted((generated | community).items()):
        if ASSET.fullmatch(name):
            continue
        target = docs / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if name in community:
            value = source.read_text(encoding="utf-8").replace("{{BUILD}}", manifest["steam_build_id"])
            target.write_text(value, encoding="utf-8")
        else:
            def shared_image(match):
                image = match[2]
                if image not in generated:
                    raise ValueError(f"Image Markdown absente du manifeste · {name} · {image}")
                return match[1] + base_url + shared_path(image) + match[5]

            value = source.read_text(encoding="utf-8")
            lang = name.split("/")[0]
            other = "en" if lang == "fr" else "fr"

            def wiki_link(match):
                target_lang, route = ((lang, match[2]) if match[1] == "wiki"
                                      else (other, STAT_PAGES[other][1] + "/"))
                return f'href="{base_url}{target_lang}/{route}'

            value = WIKI_ROUTE.sub(wiki_link, value)
            target.write_text(MARKDOWN_IMAGE.sub(shared_image, value), encoding="utf-8")
    for note in sorted(community):
        web_path = PurePosixPath(note)
        if web_path.parent.name != "notes":
            continue
        lang = web_path.parts[0]
        skill = f"{lang}/skills/{web_path.name}"
        if skill in generated:
            target = docs / skill
            with target.open("a", encoding="utf-8") as stream:
                stream.write(f"\n\n## {LABELS[lang][-1]}\n\n- [{LABELS[lang][-1]}](../notes/{web_path.name})\n")
    return manifest


def quoted(value):
    return json.dumps(value, ensure_ascii=False)


def navigation(docs, lang):
    source = (docs / "skills/index.md").read_text(encoding="utf-8")
    def unescape(title):
        return re.sub(r"\\(.)", r"\1", title)
    groups = []
    entries = groups
    ids, rules = [], []
    grouped = bool(NATIVE_LINK.search(source))
    if grouped:
        for line in source.splitlines():
            if heading := GROUP_LINK.fullmatch(line):
                icon, title, path = heading.groups()
                overview = "Fiche de constellation" if lang == "fr" else "Constellation page"
                entries = [(overview, path)]
                groups.append((unescape(title), entries))
                tail = PurePosixPath(path).stem + "/"
                group = ".md-sidebar--primary li:has(> nav > ul > li > "
                selectors = (
                    f'{group}a[href$="/{tail}"]) > label',
                    f'{group}a[href="{tail}"]) > label',
                    f'html:has(link[rel="canonical"][href$="/constellations/{tail}"]) '
                    f'{group}a[href="././"].md-nav__link--active) > label',
                )
                rules.append((selectors, icon))
            elif line.startswith("## "):
                entries = []
                groups.append((line[3:], entries))
            elif skill := NATIVE_LINK.fullmatch(line):
                icon, title, path = skill.groups()
                entries.append((unescape(title), f"skills/{path}"))
                ids.append(path)
                if icon:
                    tail = path.removesuffix(".md") + "/"
                    selectors = (
                        f'.md-sidebar--primary a[href="{tail}"]',
                        f'.md-sidebar--primary a[href$="/{tail}"]',
                        f'html:has(link[rel="canonical"][href$="/skills/{tail}"]) '
                        '.md-sidebar--primary a[href="././"].md-nav__link--active',
                    )
                    rules.append((selectors, icon))
    else:
        for title, path in SKILL_LINK.findall(source):
            groups.append((unescape(title), f"skills/{path}"))
            ids.append(path)
    expected = {page.name for page in (docs / "skills").glob("*.md")} - {"index.md"}
    if set(ids) != expected or len(ids) != len(expected):
        raise ValueError(f"Navigation des compétences incohérente · {lang}")
    return groups, rules


def config(docs, output, lang, base_url):
    names = LABELS[lang]
    links, icons = navigation(docs, lang)
    css = docs / "styles/wiki.css"
    if icons:
        with css.open("a", encoding="utf-8") as stream:
            for selectors, icon in icons:
                selector = ", ".join(f"{item}::before" for item in selectors)
                stream.write(f"\n{selector} {{ content: ''; background-image: url({quoted(icon)});"
                             " background-size: contain; background-position: center; background-repeat: no-repeat;"
                             " display: inline-block; inline-size: 1rem; block-size: 1rem;"
                             " flex: 0 0 1rem; margin-inline-end: .36rem; vertical-align: middle; }\n")
    items = [(names[0], "index.md"),
             (names[1], [(names[2], "skills/index.md"), *links]),
             (names[3], "cards/index.md"), (names[4], "about.md"), (names[5], "history.md")]

    if (docs / "constellations/index.md").is_file():
        items.insert(3, ("Constellations", "constellations/index.md"))

    stat_title, stat_route = STAT_PAGES[lang]
    if (docs / stat_route / "index.md").is_file():
        items.insert(3, (stat_title, f"{stat_route}/index.md"))

    def nav(rows):
        return "[" + ", ".join(f"{{{quoted(key)} = {nav(value) if isinstance(value, list) else quoted(value)}}}"
                               for key, value in rows) + "]"

    return f"""[project]
site_name = "Trials Survivors Wiki"
site_url = {quoted(base_url + lang + "/")}
docs_dir = {quoted(docs.relative_to(docs.parents[1]).as_posix())}
site_dir = {quoted(output.relative_to(docs.parents[1]).as_posix())}
nav = {nav(items)}
extra_css = ["styles/wiki.css"]
use_directory_urls = true

[project.theme]
language = {quoted(lang)}
font = false
features = ["navigation.sections", "navigation.top", "content.code.copy"]

[[project.theme.palette]]
scheme = "slate"
primary = "custom"
accent = "custom"

[project.extra]
alternate = [
  {{name = "Français", link = {quoted(base_url + "fr/")}, lang = "fr"}},
  {{name = "English", link = {quoted(base_url + "en/")}, lang = "en"}}
]
"""


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.language = None
        self.alternates = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.language = attrs.get("lang")
        self.ids.update(attrs[key] for key in ("id", "name") if attrs.get(key))
        self.links.extend(attrs[key] for key in ("href", "src") if attrs.get(key))
        if attrs.get("hreflang") in LANGS:
            self.alternates.add(attrs["hreflang"])


def validate_html(root, base_url):
    base = urlsplit(base_url)
    files = files_in(root)
    views = {}
    for path, source in files.items():
        if path.endswith(".html"):
            page = Page()
            page.feed(source.read_text(encoding="utf-8"))
            views[path] = page
    total, external = 0, 0
    images = {name: GAME_IMAGE.fullmatch(name)[2] for name in files if GAME_IMAGE.fullmatch(name)}
    used_images = set()
    errors = []
    image_digests = set(images.values())
    for name, path in files.items():
        if name.startswith("assets/game/") and name not in images:
            errors.append(f"{name} · chemin d’image partagée inattendu")
        elif re.fullmatch(r"(fr|en)/public-assets/.+", name):
            errors.append(f"{name} · image copiée dans une langue")
        elif image_digests and path.suffix.lower() == ".png":
            digest = stamp(path)["sha256"]
            if name in images and digest != images[name]:
                errors.append(f"{name} · empreinte d’image partagée invalide")
            elif name not in images and digest in image_digests:
                errors.append(f"{name} · copie d’une image partagée")
    if len(image_digests) != len(images):
        errors.append("Images partagées en double")
    for path, page in views.items():
        if path.startswith(("fr/", "en/")) and path.split("/")[0] != page.language and not path.endswith("404.html"):
            errors.append(f"{path} · langue HTML inattendue")
        for link in set(page.links):
            target = urlsplit(urljoin(base_url + path, link))
            if target.scheme not in ("http", "https") or target.netloc != base.netloc:
                external += 1
                continue
            total += 1
            decoded = unquote(target.path)
            if not decoded.startswith(base.path):
                errors.append(f"{path} · hors du sous-chemin · {link}")
                continue
            local = decoded[len(base.path):]
            normalized = posixpath.normpath(local)
            if not local or local.endswith("/"):
                normalized = (normalized + "/index.html") if local else "index.html"
            if normalized in images:
                used_images.add(normalized)
            if normalized not in files:
                errors.append(f"{path} · cible absente · {link}")
            elif target.fragment and normalized in views and unquote(target.fragment) not in views[normalized].ids:
                errors.append(f"{path} · ancre absente · {link}")
    if images.keys() != used_images:
        errors.append("Images publiques inutilisées")
    for lang in LANGS:
        for path in (f"{lang}/index.html", f"{lang}/skills/index.html", f"{lang}/cards/index.html"):
            if path not in views:
                errors.append(f"Page essentielle manquante · {path}")
        home = views.get(f"{lang}/index.html")
        if home and home.alternates != set(LANGS):
            errors.append(f"Sélecteur de langue incomplet · {lang}")
    if errors:
        raise ValueError(f"{len(errors)} liens ou contrôles HTML en échec\n" + "\n".join(errors[:18]))
    return {"html": len(views), "local_links": total, "external_links_skipped": external,
            "bytes": sum(file.stat().st_size for file in files.values())}


def build(root, destination, site_url):
    base = urlsplit(site_url)
    if (base.scheme not in ("https", "http") or not base.netloc or base.query or base.fragment
            or not site_url.endswith("/") or base.username or base.password):
        raise ValueError("--site-url doit être une URL HTTP(S) absolue terminée par /")
    destination = destination.parent.resolve() / destination.name
    if destination.exists() or destination.is_symlink():
        raise ValueError(f"Choisissez un dossier de construction neuf · {destination}")
    for folder in ("generated", "editorial", "styles"):
        if destination.is_relative_to(root / folder):
            raise ValueError("La destination doit rester hors des sources")
    with TemporaryDirectory(prefix="wiki-construction-") as temp:
        scratch = Path(temp)
        manifest = assemble(root, scratch / "docs", site_url)
        built = scratch / "site"
        built.mkdir()
        css = root / "styles/wiki.css"
        if css.is_symlink() or not css.is_file():
            raise ValueError("Feuille de style manquante")
        for lang in LANGS:
            docs = scratch / "docs" / lang
            (docs / "styles").mkdir()
            shutil.copyfile(css, docs / "styles/wiki.css")
            settings = scratch / f"zensical-{lang}.toml"
            settings.write_text(config(docs, built / lang, lang, site_url), encoding="utf-8")
            subprocess.run([sys.executable, "-m", "zensical", "build", "--strict", "-f", str(settings)],
                           cwd=scratch, check=True)
        for name, expected in manifest["files"].items():
            if ASSET.fullmatch(name):
                target = built / shared_path(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(root / "generated" / name, target)
                if stamp(target) != expected:
                    raise ValueError(f"Image modifiée pendant la construction · {name}")
        links = ' · '.join(f'<a hreflang="{lang}" href="{lang}/">{name}</a>'
                           for lang, name in (("fr", "Français"), ("en", "English")))
        build_id = escape(manifest["steam_build_id"])
        (built / "index.html").write_text(
            f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width">'
            f'<title>Trials Survivors Wiki</title><style>body{{font:1.125rem system-ui;background:#141a25;'
            f'color:#f1f5ff;margin:12vh auto;padding:1.5rem;max-width:36rem}}a{{color:#7eeae2}}</style>'
            f'<main><h1>Trials Survivors Wiki</h1><p>Build {build_id}</p><nav>{links}</nav></main></html>\n',
            encoding="utf-8")
        (built / ".nojekyll").touch()
        result = validate_html(built, site_url)
        if any(path.suffix not in (".html", ".css", ".js", ".json", ".wasm", ".map", ".bin",
                                   ".svg", ".png", ".jpg", ".webp", ".ico", ".xml", ".gz", ".txt", ".woff2", "")
               for path in (Path(name) for name in files_in(built))):
            raise ValueError("Type de fichier inattendu dans le site HTML")
        destination.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(prefix=".wiki-site-", dir=destination.parent) as pending:
            prepared = Path(pending) / "site"
            shutil.copytree(built, prepared)
            if destination.exists() or destination.is_symlink():
                raise ValueError(f"La destination est apparue pendant la construction · {destination}")
            prepared.rename(destination)
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "verify"))
    parser.add_argument("--site-url", required=True)
    parser.add_argument("--output", type=Path, default=Path("site"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    destination = args.output.absolute()
    try:
        report = (build(root, destination, args.site_url) if args.command == "build"
                  else validate_html(destination, args.site_url))
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"{error}\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
