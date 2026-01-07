## Конвейер json_array_len

Вычисляет длину JSON-массива в указанном поле и сохраняет результат в новое поле.

**Примеры:**

```logsql
_time:5m | unpack_words _msg as words | json_array_len(words) as words_count | first 5 (words_count desc)
```
