## Фильтр по регулярным выражениям

LogsQL поддерживает фильтрацию по регулярным выражениям (с синтаксисом **RE2**) через конструкцию `~"regex"`.

Регулярное выражение `regex` можно заключать в любые поддерживаемые кавычки — см. [документацию по строковым литералам](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).

**Пример:** следующий запрос вернёт все сообщения журнала, содержащие подстроки `err` или `warn`:

```logsql
~"err|warn"
```

Этот запрос совпадет со следующими [сообщениями журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), содержащими `err` или `warn`:

- `error: cannot read data`
- `2 warnings have been raised`
- `data transferring finished`

Запрос **не совпадет** со следующими сообщениями:

- `ERROR: cannot open file` — потому что слово `ERROR` написано заглавными буквами. Для поиска без учёта регистра используйте запрос `~"(?i)(err|warn)"`.  
  Подробнее см. в [документации по RE2](https://github.com/google/re2/wiki/Syntax) и в разделе о [фильтрах без учёта регистра](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).
- `it is warmer than usual` — потому что в нём нет ни `err`, ни `warn`.

### Экранирование кавычек и обратных слешей

Если регулярное выражение содержит двойные кавычки, их нужно либо экранировать обратным слешем `\`, либо заключить выражение в одинарные кавычки. Например, следующий запрос ищет логи, соответствующие регулярному выражению `"foo":"(bar|baz)"`:

```logsql
~'"foo":"(bar|baz)"'
```

Символ `\` внутри регулярного выражения должен быть записан как `\\`. Например, следующий запрос ищет логи, содержащие подстроку `a.b`:

```logsql
~"a\\.b"
```

### Применение фильтра к конкретному полю

По умолчанию фильтр по регулярному выражению применяется к полю [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).

Чтобы применить фильтр к определённому полю, укажите имя поля перед фильтром. Например, следующий запрос ищет в поле `event.original` подстроки `err` или `warn`:

```logsql
event.original:~"err|warn"
```

Если имя поля содержит специальные символы, которые могут конфликтовать с синтаксисом запроса, его можно заключить в кавычки — см. [документацию по строковым литералам](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).

**Пример:** запрос для поля `event:original`:

```logsql
"event:original":~"err|warn"
```

## Советы по производительности

- **Предпочитайте простые фильтры.** Вместо регулярного выражения комбинируйте [фильтр по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) с [логическим фильтром](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).  
  Например, запрос `~"error|warning"` можно заменить на `error OR warning` — он обычно работает значительно быстрее.  
  **Важно:** `~"error|warning"` совпадет с `errors` и `warnings`, а `error OR warning` — только с точными словами. См. также [фильтр по нескольким точным значениям](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter).

- **Ставьте регулярный фильтр в конец.** Перемещайте фильтр по регулярному выражению в конец [логического фильтра](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter), чтобы сначала выполнялись более лёгкие фильтры.

- **Используйте фильтр по префиксу.** Вместо `~"^some prefix"` предпочитайте `="some prefix"*` — [фильтр по точному префиксу](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter) работает намного быстрее регулярного выражения.

- См. также [другие советы по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

## См. также

- [Фильтр без учёта регистра](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)
- [Логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
