### pack_json pipe

`<q> | pack_json as field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) packs all the [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of every log
entry returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) into JSON object and stores it as a string in the given `field_name`.

For example, the following query packs all the fields into JSON object and stores it into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
for logs over the last 5 minutes:

```logsql
_time:5m | pack_json as _msg
```

The `as _msg` part can be omitted if packed JSON object is stored into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | pack_json
```

If only a subset of fields must be packed into JSON, then it must be listed inside `fields (...)` after `pack_json`. For example, the following query builds JSON with `foo` and `bar` fields
only and stores the result in `baz` field:

```logsql
_time:5m | pack_json fields (foo, bar) as baz
```

It is possible to pass field prefixes into `fields (...)` in order to pack only the fields, which start with the given prefixes.
For example, the following query builds JSON with all the fields, which start with either `foo.` or `bar.`:

```logsql
_time:5m | pack_json fields (foo.*, bar.*) as baz
```

The `pack_json` doesn't modify or delete other fields. If you do not need them, then add [`| fields ...`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) after the `pack_json` pipe. For example, the following query
leaves only the `foo` field with the original log fields packed into JSON:

```logsql
_time:5m | pack_json as foo | fields foo
```

See also:

- [`pack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_logfmt-pipe)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)

