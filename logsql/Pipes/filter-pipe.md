### Конвейер фильтрации (filter pipe)

Конструкция `<q> | filter ...` [конвейер (pipe)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) фильтрует логи, возвращённые запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), с помощью указанного [фильтра](https://docs.victoriametrics.com/victorialogs/logsql/#filters).

Например, следующий запрос возвращает значения поля `host` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), если за последний час количество сообщений с словом `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) для них превышает `1 000`:

```logsql
_time:1h error | stats by (host) count() logs_count | filter logs_count:> 1_000
```

Для удобства вместо префикса `filter` можно использовать префикс `where`. Например, следующий запрос эквивалентен предыдущему:

```logsql
_time:1h error | stats by (host) count() logs_count | where logs_count:> 1_000
```

Префикс `filter` можно опустить, если используемые фильтры не конфликтуют с [названиями конвейеров (pipe names)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).  
Так, следующий запрос эквивалентен предыдущим:

```logsql
_time:1h error | stats by (host) count() logs_count | logs_count:> 1_000
```

Смотрите также:

- [конвейер `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [конвейер `sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
