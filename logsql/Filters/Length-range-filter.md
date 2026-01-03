### Length range filter

If you need to filter log message by its length, then `len_range()` filter can be used.
For example, the following LogsQL query matches [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with lengths in the range `[5, 10]` chars:

```logsql
len_range(5, 10)
```

This query matches the following log messages, since their length is in the requested range:

- `foobar`
- `foo bar`

This query doesn't match the following log messages:

- `foo`, since it is too short
- `foo bar baz abc`, since it is too long

It is possible to use `inf` as the upper bound. For example, the following query matches [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with the length bigger or equal to 5 chars:

```logsql
len_range(5, inf)
```

The range boundaries can be expressed in the following forms:

- Hexadecimal form. For example, `len_range(0xff, 0xABCD)`.
- Binary form. For example, `len_range(0b100110, 0b11111101)`
- Integer form with `_` delimiters for better readability. For example, `len_range(1_000, 2_345_678)`.

By default the `len_range()` is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Put the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the `len_range()` in order to apply
the filter to the needed field. For example, the following query matches log entries with the `foo` field length in the range `[10, 20]` chars:

```logsql
foo:len_range(10, 20)
```

See also:

- [Range filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

