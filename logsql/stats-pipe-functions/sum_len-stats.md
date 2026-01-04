### sum_len stats

`sum_len(field1, ..., fieldN)` — [статистическая функция pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), которая вычисляет **сумму байтовых длин всех значений** для указанных [лог-полей](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

Например, следующий запрос возвращает сумму байтовых длин поля [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) во всех логах за последние 5 минут:

```logsql
_time:5m | stats sum_len(_msg) messages_len
```

Также можно вычислить сумму байтовых длин **для всех полей с общим префиксом** с помощью синтаксиса `sum_len(prefix*)`.
