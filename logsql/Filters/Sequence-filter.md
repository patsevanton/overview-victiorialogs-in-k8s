### Фильтр последовательности (Sequence filter)

Иногда требуется найти [сообщения логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), в которых слова или фразы идут в определённом порядке.

Например, если нужно найти сообщения логов, где слово `error` идёт *перед* фразой `open file`, можно использовать следующий запрос на языке LogsQL (каждое слово или фраза могут быть заключены в кавычки — см. [документацию](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals)):

```logsql
seq("error", "open file")
```

Этот запрос подойдёт для сообщения `some error: cannot open file /foo/bar`, поскольку фраза `open file` идёт после слова `error`.

Зато он *не подойдёт* для сообщения `cannot open file: error`, так как фраза `open file` расположена *перед* словом `error`.

Если же нужно найти сообщения, содержащие и слово `error`, и фразу `open file` (без учёта порядка), используйте запрос `error AND "open file"`. Подробнее — в [документации по логическим фильтрам](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).

**По умолчанию** фильтр `seq()` применяется к полю [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).

Чтобы применить фильтр к другому полю, укажите его имя перед фильтром. Например, следующий запрос ищет последовательность `(error, "open file")` в поле `event.original`:

```logsql
event.original:seq(error, "open file")
```

Если имя поля содержит специальные символы, которые могут конфликтовать с синтаксисом запроса, его можно заключить в кавычки (см. [документацию по строковым литералам](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals)).

Например, так выглядит запрос для поля `event:original`:

```logsql
"event:original":seq(error, "open file")
```
