### Фильтр точного префикса

Иногда требуется найти сообщения журнала (логи), начинающиеся с определённого префикса. Это можно сделать с помощью фильтра `="префикс"*`.

Например, следующий запрос найдёт сообщения логов, которые начинаются с префикса `Processing request`:

```logsql
="Processing request"*
```

Этот фильтр соответствует таким сообщениям логов:

- `Processing request foobar`
- `Processing requests from ...`

Он **не** соответствует следующим сообщениям:

- `processing request foobar` — поскольку сообщение начинается со строчной буквы `p`. В этом случае используйте запрос `="processing request"* OR ="Processing request"*`. Подробнее см. в [документации по логическим фильтрам](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
- `start: Processing request` — поскольку сообщение не начинается с `Processing request`. В этом случае используйте запрос `"Processing request"`. Подробнее см. в [документации по фильтрам фраз](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter).

По умолчанию фильтр `exact` применяется к полю [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).

Чтобы выполнить поиск в конкретном поле, укажите имя поля перед фильтром `exact` и поставьте после него двоеточие. Например, следующий запрос возвращает записи логов, в которых поле `log.level` начинается с префикса `err`:

```logsql
log.level:="err"*
```

И имя поля, и фраза могут содержать произвольные символы в кодировке [UTF‑8](https://en.wikipedia.org/wiki/UTF-8). Например:

```logsql
log.დონე:="შეცდომა"*
```

Если имя поля содержит специальные символы, которые могут конфликтовать с синтаксисом запроса, его можно заключить в кавычки. Например, следующий запрос находит значения `log:level`, начинающиеся с префикса `err`:

```logsql
"log:level":="err"*
```

См. также:

- [Фильтр точного совпадения](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Фильтр префикса](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Фильтр слова](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Фильтр фразы](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
