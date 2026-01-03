### stats pipe

The `<q> | stats ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) calculates various stats over the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
For example, the following LogsQL query uses [`count` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats) for calculating the number of logs for the last 5 minutes:

```logsql
_time:5m | stats count() as logs_total
```

The `| stats ...` pipe has the following basic format:

```logsql
... | stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Where `stats_func*` is any of the supported [stats function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), while the `result_name*` is the name of the log field
to store the result of the corresponding stats function. The `as` keyword is optional.

For example, the following query calculates the following stats for logs over the last 5 minutes:

- the number of logs with the help of [`count` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats);
- the number of unique [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) with the help of [`count_uniq` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats):

```logsql
_time:5m | stats count() logs_total, count_uniq(_stream) streams_total
```

It is allowed omitting `stats` prefix for convenience. So the following query is equivalent to the previous one:

```logsql
_time:5m | count() logs_total, count_uniq(_stream) streams_total
```

It is allowed omitting the result name. In this case the result name equals the string representation of the used [stats function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions).
For example, the following query returns the same stats as the previous one, but gives `count()` and `count_uniq(_stream)` names for the returned fields:

```logsql
_time:5m | count(), count_uniq(_stream)
```

See also:

- [stats pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [stats by fields](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields)
- [stats by time buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets)
- [stats by time buckets with timezone offset](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets-with-timezone-offset)
- [stats by field buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-field-buckets)
- [stats by IPv4 buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-ipv4-buckets)
- [stats with additional filters](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters)
- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)

#### Stats by fields

The following LogsQL syntax can be used for calculating independent stats per group of log fields:

```logsql
<q> | stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `(field1, ..., fieldM)` group of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
seen in the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates the number of logs and unique IP addresses over the last 5 minutes,
grouped by `(host, path)` fields:

```logsql
_time:5m | stats by (host, path) count() logs_total, count_uniq(ip) ips_total
```

The `by` keyword can be skipped in `stats ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | stats (host, path) count() logs_total, count_uniq(ip) ips_total
```

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats)

#### Stats by time buckets

The following syntax can be used for calculating stats grouped by time buckets:

```logsql
<q> | stats by (_time:step)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `step` of the [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) field
across logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax). The `step` can have any [duration value](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
For example, the following LogsQL query returns per-minute number of logs and unique IP addresses over the last 5 minutes:

```logsql
_time:5m | stats by (_time:1m) count() logs_total, count_uniq(ip) ips_total
```

It might be useful to calculate running stats over the calculated per-time bucket stats, with the help of [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe).
For example, the following query adds the running number of logs to the `running_hits` field for the query above:

```logsql
_time:5m
    | stats by (_time:1m) count() as hits
    | running_stats sum(hits) as running_hits
```

It might be useful to calculate total stats over the calculated per-time bucket stats, with the help of [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe).
For example, the following query adds the total number of logs into `total_hits` field and then uses this field for calculating the per-minute percentage of hits
with the [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe):

```logsql
_time:5m
    | stats by (_time:1m) count() as hits
    | total_stats sum(hits) as total_hits
    | math round((hits / total_hits)*100) as hits_percent
```

Additionally, the following `step` values are supported:

- `nanosecond` - equals `1ns` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `microsecond` - equals `1µs` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `millisecond` - equals `1ms` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `second` - equals `1s` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `minute` - equals `1m` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `hour` - equals `1h` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `day` - equals `1d` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `week` - equals `1w` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `month` - equals one month. It properly takes into account the number of days in each month.
- `year` - equals one year. It properly takes into account the number of days in each year.

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)

#### Stats by time buckets with timezone offset

VictoriaLogs stores [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) values as [Unix time](https://en.wikipedia.org/wiki/Unix_time)
in nanoseconds. This time corresponds to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) time zone. Sometimes it is needed calculating stats
grouped by days or weeks at non-UTC timezone. This is possible with the following syntax:

```logsql
<q> | stats by (_time:step offset timezone_offset) ...
```

For example, the following query calculates per-day number of logs over the last week, in `UTC+02:00` [time zone](https://en.wikipedia.org/wiki/Time_zone):

```logsql
_time:1w | stats by (_time:1d offset 2h) count() logs_total
```

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)

#### Stats by field buckets

Every log field inside `<q> | stats by (...)` can be bucketed in the same way as `_time` field in [this example](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets).
Any [numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values) can be used as `step` value for the bucket. For example, the following query calculates
the number of requests for the last hour, bucketed by 10KB of `request_size_bytes` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
_time:1h | stats by (request_size_bytes:10KB) count() requests
```

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)

#### Stats by IPv4 buckets

Stats can be bucketed by [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) containing [IPv4 addresses](https://en.wikipedia.org/wiki/IP_address)
via the `ip_field_name:/network_mask` syntax inside `by(...)` clause. For example, the following query returns the number of log entries per `/24` subnetwork
extracted from the `ip` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) during the last 5 minutes:

```logsql
_time:5m | stats by (ip:/24) count() requests_per_subnet
```

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`ipv4_range` filter](https://docs.victoriametrics.com/victorialogs/logsql/#ipv4-range-filter)

#### Stats with additional filters

Sometimes it is needed to calculate [stats](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) on different subsets of matching logs. This can be done by inserting an `if (<any_filters>)` condition
between the [stats function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) and `result_name`, where `any_filters` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters).
For example, the following query calculates individually the number of [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with `GET`, `POST` and `PUT` [words](https://docs.victoriametrics.com/victorialogs/logsql/#word), additionally to the total number of logs over the last 5 minutes:

```logsql
_time:5m | stats
  count() if (GET) gets,
  count() if (POST) posts,
  count() if (PUT) puts,
  count() total
```

If zero input rows match the given `if (...)` filter, then zero result is returned for the given stats function.

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)

