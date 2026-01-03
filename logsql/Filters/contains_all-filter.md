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

Существует специальный случай — `contains_all(*)`. Этот фильтр совпадает со **всеми** логами. Подробнее см. в документации по [no-op фильтрам](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter).

Внутрь фильтра `contains_all(...)` можно передать произвольный [запрос](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), чтобы выполнять сопоставление с результатами этого запроса. Подробнее см. в [этой документации](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter).

См. также:

* [фильтр `seq`](https://docs.victoriametrics.com/victorialogs/logsql/#sequence-filter)
* [фильтр по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
* [фильтр по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
* [фильтр `in`](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
* [фильтр `contains_any`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
