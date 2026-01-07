## Фильтр `contains_all`

Находит логи, которые содержат все заданные слова/фразы. Эквивалентно `v1 AND v2 ... AND vN`.

**Примеры:**

```logsql
contains_all(foo, "bar baz")
contains_all(error, file, app)
```
