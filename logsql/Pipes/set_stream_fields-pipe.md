### set_stream_fields pipe

The `| set_stream_fields field1, ..., fieldN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes)
sets the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
as [`_stream` fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).

For example, if the logs returned by `_time:5m` [filter](https://docs.victoriametrics.com/victorialogs/logsql/#filters) have `host="foo"` and `path="/bar"` fields,
then the following query sets `_stream` field to `{host="foo", path="/bar"}`:

```logsql
_time:5m | set_stream_fields host, path
```

See also:

- [conditional `set_stream_fields`](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-set_stream_fields)
- [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe)

#### Conditional set_stream_fields

The [`set_stream_fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#set_stream_fields-pipe) can be applied to a subset of input logs
which match the given [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters), by using `if (...)` after the `set_stream_fields`.
For example, the following query updates [`_stream` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
only for logs with the `host="foobar"` field, while leaving the original `_stream` value for the rest of the logs:

```logsql
_time:5m | set_stream_fields if (host:="foobar") host, app
```

