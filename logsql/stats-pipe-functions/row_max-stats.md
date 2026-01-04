### row_max stats

Функция `row_max(field)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) возвращает [лог-запись](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) с максимальным значением для указанного `field`. Лог-запись возвращается в виде словаря, закодированного в JSON, со всеми полями из оригинального лога.

Например, следующий запрос возвращает лог-запись с максимальным значением для поля `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) среди логов за последние 5 минут:

```logsql
_time:5m | stats row_max(duration) as log_with_max_duration
```

Поля из возвращаемой записи можно декодировать с помощью [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) или [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe).

Если нужны только определённые поля из возвращаемой лог-записи, их можно перечислить внутри `row_max(...)`.
Например, следующий запрос возвращает только поля `_time`, `path` и `duration` из лог-записи с максимальным `duration` за последние 5 минут:

```logsql
_time:5m | stats row_max(duration, _time, path, duration) as time_and_path_with_max_duration
```

Также можно вернуть все поля, начинающиеся с определённого префикса, используя синтаксис `row_max(field, prefix*)`.
