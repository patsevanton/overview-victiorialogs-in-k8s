### Канал `sample`

Канал `<q> | sample N` [ (канал)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) возвращает **случайную выборку** логов для запроса `<q>` в объёме `1/N`‑ю часть от всех подходящих записей.

Например, следующий запрос вернёт примерно **1 %** (1/100‑ю случайную выборку) логов за последний час, содержащих слово `error` в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
_time:1h error | sample 100
```

См. также:

- Канал [`limit`](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)
