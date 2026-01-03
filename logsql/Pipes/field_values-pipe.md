### Конвейер `field_values`

```
<q> | field_values field_name
```

[Конвейер](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) `field_values` возвращает все значения для указанного поля [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) вместе с количеством логов для каждого значения, полученных по запросу `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

Например, следующий запрос возвращает все значения поля `level` вместе с числом соответствующих логов за последние 5 минут:

```logsql
_time:5m | field_values level
```

Можно ограничить число возвращаемых значений, добавив в конец конструкции `field_values ...` параметр `limit N`. Например, следующий запрос вернёт не более 10 значений для поля `user_id` за последние 5 минут:

```logsql
_time:5m | field_values user_id limit 10
```

Если лимит достигнут, набор возвращаемых значений будет случайным. Кроме того, для повышения производительности количество соответствующих логов для каждого возвращённого значения обнуляется.

Смотрите также:

- конвейер [`field_names`](https://docs.victoriametrics.com/victorialogs/logsql/#field_names-pipe);
- конвейер [`facets`](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe);
- конвейер [`top`](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe);
- конвейер [`uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe).
