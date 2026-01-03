### Конвейер `set_stream_fields`

Конвейер `| set_stream_fields поле1, ..., полеN` задаёт указанные [поля логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) в качестве полей [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).

Например, если в логах, возвращённых фильтром `_time:5m`, присутствуют поля `host="foo"` и `path="/bar"`, то следующий запрос установит поле `_stream` равным `{host="foo", path="/bar"}`:

```logsql
_time:5m | set_stream_fields host, path
```

#### Условный `set_stream_fields`

Конвейер [`set_stream_fields`](https://docs.victoriametrics.com/victorialogs/logsql/#set_stream_fields-pipe) можно применить лишь к подмножеству входных логов, соответствующих заданным [фильтрам](https://docs.victoriametrics.com/victorialogs/logsql/#filters), — для этого после `set_stream_fields` используется конструкция `if (...)`.

Например, следующий запрос обновит поле [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) **только** для логов с полем `host="foobar"`, оставив исходное значение `_stream` для остальных логов:

```logsql
_time:5m | set_stream_fields if (host:="foobar") host, app
```
