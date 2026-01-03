### field_names pipe

`<q> | field_names` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns all the names of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with an estimated number of logs for each field name returned from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query returns all the field names with the number of matching logs over the last 5 minutes:

```logsql
_time:5m | field_names
```

Field names are returned in arbitrary order. Use [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) in order to sort them if needed.

See also:

- [`field_values` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#field_values-pipe)
- [`facets` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)

