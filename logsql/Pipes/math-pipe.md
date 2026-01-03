### math pipe

`<q> | math ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) performs mathematical calculations over [numeric values](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values) of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax). It has the following format:

```
| math
  expr1 as resultName1,
  ...
  exprN as resultNameN
```

Where `exprX` is one of the supported math expressions mentioned below, while `resultNameX` is the name of the field to store the calculated result to.
The `as` keyword is optional. The result name can be omitted. In this case the result is stored to a field with the name equal to string representation
of the corresponding math expression.

`exprX` may reference `resultNameY` calculated before the given `exprX`.

For example, the following query divides `duration_msecs` field value by 1000, then rounds it to integer and stores the result in the `duration_secs` field:

```logsql
_time:5m | math round(duration_msecs / 1000) as duration_secs
```

The following mathematical operations are supported by `math` pipe:

- `arg1 + arg2` - returns the sum of `arg1` and `arg2`
- `arg1 - arg2` - returns the difference between `arg1` and `arg2`
- `arg1 * arg2` - multiplies `arg1` by `arg2`
- `arg1 / arg2` - divides `arg1` by `arg2`
- `arg1 % arg2` - returns the remainder of the division of `arg1` by `arg2`
- `arg1 ^ arg2` - returns the power of `arg1` by `arg2`
- `arg1 & arg2` - returns bitwise `and` for `arg1` and `arg2`. It is expected that `arg1` and `arg2` are in the range `[0 .. 2^53-1]`
- `arg1 or arg2` - returns bitwise `or` for `arg1` and `arg2`. It is expected that `arg1` and `arg2` are in the range `[0 .. 2^53-1]`
- `arg1 xor arg2` - returns bitwise `xor` for `arg1` and `arg2`. It is expected that `arg1` and `arg2` are in the range `[0 .. 2^53-1]`
- `arg1 default arg2` - returns `arg2` if `arg1` is non-[numeric](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values) or equals `NaN`
- `abs(arg)` - returns an absolute value for the given `arg`
- `ceil(arg)` - returns the least integer value greater than or equal to `arg`
- `exp(arg)` - powers [`e`](https://en.wikipedia.org/wiki/E_(mathematical_constant)) by `arg`
- `floor(arg)` - returns the greatest integer value less than or equal to `arg`
- `ln(arg)` - returns [natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm) for the given `arg`
- `max(arg1, ..., argN)` - returns the maximum value among the given `arg1`, ..., `argN`
- `min(arg1, ..., argN)` - returns the minimum value among the given `arg1`, ..., `argN`
- `now()` - returns the current [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time) in nanoseconds.
- `rand()` - returns pseudo-random number in the range `[0...1)`.
- `round(arg)` - returns rounded to integer value for the given `arg`. The `round()` accepts optional `nearest` arg, which allows rounding the number to the given `nearest` multiple.
  For example, `round(temperature, 0.1)` rounds `temperature` field to one decimal digit after the point.

Every `argX` argument in every mathematical operation can contain one of the following values:

- The name of [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model). For example, `errors_total / requests_total`.
  The log field is parsed into numeric value if it contains [supported numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values). The log field is parsed into [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time)
  in nanoseconds if it contains [rfc3339 time](https://www.rfc-editor.org/rfc/rfc3339). The log field is parsed into `uint32` number if it contains IPv4 address.
  The log field is parsed into `NaN` in other cases.
- Any [supported numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values), [rfc3339 time](https://www.rfc-editor.org/rfc/rfc3339) or IPv4 address. For example, `1MiB`, `"2024-05-15T10:20:30.934324Z"` or `"12.34.56.78"`.
- Another mathematical expression, which can be put inside `(...)`. For example, `(a + b) * c`.

The parsed time, duration and IPv4 address can be converted back to string representation after math transformations with the help of [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe). For example,
the following query rounds the `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) to seconds before converting it back to string representation:

```logsql
_time:5m | math round(request_duration, 1e9) as request_duration_nsecs | format '<duration:request_duration_nsecs>' as request_duration
```

The `eval` keyword can be used instead of `math` for convenience. For example, the following query calculates `duration_msecs` field
by multiplying `duration_secs` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) to `1000`:

```logsql
_time:5m | eval (duration_secs * 1000) as duration_msecs
```

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe)

