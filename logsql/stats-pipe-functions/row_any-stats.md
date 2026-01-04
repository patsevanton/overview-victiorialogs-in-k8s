### Статистика `row_any`

Функция конвейера статистики [`row_any()`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) возвращает произвольную [запись лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
(также называемую sample) для каждой выбранной [группы статистики](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields). Запись лога возвращается в виде JSON-кодированного словаря со всеми полями исходного лога.

Например, следующий запрос возвращает одну примерную запись лога для каждого [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
среди логов за последние 5 минут:

```logsql
_time:5m | stats by (_stream) row_any() as sample_row
```

Поля из возвращаемых значений можно декодировать с помощью конвейеров [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) или [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe).

Если нужны только конкретные поля, их можно перечислить внутри `row_any(...)`.
Например, следующий запрос возвращает только поля `_time` и `path` из примерной записи лога за последние 5 минут:

```logsql
_time:5m | stats row_any(_time, path) as time_and_path_sample
```

Также можно вернуть все поля, начинающиеся с определённого префикса, используя синтаксис `row_any(prefix*)`.
