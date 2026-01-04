### Статистика `rate_sum`

Функция конвейера статистики [`rate_sum(field1, ..., fieldN)`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) возвращает среднюю скорость в секунду для суммы по указанным
числовым [полям](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

Например, следующий запрос возвращает среднюю скорость в секунду для суммы поля журнала `bytes_sent`
за последние 5 минут:

```logsql
_time:5m | stats rate_sum(bytes_sent)
```

Также можно вычислить среднюю скорость в секунду для суммы по всем полям, начинающимся с заданного префикса,
используя синтаксис `rate_sum(prefix*)`.
