## Filters

LogsQL supports various filters for searching for log messages (see below).
They can be combined into arbitrary complex queries via [logical filters](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).

Filters are applied to [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) by default.
If the filter must be applied to other [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then its name followed by the colon must be put in front of the filter. For example, if `error` [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) must be applied
to the `log.level` field, then use `log.level:error` query.

Field names and filter args can be put into quotes if they contain special chars, which may clash with LogsQL syntax. LogsQL supports quoting via double quotes `"`,
single quotes `'` and backticks according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals):

```logsql
"some 'field':123":i('some("value")') AND `other"value'`
```

If in doubt, it is recommended quoting field names and filter args.

The list of LogsQL filters:

- [Time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) - matches logs with [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) in the given time range
- [Day range filter](https://docs.victoriametrics.com/victorialogs/logsql/#day-range-filter) - matches logs with [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) in the given per-day time range
- [Week range filter](https://docs.victoriametrics.com/victorialogs/logsql/#week-range-filter) - matches logs with [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) in the given per-week day range
- [Stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter) - matches logs, which belong to the given [streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) - matches logs with the given [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) - matches logs with the given phrase
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) - matches logs with the given word prefix or phrase prefix
- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter) - matches logs with the given substring
- [Pattern match filter](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter) - matches logs by the given pattern
- [Range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter) - matches logs with field values in the provided range
- [Empty value filter](https://docs.victoriametrics.com/victorialogs/logsql/#empty-value-filter) - matches logs without the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
- [Any value filter](https://docs.victoriametrics.com/victorialogs/logsql/#any-value-filter) - matches logs with the given non-empty [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter) - matches logs with the exact value for the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
- [Exact prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter) - matches logs starting with the given prefix for the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
- [Multi-exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter) - matches logs with one of the specified exact values for the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
- [Subquery filter](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) - matches logs with [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) values matching the results of another query
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter) - matches logs with [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) containing
  all the provided [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrases
- [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter) - matches logs with [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) containing
  at least one of the provided [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrases
- [Case-insensitive filter](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) - matches logs with the given case-insensitive word, phrase or prefix
- [`contains_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter) - matches logs with log fields containing the given words and phrases with cases according to the given pattern
- [`equals_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#equals_common_case-filter) - matches logs with log fields equal to the given words and phrases with cases according to the given pattern
- [Sequence filter](https://docs.victoriametrics.com/victorialogs/logsql/#sequence-filter) - matches logs with the given sequence of words or phrases
- [Regexp filter](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) - matches logs for the given regexp
- [Range filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter) - matches logs with numeric [field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in the given range
- [IPv4 range filter](https://docs.victoriametrics.com/victorialogs/logsql/#ipv4-range-filter) - matches logs with IP address [field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in the given range
- [String range filter](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter) - matches logs with [field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in the given string range
- [Length range filter](https://docs.victoriametrics.com/victorialogs/logsql/#length-range-filter) - matches logs with [field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of the given length range
- [Value type filter](https://docs.victoriametrics.com/victorialogs/logsql/#value_type-filter) - matches logs with [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) stored under the given value type
- [Fields' equality filter](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter) - matches logs, which contain identical values in the given [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
- [`Less than` filter](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter) - matches logs where the given field value is smaller than the other field value
- [`Less than or equal` filter](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter) - matches logs where the given field value doesn't exceed the other field value
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) - allows combining other filters

### Time filter

VictoriaLogs scans all the logs for each query if it doesn't contain the filter on the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).
It uses various optimizations in order to accelerate full scan queries without the `_time` filter,
but such queries can be slow if the storage contains large number of logs over long time range. The easiest way to optimize queries
is to narrow down the search with the filter on [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).

For example, the following query returns logs ingested into VictoriaLogs during the last hour, which contain the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
at the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
_time:1h AND error
```

The following formats are supported for `_time` filter:

- `_time:duration` matches logs with timestamps on the time range `(now-duration, now]`, where `duration` can have [these values](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values). Examples:
  - `_time:5m` - returns logs for the last 5 minutes
  - `_time:2.5d15m42.345s` - returns logs for the last 2.5 days, 15 minutes and 42.345 seconds
  - `_time:1y` - returns logs for the last year
- `_time:>duration` - matches logs with timestamps older than `now-duration`.
- `_time:YYYY-MM-DDZ` - matches all the logs for the particular day by UTC. For example, `_time:2023-04-25Z` matches logs on April 25, 2023 by UTC.
- `_time:YYYY-MMZ` - matches all the logs for the particular month by UTC. For example, `_time:2023-02Z` matches logs on February, 2023 by UTC.
- `_time:YYYYZ` - matches all the logs for the particular year by UTC. For example, `_time:2023Z` matches logs on 2023 by UTC.
- `_time:YYYY-MM-DDTHHZ` - matches all the logs for the particular hour by UTC. For example, `_time:2023-04-25T22Z` matches logs on April 25, 2023 at 22 hour by UTC.
- `_time:YYYY-MM-DDTHH:MMZ` - matches all the logs for the particular minute by UTC. For example, `_time:2023-04-25T22:45Z` matches logs on April 25, 2023 at 22:45 by UTC.
- `_time:YYYY-MM-DDTHH:MM:SSZ` - matches all the logs for the particular second by UTC. For example, `_time:2023-04-25T22:45:59Z` matches logs on April 25, 2023 at 22:45:59 by UTC.
- `_time:>min_time` - matches logs with timestamps bigger than the `min_time`.
- `_time:>=min_time` - matches logs with timestamps bigger or equal to the `min_time`.
- `_time:<max_time` - matches logs with timestamps smaller than the `max_time`.
- `_time:<=max_time` - matches logs with timestamps smaller or equal to the `max_time`.
- `_time:[min_time, max_time]` - matches logs on the time range `[min_time, max_time]`, including both `min_time` and `max_time`.
    The `min_time` and `max_time` can contain any format specified [here](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#timestamp-formats).
    For example, `_time:[2023-04-01Z, 2023-04-30Z]` matches logs for the whole April, 2023 by UTC, e.g. it is equivalent to `_time:2023-04Z`.
- `_time:[min_time, max_time)` - matches logs on the time range `[min_time, max_time)`, not including `max_time`.
    The `min_time` and `max_time` can contain any format specified [here](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#timestamp-formats).
    For example, `_time:[2023-02-01Z, 2023-03-01Z)` matches logs for the whole February, 2023 by UTC, e.g. it is equivalent to `_time:2023-02Z`.

It is possible to specify time zone offset for all the absolute time formats by appending `+hh:mm` or `-hh:mm` suffix.
For example, `_time:2023-04-25+05:30` matches all the logs on April 25, 2023 by India time zone,
while `_time:2023-02-07:00` matches all the logs on February, 2023 by California time zone.

If the timezone offset information is missing, then the local time zone of the host where VictoriaLogs runs is used.
For example, `_time:2023-10-20` matches all the logs for `2023-10-20` day according to the local time zone of the host where VictoriaLogs runs.

It is possible to specify generic offset for the selected time range by appending `offset` after the `_time` filter. Examples:

- `_time:offset 1h` matches logs until `now-1h`.
- `_time:5m offset 1h` matches logs on the time range `(now-1h5m, now-1h]`.
- `_time:2023-07Z offset 5h30m` matches logs on July, 2023 by UTC with offset 5h30m.
- `_time:[2023-02-01Z, 2023-03-01Z) offset 1w` matches logs the week before the time range `[2023-02-01Z, 2023-03-01Z)` by UTC.

See also [`time_offset` option](https://docs.victoriametrics.com/victorialogs/logsql/#query-options), which allows applying the given offset to all the filters on `_time` field without the need to modify the query.

See also [`time_add` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#time_add-pipe), which allows adding the given duration to the given log field.

Performance tips:

- It is recommended to specify the smallest possible time range during the search, since it reduces the amount of log entries that need to be scanned during the query.
  For example, `_time:1h` is usually faster than `_time:5h`.

- While LogsQL supports arbitrary number of `_time:...` filters at any level of [logical filters](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter),
  it is recommended specifying a single `_time` filter at the top level of the query.

- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Day range filter](https://docs.victoriametrics.com/victorialogs/logsql/#day-range-filter)
- [Week range filter](https://docs.victoriametrics.com/victorialogs/logsql/#week-range-filter)
- [Stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)

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

### Stream filter

VictoriaLogs provides an optimized way to select logs, which belong to particular [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
This can be done via `{...}` filter, which may contain arbitrary
[Prometheus-compatible label selector](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering)
over fields associated with [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
For example, the following query selects [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with `app` field equal to `nginx`:

```logsql
{app="nginx"}
```

This query is equivalent to the following [`exact` filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter) query, but the upper query usually works much faster:

```logsql
app:="nginx"
```

The stream filter supports `{label in (v1,...,vN)}` and `{label not_in (v1,...,vN)}` syntax.
It is equivalent to `{label=~"v1|...|vN"}` and `{label!~"v1|...|vN"}` respectively. The `v1`, ..., `vN` are properly escaped inside the regexp.
For example, `{app in ("nginx", "foo.bar")}` is equivalent to `{app=~"nginx|foo\\.bar"}` - note that the `.` char is properly escaped.

It is allowed to add `_stream:` prefix in front of `{...}` filter in order to make clear that the filtering is performed
on the [`_stream` log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
The following filter is equivalent to `{app="nginx"}`:

```logsql
_stream:{app="nginx"}
```

Performance tips:

- It is recommended to use the most specific `{...}` filter matching the smallest number of log streams,
  which needs to be scanned by the rest of filters in the query.

- While LogsQL supports arbitrary number of `{...}` filters at any level of [logical filters](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter),
  it is recommended specifying a single `{...}` filter at the top level of the query.

- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [`_stream_id` filter](https://docs.victoriametrics.com/victorialogs/logsql/#_stream_id-filter)
- [Time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)

### _stream_id filter

Every [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) in VictoriaLogs is uniquely identified by `_stream_id` field.
The `_stream_id:...` filter allows quickly selecting all the logs belonging to the particular stream.

For example, the following query selects all the logs, which belong to the [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
with `_stream_id` equal to `0000007b000001c850d9950ea6196b1a4812081265faa1c7`:

```logsql
_stream_id:0000007b000001c850d9950ea6196b1a4812081265faa1c7
```

If the log stream contains too many logs, then it is a good idea to limit the number of returned logs with a [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter). For example, the following
query selects logs for the given stream for the last hour:

```logsql
_time:1h _stream_id:0000007b000001c850d9950ea6196b1a4812081265faa1c7
```

The `_stream_id` filter supports specifying multiple `_stream_id` values via `_stream_id:in(...)` syntax. For example:

```logsql
_stream_id:in(0000007b000001c850d9950ea6196b1a4812081265faa1c7, 1230007b456701c850d9950ea6196b1a4812081265fff2a9)
```

It is also possible to specify a subquery inside `in(...)`, which selects the needed `_stream_id` values. For example, the following query returns
logs for [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) containing `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) during the last 5 minutes:

```logsql
_stream_id:in(_time:5m error | fields _stream_id)
```

See also:

- [subquery filter](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)
- [stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)

### Word filter

The simplest LogsQL query consists of a single [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) to search in log messages. For example, the following query matches
[log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) with `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) inside them:

```logsql
error
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `error`
- `an error happened`
- `error: cannot open file`

This query doesn't match the following log messages:

- `ERROR`, since the filter is case-sensitive by default. Use `i(error)` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.
- `multiple errors occurred`, since the `errors` word doesn't match `error` word. Use `error*` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) for details.

By default the given [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) is searched in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the word and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries containing the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in the `log.level` field:

```logsql
log.level:error
```

Both the field name and the word in the query can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
სფერო:τιμή
```

Both the field name and the word in the query can be put inside quotes if they contain special chars, which may clash with the query syntax.
For example, the following query searches for the ip `1.2.3.45` in the field `ip:remote`:

```logsql
"ip:remote":"1.2.3.45"
```

See also:

- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Phrase filter

If you need to search for log messages with the specific phrase inside them, then just wrap the phrase into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
The phrase can contain any chars, including whitespace, punctuation, parens, etc. They are taken into account during the search.
For example, the following query matches [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with `ssh: login fail` phrase inside them:

```logsql
"ssh: login fail"
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `ERROR: ssh: login fail for user "foobar"`
- `ssh: login fail!`

This query doesn't match the following log messages:

- `ssh login fail`, since the message misses `:` char just after the `ssh`.
  Use `seq("ssh", "login", "fail")` query if log messages with the sequence of these words must be found. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#sequence-filter) for details.
- `login fail: ssh error`, since the message doesn't contain the full phrase requested in the query. If you need matching a message
  with all the [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) listed in the query, then use `ssh AND login AND fail` query. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- `ssh: login failed`, since the message ends with `failed` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) instead of `fail` word. Use `"ssh: login fail"*` query for this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) for details.
- `SSH: login fail`, since the `SSH` word is in capital letters. Use `i("ssh: login fail")` for case-insensitive search.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.

If the phrase contains double quotes, then either put `\` in front of double quotes or put the phrase inside single quotes. For example, the following filter searches
logs with `"foo":"bar"` phrase:

```logsql
'"foo":"bar"'
```

By default the given phrase is searched in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the phrase and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries containing the `cannot open file` phrase in the `event.original` field:

```logsql
event.original:"cannot open file"
```

Both the field name and the phrase can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
შეტყობინება:"Το αρχείο δεν μπορεί να ανοίξει"
```

The field name can be put inside quotes if it contains special chars, which may clash with the query syntax.
For example, the following query searches for the `cannot open file` phrase in the field `some:message`:

```logsql
"some:message":"cannot open file"
```

See also:

- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Prefix filter

If you need to search for log messages with [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrases containing some prefix, then just add `*` char to the end of the [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrase in the query.
For example, the following query returns [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), which contain [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) with `err` prefix:

```logsql
err*
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `err: foobar`
- `cannot open file: error occurred`

This query doesn't match the following log messages:

- `Error: foobar`, since the `Error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) starts with capital letter. Use `i(err*)` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.
- `fooerror`, since the `fooerror` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) doesn't start with `err`. Use `*err*` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter) for details.

Prefix filter can be applied to [phrases](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) put inside quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals). For example, the following query matches
[log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing phrases with `unexpected fail` prefix:

```logsql
"unexpected fail"*
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `unexpected fail: IO error`
- `error:unexpected failure`

This query doesn't match the following log messages:

- `unexpectedly failed`, since the `unexpectedly` doesn't match `unexpected` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word). Use `unexpected* AND fail*` for this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- `failed to open file: unexpected EOF`, since `failed` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) occurs before the `unexpected` word. Use `unexpected AND fail*` for this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.

If the prefix contains double quotes, then either put `\` in front of double quotes or put the prefix inside single quotes. For example, the following filter searches
logs with `"foo":"bar` prefix:

```logsql
'"foo":"bar'*
```

By default the prefix filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the prefix filter
in order to apply it to the given field. For example, the following query matches `log.level` field containing any word with the `err` prefix:

```logsql
log.level:err*
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `log:level` field containing any word with the `err` prefix.

```logsql
"log:level":err*
```

Performance tips:

- Prefer using [word filters](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filters](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) combined via [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
  instead of prefix filter.
- Prefer moving [word filters](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filters](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) in front of prefix filter when using [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Exact prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Pattern match filter

VictoriaLogs supports filtering logs by patterns with the `pattern_match("pattern")` filter. This filter matches logs where
[`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) contains the given `"pattern"`.

The filter can be applied to any given log field with the `log_field:pattern_match("pattern")` syntax.

The `"pattern"` must contain the text to match, plus arbitrary number of the following placeholders:

- `<N>` - matches any integer number. It also matches hexadecimal numbers with the length of 4 chars and longer. For example, it matches `123` and `12abcdEF`.
  It doesn't match floating point numbers such as `123.456`. Use `<N>.<N>` pattern for matching such numbers.
- `<UUID>` - matches any UUID such as `2edfed59-3e98-4073-bbb2-28d321ca71a7`.
- `<IP4>` - matches IPv4 such as `123.45.67.89`. Use `<IP4>/<N>` for matching IPv4 masks.
- `<TIME>` - matches time strings such as `10:20:30`. It also captures fractional seconds such as `10:20:30.123` and `10:20:30,123`.
- `<DATE>` - matches date strings such as `2025-10-20` and `2025/10/20`.
- `<DATETIME>` - matches datetime strings such as `2025-10-20T08:09:11` and `2025-10-20 08:09:11`. It also captures fractional seconds and timezones.
- `<W>` - matches any [word](#word) or any quoted string in single quotes, double quotes and backticks.

Such patterns are generated by the [`collapse_nums` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe).

For example, the following filter matches `_msg` field with the `<arbitrary_prefix>user_id=123, ip=45.67.89.12, time=2025-10-20T23:32:12Z<arbitrary_suffix>` contents:

```logsql
pattern_match("user_id=<N>, ip=<IP4>, time=<DATETIME>")
```

If you need to match the whole `_msg` field value, then use the `pattern_match_full("pattern")` filter.

See also:

- [`collapse_nums` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe)
- [Sequence filter](https://docs.victoriametrics.com/victorialogs/logsql/#sequence-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Substring filter

If it is needed to find logs with some substring, then `*substring*` filter can be used. The substring can be put in quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals) if needed.
For example, the following query matches log entries, which contain `ampl` text in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
*ampl*
```

It matches the following messages:

- `Example message`
- `This is a sample`

It doesn't match `EXAMPLE message`, since `AMPL` substring here is in uppercase. Use [`~"(?i)ampl"` filter](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) instead. Note that case-insensitive filter
may be much slower than case-sensitive one.

Performance tip: prefer using [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter), since substring filter may be quite slow.

See also:

- [Pattern match filter](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Regexp filter](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter)

### Range comparison filter

LogsQL supports `field:>X`, `field:>=X`, `field:<X` and `field:<=X` filters, where `field` is the name of [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
and `X` is [numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values), IPv4 address or a string. For example, the following query returns logs containing numeric values for the `response_size` field bigger than `10*1024`:

```logsql
response_size:>10KiB
```

The following query returns logs with `username` field containing string values smaller than `John`:

```logsql
username:<"John"
```

See also:

- [String range filter](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter)
- [Range filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter)
- [`le_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter)
- [`lt_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter)

### Empty value filter

Sometimes it is needed to find log entries without the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
This can be performed with `log_field:""` syntax. For example, the following query matches log entries without `host.hostname` field:

```logsql
host.hostname:""
```

See also:

- [No-op filter](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter)
- [Any value filter](https://docs.victoriametrics.com/victorialogs/logsql/#any-value-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Any value filter

Sometimes it is needed to find log entries containing any non-empty value for the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
This can be performed with `log_field:*` syntax. For example, the following query matches log entries with non-empty `host.hostname` field:

```logsql
host.hostname:*
```

See also:

- [No-op filter](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter)
- [Empty value filter](https://docs.victoriametrics.com/victorialogs/logsql/#empty-value-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### No-op filter

Sometimes it is needed to apply e.g. `no-op` filter to the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
which does nothing, e.g. it matches any logs, even if they do not contain the given log field.

The following options are supported for no-op flter:

- `field_name:in(*)` - a special case for the [`in()` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- `field_name:contains_any(*)` - a special case for the [`contains_any()` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
- `field_name:contains_all(*)` - a special case for the [`contains_all()` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)

See also:

- [Empty value filter](https://docs.victoriametrics.com/victorialogs/logsql/#empty-value-filter)
- [Any value filter](https://docs.victoriametrics.com/victorialogs/logsql/#any-value-filter)


### Exact filter

The [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) return [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
which contain the given word or phrase inside them. The message may contain additional text other than the requested word or phrase. If you need to search for log messages
or [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) with the exact value, then use the `exact` filter.
For example, the following query returns log messages with the exact value `fatal error: cannot find /foo/bar`:

```logsql
="fatal error: cannot find /foo/bar"
```

The query doesn't match the following log messages:

- `fatal error: cannot find /foo/bar/baz` or `some-text fatal error: cannot find /foo/bar`, since they contain an additional text
  other than the specified in the `exact` filter. Use `"fatal error: cannot find /foo/bar"` query in this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) for details.

- `FATAL ERROR: cannot find /foo/bar`, since the `exact` filter is case-sensitive. Use `i("fatal error: cannot find /foo/bar")` in this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.

By default the `exact` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the `exact` filter and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries with the exact `error` value at `log.level` field:

```logsql
log.level:="error"
```

Both the field name and the phrase can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
log.დონე:="შეცდომა"
```

The field name can be put inside quotes if it contains special chars, which may clash with the query syntax.
For example, the following query matches the `error` value in the field `log:level`:

```logsql
"log:level":="error"
```

See also:

- [Field equality filter](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter)
- [Exact prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter)
- [Multi-exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Exact prefix filter

Sometimes it is needed to find log messages starting with some prefix. This can be done with the `="prefix"*` filter.
For example, the following query matches log messages, which start from `Processing request` prefix:

```logsql
="Processing request"*
```

This filter matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `Processing request foobar`
- `Processing requests from ...`

It doesn't match the following log messages:

- `processing request foobar`, since the log message starts with lowercase `p`. Use `="processing request"* OR ="Processing request"*`
  query in this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- `start: Processing request`, since the log message doesn't start with `Processing request`. Use `"Processing request"` query in this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) for details.

By default the `exact` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the `exact` filter and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries with `log.level` field, which starts with `err` prefix:

```logsql
log.level:="err"*
```

Both the field name and the phrase can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
log.დონე:="შეცდომა"*
```

The field name can be put inside quotes if it contains special chars, which may clash with the query syntax.
For example, the following query matches `log:level` values starting with `err` prefix:

```logsql
"log:level":="err"*
```

See also:

- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Multi-exact filter

Sometimes it is needed to locate log messages with a field containing one of the given values. This can be done with multiple [exact filters](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
combined into a single [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter). For example, the following query matches log messages with `log.level` field
containing either `error` or `fatal` exact values:

```logsql
log.level:(="error" OR ="fatal")
```

While this solution works OK, LogsQL provides simpler and faster solution for this case - the `in()` filter.

```logsql
log.level:in("error", "fatal")
```

It works very fast for long lists passed to `in()`.

There is a special case - `in(*)` - this filter matches all the logs. See [no-op filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter) for details.

It is possible to pass arbitrary [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) inside `in(...)` filter in order to match against the results of this query.
See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) for details.

See also:

- [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### contains_all filter

If it is needed to find logs, which contain all the given [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrases, then `v1 AND v2 ... AND vN` [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
can be used. VictoriaLogs provides an alternative approach with the `contains_all(v1, v2, ..., vN)` filter. For example, the following query matches logs,
which contain both `foo` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) and `"bar baz"` phrase in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
contains_all(foo, "bar baz")
```

This is equivalent to the following query:

```logsql
foo AND "bar baz"
```

There is a special case - `contains_all(*)` - this filter matches all the logs. See [no-op filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter) for details.

It is possible to pass arbitrary [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) inside `contains_all(...)` filter in order to match against the results of this query.
See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) for details.

See also:

- [`seq` filter](https://docs.victoriametrics.com/victorialogs/logsql/#sequence-filter)
- [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [`in` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)

### contains_any filter

Sometimes it is needed to find logs, which contain at least one [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) or phrase out of many words / phrases.
This can be done with `v1 OR v2 OR ... OR vN` [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
VictoriaLogs provides an alternative approach with the `contains_any(v1, v2, ..., vN)` filter. For example, the following query matches logs,
which contain `foo` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) or `"bar baz"` phrase in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
contains_any(foo, "bar baz")
```

This is equivalent to the following query:

```logsql
foo OR "bar baz"
```

There is a special case - `contains_any(*)` - this filter matches all the logs. See [no-op filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter) for details.

It is possible to pass arbitrary [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) inside `contains_any(...)` filter in order to match against the results of this query.
See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) for details.

See also:

- [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [`in` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)

### Subquery filter

Sometimes it is needed to select logs with [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) matching values
selected by another [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) (aka subquery). LogsQL provides such an ability with the following filters:

- `field:in(<subquery>)` - it returns logs with `field` values matching the values returned by the `<subquery>`.
  For example, the following query selects all the logs for the last 5 minutes for users,
  who visited pages with `admin` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in the `path` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  during the last day:

  ```logsql
  _time:5m AND user_id:in(_time:1d AND path:admin | fields user_id)
  ```

- `field:contains_all(<subquery>)` - it returns logs with `field` values containing all the [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) and phrases returned by the `<subquery>`.
  For example, the following query selects all the logs for the last 5 minutes, which contain all the `user_id` values from admin logs over the last day
  in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

  ```logsql
  _time:5m _msg:contains_all(_time:1d is_admin:true | fields user_id)
  ```

- `field:contains_any(<subquery>)` - it returns logs with the `field` values containing at least one [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) or phrase returned by the `<subquery>`.
  For example, the following query selects all the logs for the last 5 minutes, which contain at least one `user_id` value from admin logs over the last day
  in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

  ```logsql
  _time:5m _msg:contains_any(_time:1d is_admin:true | fields user_id)
  ```

The `<subquery>` must end with either [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) or [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe) containing a single field name,
so VictoriaLogs could use values of this field for matching the given filter.

See also:

- [`in` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)
- [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)
- [`union` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#union-pipe)

### Case-insensitive filter

Case-insensitive filter can be applied to any word, phrase or prefix by wrapping the corresponding [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter),
[phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) or [prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) into `i()`. For example, the following query returns
log messages with `error` word in any case:

```logsql
i(error)
```

The query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `unknown error happened`
- `ERROR: cannot read file`
- `Error: unknown arg`
- `An ErRoR occurred`

The query doesn't match the following log messages:

- `FooError`, since the `FooError` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) has superfluous prefix `Foo`. Use `~"(?i)error"` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) for details.
- `too many Errors`, since the `Errors` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) has superfluous suffix `s`. Use `i(error*)` for this case.

By default the `i()` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the filter
in order to apply it to the given field. For example, the following query matches `log.level` field containing `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in any case:

```logsql
log.level:i(error)
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `log:level` field containing `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in any case.

```logsql
"log:level":i("error")
```

Performance tips:

- Prefer using [`contains_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter) over `i(...)`,
  since `contains_common_case(...)` usually works much faster.
- Prefer using case-sensitive filters such as [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
  and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) over case-insensitive filter.
- Prefer moving [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter), [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
  and [prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) in front of the case-insensitive filter
  when using [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [`contains_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### equals_common_case filter

The `field_name:equals_common_case(phrase1, ..., phraseN)` filter searches for logs where the `field_name` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
equals the following [phrases](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) and [words](https://docs.victoriametrics.com/victorialogs/logsql/#word):

- the given phrases - `phrase1`, ..., `phraseN`
- uppercase and lowercase phrases
- individual phrases where every uppercase letter is independently replaced with the corresponding lowercase letter

For example, `_msg:equals_common_case("VictoriaMetrics")` finds logs where the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
equals one of the following [words](https://docs.victoriametrics.com/victorialogs/logsql/#word):

- VictoriaMetrics
- VICTORIAMETRICS
- victoriametrics
- Victoriametrics
- victoriaMetrics

The `equals_common_case(...)` usually works much faster than the [`i(...)`](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).

If you need to find logs with log fields containing the common case words or phrases,
then use [`contains_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter).

See also:

- [case-insensitive filter](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)
- [`contains_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter)

### contains_common_case filter

The `field_name:contains_common_case(phrase1, ..., phraseN)` filter searches for logs where the `field_name` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
contains the following [phrases](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) and [words](https://docs.victoriametrics.com/victorialogs/logsql/#word):

- the given phrases - `phrase1`, ..., `phraseN`
- uppercase and lowercase phrases
- individual phrases where every uppercase letter is independently replaced with the corresponding lowercase letter

For example, `_msg:contains_common_case("VictoriaMetrics")` finds logs where the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
contains at least one of the following [words](https://docs.victoriametrics.com/victorialogs/logsql/#word):

- VictoriaMetrics
- VICTORIAMETRICS
- victoriametrics
- Victoriametrics
- victoriaMetrics

The `contains_common_case(...)` usually works much faster than the [`i(...)`](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).

If you need to find logs with log fields equal to the common case words or phrases,
then use [`equals_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#equals_common_case-filter).

See also:

- [case-insensitive filter](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)
- [`equals_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#equals_common_case-filter)

### Sequence filter

Sometimes it is needed to find [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) or phrases in a particular order. For example, if log messages with `error` word followed by `open file` phrase
must be found, then the following LogsQL query can be used (every word / phrase can be quoted according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals)):

```logsql
seq("error", "open file")
```

This query matches `some error: cannot open file /foo/bar` message, since the `open file` phrase goes after the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word).
The query doesn't match the `cannot open file: error` message, since the `open file` phrase is located in front of the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word).
If you need to match log messages with both the `error` word and the `open file` phrase, then use the `error AND "open file"` query. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
for details.

By default the `seq()` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the filter
in order to apply it to the given field. For example, the following query matches `event.original` field containing `(error, "open file")` sequence:

```logsql
event.original:seq(error, "open file")
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `event:original` field containing `(error, "open file")` sequence:

```logsql
"event:original":seq(error, "open file")
```

See also:

- [Pattern match filter](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### Regexp filter

LogsQL supports regular expression filter with [RE2 syntax](https://github.com/google/re2/wiki/Syntax) via `~"regex"` syntax.
The `regex` can be put in one of the supported quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query returns all the log messages containing `err` or `warn` substrings:

```logsql
~"err|warn"
```

The query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), which contain either `err` or `warn` substrings:

- `error: cannot read data`
- `2 warnings have been raised`
- `data transferring finished`

The query doesn't match the following log messages:

- `ERROR: cannot open file`, since the `ERROR` word is in uppercase letters. Use `~"(?i)(err|warn)"` query for case-insensitive regexp search.
  See [these docs](https://github.com/google/re2/wiki/Syntax) for details. See also [case-insensitive filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).
- `it is warmer than usual`, since it doesn't contain neither `err` nor `warn` substrings.

If the regexp contains double quotes, then either put `\` in front of double quotes or put the regexp inside single quotes. For example, the following regexp searches
logs matching `"foo":"(bar|baz)"` regexp:

```logsql
~'"foo":"(bar|baz)"'
```

The `\` char inside the regexp must be encoded as `\\`. For example, the following query searches for logs with `a.b` substring inside them:

```logsql
~"a\\.b"
```

It is recommended to use the [substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter) when a substring search is needed.

By default the regexp filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the filter
in order to apply it to the given field. For example, the following query matches `event.original` field containing either `err` or `warn` substrings:

```logsql
event.original:~"err|warn"
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `event:original` field containing either `err` or `warn` substrings:

```logsql
"event:original":~"err|warn"
```

Performance tips:

- Prefer combining simple [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) with [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) instead of using regexp filter.
  For example, the `~"error|warning"` query can be substituted with `error OR warning` query, which usually works much faster.
  Note that the `~"error|warning"` matches `errors` as well as `warnings` [words](https://docs.victoriametrics.com/victorialogs/logsql/#word), while `error OR warning` matches
  only the specified [words](https://docs.victoriametrics.com/victorialogs/logsql/#word). See also [multi-exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter).
- Prefer moving the regexp filter to the end of the [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter), so lighter filters are executed first.
- Prefer using `="some prefix"*` instead of `~"^some prefix"`, since the [`exact prefix` filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter) works much faster than the regexp filter.
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Case-insensitive filter](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

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

### IPv4 range filter

If you need to filter log message by some field containing only [IPv4](https://en.wikipedia.org/wiki/Internet_Protocol_version_4) addresses such as `1.2.3.4`,
then the `ipv4_range()` filter can be used. For example, the following query matches log entries with `user.ip` address in the range `[127.0.0.0 - 127.255.255.255]`:

```logsql
user.ip:ipv4_range(127.0.0.0, 127.255.255.255)
```

The `ipv4_range()` accepts also IPv4 subnetworks in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).
For example, the following query is equivalent to the query above:

```logsql
user.ip:ipv4_range("127.0.0.0/8")
```

If you need matching a single IPv4 address, then just put it inside `ipv4_range()`. For example, the following query matches `1.2.3.4` IP
at `user.ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
user.ip:ipv4_range("1.2.3.4")
```

Note that the `ipv4_range()` doesn't match a string with IPv4 address if this string contains other text. For example, `ipv4_range("127.0.0.0/24")`
doesn't match `request from 127.0.0.1: done` [log message](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
since the `127.0.0.1` ip is surrounded by other text. Extract the IP from the message with [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
and then apply the `ipv4_range()` [filter pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe) to the extracted field.

Hints:

- If you need to search for [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing the given `X.Y.Z.Q` IPv4 address,
  then `"X.Y.Z.Q"` query can be used. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) for details.
- If you need to search for [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing
  at least a single IPv4 address out of the given list, then `"ip1" OR "ip2" ... OR "ipN"` query can be used. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- If you need to find log entries with the `ip` field in multiple ranges, then use `ip:(ipv4_range(range1) OR ipv4_range(range2) ... OR ipv4_range(rangeN))` query.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.

Performance tips:

- It is better querying pure IPv4 [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of extracting IPv4 from text field via [transformations](https://docs.victoriametrics.com/victorialogs/logsql/#transformations) at query time.
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Range filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter)
- [String range filter](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter)
- [Length range filter](https://docs.victoriametrics.com/victorialogs/logsql/#length-range-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

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

### value_type filter

VictoriaLogs automatically detects types for the ingested [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) and stores log field values
according to the detected type (such as `const`, `dict`, `string`, `int64`, `float64`, etc.). Value types for stored fields can be obtained via [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe).

Sometimes it is needed to select logs with fields of a particular value type. Then `value_type(type)` filter can be used.
For example, the following filter selects logs where `user_id` field values are stored as `uint64` type:

```logsql
user_id:value_type(uint64)
```

See also:

- [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe)
- [`query_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

### eq_field filter

Sometimes it is needed to find logs, which contain identical values in the given [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
This can be done with `field1:eq_field(field2)` filter.

For example, the following query matches logs with identical values at `user_id` and `customer_id` fields:

```logsql
user_id:eq_field(customer_id)
```

Quick tip: use `NOT user_id:eq_field(customer_id)` for finding logs where `user_id` isn't equal to `customer_id`. It uses [`NOT` logical operator](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).

See also:

- [`exact` filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [`le_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter)
- [`lt_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter)

### le_field filter

Sometimes it is needed to find logs where one [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) value doesn't exceed the other field value.
This can be done with `field1:le_field(field2)` filter.

For example, the following query matches logs where `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) doesn't exceed the `max_duration` field:

```logsql
duration:le_field(max_duration)
```

Quick tip: use `NOT duration:le_field(max_duration)` for finding logs where `duration` exceeds the `max_duration`.

See also:

- [range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter)
- [`lt_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter)
- [`eq_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter)

### lt_field filter

Sometimes it is needed to find logs where one [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) value is smaller than the other field value.
This can be done with `field1:lt_field(field2)` filter.

For example, the following query matches logs where `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) is smaller than the `max_duration` field:

```logsql
duration:lt_field(max_duration)
```

Quick tip: use `NOT duration:lt_field(max_duration)` for finding logs where `duration` is bigger or equal to the `max_duration`.

See also:

- [range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter)
- [`le_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter)
- [`eq_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter)

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

