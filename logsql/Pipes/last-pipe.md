### Последний конвейер (`last pipe`)

Конструкция `<q> | last N by (fields)` [конвейер (pipe)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) возвращает **последние `N` записей журнала** из запроса `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) после их сортировки по указанным полям [`fields`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

**Пример:** следующий запрос возвращает **последние 10 записей журнала** с наибольшим значением поля `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) за последние 5 минут:

```logsql
_time:5m | last 10 by (request_duration)
```

Можно вернуть до `N` записей **для каждой группы** журналов с одинаковым набором полей, перечислив эти поля в `partition by (...)`.

**Пример:** следующий запрос возвращает **до 3 записей журнала** с наибольшим `request_duration` для каждого хоста за последний час:

```logsql
_time:1h | last 3 by (request_duration) partition by (host)
```

См. также:

- конвейер [`first`](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe);
- конвейер [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).
