### квантильная статистика

`quantile(phi, field1, ..., fieldN)` — это [stats pipe-функция](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), которая вычисляет приближённый `phi`-й [процентиль](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%86%D0%B5%D0%BD%D1%82%D0%B8%D0%BB%D1%8C) по значениям
указанных [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Параметр `phi` должен находиться в диапазоне `0 ... 1`, где `0` означает `0`-й процентиль,
а `1` — `100`-й процентиль.

Например, следующий запрос вычисляет `50`-й, `90`-й и `99`-й процентили для поля
`request_duration_seconds` по логам за последние 5 минут:

```logsql
_time:5m | stats
  quantile(0.5, request_duration_seconds) p50,
  quantile(0.9, request_duration_seconds) p90,
  quantile(0.99, request_duration_seconds) p99
```

Функция `quantile(phi, some_field)` работает и со строковыми значениями поля `some_field`,
поэтому она возвращает пустую строку, если `some_field` отсутствует в части обрабатываемых логов
согласно [модели данных VictoriaLogs](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Чтобы отфильтровать пустые строковые значения, используйте синтаксис:

```
quantile(phi, some_field) if (some_field:*) as min_value_without_empty_string
```

Подробнее см. в документации по
[условной статистике](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters).

Также возможно вычислять квантили сразу по всем полям с общим префиксом, используя синтаксис
`quantile(phi, prefix*)`.
