### Range filter

If you need to filter log message by some field containing only numeric values, then the `range()` filter can be used.
For example, if the `request.duration` field contains the request duration in seconds, then the following LogsQL query can be used
for searching for log entries with request durations exceeding 4.2 seconds:

```logsql
request.duration:range(4.2, Inf)
```

This query can be shortened by using the [range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter):

```logsql
request.duration:>4.2
```

The lower and the upper bounds of the `range(lower, upper)` are excluded by default. If they must be included, then substitute the corresponding
parentheses with square brackets. For example:

- `range[1, 10)` includes `1` in the matching range
- `range(1, 10]` includes `10` in the matching range
- `range[1, 10]` includes `1` and `10` in the matching range

The range boundaries can contain any [supported numeric values](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).

Note that the `range()` filter doesn't match [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with non-numeric values alongside numeric values. For example, `range(1, 10)` doesn't match `the request took 4.2 seconds`
[log message](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), since the `4.2` number is surrounded by other text.
Extract the numeric value from the message with [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) and then apply the `range()` [filter pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe) to the extracted field.

Performance tips:

- It is better to query pure numeric [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of extracting numeric field from text field via [transformations](https://docs.victoriametrics.com/victorialogs/logsql/#transformations) at query time.
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter)
- [IPv4 range filter](https://docs.victoriametrics.com/victorialogs/logsql/#ipv4-range-filter)
- [String range filter](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter)
- [Length range filter](https://docs.victoriametrics.com/victorialogs/logsql/#length-range-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

