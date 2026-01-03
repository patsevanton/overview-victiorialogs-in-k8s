### len pipe

`<q> | len(field) as result` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) stores byte length of the given `field` value into the `result` field
across all the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query shows top 5 log entries with the maximum byte length of `_msg` field across
logs for the last 5 minutes:

```logsql
_time:5m | len(_msg) as msg_len | sort by (msg_len desc) | limit 5
```

See also:

- [`json_array_len` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#json_array_len-pipe)
- [`sum_len` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#sum_len-stats)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)
- [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe)

