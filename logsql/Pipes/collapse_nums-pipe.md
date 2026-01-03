### collapse_nums pipe

`<q> | collapse_nums at <field>` pipe replaces all the decimal and hexadecimal numbers at the given [`<field>`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
returned by the `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) with `<N>` placeholder.
For example, if the `_msg` field contains `2024-10-20T12:34:56Z request duration 1.34s`, then it is replaced with `<N>-<N>-<N>T<N>:<N>:<N>Z request duration <N>.<N>s` by the following query:

```logsql
_time:5m | collapse_nums at _msg
```

The `at ...` suffix can be omitted if `collapse_nums` is applied to [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) field.
The following query is equivalent to the previous one:

```logsql
_time:5m | collapse_nums
```

This functionality is useful for locating the most frequently seen log patterns across log messages with various decimal and hexadecimal numbers.
This includes the following entities: timestamps, IP addresses, request durations, response sizes, [UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier), trace IDs, user IDs, etc.
Log messages with such entities become identical after applying `collapse_nums` pipe to them, so the [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe) can be applied to them in order to get the most frequently
seen patterns across log messages. For example, the following query returns top 5 the most frequently seen log patterns across log messages for the last hour:

```logsql
_time:1h | collapse_nums | top 5 by (_msg)
```

`collapse_nums` can detect certain patterns in the collapsed numbers and replace them with the corresponding placeholders if `prettify` suffix is added to the `collapse_nums` pipe:

- `<N>-<N>-<N>-<N>-<N>` is replaced with `<UUID>` placeholder.
- `<N>.<N>.<N>.<N>` is replaced with `<IP4>` placeholder.
- `<N>:<N>:<N>` is replaced with `<TIME>` placeholder. Optional fractional seconds after the time are treated as a part of `<TIME>`.
- `<N>-<N>-<N>` and `<N>/<N>/<N>` is replaced with `<DATE>` placeholder.
- `<N>-<N>-<N>T<N>:<N>:<N>` and `<N>-<N>-<N> <N>:<N>:<N>` is replaced with `<DATETIME>` placeholder. Optional timezone after the datetime is treated as a part of `<DATETIME>`.

For example, the [log message](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
`2edfed59-3e98-4073-bbb2-28d321ca71a7 - [2024/12/08 15:21:02] 10.71.20.32 GET /foo 200` is replaced with `<UUID> - [<DATETIME>] <IP4> GET /foo <N>`
when the following query is executed:

```logsql
_time:1h | collapse_nums prettify
```

The patterns returned by `collapse_nums prettify` pipe can be used in [pattern match filter](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter).

`collapse_nums` can miss some numbers or can collapse unexpected numbers. In this case [conditional `collapse_nums`](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-collapse_nums) can be used
for skipping such values and pre-processing them separately with [`replace_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe).

See also:

- [conditional `collapse_nums`](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-collapse_nums)
- [pattern match filter](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter)
- [`replace`](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe)
- [`replace_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe)

#### Conditional collapse_nums

If the [`collapse_nums` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `collapse_nums`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query collapses nums in the `foo` field only if the `user_type` field equals `admin`:

```logsql
_time:5m | collapse_nums if (user_type:=admin) at foo
```

