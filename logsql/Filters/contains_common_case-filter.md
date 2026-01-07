## Фильтр contains_common_case

Ищет логи, в которых поле содержит заданные фразы, учитывая различные варианты регистра (обычно быстрее, чем `i(...)`).

**Примеры:**

```logsql
_msg:contains_common_case("VictoriaMetrics")
```
