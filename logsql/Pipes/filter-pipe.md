## Конвейер фильтрации (filter pipe)

Фильтрует логи с помощью указанного фильтра. Можно использовать `where` вместо `filter`. Префикс `filter` можно опустить, если фильтры не конфликтуют с названиями конвейеров.

**Примеры:**

```logsql
_time:1h error | stats by (host) count() logs_count | filter logs_count:> 1_000
_time:1h error | stats by (host) count() logs_count | where logs_count:> 1_000
_time:1h error | stats by (host) count() logs_count | logs_count:> 1_000
```
