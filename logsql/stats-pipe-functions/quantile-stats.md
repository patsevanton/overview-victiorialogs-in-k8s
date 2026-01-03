### quantile stats

`quantile(phi, field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates an estimated `phi` [percentile](https://en.wikipedia.org/wiki/Percentile) over values
for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model). The `phi` must be in the range `0 ... 1`, where `0` means `0th` percentile,
while `1` means `100th` percentile.

For example, the following query calculates `50th`, `90th` and `99th` percentiles for the `request_duration_seconds` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats
  quantile(0.5, request_duration_seconds) p50,
  quantile(0.9, request_duration_seconds) p90,
  quantile(0.99, request_duration_seconds) p99
```

The `quantile(phi, some_field)` function works with string values for the `some_field`, so it returns an empty string value if `some_field`
is missing in some of the processed logs according to [VictoriaLogs data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Use `quantile(phi, some_field) if (some_field:*) as min_value_without_empty_string` syntax for filtering out empty string values.
See [conditional stats docs](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) for more details.

It is possible to calculate the quantile across all the fields with common prefix via `quantile(phi, prefix*)` syntax.

See also:

- [`histogram`](https://docs.victoriametrics.com/victorialogs/logsql/#histogram-stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-stats)
- [`median`](https://docs.victoriametrics.com/victorialogs/logsql/#median-stats)
- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats)

