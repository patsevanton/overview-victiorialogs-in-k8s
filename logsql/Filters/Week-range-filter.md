## Фильтр диапазона дней недели

Фильтрует логи по дням недели. Дни: `Sun/Sunday`, `Mon/Monday`, ..., `Sat/Saturday`. Границы: `[`/`]` — включить, `(`/`)` — исключить.

**Примеры:**

```logsql
_time:week_range[Mon, Fri]
_time:week_range(Sun, Sat)
_time:week_range[Mon, Fri] offset 2h
_time:week_range[Mon, Fri] _time:day_range(08:00, 18:00)
```
