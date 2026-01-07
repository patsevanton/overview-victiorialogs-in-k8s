## Разделение строки (split pipe)

Разделяет поле журнала на элементы по заданному разделителю и сохраняет результат в виде JSON-массива. Части `from <src_field>` и `as <dst_field>` необязательны.

**Примеры:**

```logsql
_time:5m | split "," from _msg as items
_time:5m | split "," from _msg
_time:5m | split ","
_time:5m | split "," as items | unroll items | top 5 (items)
```
