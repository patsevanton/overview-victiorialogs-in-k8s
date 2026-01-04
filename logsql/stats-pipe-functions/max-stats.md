### max stats

Функция конвейера статистики
`max(field1, ..., fieldN)` возвращает максимальное значение среди всех указанных [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

Например, следующий запрос возвращает максимальное значение поля `duration` за последние 5 минут:

```logsql
_time:5m | stats max(duration) max_duration
```

Функция `max(some_field)` работает и со строковыми значениями поля `some_field`, поэтому она возвращает пустую строку, если `some_field`
отсутствует в части обрабатываемых логов, согласно [модели данных VictoriaLogs](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Чтобы отфильтровать пустые строковые значения, используйте синтаксис
`max(some_field) if (some_field:*) as min_value_without_empty_string`.
Подробнее см. в документации по [условной статистике](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters).

Также можно вычислить максимальное значение сразу по всем полям с общим префиксом, используя синтаксис `max(prefix*)`.

Функция [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats) может использоваться для получения других полей, связанных с максимальным значением `duration`.
