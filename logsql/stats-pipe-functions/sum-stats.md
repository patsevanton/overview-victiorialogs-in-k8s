### sum stats

`sum(field1, ..., fieldN)` — это [функция stats pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), которая вычисляет сумму числовых значений по всем указанным [полям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Нечисловые значения пропускаются. Если все значения в `field1`, …, `fieldN` являются нечисловыми, то возвращается `NaN`.

Например, следующий запрос возвращает сумму числовых значений поля `duration` за последние 5 минут:

```logsql
_time:5m | stats sum(duration) sum_duration
```

Также можно вычислить сумму по всем полям с общим префиксом, используя синтаксис `sum(prefix*)`.
