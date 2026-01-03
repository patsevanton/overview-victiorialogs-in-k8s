### unpack_logfmt pipe

`<q> | unpack_logfmt from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks `k1=v1 ... kN=vN` [logfmt](https://brandur.org/logfmt) fields
from the given [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `k1`, ... `kN` field names
with the corresponding `v1`, ..., `vN` values. It overrides existing fields with names from the `k1`, ..., `kN` list. Other fields remain untouched.

For example, the following query unpacks [logfmt](https://brandur.org/logfmt) fields from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
across logs for the last 5 minutes:

```logsql
_time:5m | unpack_logfmt from _msg
```

The `from _msg` part can be omitted when [logfmt](https://brandur.org/logfmt) fields are unpacked from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_logfmt
```

If only some fields must be unpacked from logfmt, then they can be enumerated inside `fields (...)`. For example, the following query extracts only `foo` and `bar` fields
from logfmt stored in the `my_logfmt` field:

```logsql
_time:5m | unpack_logfmt from my_logfmt fields (foo, bar)
```

If it is needed to extract all the fields with some common prefix, then this can be done via `fields(prefix*)` syntax.

If it is needed to preserve the original non-empty field values, then add `keep_original_fields` to the end of `unpack_logfmt ...`. For example,
the following query preserves the original non-empty values for `ip` and `host` fields instead of overwriting them with the unpacked values:

```logsql
_time:5m | unpack_logfmt from foo fields (ip, host) keep_original_fields
```

Add `skip_empty_results` to the end of `unpack_logfmt ...` if the original field values must be preserved when the corresponding unpacked values are empty.
For example, the following query preserves the original `ip` and `host` field values for empty unpacked values:

```logsql
_time:5m | unpack_logfmt fields (ip, host) skip_empty_results
```

Performance tip: if you need to extract a single field from a long [logfmt](https://brandur.org/logfmt) line, it is faster to use the [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe).
For example, the following query extracts `"ip"` field from [logfmt](https://brandur.org/logfmt) line stored
in [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```
_time:5m | extract ' ip=<ip>'
```

If you want to make sure that the unpacked [logfmt](https://brandur.org/logfmt) fields do not clash with the existing fields, then specify common prefix for all the fields extracted from logfmt,
by adding `result_prefix "prefix_name"` to `unpack_logfmt`. For example, the following query adds `foo_` prefix for all the unpacked fields
from `foo` field:

```logsql
_time:5m | unpack_logfmt from foo result_prefix "foo_"
```

Performance tips:

- It is better from performance and resource usage PoV ingesting parsed [logfmt](https://brandur.org/logfmt) logs into VictoriaLogs
  according to the [supported data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of ingesting unparsed logfmt lines into VictoriaLogs and then parsing them at query time with [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe).

- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `unpack_logfmt`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional unpack_logfmt](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-unpack_logfmt)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
- [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Conditional unpack_logfmt

If the [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unpack_logfmt`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unpacks logfmt fields from `foo` field
only if `ip` field in the current log entry isn't set or empty:

```logsql
_time:5m | unpack_logfmt if (ip:"") from foo
```

