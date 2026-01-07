## Оператор sort (сортировка)

Сортирует логи по указанным полям с естественным порядком сортировки. Поддерживает `desc` для обратного порядка, `limit`, `offset`, `partition by`, `rank`.

**Примеры:**

```logsql
_time:5m | sort by (_stream, _time)
_time:5m | sort by (request_duration_seconds desc)
_time:1h | sort by (request_duration desc) limit 10
_time:1h | sort by (request_duration desc) offset 10 limit 20
_time:1h | sort by (request_duration desc) partition by (host) limit 3
_time:5m | sort by (_time) rank as position
```
