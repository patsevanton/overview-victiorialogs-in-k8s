## Статистика count_uniq_hash

Вычисляет приблизительное количество уникальных хешей для непустых кортежей по указанным полям логов. Работает быстрее и использует меньше памяти, чем `count_uniq`.

**Примеры:**

```logsql
_time:5m | stats count_uniq_hash(ip) unique_ips_count
_time:5m | stats count_uniq_hash(host, path) unique_host_path_pairs
```
