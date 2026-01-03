### rate stats

`rate()` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the average per-second rate of matching logs on the selected time range.

For example, the following query returns the average per-second rate of logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) over the last 5 minutes:

```logsql
_time:5m error | stats rate()
```

See also:

- [`rate_sum`](https://docs.victoriametrics.com/victorialogs/logsql/#rate_sum-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

