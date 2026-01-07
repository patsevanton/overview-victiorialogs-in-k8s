## Логический фильтр

Объединяет базовые фильтры с помощью логических операций: `AND`, `OR`, `NOT` (или `-`, `!`). Приоритет: `NOT` > `AND` > `OR`. Можно использовать скобки для изменения порядка.

**Примеры:**

```logsql
error AND file AND app
error file app
error OR warning OR info
NOT info
-info
log.level:(error OR warning OR info)
NOT (info OR debug)
```
