### count_uniq статистика

`count_uniq(field1, ..., fieldN)` [функция pipe stats](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) вычисляет количество уникальных непустых кортежей `(field1, ..., fieldN)`.

Например, следующий запрос возвращает количество уникальных непустых значений для поля `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) за последние 5 минут:

```logsql
_time:5m | stats count_uniq(ip) ips
```

Следующий запрос возвращает количество уникальных пар `(host, path)` для соответствующих [полей](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) за последние 5 минут:

```logsql
_time:5m | stats count_uniq(host, path) unique_host_path_pairs
```

Каждое уникальное значение хранится в памяти во время выполнения запроса. Большое количество уникальных значений может потребовать много памяти.
Иногда необходимо знать, достигает ли количество уникальных значений определённого предела. В этом случае добавьте `limit N` сразу после `count_uniq(...)`, чтобы ограничить количество учитываемых уникальных значений до `N` и при этом ограничить максимальное использование памяти. Например, следующий запрос считает до `1_000_000` уникальных значений для поля `ip`:

```logsql
_time:5m | stats count_uniq(ip) limit 1_000_000 as ips_1_000_000
```

Если допустимо подсчитать приблизительное количество уникальных значений, можно использовать [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats) — более быструю альтернативу `count_uniq`.

См. также:

* [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats)
* [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
* [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)


