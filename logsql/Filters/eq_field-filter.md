## Фильтр eq_field

Находит логи, которые содержат одинаковые значения в заданных полях.

**Примеры:**
Например, следующий запрос находит логи с одинаковыми значениями в полях `user_id` и `customer_id`:

```logsql
user_id:eq_field(customer_id)
NOT user_id:eq_field(customer_id)
```
