### Logical filter

Basic LogsQL [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) can be combined into more complex filters with the following logical operations:

- `q1 AND q2` - matches common log entries returned by both `q1` and `q2`. Arbitrary number of [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) can be combined with `AND` operation.
  For example, `error AND file AND app` matches [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
  which simultaneously contain `error`, `file` and `app` [words](https://docs.victoriametrics.com/victorialogs/logsql/#word).
  The `AND` operation is frequently used in LogsQL queries, so it is allowed to skip the `AND` word.
  For example, `error file app` is equivalent to `error AND file AND app`. See also [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter).

- `q1 OR q2` - merges log entries returned by both `q1` and `q2`. Arbitrary number of [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) can be combined with `OR` operation.
  For example, `error OR warning OR info` matches [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
  which contain at least one of `error`, `warning` or `info` [words](https://docs.victoriametrics.com/victorialogs/logsql/#word). See also [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter).

- `NOT q` - returns all the log entries except of those which match `q`. For example, `NOT info` returns all the
  [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
  which do not contain `info` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word). The `NOT` operation is frequently used in LogsQL queries, so it is allowed substituting `NOT` with `-` and `!` in queries.
  For example, `-info` and `!info` are equivalent to `NOT info`.
  The `!` must be used instead of `-` in front of [`=`](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
  and [`~`](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) filters like `!=` and `!~`.

The `NOT` operation has the highest priority, `AND` has the middle priority and `OR` has the lowest priority.
The priority order can be changed with parentheses. For example, `NOT info OR debug` is interpreted as `(NOT info) OR debug`,
so it matches [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
which do not contain `info` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word), while it also matches messages with `debug` word (which may contain the `info` word).
This is not what most users expect. In this case the query can be rewritten to `NOT (info OR debug)`,
which correctly returns log messages without `info` and `debug` [words](https://docs.victoriametrics.com/victorialogs/logsql/#word).

LogsQL supports arbitrary complex logical queries with arbitrary mix of `AND`, `OR` and `NOT` operations and parentheses.

By default logical filters apply to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
unless the inner filters explicitly specify the needed [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) via `field_name:filter` syntax.
For example, `(error OR warn) AND host.hostname:host123` is interpreted as `(_msg:error OR _msg:warn) AND host.hostname:host123`.

It is possible to specify a single [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) for multiple filters
with the following syntax:

```logsql
field_name:(q1 OR q2 OR ... qN)
```

For example, `log.level:error OR log.level:warning OR log.level:info` can be substituted with the shorter query: `log.level:(error OR warning OR info)`.

Performance tips:

- VictoriaLogs executes logical operations from the left to the right, so it is recommended moving the most specific
  and the fastest filters (such as [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)) to the left,
  while moving less specific and the slowest filters (such as [regexp filter](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) and [case-insensitive filter](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter))
  to the right. For example, if you need to find [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
  with the `error` word, which match some `/foo/(bar|baz)` regexp,
  it is better from performance PoV to use the query `error ~"/foo/(bar|baz)"` instead of `~"/foo/(bar|baz)" error`.

  The most specific filter means that it matches the lowest number of log entries comparing to other filters.

- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

