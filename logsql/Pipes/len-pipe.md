### `len` (длина) — конвейер (pipe)

Конструкция  
```
<q> | len(field) as result
```  
сохраняет **длину в байтах** значения указанного поля `field` в новое поле `result` — для всех логов, возвращённых запросом `<q>`.

**Пример.** Следующий запрос выводит 5 записей логов с максимальной длиной поля `_msg` за последние 5 минут:

```logsql
_time:5m | len(_msg) as msg_len | sort by (msg_len desc) | limit 5
```

**Пояснения к примеру:**
- `_time:5m` — фильтрует логи за последние 5 минут;
- `len(_msg) as msg_len` — вычисляет длину поля `_msg` в байтах и сохраняет в поле `msg_len`;
- `sort by (msg_len desc)` — сортирует записи по убыванию значения `msg_len`;
- `limit 5` — ограничивает вывод 5 записями.

**См. также:**
- конвейер [`json_array_len`](https://docs.victoriametrics.com/victorialogs/logsql/#json_array_len-pipe) — длина JSON‑массива;
- статистическая функция [`sum_len`](https://docs.victoriametrics.com/victorialogs/logsql/#sum_len-stats) — сумма длин;
- конвейер [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) — сортировка;
- конвейер [`limit`](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe) — ограничение числа записей;
- конвейер [`block_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe) — статистика по блокам.
