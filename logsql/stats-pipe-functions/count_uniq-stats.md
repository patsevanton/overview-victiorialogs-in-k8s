## Статистика count_uniq

Вычисляет количество уникальных непустых кортежей по указанным полям логов. Поддерживает `limit N` для ограничения памяти. Для приблизительного подсчёта можно использовать `count_uniq_hash`.

**Примеры:**

```logsql
_time:5m | stats count_uniq(ip) ips
_time:5m | stats count_uniq(host, path) unique_host_path_pairs
_time:5m | stats count_uniq(ip) limit 1_000_000 as ips_1_000_000
```
