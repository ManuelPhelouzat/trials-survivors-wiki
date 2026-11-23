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
    ["transpercent", "skills/", "text"],
  ],
  en: [
    ["Frost Ball", "skills/" + frost + "/", "title"],
    ["Frost Ball Of Galaxy", "cards/", "title"],
    ["Chill Chance", "cards/card-", "title"],
    ["Cooldown", "cards/", "text"],
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
  if ((await request(0, index)).type !== 1) throw new Error(`Index inutilisable · ${lang}`);

  const results = [];
  for (const [input, prefix, field] of samples[lang]) {
    const response = await request(2, { input, filter: {
      input: { type: "operator", data: { operator: "and", operands: [] } },
      aggregation: { input: [{ type: "term", data: { field: "tags" } }] },
    } });
    if (response.type !== 3) throw new Error(`Erreur de recherche · ${lang} · ${input}`);
    const match = response.data.items.find((item) =>
      index.items[item.id].location.startsWith(prefix) && item.matches.some((value) => value.field === field));
    if (!match) throw new Error(`Résultat attendu absent · ${lang} · ${input} · ${prefix}`);
    results.push({ query: input, location: index.items[match.id].location });
  }
  return { lang, bytes: statSync(path).size, entries: index.items.length, results };
}

console.log(JSON.stringify([await check("fr"), await check("en")], null, 2));
