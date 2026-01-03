### Stream filter

VictoriaLogs provides an optimized way to select logs, which belong to particular [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
This can be done via `{...}` filter, which may contain arbitrary
[Prometheus-compatible label selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering)
over fields associated with [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
For example, the following query selects [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with `app` field equal to `nginx`:

```logsql
{app="nginx"}
```

This query is equivalent to the following [`exact` filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter) query, but the upper query usually works much faster:

```logsql
app:="nginx"
```

The stream filter supports `{label in (v1,...,vN)}` and `{label not_in (v1,...,vN)}` syntax.
It is equivalent to `{label=~"v1|...|vN"}` and `{label!~"v1|...|vN"}` respectively. The `v1`, ..., `vN` are properly escaped inside the regexp.
For example, `{app in ("nginx", "foo.bar")}` is equivalent to `{app=~"nginx|foo\\.bar"}` - note that the `.` char is properly escaped.

It is allowed to add `_stream:` prefix in front of `{...}` filter in order to make clear that the filtering is performed
on the [`_stream` log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
The following filter is equivalent to `{app="nginx"}`:

```logsql
_stream:{app="nginx"}
```

Performance tips:

- It is recommended to use the most specific `{...}` filter matching the smallest number of log streams,
  which needs to be scanned by the rest of filters in the query.

- While LogsQL supports arbitrary number of `{...}` filters at any level of [logical filters](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter),
  it is recommended specifying a single `{...}` filter at the top level of the query.

- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [`_stream_id` filter](https://docs.victoriametrics.com/victorialogs/logsql/#_stream_id-filter)
- [Time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)

