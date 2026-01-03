### sample pipe

The `<q> | sample N` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns `1/N`th random sample of logs for the `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
For example, the following query returns ~1% (1/100th random sample) of logs over the last hour with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
_time:1h error | sample 100
```

See also:

- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)

