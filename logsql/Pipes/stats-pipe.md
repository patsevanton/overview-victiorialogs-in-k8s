## Пайп stats

Вычисляет статистику по логам. Поддерживает группировку по полям (`by (field1, ...)`), по временным бакетам (`by (_time:step)`), по бакетам полей, по IPv4-бакетам, дополнительные фильтры (`if (...)`).

**Примеры:**

```logsql
_time:5m | stats count() as logs_total
_time:5m | stats by (host, path) count() logs_total, count_uniq(ip) ips_total
_time:5m | stats by (_time:1m) count() logs_total, count_uniq(ip) ips_total
_time:1h | stats by (request_size_bytes:10KB) count() requests
_time:5m | stats by (ip:/24) count() requests_per_subnet
_time:5m | stats count() if (GET) gets, count() if (POST) posts, count() total
```
