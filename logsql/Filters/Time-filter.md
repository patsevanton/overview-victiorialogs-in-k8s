### Time filter

VictoriaLogs scans all the logs for each query if it doesn't contain the filter on the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).
It uses various optimizations in order to accelerate full scan queries without the `_time` filter,
but such queries can be slow if the storage contains large number of logs over long time range. The easiest way to optimize queries
is to narrow down the search with the filter on [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).

For example, the following query returns logs ingested into VictoriaLogs during the last hour, which contain the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
at the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
_time:1h AND error
```

The following formats are supported for `_time` filter:

- `_time:duration` matches logs with timestamps on the time range `(now-duration, now]`, where `duration` can have [these values](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values). Examples:
  - `_time:5m` - returns logs for the last 5 minutes
  - `_time:2.5d15m42.345s` - returns logs for the last 2.5 days, 15 minutes and 42.345 seconds
  - `_time:1y` - returns logs for the last year
- `_time:>duration` - matches logs with timestamps older than `now-duration`.
- `_time:YYYY-MM-DDZ` - matches all the logs for the particular day by UTC. For example, `_time:2023-04-25Z` matches logs on April 25, 2023 by UTC.
- `_time:YYYY-MMZ` - matches all the logs for the particular month by UTC. For example, `_time:2023-02Z` matches logs on February, 2023 by UTC.
- `_time:YYYYZ` - matches all the logs for the particular year by UTC. For example, `_time:2023Z` matches logs on 2023 by UTC.
- `_time:YYYY-MM-DDTHHZ` - matches all the logs for the particular hour by UTC. For example, `_time:2023-04-25T22Z` matches logs on April 25, 2023 at 22 hour by UTC.
- `_time:YYYY-MM-DDTHH:MMZ` - matches all the logs for the particular minute by UTC. For example, `_time:2023-04-25T22:45Z` matches logs on April 25, 2023 at 22:45 by UTC.
- `_time:YYYY-MM-DDTHH:MM:SSZ` - matches all the logs for the particular second by UTC. For example, `_time:2023-04-25T22:45:59Z` matches logs on April 25, 2023 at 22:45:59 by UTC.
- `_time:>min_time` - matches logs with timestamps bigger than the `min_time`.
- `_time:>=min_time` - matches logs with timestamps bigger or equal to the `min_time`.
- `_time:<max_time` - matches logs with timestamps smaller than the `max_time`.
- `_time:<=max_time` - matches logs with timestamps smaller or equal to the `max_time`.
- `_time:[min_time, max_time]` - matches logs on the time range `[min_time, max_time]`, including both `min_time` and `max_time`.
    The `min_time` and `max_time` can contain any format specified [here](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#timestamp-formats).
    For example, `_time:[2023-04-01Z, 2023-04-30Z]` matches logs for the whole April, 2023 by UTC, e.g. it is equivalent to `_time:2023-04Z`.
- `_time:[min_time, max_time)` - matches logs on the time range `[min_time, max_time)`, not including `max_time`.
    The `min_time` and `max_time` can contain any format specified [here](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#timestamp-formats).
    For example, `_time:[2023-02-01Z, 2023-03-01Z)` matches logs for the whole February, 2023 by UTC, e.g. it is equivalent to `_time:2023-02Z`.

It is possible to specify time zone offset for all the absolute time formats by appending `+hh:mm` or `-hh:mm` suffix.
For example, `_time:2023-04-25+05:30` matches all the logs on April 25, 2023 by India time zone,
while `_time:2023-02-07:00` matches all the logs on February, 2023 by California time zone.

If the timezone offset information is missing, then the local time zone of the host where VictoriaLogs runs is used.
For example, `_time:2023-10-20` matches all the logs for `2023-10-20` day according to the local time zone of the host where VictoriaLogs runs.

It is possible to specify generic offset for the selected time range by appending `offset` after the `_time` filter. Examples:

- `_time:offset 1h` matches logs until `now-1h`.
- `_time:5m offset 1h` matches logs on the time range `(now-1h5m, now-1h]`.
- `_time:2023-07Z offset 5h30m` matches logs on July, 2023 by UTC with offset 5h30m.
- `_time:[2023-02-01Z, 2023-03-01Z) offset 1w` matches logs the week before the time range `[2023-02-01Z, 2023-03-01Z)` by UTC.

See also [`time_offset` option](https://docs.victoriametrics.com/victorialogs/logsql/#query-options), which allows applying the given offset to all the filters on `_time` field without the need to modify the query.

See also [`time_add` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#time_add-pipe), which allows adding the given duration to the given log field.

Performance tips:

- It is recommended to specify the smallest possible time range during the search, since it reduces the amount of log entries that need to be scanned during the query.
  For example, `_time:1h` is usually faster than `_time:5h`.

- While LogsQL supports arbitrary number of `_time:...` filters at any level of [logical filters](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter),
  it is recommended specifying a single `_time` filter at the top level of the query.

- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Day range filter](https://docs.victoriametrics.com/victorialogs/logsql/#day-range-filter)
- [Week range filter](https://docs.victoriametrics.com/victorialogs/logsql/#week-range-filter)
- [Stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)

