### field_values pipe

`<q> | field_values field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns all the values for the given [`field_name` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the number of logs for each value returned from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
For example, the following query returns all the values with the number of matching logs for the field `level` over logs for the last 5 minutes:

```logsql
_time:5m | field_values level
```

It is possible to limit the number of returned values by adding `limit N` to the end of `field_values ...`. For example, the following query returns
up to 10 values for the field `user_id` over logs for the last 5 minutes:

```logsql
_time:5m | field_values user_id limit 10
```

If the limit is reached, then the set of returned values is random. Also the number of matching logs for each returned value is zeroed for performance reasons.

See also:

- [`field_names` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#field_names-pipe)
- [`facets` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)

