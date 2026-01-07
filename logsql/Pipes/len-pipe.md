## len (длина) — конвейер

Сохраняет длину в байтах значения указанного поля в новое поле.

**Примеры:**

```logsql
_time:5m | len(_msg) as msg_len | sort by (msg_len desc) | limit 5
```
