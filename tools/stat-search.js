// Les deux hooks s'exécutent avant la correction floue et avant la pagination.
const wikiStatSearch = (() => {
  const names = new Map();
  const withoutAccents = new Map();
  const withoutUnit = new Map();
  let preferred = [];

  function normalize(value) {
    return value.normalize("NFC").toLowerCase()
      .replaceAll("’", "'").trim().replace(/\s+/gu, " ");
  }

  function fold(value) {
    return value.normalize("NFD").replace(/\p{M}/gu, "");
  }

  function add(map, key, id) {
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(id);
  }

  return {
    capture: {
      onTextOptions(_options, items) {
        for (const [id, item] of items.entries()) {
          // Le navigateur résout les URL de l'index avant de les transmettre.
          if (!/^(?:(?:https?:\/\/[^#?]+\/(?:fr\/caracteristiques|en\/stats))|caracteristiques|stats)\/#stat--?\d+$/u
            .test(item.location)) continue;
          const name = normalize(item.title.replace(/^◇\s*/u, ""));
          add(names, name, id);
          add(withoutAccents, fold(name), id);
          if (name.endsWith(" (%)")) add(withoutUnit, fold(name.slice(0, -4)), id);
        }
      },
      onTextQuery(query) {
        preferred = [];
        if (typeof query.input !== "string") return;
        const name = normalize(query.input);
        const alternate = withoutAccents.get(fold(name));
        const unit = withoutUnit.get(fold(name));
        preferred = names.get(name) ?? (alternate?.length === 1 ? alternate : undefined)
          ?? (unit?.length === 1 ? unit : []);
      },
    },
    rank: {
      onTextResult(result) {
        if (!preferred.length) return;
        const promoted = [];
        const remaining = [];
        for (const item of result.items) {
          (preferred.includes(item.id) ? promoted : remaining).push(item);
        }
        result.items = promoted.concat(remaining);
      },
    },
  };
})();
