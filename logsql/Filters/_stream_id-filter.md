### _stream_id filter

Every [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) in VictoriaLogs is uniquely identified by `_stream_id` field.
The `_stream_id:...` filter allows quickly selecting all the logs belonging to the particular stream.

For example, the following query selects all the logs, which belong to the [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
with `_stream_id` equal to `0000007b000001c850d9950ea6196b1a4812081265faa1c7`:

```logsql
_stream_id:0000007b000001c850d9950ea6196b1a4812081265faa1c7
```

If the log stream contains too many logs, then it is a good idea to limit the number of returned logs with a [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter). For example, the following
query selects logs for the given stream for the last hour:

```logsql
_time:1h _stream_id:0000007b000001c850d9950ea6196b1a4812081265faa1c7
```

The `_stream_id` filter supports specifying multiple `_stream_id` values via `_stream_id:in(...)` syntax. For example:

```logsql
_stream_id:in(0000007b000001c850d9950ea6196b1a4812081265faa1c7, 1230007b456701c850d9950ea6196b1a4812081265fff2a9)
```

It is also possible to specify a subquery inside `in(...)`, which selects the needed `_stream_id` values. For example, the following query returns
logs for [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) containing `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) during the last 5 minutes:

```logsql
_stream_id:in(_time:5m error | fields _stream_id)
```

See also:

- [subquery filter](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)
- [stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)

