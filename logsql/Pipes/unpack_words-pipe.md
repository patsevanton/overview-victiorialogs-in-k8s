## Пайп unpack_words

Распаковывает слова из указанного поля и сохраняет их в виде JSON-массива. Части `from <src_field>` и `as <dst_field>` необязательны. Поддерживает `drop_duplicates`.

**Примеры:**

```logsql
_time:5m | unpack_words from _msg as words
_time:5m | unpack_words from _msg
_time:5m | unpack_words
_time:5m | unpack_words from text as words drop_duplicates
_time:5m | unpack_words as words | unroll words | top 5 (words)
```
