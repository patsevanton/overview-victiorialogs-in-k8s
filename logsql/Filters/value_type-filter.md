### value_type filter

VictoriaLogs automatically detects types for the ingested [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) and stores log field values
according to the detected type (such as `const`, `dict`, `string`, `int64`, `float64`, etc.). Value types for stored fields can be obtained via [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe).

Sometimes it is needed to select logs with fields of a particular value type. Then `value_type(type)` filter can be used.
For example, the following filter selects logs where `user_id` field values are stored as `uint64` type:

```logsql
user_id:value_type(uint64)
```

See also:

- [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe)
- [`query_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

