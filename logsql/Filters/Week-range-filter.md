### Week range filter

`_time:week_range[start, end]` filter allows returning logs on the particular `start ... end` days for each week, where `start` and `end` can have the following values:

- `Sun` or `Sunday`
- `Mon` or `Monday`
- `Tue` or `Tuesday`
- `Wed` or `Wednesday`
- `Thu` or `Thursday`
- `Fri` or `Friday`
- `Sat` or `Saturday`

For example, the following query matches logs between Monday and Friday UTC every day:

```logsql
_time:week_range[Mon, Fri]
```

This query includes Monday and Friday.
Replace `[` with `(` in order to exclude the starting day. Replace `]` with `)` in order to exclude the ending day.
For example, the following query matches logs between Sunday and Saturday, excluding Sunday and Saturday (e.g. it is equivalent to the previous query):

```logsql
_time:week_range(Sun, Sat)
```

If the day range must be applied to other than UTC time zone, then add `offset <duration>`, where `<duration>` can have [any supported duration value](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
For example, the following query selects logs between Monday and Friday at `+0200` time zone:

```logsql
_time:week_range[Mon, Fri] offset 2h
```

The `week_range` filter can be combined with [`day_range` filter](https://docs.victoriametrics.com/victorialogs/logsql/#day-range-filter) using [logical filters](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter). For example, the following query
selects logs between `08:00` and `18:00` every day of the week excluding Sunday and Saturday:

```logsql
_time:week_range[Mon, Fri] _time:day_range[08:00, 18:00)
```

Performance tip: it is recommended to specify a regular [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) additionally to the `week_range` filter. For example, the following query selects logs
between Monday and Friday for each week over the last 4 weeks:

```logsql
_time:4w _time:week_range[Mon, Fri]
```

See also:

- [Day range filter](https://docs.victoriametrics.com/victorialogs/logsql/#day-range-filter)
- [Time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter)

