### Статистика `count_uniq_hash`

`count_uniq_hash(field1, ..., fieldN)` — [stats-функция конвейера](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), которая вычисляет количество уникальных хешей для непустых кортежей `(field1, ..., fieldN)`.
Это хороший способ приблизительно оценить количество уникальных значений в общем случае. При этом функция работает быстрее и использует меньше памяти, чем [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats),
когда требуется посчитать большое количество уникальных значений.

Например, следующий запрос возвращает приблизительное количество уникальных непустых значений для поля `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) за последние 5 минут:

```logsql
_time:5m | stats count_uniq_hash(ip) unique_ips_count
```

Следующий запрос возвращает приблизительное количество уникальных пар `(host, path)` для соответствующих [полей](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) за последние 5 минут:

```logsql
_time:5m | stats count_uniq_hash(host, path) unique_host_path_pairs
```

См. также:

* [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
* [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
* [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)
