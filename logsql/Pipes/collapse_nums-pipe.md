## Конвейер collapse_nums

Заменяет все десятичные и шестнадцатеричные числа в указанном поле на заполнитель `<N>`. Если применяется к `_msg`, суффикс `at ...` можно опустить. Поддерживает `prettify` для распознавания шаблонов (UUID, IP4, TIME, DATE, DATETIME), условное применение `if (...)`.

**Примеры:**

```logsql
_time:5m | collapse_nums at _msg
_time:5m | collapse_nums
_time:1h | collapse_nums | top 5 by (_msg)
_time:1h | collapse_nums prettify
_time:5m | collapse_nums if (user_type:=admin) at foo
```
