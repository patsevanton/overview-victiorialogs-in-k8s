### String range filter

If you need to filter log message by some field with string values in some range, then `string_range()` filter can be used.
For example, the following LogsQL query matches log entries with `user.name` field starting from `A` and `B` chars:

```logsql
user.name:string_range(A, C)
```

The `string_range()` includes the lower bound, while excluding the upper bound. This simplifies querying distinct sets of logs.
For example, the `user.name:string_range(C, E)` would match `user.name` fields, which start from `C` and `D` chars.

See also:

- [Range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter)
- [Range filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter)
- [IPv4 range filter](https://docs.victoriametrics.com/victorialogs/logsql/#ipv4-range-filter)
- [Length range filter](https://docs.victoriametrics.com/victorialogs/logsql/#length-range-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

