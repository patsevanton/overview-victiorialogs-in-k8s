### Регистронезависимый фильтр

Регистронезависимый фильтр можно применять к любому слову, фразе или префиксу, обернув соответствующий [фильтр слова](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter),
[фильтр фразы](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) или [фильтр префикса](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) в `i()`.
Например, следующий запрос возвращает лог-сообщения со словом `error` в любом регистре:

```logsql
i(error)
```

Запрос соответствует следующим [лог-сообщениям](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

* `unknown error happened`
* `ERROR: cannot read file`
* `Error: unknown arg`
* `An ErRoR occurred`

Запрос **не** соответствует следующим лог-сообщениям:

* `FooError`, поскольку [слово](https://docs.victoriametrics.com/victorialogs/logsql/#word) `FooError` имеет лишний префикс `Foo`. Для этого случая используйте `~"(?i)error"`. Подробности см. в [документации](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter).
* `too many Errors`, поскольку [слово](https://docs.victoriametrics.com/victorialogs/logsql/#word) `Errors` имеет лишний суффикс `s`. Для этого случая используйте `i(error*)`.

По умолчанию фильтр `i()` применяется к [полю `_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Укажите нужное [имя поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) перед фильтром, чтобы применить его к конкретному полю.
Например, следующий запрос находит записи, где поле `log.level` содержит [слово](https://docs.victoriametrics.com/victorialogs/logsql/#word) `error` в любом регистре:

```logsql
log.level:i(error)
```

Если имя поля содержит специальные символы, которые могут конфликтовать с синтаксисом запроса, его можно заключить в кавычки согласно [документации](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
Например, следующий запрос находит записи, где поле `log:level` содержит [слово](https://docs.victoriametrics.com/victorialogs/logsql/#word) `error` в любом регистре:

```logsql
"log:level":i("error")
```

#### Советы по производительности

* Предпочитайте использовать фильтр [`contains_common_case`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter) вместо `i(...)`,
  поскольку `contains_common_case(...)` обычно работает значительно быстрее.
* По возможности используйте регистрозависимые фильтры, такие как [фильтр слова](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
  и [фильтр фразы](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter), вместо регистронезависимого фильтра.
* При использовании [логического фильтра](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
  старайтесь располагать [фильтр слова](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter),
  [фильтр фразы](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
  и [фильтр префикса](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
  перед регистронезависимым фильтром.
