### Точный фильтр (`exact`)

Фильтры [по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) и [по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) возвращают [сообщения журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), содержащие заданное слово или фразу. При этом в сообщении может присутствовать и другой текст помимо искомого.

Если требуется найти сообщения журнала или [поля журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) с **точным** значением, используйте фильтр `exact`.

Например, следующий запрос вернёт сообщения журнала с точным значением `fatal error: cannot find /foo/bar`:

```logsql
="fatal error: cannot find /foo/bar"
```

Этот запрос **не** сопоставит такие сообщения журнала:

- `fatal error: cannot find /foo/bar/baz` или `some-text fatal error: cannot find /foo/bar` — поскольку они содержат дополнительный текст, отличный от указанного в фильтре `exact`. В этом случае используйте запрос `"fatal error: cannot find /foo/bar"`. Подробнее см. в [документации](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter).
- `FATAL ERROR: cannot find /foo/bar` — поскольку фильтр `exact` чувствителен к регистру. В этом случае используйте `i("fatal error: cannot find /foo/bar")`. Подробнее см. в [документации](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).

По умолчанию фильтр `exact` применяется к полю [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).

Чтобы выполнить поиск в конкретном поле, укажите имя [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) перед фильтром `exact` и поставьте после него двоеточие. Например, следующий запрос вернёт записи журнала с точным значением `error` в поле `log.level`:

```logsql
log.level:="error"
```

И имя поля, и фраза могут содержать произвольные символы в кодировке [UTF‑8](https://en.wikipedia.org/wiki/UTF-8). Например:

```logsql
log.დონე:="შეცდომა"
```

Имя поля можно заключить в кавычки, если оно содержит специальные символы, которые могут конфликтовать с синтаксисом запроса.

Например, следующий запрос найдёт значение `error` в поле `log:level`:

```logsql
"log:level":="error"
```

См. также:

- [Фильтр равенства полей](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter)
- [Фильтр точного префикса](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter)
- [Множественный точный фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [Фильтр по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Фильтр по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Фильтр по префиксу](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
