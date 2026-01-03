### Фильтр «множественного точного совпадения» (multi‑exact filter)

Иногда требуется найти сообщения журнала (логи), в которых определённое поле содержит одно из заданных значений. Это можно сделать с помощью нескольких **[фильтров точного совпадения](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)**, объединённых в единый **[логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)**.

Например, следующий запрос подберёт сообщения журнала, в поле `log.level` которых содержится *точно* одно из значений: `error` или `fatal`:

```logsql
log.level:(="error" OR ="fatal")
```

Хотя такое решение работает, в LogsQL есть более простой и быстрый способ для этого случая — фильтр `in()`.

```logsql
log.level:in("error", "fatal")
```

Этот фильтр работает очень быстро, даже если в `in()` передаётся длинный список значений.

Есть особый случай — `in(*)`. Такой фильтр сопоставляется со *всеми* логами. Подробнее см. в документации по **[фильтру без действия (no‑op filter)](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter)**.

Внутри фильтра `in(...)` можно передать произвольный **[запрос](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)**, чтобы сопоставлять значения с результатами этого запроса. Подробности — в документации по **[фильтру с подзапросом (subquery filter)](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)**.
