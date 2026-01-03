### pipe `unpack_words`

Pipe `<q> | unpack_words from <src_field> as <dst_field>` распаковывает [слова](https://docs.victoriametrics.com/victorialogs/logsql/#word) из указанного [поля лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `<src_field>` в результатах [запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) `<q>` и сохраняет их в `<dst_field>` в виде JSON-массива.

Например, следующий запрос распаковывает слова из [сообщений лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) в поле `words`:

```logsql
_time:5m | unpack_words from _msg as words
```

Часть `as <dst_field>` является необязательной. Если она отсутствует, результат сохраняется в поле `<src_field>`, указанное в `from <src_field>`.
Например, следующий запрос сохраняет распакованные слова в поле `_msg`:

```logsql
_time:5m | unpack_words from _msg
```

Часть `from <src_field>` также является необязательной. Если она отсутствует, слова распаковываются из поля `_msg`. Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | unpack_words
```

По умолчанию pipe `unpack_words` распаковывает все слова, включая дубликаты, из `<src_field>`.
Дубликаты можно отбросить, добавив суффикс `drop_duplicates` к pipe.
Например, следующий запрос извлекает только уникальные слова из каждого поля `text`:

```logsql
_time:5m | unpack_words from text as words drop_duplicates
```

Удобно использовать pipe [`unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) для «разворачивания» JSON-массива с распакованными словами из поля назначения.
Например, следующий запрос возвращает топ-5 самых часто встречающихся слов в [сообщениях лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) за последние 5 минут:

```logsql
_time:5m | unpack_words as words | unroll words | top 5 (words)
```

См. также:

* pipe [`unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
* pipe [`split`](https://docs.victoriametrics.com/victorialogs/logsql/#split-pipe)
