# Trials Survivors Wiki

Sources du site communautaire bilingue. `generated/` contient les fichiers Markdown autorisés et leur manifeste léger. `editorial/` contient les contributions humaines. Pour compléter une compétence, ajoutez une note dans `editorial/fr/notes/` ou `editorial/en/notes/` avec le nom de fichier de la compétence.

Avec Python 3.12 depuis un clone du dépôt wiki contenant `generated/` :

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tools/site.py build --site-url http://127.0.0.1:8765/
.venv/bin/python -m http.server 8765 --bind 127.0.0.1 --directory site
```

Le dossier de sortie doit être neuf. Utilisez `--output site-suivant` pour une autre construction. Le workflow suppose que la branche de publication autorisée est `main` et que la source GitHub Pages est configurée sur GitHub Actions. Les pull requests contrôlent la construction. Les pushes de la branche de publication déclenchent le déploiement.

L’outillage d’extraction et les données techniques restent dans GameDataExtractor.

## Adresse de publication

Le site cible `https://manuelphelouzat.github.io/trials-survivors-wiki/`. Pour vérifier le préfixe de production, construisez dans un nouveau dossier avec `python tools/site.py build --site-url https://manuelphelouzat.github.io/trials-survivors-wiki/ --output site-production`.
