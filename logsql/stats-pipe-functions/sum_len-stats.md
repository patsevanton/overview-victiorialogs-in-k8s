## Статистика sum_len

Вычисляет сумму байтовых длин всех значений для указанных полей логов. Поддерживает префиксы.

**Примеры:**

```logsql
_time:5m | stats sum_len(_msg) messages_len
_time:5m | stats sum_len(prefix*)
```
