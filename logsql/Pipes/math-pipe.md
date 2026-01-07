## Конвейер math (математические вычисления)

Выполняет математические вычисления над числовыми значениями полей. Поддерживает операции: `+`, `-`, `*`, `/`, `%`, `^`, `&`, `or`, `xor`, `default`, функции: `abs`, `ceil`, `exp`, `floor`, `ln`, `max`, `min`, `now()`, `rand()`, `round`. Можно использовать `eval` вместо `math`.

**Примеры:**

```logsql
_time:5m | math round(duration_msecs / 1000) as duration_secs
_time:5m | eval (duration_secs * 1000) as duration_msecs
_time:5m | math round(request_duration, 1e9) as request_duration_nsecs | format '<duration:request_duration_nsecs>' as request_duration
```
