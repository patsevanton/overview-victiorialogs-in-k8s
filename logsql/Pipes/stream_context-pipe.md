## Конвейер stream_context

Позволяет выбирать окружающие записи логов в рамках одного потока логов, аналогично `grep -A` / `grep -B`. Возвращаемые фрагменты разделяются сообщением `---`. Должен располагаться первым после фильтров. Поддерживает `before N`, `after N`, `time_window`.

**Примеры:**

```logsql
_time:5m panic | stream_context after 10
_time:5m stacktrace | stream_context before 5
_time:5m error | stream_context before 2 after 5
_time:5m error | stream_context before 10 time_window 1w
```
