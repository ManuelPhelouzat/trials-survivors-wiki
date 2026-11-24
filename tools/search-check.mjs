// Contrôle le worker de recherche livré par la version verrouillée de Zensical.
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";
import vm from "node:vm";

const root = process.argv[2] || "site";
const frost = "871329250-7b854bf6fec56d45";
const samples = {
  fr: [
    ["Boule de Givre", "skills/" + frost + "/", "title"],
    ["Boule de Givre Galactique", "cards/", "title"],
    ["Chance de Gel", "cards/card-", "title"],
    ["Recharge", "cards/", "text"],
    ["Portée de Ramassage", "cards/card-17330-43e9b50e438688a1/", "title"],
    ["transpercent", "skills/", "text"],
  ],
  en: [
    ["Frost Ball", "skills/" + frost + "/", "title"],
    ["Frost Ball Of Galaxy", "cards/", "title"],
    ["Chill Chance", "cards/card-", "title"],
    ["Cooldown", "cards/", "text"],
    ["Pickup Range", "cards/card-17330-43e9b50e438688a1/", "title"],
    ["pierce everything", "skills/", "text"],
  ],
};

async function check(lang) {
  const path = join(root, lang, "search.json");
  const index = JSON.parse(readFileSync(path, "utf8"));
  if (index.config.lang.join() !== lang) throw new Error(`Langue incorrecte dans ${path}`);
  const workers = join(root, lang, "assets/javascripts/workers");
  const file = readdirSync(workers).find((name) => name.startsWith("search.") && name.endsWith(".js"));
  if (!file) throw new Error(`Worker absent · ${lang}`);
  let reply;
  const self = { postMessage(message) { reply(message); } };
  vm.runInNewContext(readFileSync(join(workers, file), "utf8"), { self });
  const request = (type, data) => new Promise((resolve) => {
    const timer = setTimeout(() => { throw new Error(`Recherche expirée · ${lang}`); }, 30000);
    reply = (result) => { clearTimeout(timer); resolve(result); };
    self.onmessage({ data: { type, data } });
  });
  const browserIndex = { ...index, items: index.items.map(item => ({
    ...item, location: new URL(item.location, `https://example.invalid/wiki/${lang}/`).href,
  })) };
  if ((await request(0, browserIndex)).type !== 1) throw new Error(`Index inutilisable · ${lang}`);

  const query = (input, page) => request(2, { input, page, filter: {
    input: { type: "operator", data: { operator: "and", operands: [] } },
    aggregation: { input: [{ type: "term", data: { field: "tags" } }] },
  } });
  const results = [];
  for (const [input, prefix, field] of samples[lang]) {
    const response = await query(input);
    if (response.type !== 3) throw new Error(`Erreur de recherche · ${lang} · ${input}`);
    const match = response.data.items.find((item) =>
      index.items[item.id].location.startsWith(prefix) && item.matches.some((value) => value.field === field));
    if (!match) throw new Error(`Résultat attendu absent · ${lang} · ${input} · ${prefix}`);
    results.push({ query: input, location: index.items[match.id].location });
  }
  const route = lang === "fr" ? "caracteristiques/" : "stats/";
  const stats = index.items.filter(({ location }) => location.startsWith(route + "#stat-"));
  if (stats.length !== 88) throw new Error(`Référentiel incomplet · ${lang} · ${stats.length}`);
  const explicit = lang === "fr" ? [
    ["Degats de froid", 2056331723], ["Accélération des Compétences", -858402365],
    ["Chance de Poison", 1687477670], ["Chance de Poison (%)", 1955502493],
  ] : [
    ["cold damage", 2056331723], ["Ability Haste", -858402365],
    ["Poison Chance", 1687477670], ["Poison Chance (%)", 1955502493],
  ];
  const exact = [...stats.map(({ title, location }) => [title.replace(/^◇\s*/u, ""), location]),
    ...explicit.map(([name, id]) => [name, route + "#stat-" + id])];
  for (const [name, location] of exact) {
    const response = await query(name);
    const first = response.data.items[0];
    if (!first || index.items[first.id].location !== location) {
      throw new Error(`Définition attendue en tête · ${lang} · ${name} · ${location}`);
    }
  }

  // Une définition promue conserve la pagination et les résultats de cartes.
  const phrase = lang === "fr" ? "Dégâts de Froid" : "Cold Damage";
  const first = (await query(phrase)).data;
  const second = (await query(phrase, first.pagination.next)).data;
  const ids = [...first.items, ...second.items].map(({ id }) => id);
  if (!first.pagination.next || ids.length !== 20 || new Set(ids).size !== 20
      || !ids.some(id => index.items[id].location.startsWith("cards/"))) {
    throw new Error(`Pagination ou résultats de cartes modifiés · ${lang}`);
  }
  return { lang, bytes: statSync(path).size, entries: index.items.length, statQueries: exact.length, results };
}

console.log(JSON.stringify([await check("fr"), await check("en")], null, 2));
