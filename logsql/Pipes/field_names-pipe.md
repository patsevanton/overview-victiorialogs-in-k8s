### Конвейер `field_names`

`<q> | field_names` [конвейер (pipe)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) возвращает все имена [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) вместе с оценочным количеством записей логов для каждого имени поля, полученных по запросу `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

Например, следующий запрос вернёт все имена полей с количеством соответствующих записей логов за последние 5 минут:

```logsql
_time:5m | field_names
```

Имена полей возвращаются в произвольном порядке. Если требуется их отсортировать, используйте [конвейер `sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).
