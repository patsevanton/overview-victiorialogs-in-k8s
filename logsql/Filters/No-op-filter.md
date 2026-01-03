### Фильтр‑заглушка (no‑op filter)

Иногда требуется применить, например, фильтр‑заглушку (`no‑op`) к заданному [полю лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), который ничего не делает — то есть он сопоставляет любые логи, даже если они не содержат указанное поле лога.

Для фильтра‑заглушки поддерживаются следующие варианты:

- `field_name:in(*)` — особый случай для фильтра [`in()`](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter);
- `field_name:contains_any(*)` — особый случай для фильтра [`contains_any()`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter);
- `field_name:contains_all(*)` — особый случай для фильтра [`contains_all()`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter).
