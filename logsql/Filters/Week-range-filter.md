### Фильтр диапазона дней недели

`_time:week_range[start, end]` — фильтрует логи по дням недели от `start` до `end`.

Дни можно задавать коротко или полностью: `Sun/Sunday`, `Mon/Monday`, …, `Sat/Saturday`.

**Включение/исключение границ:**

* `[` и `]` — включают день.
* `(` и `)` — исключают день.

**Примеры:**

```logsql
_time:week_range[Mon, Fri]           // понедельник–пятница включительно
_time:week_range(Sun, Sat)           // исключая воскресенье и субботу
```

**Часовой пояс:**

```logsql
_time:week_range[Mon, Fri] offset 2h
```

**Комбинация с day_range:**

```logsql
_time:week_range[Mon, Fri] _time:day_range(08:00, 18:00)
```
