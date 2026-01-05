### Статистика `uniq_values`

Функция конвейера статистики `uniq_values(field1, ..., fieldN)`
([stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)) возвращает уникальные непустые значения по указанным [полям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Возвращаемые значения кодируются в виде отсортированного JSON-массива.

Например, следующий запрос возвращает уникальные непустые значения поля `ip`
([field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)) по логам за последние 5 минут:

```logsql
_time:5m | stats uniq_values(ip) unique_ips
```

Полученные уникальные IP-адреса можно развернуть в отдельные записи логов с помощью конвейера [`unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

Каждое уникальное значение хранится в памяти во время выполнения запроса. Большое количество уникальных значений может потребовать значительный объём памяти. Иногда достаточно вернуть только подмножество уникальных значений. В этом случае добавьте `limit N` после `uniq_values(...)`, чтобы ограничить количество возвращаемых уникальных значений числом `N`, тем самым ограничив максимальное потребление памяти.

Например, следующий запрос возвращает до `100` уникальных значений поля `ip`
([field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)) по логам за последние 5 минут:

```logsql
_time:5m | stats uniq_values(ip) limit 100 as unique_ips_100
```

Если достигается ограничение `limit`, каждый раз возвращается произвольное подмножество уникальных значений `ip`.

Также можно найти уникальные значения для всех полей с общим префиксом, используя синтаксис `uniq_values(prefix*)`.
