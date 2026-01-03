## stats pipe functions

LogsQL supports the following functions for [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe):

- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats) returns the average value over the given numeric [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats) returns the number of log entries.
- [`count_empty`](https://docs.victoriametrics.com/victorialogs/logsql/#count_empty-stats) returns the number logs with empty [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats) returns the number of unique non-empty values for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats) returns the number of unique hashes for non-empty values at the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`histogram`](https://docs.victoriametrics.com/victorialogs/logsql/#histogram-stats) returns [VictoriaMetrics histogram](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350) for the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`json_values`](https://docs.victoriametrics.com/victorialogs/logsql/#json_values-stats) returns JSON-encoded logs as JSON array.
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-stats) returns the maximum value over the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`median`](https://docs.victoriametrics.com/victorialogs/logsql/#median-stats) returns the [median](https://en.wikipedia.org/wiki/Median) value over the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-stats) returns the minimum value over the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`quantile`](https://docs.victoriametrics.com/victorialogs/logsql/#quantile-stats) returns the given quantile for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`rate`](https://docs.victoriametrics.com/victorialogs/logsql/#rate-stats) returns the average per-second rate of matching logs on the selected time range.
- [`rate_sum`](https://docs.victoriametrics.com/victorialogs/logsql/#rate_sum-stats) returns the average per-second rate of sum for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats) returns a sample [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) for each selected [stats group](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields).
- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats) returns the [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) with the maximum value at the given field.
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats) returns the [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) with the minimum value at the given field.
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-stats) returns the sum for the given numeric [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`sum_len`](https://docs.victoriametrics.com/victorialogs/logsql/#sum_len-stats) returns the sum of lengths for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats) returns unique non-empty values for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`values`](https://docs.victoriametrics.com/victorialogs/logsql/#values-stats) returns all the values for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

### avg stats

`avg(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the average value across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Non-numeric values are ignored. If all the values are non-numeric, then `NaN` is returned.

For example, the following query returns the average value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats avg(duration) avg_duration
```

It is possible to calculate the average over fields with common prefix via `avg(prefix*)` syntax. For example, the following query calculates the average
over all the log fields with `foo` prefix:

```logsql
_time:5m | stats avg(foo*)
```

See also:

- [`median`](https://docs.victoriametrics.com/victorialogs/logsql/#median-stats)
- [`quantile`](https://docs.victoriametrics.com/victorialogs/logsql/#quantile-stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

### count stats

`count()` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of selected logs.

For example, the following query returns the number of logs over the last 5 minutes:

```logsql
_time:5m | stats count() logs
```

It is possible to calculate the number of logs with non-empty values for some [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the `count(fieldName)` syntax. For example, the following query returns the number of logs with non-empty `username` field over the last 5 minutes:

```logsql
_time:5m | stats count(username) logs_with_username
```

If multiple fields are enumerated inside `count()`, then it counts the number of logs with at least a single non-empty field mentioned inside `count()`.
For example, the following query returns the number of logs with non-empty `username` or `password` [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count(username, password) logs_with_username_or_password
```

It is possible to calculate the number of logs with at least a single non-empty field with common prefix with `count(prefix*)` syntax.
For example, the following query returns the number of logs with at least a single non-empty field with `foo` prefix over the last 5 minutes:

```logsql
_time:5m | stats count(foo*)
```

See also:

- [`rate`](https://docs.victoriametrics.com/victorialogs/logsql/#rate-stats)
- [`rate_sum`](https://docs.victoriametrics.com/victorialogs/logsql/#rate_sum-stats)
- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
- [`count_empty`](https://docs.victoriametrics.com/victorialogs/logsql/#count_empty-stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-stats)
- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats)

### count_empty stats

`count_empty(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of logs with empty `(field1, ..., fieldN)` tuples.

For example, the following query calculates the number of logs with empty `username` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
during the last 5 minutes:

```logsql
_time:5m | stats count_empty(username) logs_with_missing_username
```

It is possible to calculate the number of logs with empty fields with common prefix via `count_empty(prefix*)` syntax. For example, the following query
calculates the number of logs with empty fields with `foo` prefix during the last 5 minutes:

```logsql
_time:5m | stats count_empty(foo*)
```

See also:

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)
- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)

### count_uniq stats

`count_uniq(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of unique non-empty `(field1, ..., fieldN)` tuples.

For example, the following query returns the number of unique non-empty values for `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq(ip) ips
```

The following query returns the number of unique `(host, path)` pairs for the corresponding [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq(host, path) unique_host_path_pairs
```

Every unique value is stored in memory during query execution. A large number of unique values may require a lot of memory.
Sometimes it is necessary to know whether the number of unique values reaches a limit. In this case add `limit N` just after `count_uniq(...)`
for limiting the number of counted unique values up to `N`, while limiting the maximum memory usage. For example, the following query counts
up to `1_000_000` unique values for the `ip` field:

```logsql
_time:5m | stats count_uniq(ip) limit 1_000_000 as ips_1_000_000
```

If it is OK to count an estimated number of unique values, then [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats) can be used as faster alternative to `count_uniq`.

See also:

- [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats)
- [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

### count_uniq_hash stats

`count_uniq_hash(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of unique hashes for non-empty `(field1, ..., fieldN)` tuples.
This is a good estimate for the number of unique values in the general case, while it works faster and uses less memory than [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
when counting a large number of unique values.

For example, the following query returns an estimated number of unique non-empty values for `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq_hash(ip) unique_ips_count
```

The following query returns an estimated number of unique `(host, path)` pairs for the corresponding [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq_hash(host, path) unique_host_path_pairs
```

See also:

- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
- [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

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

See also:

- [`quantile`](https://docs.victoriametrics.com/victorialogs/logsql/#quantile-stats)
- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)

### json_values stats

`json_values(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) packs the given fields into JSON for every log entry and returns a JSON array,
which can be unrolled with [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

For example, the following query returns per-`app` JSON arrays containing [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field)
and [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) fields for the last 5 minutes:

```logsql
_time:5m | stats by (app) json_values(_time, _msg) as json_logs
```

If the list of fields is empty, then all the log fields are encoded into a JSON array:

```logsql
_time:5m | stats json_values() as json_logs
```

It is possible to select values with the given prefix via `json_values(prefix*)` syntax.

It is possible to set the upper limit on the number of JSON-encoded logs with the `limit N` suffix. For example, the following query
returns up to 3 JSON-encoded logs for every `host`:

```logsql
_time:5m | stats by (host) json_values() limit 3 as json_logs
```

It is possible to sort the selected log entries by appending `sort by (...)`. For example, the following query returns per-`host` logs
over the last 5 minutes sorted by descending order of [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field):

```logsql
_time:5m | stats by (host) json_values() sort by (_time desc) as json_logs
```

The `sort by (...)` allows selecting top N logs for each group when combined with `limit N`. For example, the following query selects up to 3 of the most recent logs for every `host`
over the last 5 minutes:

```logsql
_time:5m | stats by (host) json_values() sort by (_time desc) limit 3 as json_logs
```

See also:

- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats)
- [`values`](https://docs.victoriametrics.com/victorialogs/logsql/#values-stats)

### max stats

`max(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the maximum value across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the maximum value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats max(duration) max_duration
```

The `max(some_field)` function works with string values for the `some_field`, so it returns an empty string value if `some_field`
is missing in some of the processed logs according to [VictoriaLogs data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Use `max(some_field) if (some_field:*) as min_value_without_empty_string` syntax for filtering out empty string values.
See [conditional stats docs](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) for more details.

It is possible to calculate the maximum value across all the fields with common prefix via `max(prefix*)` syntax.

[`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats) function can be used for obtaining other fields with the maximum duration.

See also:

- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-stats)
- [`quantile`](https://docs.victoriametrics.com/victorialogs/logsql/#quantile-stats)
- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats)

### median stats

`median(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the estimated [median](https://en.wikipedia.org/wiki/Median) value across
the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query return median for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats median(duration) median_duration
```

The `median(some_field)` function works with string values for the `some_field`, so it returns an empty string value if `some_field`
is missing in some of the processed logs according to [VictoriaLogs data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Use `median(some_field) if (some_field:*) as min_value_without_empty_string` syntax for filtering out empty string values.
See [conditional stats docs](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) for more details.

It is possible to calculate the median across all the fields with common prefix via `median(prefix*)` syntax.

See also:

- [`quantile`](https://docs.victoriametrics.com/victorialogs/logsql/#quantile-stats)
- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats)

### min stats

`min(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the minimum value across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the minimum value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats min(duration) min_duration
```

The `min(some_field)` function works with string values for the `some_field`, so it returns an empty string value if `some_field`
is missing in some of the processed logs according to [VictoriaLogs data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Use `min(some_field) if (some_field:*) as min_value_without_empty_string` syntax for filtering out empty string values.
See [conditional stats docs](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) for more details.

It is possible to find the minimum across all the fields with common prefix via `min(prefix*)` syntax.

[`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats) function can be used for obtaining other fields with the minimum duration.

See also:

- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-stats)
- [`quantile`](https://docs.victoriametrics.com/victorialogs/logsql/#quantile-stats)
- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats)

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

### rate stats

`rate()` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the average per-second rate of matching logs on the selected time range.

For example, the following query returns the average per-second rate of logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) over the last 5 minutes:

```logsql
_time:5m error | stats rate()
```

See also:

- [`rate_sum`](https://docs.victoriametrics.com/victorialogs/logsql/#rate_sum-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

### rate_sum stats

`rate_sum(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the average per-second rate of the sum over the given
numeric [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the average per-second rate of the sum of `bytes_sent` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats rate_sum(bytes_sent)
```

It is possible to calculate the average per-second rate of the sum over all the fields starting with a particular prefix by using `rate_sum(prefix*)` syntax.

See also:

- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-stats)
- [`rate`](https://docs.victoriametrics.com/victorialogs/logsql/#rate-stats)

### row_any stats

`row_any()` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns an arbitrary [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
(aka sample) for each selected [stats group](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields). The log entry is returned as a JSON-encoded dictionary with all the fields from the original log.

For example, the following query returns a sample log entry for each [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
across logs for the last 5 minutes:

```logsql
_time:5m | stats by (_stream) row_any() as sample_row
```

Fields from the returned values can be decoded with [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) or [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) pipes.

If only the specific fields are needed, then they can be enumerated inside `row_any(...)`.
For example, the following query returns only `_time` and `path` fields from a sample log entry for logs over the last 5 minutes:

```logsql
_time:5m | stats row_any(_time, path) as time_and_path_sample
```

It is possible to return all the fields starting with particular prefix by using `row_any(prefix*)` syntax.

See also:

- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`json_values`](https://docs.victoriametrics.com/victorialogs/logsql/#json_values-stats)

### row_max stats

`row_max(field)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the maximum value for the given `field`. Log entry is returned as JSON-encoded dictionary with all the fields from the original log.

For example, the following query returns log entry with the maximum value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
across logs for the last 5 minutes:

```logsql
_time:5m | stats row_max(duration) as log_with_max_duration
```

Fields from the returned values can be decoded with [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) or [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) pipes.

If only the specific fields are needed from the returned log entry, then they can be enumerated inside `row_max(...)`.
For example, the following query returns only `_time`, `path` and `duration` fields from the log entry with the maximum `duration` over the last 5 minutes:

```logsql
_time:5m | stats row_max(duration, _time, path, duration) as time_and_path_with_max_duration
```

It is possible to return all the fields starting with particular prefix by using `row_max(field, prefix*)` syntax.

See also:

- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-stats)
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats)
- [`json_values`](https://docs.victoriametrics.com/victorialogs/logsql/#json_values-stats)

### row_min stats

`row_min(field)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the minimum value for the given `field`. Log entry is returned as JSON-encoded dictionary with all the fields from the original log.

For example, the following query returns log entry with the minimum value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
across logs for the last 5 minutes:

```logsql
_time:5m | stats row_min(duration) as log_with_min_duration
```

Fields from the returned values can be decoded with [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) or [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) pipes.

If only the specific fields are needed from the returned log entry, then they can be enumerated inside `row_max(...)`.
For example, the following query returns only `_time`, `path` and `duration` fields from the log entry with the minimum `duration` over the last 5 minutes:

```logsql
_time:5m | stats row_min(duration, _time, path, duration) as time_and_path_with_min_duration
```

It is possible to return all the fields starting with particular prefix by using `row_min(field, prefix*)` syntax.

See also:

- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-stats)
- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats)
- [`json_values`](https://docs.victoriametrics.com/victorialogs/logsql/#json_values-stats)

### sum stats

`sum(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the sum of numeric values across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Non-numeric values are skipped. If all the values across `field1`, ..., `fieldN` are non-numeric, then `NaN` is returned.

For example, the following query returns the sum of numeric values for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats sum(duration) sum_duration
```

It is possible to find the sum for all the fields with common prefix via `sum(prefix*)` syntax.

See also:

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)
- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-stats)

### sum_len stats

`sum_len(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the sum of byte lengths of all the values
for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the sum of byte lengths of [`_msg` fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
across all the logs for the last 5 minutes:

```logsql
_time:5m | stats sum_len(_msg) messages_len
```

It is possible to find the sum of byte lengths for all the fields with common prefix via `sum_len(prefix*)` syntax.

See also:

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)
- [`len` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#len-pipe)

### uniq_values stats

`uniq_values(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the unique non-empty values across
the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
The returned values are encoded in sorted JSON array.

For example, the following query returns unique non-empty values for the `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats uniq_values(ip) unique_ips
```

The returned unique IP addresses can be unrolled into distinct log entries with [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

Every unique value is stored in memory during query execution. Big number of unique values may require a lot of memory. Sometimes it is enough to return
only a subset of unique values. In this case add `limit N` after `uniq_values(...)` in order to limit the number of returned unique values to `N`,
while limiting the maximum memory usage.
For example, the following query returns up to `100` unique values for the `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the logs for the last 5 minutes:

```logsql
_time:5m | stats uniq_values(ip) limit 100 as unique_ips_100
```

Arbitrary subset of unique `ip` values is returned every time if the `limit` is reached.

It is possible to find unique values for all the fields with common prefix via `uniq_values(prefix*)` syntax.

See also:

- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)
- [`values`](https://docs.victoriametrics.com/victorialogs/logsql/#values-stats)
- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
- [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

### values stats

`values(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns all the values (including empty values)
for the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
The returned values are encoded in JSON array.

For example, the following query returns all the values for the `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats values(ip) ips
```

The returned IP addresses can be unrolled into distinct log entries with [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

It is possible to get values for all the fields with common prefix via `values(prefix*)` syntax.

See also:

- [`json_values`](https://docs.victoriametrics.com/victorialogs/logsql/#json_values-stats)
- [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)
- [`count_empty`](https://docs.victoriametrics.com/victorialogs/logsql/#count_empty-stats)

