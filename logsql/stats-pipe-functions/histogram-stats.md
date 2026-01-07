## Статистика histogram

Возвращает бакеты гистограммы VictoriaMetrics для заданного поля. Нормализует значения длительности к наносекундам и короткие числовые значения. Возвращает JSON-массив с `vmrange` и `hits`.

**Примеры:**

```logsql
_time:5m | stats by (host) histogram(response_size)
_time:5m | stats histogram(response_size) as buckets | unroll (buckets) | unpack_json from buckets
```
