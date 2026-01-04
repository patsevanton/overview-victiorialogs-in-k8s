### row_min stats

`row_min(field)` — [функция stats pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), которая возвращает [запись лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) с минимальным значением для указанного поля `field`. Запись лога возвращается в виде JSON-кодированного словаря со всеми полями из исходного лога.

Например, следующий запрос возвращает запись лога с минимальным значением поля `duration` за последние 5 минут:

```logsql
_time:5m | stats row_min(duration) as log_with_min_duration
```

Поля из возвращаемого значения можно декодировать с помощью [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) или [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe).

Если нужны только конкретные поля из возвращаемой записи лога, их можно перечислить внутри `row_min(...)`.
Например, следующий запрос возвращает только поля `_time`, `path` и `duration` из записи лога с минимальным `duration` за последние 5 минут:

```logsql
_time:5m | stats row_min(duration, _time, path, duration) as time_and_path_with_min_duration
```

Также можно вернуть все поля, начинающиеся с определённого префикса, используя синтаксис `row_min(field, prefix*)`.
