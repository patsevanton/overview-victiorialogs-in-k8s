### facets pipe

`<q> | facets` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the most frequent values for every seen [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax). It also returns an estimated number of hits for every returned `field=value` pair.

For example, the following query returns the most frequent values for every seen log field across logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) over the last hour:

```logsql
_time:1h error | facets
```

It is possible to specify the number of most frequently seen values to return for each log field by using the `facets N` syntax. For example,
the following query returns up to 3 most frequently seen values for each field across logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) over the last hour:

```logsql
_time:1h error | facets 3
```

By default `facets` pipe doesn't return log fields with too many unique values, since this may require a lot of additional memory to track.
The limit can be changed during the query via `max_values_per_field M` suffix. For example, the following query returns up to 15 most frequently seen
field values across fields with up to 100000 unique values:

```logsql
_time:1h error | facets 15 max_values_per_field 100000
```

By default `facets` pipe doesn't return log fields with too long values. The limit can be changed during query via `max_value_len K` suffix.
For example, the following query returns the most frequent values for all the log fields containing values no longer than 100 bytes:

```logsql
_time:1h error | facets max_value_len 100
```

By default `facets` pipe doesn't return log fields, which contain a single constant value across all the selected logs, since such facets aren't interesting in most cases.
Add `keep_const_fields` suffix to the `facets` pipe in order to get such fields:

```logsql
_time:1h error | facets keep_const_fields
```

See also:

- [`top`](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`field_names`](https://docs.victoriametrics.com/victorialogs/logsql/#field_names-pipe)
- [`field_values`](https://docs.victoriametrics.com/victorialogs/logsql/#field_values-pipe)

