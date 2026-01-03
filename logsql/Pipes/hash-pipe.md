### Конвейер `hash`

Конструкция  
```
<q> | hash(поле) as результирующее_поле
```  
вычисляет хеш‑значение для указанного поля [`поле`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) и сохраняет его в поле `результирующее_поле` для каждой записи журнала, возвращённой запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

Например, следующий запрос вычисляет хеш‑значение для поля `user_id` и сохраняет его в поле `user_id_hash` для журналов за последние 5 минут:

```logsql
_time:5m | hash(user_id) as user_id_hash
```
