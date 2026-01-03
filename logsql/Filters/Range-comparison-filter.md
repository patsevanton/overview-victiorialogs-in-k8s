### Фильтр сравнения диапазонов

LogsQL поддерживает фильтры вида `field:>X`, `field:>=X`, `field:<X` и `field:<=X`, где:
- `field` — имя [поля лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model);
- `X` — [числовое значение](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values), IPv4‑адрес или строка.

Например, следующий запрос возвращает логи, содержащие числовые значения для поля `response_size`, превышающие `10*1024`:

```logsql
response_size:>10KiB
```

Следующий запрос возвращает логи, в которых поле `username` содержит строковые значения, меньшие, чем `John`:

```logsql
username:<"John"
```

См. также:

- [Фильтр диапазона строк](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter);
- [Фильтр диапазона](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter);
- Фильтр [`le_field`](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter);
- Фильтр [`lt_field`](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter).
