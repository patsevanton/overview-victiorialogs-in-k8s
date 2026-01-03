## Duration values

LogsQL accepts duration values with the following suffixes at places where the duration is allowed:

- `ns` - nanoseconds. For example, `123ns`.
- `µs` - microseconds. For example, `1.23µs`.
- `ms` - milliseconds. For example, `1.23456ms`
- `s` - seconds. For example, `1.234s`
- `m` - minutes. For example, `1.5m`
- `h` - hours. For example, `1.5h`
- `d` - days. For example, `1.5d`
- `w` - weeks. For example, `1w`
- `y` - years as 365 days. For example, `1.5y`

Multiple durations can be combined. For example, `1h33m55s`.

Internally duration values are converted into nanoseconds.

