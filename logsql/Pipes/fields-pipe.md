### fields pipe

By default all the [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) are returned in the response.
It is possible to select the given set of log fields with `| fields field1, ..., fieldN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes). For example, the following query selects only `host`
and [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) fields from logs for the last 5 minutes:

```logsql
_time:5m | fields host, _msg
```

`keep` can be used instead of `fields` for convenience. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | keep host, _msg
```

It is possible to use wildcard prefixes in the list of fields to keep. For example, the following query keeps all the fields with names starting with `foo` prefix,
while drops the rest of the fields:

```logsql
_time:5m | fields foo*
```

See also:

- [`copy` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#copy-pipe)
- [`rename` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe)
- [`delete` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe)

