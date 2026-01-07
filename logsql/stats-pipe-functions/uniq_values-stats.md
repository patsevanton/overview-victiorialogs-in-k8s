## Статистика uniq_values

Возвращает уникальные непустые значения по указанным полям логов в виде отсортированного JSON-массива. Поддерживает `limit N` и префиксы.

**Примеры:**

```logsql
_time:5m | stats uniq_values(ip) unique_ips
_time:5m | stats uniq_values(ip) limit 100 as unique_ips_100
_time:5m | stats uniq_values(prefix*)
```
