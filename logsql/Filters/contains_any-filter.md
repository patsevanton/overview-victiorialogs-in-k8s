### Фильтр `contains_any`

Иногда требуется найти логи, которые содержат хотя бы одно [слово](https://docs.victoriametrics.com/victorialogs/logsql/#word) или фразу из множества слов / фраз.
Это можно сделать с помощью [логического фильтра](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) `v1 OR v2 OR ... OR vN`.

VictoriaLogs предоставляет альтернативный подход — фильтр `contains_any(v1, v2, ..., vN)`.
Например, следующий запрос находит логи, которые содержат слово `foo` или фразу `"bar baz"` в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
contains_any(foo, "bar baz")
```

Это эквивалентно следующему запросу:

```logsql
foo OR "bar baz"
```

Существует специальный случай — `contains_any(*)`. Этот фильтр совпадает со всеми логами. Подробности см. в документации по [no-op фильтру](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter).

Внутрь фильтра `contains_any(...)` можно передавать произвольный [запрос](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), чтобы выполнять сопоставление по результатам этого запроса. Подробности см. в [этой документации](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter).

См. также:

* [фильтр по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
* [фильтр по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
* [фильтр `in`](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
* [фильтр `contains_all`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)
