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
