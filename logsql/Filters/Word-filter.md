### Фильтр по слову

Самый простой запрос на языке LogsQL состоит из одного **[слова](https://docs.victoriametrics.com/victorialogs/logsql/#word)**, которое ищут в сообщениях журнала. Например, следующий запрос находит **[сообщения журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)**, содержащие внутри слово `error`:

```logsql
error
```

Этот запрос соответствует таким **[сообщениям журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)**:

- `error`
- `an error happened`
- `error: cannot open file`

Этот запрос **не** соответствует следующим сообщениям журнала:

- `ERROR` — поскольку по умолчанию фильтр чувствителен к регистру. Для учёта разных регистров используйте `i(error)`. Подробности см. в **[этой документации](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)**.
- `multiple errors occurred` — поскольку слово `errors` не совпадает с `error`. Для поиска по префиксу используйте `error*`. Подробности см. в **[этой документации](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)**.

По умолчанию указанное **[слово](https://docs.victoriametrics.com/victorialogs/logsql/#word)** ищется в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).

Чтобы искать слово в конкретном поле, укажите **[имя поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)** перед словом и поставьте после него двоеточие. Например, следующий запрос возвращает записи журнала, содержащие слово `error` в поле `log.level`:

```logsql
log.level:error
```

И имя поля, и слово в запросе могут содержать произвольные символы в кодировке **[UTF‑8](https://en.wikipedia.org/wiki/UTF-8)**. Например:

```logsql
სფერო:τιμή
```

Если имя поля или слово содержат специальные символы, которые могут конфликтовать с синтаксисом запроса, их можно заключить в кавычки. Например, следующий запрос ищет IP‑адрес `1.2.3.45` в поле `ip:remote`:

```logsql
"ip:remote":"1.2.3.45"
```

См. также:

- **[Фильтр по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)**
- **[Точный фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)**
- **[Фильтр по префиксу](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)**
- **[Фильтр по подстроке](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)**
- **[Логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)**
