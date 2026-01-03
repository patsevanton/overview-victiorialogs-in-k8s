### pack_logfmt pipe

`<q> | pack_logfmt as field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) packs all the [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) for every log entry
returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) into [logfmt](https://brandur.org/logfmt) message and stores it as a string in the given `field_name`.

For example, the following query packs all the fields into [logfmt](https://brandur.org/logfmt) message and stores it
into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) for logs over the last 5 minutes:

```logsql
_time:5m | pack_logfmt as _msg
```

The `as _msg` part can be omitted if packed message is stored into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | pack_logfmt
```

If only a subset of fields must be packed into [logfmt](https://brandur.org/logfmt), then it must be listed inside `fields (...)` after `pack_logfmt`.
For example, the following query builds [logfmt](https://brandur.org/logfmt) message with `foo` and `bar` fields only and stores the result in `baz` field:

```logsql
_time:5m | pack_logfmt fields (foo, bar) as baz
```

It is possible to pass field prefixes into `fields (...)` in order to pack only the fields, which start with the given prefixes.
For example, the following query builds `logfmt` message with all the fields, which start with either `foo.` or `bar.`:

```logsql
_time:5m | pack_logfmt fields (foo.*, bar.*) as baz
```

The `pack_logfmt` doesn't modify or delete other fields. If you do not need them, then add [`| fields ...`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) after the `pack_logfmt` pipe. For example, the following query
leaves only the `foo` field with the original log fields packed into [logfmt](https://brandur.org/logfmt):

```logsql
_time:5m | pack_logfmt as foo | fields foo
```

See also:

- [`pack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_json-pipe)
- [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)

