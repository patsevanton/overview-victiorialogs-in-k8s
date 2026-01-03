## Numeric values

LogsQL accepts numeric values in the following formats:

- regular integers like `12345` or `-12345`
- regular floating point numbers like `0.123` or `-12.34`
- [short numeric format](https://docs.victoriametrics.com/victorialogs/logsql/#short-numeric-values)
- [duration format](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values)

### Short numeric values

LogsQL accepts integer and floating point values with the following suffixes:

- `K` and `KB` - the value is multiplied by `10^3`
- `M` and `MB` - the value is multiplied by `10^6`
- `G` and `GB` - the value is multiplied by `10^9`
- `T` and `TB` - the value is multiplied by `10^12`
- `Ki` and `KiB` - the value is multiplied by `2^10`
- `Mi` and `MiB` - the value is multiplied by `2^20`
- `Gi` and `GiB` - the value is multiplied by `2^30`
- `Ti` and `TiB` - the value is multiplied by `2^40`

All the numbers may contain `_` delimiters, which may improve readability of the query. For example, `1_234_567` is equivalent to `1234567`,
while `1.234_567` is equivalent to `1.234567`.

