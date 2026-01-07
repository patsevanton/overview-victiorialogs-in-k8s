## Фильтр потоков

Оптимизированный способ выбора логов по потокам с помощью селектора меток Prometheus `{...}`.

**Примеры:**

```logsql
{app="nginx"}
{app in ("nginx", "foo.bar")}
{app not_in ("nginx", "foo.bar")}
_stream:{app="nginx"}
```
