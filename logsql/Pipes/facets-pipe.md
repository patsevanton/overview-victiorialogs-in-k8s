## Конвейер facets

Возвращает наиболее частые значения для каждого встреченного поля лога и оценку числа попаданий. Поддерживает `facets N`, `max_values_per_field M`, `max_value_len K`, `keep_const_fields`.

**Примеры:**

```logsql
_time:1h error | facets
_time:1h error | facets 3
_time:1h error | facets 15 max_values_per_field 100000
_time:1h error | facets max_value_len 100
_time:1h error | facets keep_const_fields
```
