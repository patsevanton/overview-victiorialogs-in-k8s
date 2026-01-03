### Day range filter

`_time:day_range[start, end]` filter allows returning logs in the particular `start ... end` time for each day, where `start` and `end` have the format `hh:mm`.
For example, the following query matches logs between `08:00` and `18:00` UTC every day:

```logsql
_time:day_range[08:00, 18:00)
```

This query includes `08:00`, while `18:00` is excluded, e.g. the last matching time is `17:59:59.999999999`.
Replace `[` with `(` in order to exclude the starting time. Replace `)` with `]` in order to include the ending time.
For example, the following query matches logs between `08:00` and `18:00`, excluding `08:00:00.000000000` and including `18:00`:

```logsql
_time:day_range(08:00, 18:00]
```

If the time range must be applied to other than UTC time zone, then add `offset <duration>`, where `<duration>` can have [any supported duration value](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
For example, the following query selects logs between `08:00` and `18:00` at `+0200` time zone:

```logsql
_time:day_range[08:00, 18:00) offset 2h
```

Performance tip: it is recommended to specify a regular [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) additionally to the `day_range` filter. For example, the following query selects logs
between `08:00` and `18:00` every day for the last week:

```logsql
_time:1w _time:day_range[08:00, 18:00)
```

See also:

- [Week range filter](https://docs.victoriametrics.com/victorialogs/logsql/#week-range-filter)
- [Time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter)

