### Фильтр `value_type`

VictoriaLogs автоматически определяет типы для загружаемых [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) и сохраняет значения полей логов в соответствии с обнаруженным типом (например, `const`, `dict`, `string`, `int64`, `float64` и т. д.). Типы значений для сохранённых полей можно получить с помощью конвейера [`block_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe).

Иногда требуется выбрать логи с полями определённого типа значения. В этом случае можно использовать фильтр `value_type(type)`.

Например, следующий фильтр выбирает логи, в которых значения поля `user_id` хранятся как тип `uint64`:

```logsql
user_id:value_type(uint64)
```

См. также:

- конвейер [`block_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe);
- конвейер [`query_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe);
- [логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
