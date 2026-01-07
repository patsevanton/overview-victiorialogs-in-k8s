## Фильтр сравнения диапазонов

Поддерживает фильтры вида `field:>X`, `field:>=X`, `field:<X` и `field:<=X`, где `X` — числовое значение, IPv4-адрес или строка.

**Примеры:**

```logsql
response_size:>10KiB
username:<"John"
```
