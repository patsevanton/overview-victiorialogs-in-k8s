## Фильтр `contains_any`

Находит логи, которые содержат хотя бы одно слово или фразу из множества. Эквивалентно `v1 OR v2 OR ... OR vN`.

**Примеры:**

```logsql
contains_any(foo, "bar baz")
contains_any(error, warning, info)
```
