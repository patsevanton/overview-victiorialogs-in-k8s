### hash pipe

`<q> | hash(field) as result_field` calculates hash value for the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
and stores it into the `result_field`, for every log entry returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates the hash value over `user_id` field and stores it into `user_id_hash` field, across logs for the last 5 minutes:

```logsql
_time:5m | hash(user_id) as user_id_hash
```

See also:

- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`filter` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe)

