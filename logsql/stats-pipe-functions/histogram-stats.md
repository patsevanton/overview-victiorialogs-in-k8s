### histogram stats

`histogram(field)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns [VictoriaMetrics histogram buckets](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350)
for the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns histogram buckets for the `response_size` field grouped by `host` field, across logs for the last 5 minutes:

```logsql
_time:5m | stats by (host) histogram(response_size)
```

If the field contains [duration value](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values), then `histogram` normalizes it to nanoseconds. For example, `1.25ms` is normalized to `1_250_000`.

If the field contains [short numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#short-numeric-values), then `histogram` normalizes it to numeric value without any suffixes. For example, `1KiB` is converted to `1024`.

Histogram buckets are returned as the following JSON array:

```json
[{"vmrange":"...","hits":...},...,{"vmrange":"...","hits":...}]
```

Every `vmrange` value contains value range for the corresponding [VictoriaMetrics histogram bucket](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350),
while `hits` contains the number of values, which hit the given bucket.

It may be handy to unroll the returned histogram buckets for further processing during the query. For example, the following query
calculates a histogram over the `response_size` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
and then unrolls it into distinct rows with `vmrange` and `hits` fields with the help of [`unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) and [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) pipes:

```logsql
_time:5m
  | stats histogram(response_size) as buckets
  | unroll (buckets)
  | unpack_json from buckets
```
