## Фильтр le_field

Находит логи, в которых значение одного поля не превышает значение другого поля.

**Примеры:**
Например, следующий запрос отбирает логи, в которых значение поля `duration` `поля` не превышает значения поля 
`max_duration`:

```logsql
duration:le_field(max_duration)
NOT duration:le_field(max_duration)
```
