### unpack_json pipe

`<q> | unpack_json from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks `{"k1":"v1", ..., "kN":"vN"}` JSON from the given [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `k1`, ... `kN` output field names with the corresponding `v1`, ..., `vN` values.
It overrides existing fields with names from the `k1`, ..., `kN` list. Other fields remain untouched.

Nested JSON is unpacked according to the rules defined [here](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query unpacks JSON fields from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) across logs for the last 5 minutes:

```logsql
_time:5m | unpack_json from _msg
```

The `from _msg` part can be omitted when JSON fields are unpacked from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_json
```

If only some fields must be extracted from JSON, then they can be enumerated inside `fields (...)`. For example, the following query unpacks only `foo` and `bar`
fields from JSON value stored in `my_json` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
_time:5m | unpack_json from my_json fields (foo, bar)
```

If it is needed to extract all the fields with some common prefix, then this can be done via `fields(prefix*)` syntax.

If it is needed to preserve the original non-empty field values, then add `keep_original_fields` to the end of `unpack_json ...`. For example,
the following query preserves the original non-empty values for `ip` and `host` fields instead of overwriting them with the unpacked values:

```logsql
_time:5m | unpack_json from foo fields (ip, host) keep_original_fields
```

Add `skip_empty_results` to the end of `unpack_json ...` if the original field values must be preserved when the corresponding unpacked values are empty.
For example, the following query preserves the original `ip` and `host` field values for empty unpacked values:

```logsql
_time:5m | unpack_json fields (ip, host) skip_empty_results
```

Performance tip: if you need to extract a single field from long JSON, it is faster to use the [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe). For example, the following query extracts the `"ip"` field from JSON
stored in [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) at the maximum speed:

```
_time:5m | extract '"ip":<ip>'
```

If you want to make sure that the unpacked JSON fields do not clash with the existing fields, then specify common prefix for all the fields extracted from JSON,
by adding `result_prefix "prefix_name"` to `unpack_json`. For example, the following query adds the `foo_` prefix for all the unpacked fields
from `foo`:

```logsql
_time:5m | unpack_json from foo result_prefix "foo_"
```

Performance tips:

- It is better from performance and resource usage PoV ingesting parsed JSON logs into VictoriaLogs
  according to the [supported data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of ingesting unparsed JSON lines into VictoriaLogs and then parsing them at query time with [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe).

- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `unpack_json`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional `unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-unpack_json)
- [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)
- [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`split` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#split-pipe)
- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`pack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_json-pipe)
- [`pack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_logfmt-pipe)

#### Conditional unpack_json

If the [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unpack_json`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unpacks JSON fields from `foo` field only if `ip` field in the current log entry isn't set or empty:

```logsql
_time:5m | unpack_json if (ip:"") from foo
```

