### Фильтр по префиксу

Если нужно найти сообщения логов, содержащие [слова](https://docs.victoriametrics.com/victorialogs/logsql/#word) / фразы с определённым префиксом, просто добавьте символ `*` в конец [слова](https://docs.victoriametrics.com/victorialogs/logsql/#word) / фразы в запросе.

Например, следующий запрос вернёт [сообщения логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), содержащие [слова](https://docs.victoriametrics.com/victorialogs/logsql/#word) с префиксом `err`:

```logsql
err*
```

Этот запрос соответствует таким [сообщениям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `err: foobar`
- `cannot open file: error occurred`

Этот запрос **не** соответствует следующим сообщениям логов:

- `Error: foobar`, поскольку слово `Error` начинается с заглавной буквы. Для такого случая используйте `i(err*)`. Подробности — в [документации](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).
- `fooerror`, поскольку слово `fooerror` не начинается с `err`. Для такого случая используйте `*err*`. Подробности — в [документации](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter).

Фильтр по префиксу можно применять к [фразам](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter), заключённым в кавычки (согласно [документации](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals)). Например, следующий запрос находит [сообщения логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), содержащие фразы с префиксом `unexpected fail`:

```logsql
"unexpected fail"*
```

Этот запрос соответствует таким [сообщениям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `unexpected fail: IO error`
- `error:unexpected failure`

Этот запрос **не** соответствует следующим сообщениям логов:

- `unexpectedly failed`, поскольку `unexpectedly` не совпадает со словом `unexpected`. Для такого случая используйте `unexpected* AND fail*`. Подробности — в [документации](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
- `failed to open file: unexpected EOF`, поскольку слово `failed` идёт перед словом `unexpected`. Для такого случая используйте `unexpected AND fail*`. Подробности — в [документации](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).

Если префикс содержит двойные кавычки, поставьте перед ними обратный слеш `\` либо заключите префикс в одинарные кавычки. Например, следующий фильтр ищет логи с префиксом `"foo":"bar`:

```logsql
'"foo":"bar'*
```

По умолчанию фильтр по префиксу применяется к полю [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field). Чтобы применить его к конкретному полю, укажите имя [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) перед фильтром. Например, следующий запрос находит поле `log.level`, содержащее любое слово с префиксом `err`:

```logsql
log.level:err*
```

Если имя поля содержит специальные символы, которые могут конфликтовать с синтаксисом запроса, его можно заключить в кавычки (согласно [документации](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals)). Например, следующий запрос находит поле `log:level`, содержащее любое слово с префиксом `err`:

```logsql
"log:level":err*
```

**Советы по производительности:**

- Предпочитайте комбинировать [фильтры по словам](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) и [фильтры по фразам](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) через [логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) вместо фильтра по префиксу.
- При использовании [логического фильтра](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) ставьте [фильтры по словам](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) и [фильтры по фразам](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) перед фильтром по префиксу.
- Смотрите также [другие советы по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

**См. также:**

- [Фильтр по подстроке](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Фильтр по точному префиксу](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter)
- [Фильтр по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Фильтр по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Точный фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
