### Фильтр `contains_all`

Если нужно найти логи, которые содержат **все** заданные [слова](https://docs.victoriametrics.com/victorialogs/logsql/#word) / фразы, то можно использовать [логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
`v1 AND v2 ... AND vN`.

VictoriaLogs предоставляет альтернативный подход с фильтром `contains_all(v1, v2, ..., vN)`.
Например, следующий запрос находит логи, которые содержат и [слово](https://docs.victoriametrics.com/victorialogs/logsql/#word) `foo`, и фразу `"bar baz"` в [поле `_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
contains_all(foo, "bar baz")
```

Это эквивалентно следующему запросу:

```logsql
foo AND "bar baz"
```

