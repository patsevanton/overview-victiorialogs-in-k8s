### Конвейер `set_stream_fields`

Конвейер `| set_stream_fields поле1, ..., полеN` задаёт указанные `поля логов` в качестве полей ``_stream``.

Например, если в логах, возвращённых фильтром `_time:5m`, присутствуют поля `host="foo"` и `path="/bar"`, то следующий запрос установит поле `_stream` равным `{host="foo", path="/bar"}`:

```logsql
_time:5m | set_stream_fields host, path
```

#### Условный `set_stream_fields`

Конвейер ``set_stream_fields`` можно применить лишь к подмножеству входных логов, соответствующих заданным `фильтрам`, — для этого после `set_stream_fields` используется конструкция `if (...)`.

Например, следующий запрос обновит поле ``_stream`` **только** для логов с полем `host="foobar"`, оставив исходное значение `_stream` для остальных логов:

```logsql
_time:5m | set_stream_fields if (host:="foobar") host, app
```
