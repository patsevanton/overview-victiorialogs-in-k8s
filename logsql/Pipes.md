## Pipes

Additionally to [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters), LogsQL query may contain arbitrary mix of '|'-delimited actions known as `pipes`.
For example, the following query uses [`stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe), [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) and [`limit`](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe) pipes
for returning top 10 [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
with the biggest number of logs during the last 5 minutes:

```logsql
_time:5m | stats by (_stream) count() per_stream_logs | sort by (per_stream_logs desc) | limit 10
```

LogsQL supports the following pipes:

- [`block_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe) returns various stats for the selected blocks with logs.
- [`blocks_count`](https://docs.victoriametrics.com/victorialogs/logsql/#blocks_count-pipe) counts the number of blocks with logs processed by the query.
- [`collapse_nums`](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe) replaces all the decimal and hexadecimal numbers with `<N>` in the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`copy`](https://docs.victoriametrics.com/victorialogs/logsql/#copy-pipe) copies [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`decolorize`](https://docs.victoriametrics.com/victorialogs/logsql/#decolorize-pipe) drops [ANSI color codes](https://en.wikipedia.org/wiki/ANSI_escape_code) from the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`delete`](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe) deletes [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`drop_empty_fields`](https://docs.victoriametrics.com/victorialogs/logsql/#drop_empty_fields-pipe) drops [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) with empty values.
- [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) extracts the specified text into the given log fields.
- [`extract_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#extract_regexp-pipe) extracts the specified text into the given log fields via [RE2 regular expressions](https://github.com/google/re2/wiki/Syntax).
- [`facets`](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe) returns the most frequently seen [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) across the selected logs.
- [`field_names`](https://docs.victoriametrics.com/victorialogs/logsql/#field_names-pipe) returns all the names of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`field_values`](https://docs.victoriametrics.com/victorialogs/logsql/#field_values-pipe) returns all the values for the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`fields`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) selects the given set of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`filter`](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe) applies additional [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) to results.
- [`first`](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe) returns the first N logs after sorting them by the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`format`](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe) formats output field from input [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`generate_sequence`](https://docs.victoriametrics.com/victorialogs/logsql/#generate_sequence-pipe) generates output logs with messages containing integer sequence.
- [`join`](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe) joins query results by the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`json_array_len`](https://docs.victoriametrics.com/victorialogs/logsql/#json_array_len-pipe) returns the length of JSON array stored at the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`hash`](https://docs.victoriametrics.com/victorialogs/logsql/#hash-pipe) returns the hash over the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) value.
- [`last`](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe) returns the last N logs after sorting them by the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`len`](https://docs.victoriametrics.com/victorialogs/logsql/#len-pipe) returns byte length of the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) value.
- [`limit`](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe) limits the number selected logs.
- [`math`](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe) performs mathematical calculations over [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`offset`](https://docs.victoriametrics.com/victorialogs/logsql/#offset-pipe) skips the given number of selected logs.
- [`pack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#pack_json-pipe) packs [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) into JSON object.
- [`pack_logfmt`](https://docs.victoriametrics.com/victorialogs/logsql/#pack_logfmt-pipe) packs [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) into [logfmt](https://brandur.org/logfmt) message.
- [`query_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe) returns query execution statistics.
- [`rename`](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe) renames [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`replace`](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) replaces substrings in the specified [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`replace_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe) updates [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) with regular expressions.
- [`running_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe) performs running stats calculations over the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`sample`](https://docs.victoriametrics.com/victorialogs/logsql/#sample-pipe) returns a sample of the matching logs according to the provided `sample` value.
- [`set_stream_fields`](https://docs.victoriametrics.com/victorialogs/logsql/#set_stream_fields-pipe) sets the given log fields as [`_stream` fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
- [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) sorts logs by the given [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`split`](https://docs.victoriametrics.com/victorialogs/logsql/#split-pipe) splits the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) into tokens by the given separator.
- [`stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) calculates various stats over the selected logs.
- [`stream_context`](https://docs.victoriametrics.com/victorialogs/logsql/#stream_context-pipe) allows selecting surrounding logs before and after the matching logs
  for each [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
- [`time_add`](https://docs.victoriametrics.com/victorialogs/logsql/#time_add-pipe) adds the given duration to the given field containing [RFC3339 time](https://www.rfc-editor.org/rfc/rfc3339).
- [`top`](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe) returns top `N` field sets with the maximum number of matching logs.
- [`total_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe) performs total (global) stats calculations over the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`union`](https://docs.victoriametrics.com/victorialogs/logsql/#union-pipe) returns results from multiple LogsQL queries.
- [`uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe) returns unique log entries.
- [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) unpacks JSON messages from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`unpack_logfmt`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe) unpacks [logfmt](https://brandur.org/logfmt) messages from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`unpack_syslog`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe) unpacks [syslog](https://en.wikipedia.org/wiki/Syslog) messages from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`unpack_words`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe) unpacks [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) from the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) unrolls JSON arrays from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) into separate rows.

### block_stats pipe

`<q> | block_stats` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the following stats for each field in every data block
processed by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax):

- `field` - [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) name
- `rows` - the number of rows at the given `field`
- `type` - internal storage type for the given `field`
- `values_bytes` - on-disk size of the data for the given `field`
- `bloom_bytes` - on-disk size of bloom filter data for the given `field`
- `dict_bytes` - on-disk size of the dictionary data for the given `field`
- `dict_items` - the number of unique values in the dictionary for the given `field`
- `_stream` - the [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) for the given `field`
- `part_path` - the path to the data part where the field data is stored

The `block_stats` pipe is needed mostly for debugging purposes.
See, for example, [how to detect which log field occupies the most of the disk space](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-fields-occupy-the-most-of-disk-space),
or [how to detect which log stream occupies the most of the disk space](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-streams-occupy-the-most-of-disk-space).

See also:

- [`query_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe)
- [`value_type` filter](https://docs.victoriametrics.com/victorialogs/logsql/#value_type-filter)
- [`blocks_count` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#blocks_count-pipe)
- [`len` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#len-pipe)

### blocks_count pipe

`<q> | blocks_count` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) counts the number of blocks with logs processed by `<q>`. This pipe is needed mostly for debugging.

See also:

- [`query_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe)
- [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe)
- [`len` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#len-pipe)

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

### copy pipe

If some [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) must be copied, then `| copy src1 as dst1, ..., srcN as dstN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used.
For example, the following query copies `host` field to `server` for logs over the last 5 minutes, so the output contains both `host` and `server` fields:

```logsql
_time:5m | copy host as server
```

Multiple fields can be copied with a single `| copy ...` pipe. For example, the following query copies
[`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) to `timestamp`, while [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
is copied to `message`:

```logsql
_time:5m | copy _time as timestamp, _msg as message
```

The `as` keyword is optional.

`cp` keyword can be used instead of `copy` for convenience. For example, `_time:5m | cp foo bar` is equivalent to `_time:5m | copy foo as bar`.

It is possible to copy multiple fields with identical prefix to fields with another prefix. For example, the following query copies
all the fields with the prefix `foo` to fields with the prefix `bar`:

```logsql
_time:5m | copy foo* as bar*
```

See also:

- [`rename` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe)
- [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe)
- [`delete` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe)

### decolorize pipe

`<q> | decolorize <field>` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) drops [ANSI color codes](https://en.wikipedia.org/wiki/ANSI_escape_code)
from the given [`<field>`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) across all the logs returned by [`<q>` query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

The `<field>` may be omitted if ANSI color codes must be dropped from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
For example, the following query drops ANSI color codes from all the `_msg` fields over the logs for the last 5 minutes:

```logsql
_time:5m | decolorize
```

This query is equivalent to the following query:

```logsql
_time:5m | decolorize _msg
```

It is recommended to drop ANSI color codes at the data ingestion stage according to [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/#decolorizing).
This simplifies further querying of the logs without the need to apply `| decolorize` pipe to them.

See also:

- [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe)
- [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe)

### delete pipe

If some [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) must be deleted, then `| delete field1, ..., fieldN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used.
For example, the following query deletes `host` and `app` fields from the logs over the last 5 minutes:

```logsql
_time:5m | delete host, app
```

`drop`, `del` and `rm` keywords can be used instead of `delete` for convenience. For example, `_time:5m | drop host` is equivalent to `_time:5m | delete host`.

It is possible to delete fields with common prefix. For example, the following query deletes all the fields with `foo` prefix:

```logsql
_time:5m | delete foo*
```

See also:

- [`rename` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe)
- [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe)

### drop_empty_fields pipe

`<q> | drop_empty_fields` pipe drops [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) with empty values from results returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
It also skips log entries with zero non-empty fields.

For example, the following query drops possible empty `email` field generated by [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) if the `foo` field doesn't contain email:

```logsql
_time:5m | extract 'email: <email>,' from foo | drop_empty_fields
```

See also:

- [`filter` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

### extract pipe

`<q> | extract "pattern" from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) extracts text into output fields according to the [`pattern`](https://docs.victoriametrics.com/victorialogs/logsql/#format-for-extract-pipe-pattern) from the given
[`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
Existing log fields remain unchanged after the `| extract ...` pipe.

`extract` pipe can be useful for extracting additional fields needed for further data processing with other pipes such as [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) or [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).

For example, the following query selects logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) for the last day,
extracts IP address from [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) into `ip` field and then calculates top 10 IP addresses
with the biggest number of logs using [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe):

```logsql
_time:1d error | extract "ip=<ip> " from _msg | top 10 (ip)
```

It is expected that `_msg` field contains `ip=...` substring ending with space. For example, `error ip=1.2.3.4 from user_id=42`.
If there is no such substring in the current `_msg` field, then the `ip` output field will be empty.

If the `extract` pipe is applied to [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), then the `from _msg` part can be omitted.
For example, the following query is equivalent to the previous one:

```logsql
_time:1d error | extract "ip=<ip> " | top 10 (ip)
```

If the `pattern` contains double quotes, then either put `\` in front of double quotes or put the `pattern` inside single quotes.
For example, the following query extracts `ip` from the corresponding JSON field:

```logsql
_time:5m | extract '"ip":"<ip>"'
```

Add `keep_original_fields` to the end of `extract ...` when the original non-empty values of the fields mentioned in the pattern must be preserved
instead of overwriting them with the extracted values. For example, the following query extracts `<ip>` only if the original value for `ip` field is missing or is empty:

```logsql
_time:5m | extract 'ip=<ip> ' keep_original_fields
```

By default `extract` writes empty matching fields to the output, which may overwrite existing values. Add `skip_empty_results` to the end of `extract ...`
in order to prevent overwriting the existing values for the corresponding fields with empty values.
For example, the following query preserves the original `ip` field value if the `foo` field doesn't contain the matching IP:

```logsql
_time:5m | extract 'ip=<ip> ' from foo skip_empty_results
```

Performance tip: it is recommended using more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries, which are passed to `extract`.
See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Format for extract pipe pattern](https://docs.victoriametrics.com/victorialogs/logsql/#format-for-extract-pipe-pattern)
- [Conditional extract](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-extract)
- [`extract_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract_regexp-pipe)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
- [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)
- [`split` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#split-pipe)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)

#### Format for extract pipe pattern

The `pattern` part from [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) has the following format:

```
text1<field1>text2<field2>...textN<fieldN>textN+1
```

Where `text1`, ... `textN+1` is arbitrary non-empty text, which matches as is to the input text.

The `field1`, ... `fieldN` are placeholders, which match a substring of any length (including zero length) in the input text until the next `textX`.
Placeholders can be anonymous and named. Anonymous placeholders are written as `<_>`. They are used for convenience when some input text
must be skipped until the next `textX`. Named placeholders are written as `<some_name>`, where `some_name` is the name of the log field to store
the corresponding matching substring to.

Matching starts from the first occurrence of the `text1` in the input text. If the `pattern` starts with `<field1>` and doesn't contain `text1`,
then the matching starts from the beginning of the input text. Matching is performed sequentially according to the `pattern`. If some `textX` isn't found
in the remaining input text, then the remaining named placeholders receive empty string values and the matching finishes prematurely.
The empty string values can be dropped with [`drop_empty_fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#drop_empty_fields-pipe).

Matching finishes successfully when `textN+1` is found in the input text.
If the `pattern` ends with `<fieldN>` and doesn't contain `textN+1`, then the `<fieldN>` matches the remaining input text.

For example, if [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) contains the following text:

```
1.2.3.4 GET /foo/bar?baz 404 "Mozilla  foo bar baz" some tail here
```

Then the following `pattern` can be used for extracting `ip`, `path` and `user_agent` fields from it:

```
<ip> <_> <path> <_> "<user_agent>"
```

Note that the user-agent part of the log message is in double quotes. This means that it may contain special chars, including escaped double quote, e.g. `\"`.
This may break proper matching of the string in double quotes.

VictoriaLogs automatically detects quoted strings and automatically unquotes them if the first matching char in the placeholder is a single quote, double quote or a backtick.
So it is better to use the following `pattern` for proper matching of quoted `user_agent` string:

```
<ip> <_> <path> <_> <user_agent>
```

This is useful for extracting JSON strings. For example, the following `pattern` properly extracts the `message` JSON string into `msg` field, even if it contains special chars:

```
"message":<msg>
```

The automatic string unquoting can be disabled if needed by adding `plain:` prefix in front of the field name. For example, if some JSON array of string values must be captured
into `json_array` field, then the following `pattern` can be used:

```
some json string array: [<plain:json_array>]
```

If some special chars such as `<` must be matched by the `pattern`, then they can be [html-escaped](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references).
For example, the following `pattern` properly matches `a < b` text by extracting `a` into `left` field and `b` into `right` field:

```
<left> &lt; <right>
```

#### Conditional extract

If some log entries must be skipped from [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe), then add `if (<filters>)` filter after the `extract` word.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query extracts `ip` field
from [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) only
if the input [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) doesn't contain `ip` field or this field is empty:

```logsql
_time:5m | extract if (ip:"") "ip=<ip> "
```

An alternative approach is to add `keep_original_fields` to the end of `extract`, in order to keep the original non-empty values for the extracted fields.
For example, the following query is equivalent to the previous one:

```logsql
_time:5m | extract "ip=<ip> " keep_original_fields
```

### extract_regexp pipe

`<q> | extract_regexp "pattern" from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) extracts substrings from the [`field_name` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
returned from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) according to the provided `pattern`, and stores them into field names according to the named fields inside the `pattern`.
The `pattern` must contain [RE2 regular expression](https://github.com/google/re2/wiki/Syntax) with named fields (aka capturing groups) in the form `(?P<capture_field_name>...)`.
Matching substrings are stored to the given `capture_field_name` [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
For example, the following query extracts ipv4 addresses from [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
and puts them into `ip` field for logs over the last 5 minutes:

```logsql
_time:5m | extract_regexp "(?P<ip>([0-9]+[.]){3}[0-9]+)" from _msg
```

The `from _msg` part can be omitted if the data extraction is performed from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
So the following query is equivalent to the previous one:

```logsql
_time:5m | extract_regexp "(?P<ip>([0-9]+[.]){3}[0-9]+)"
```

Add `keep_original_fields` to the end of `extract_regexp ...` when the original non-empty values of the fields mentioned in the pattern must be preserved
instead of overwriting it with the extracted values. For example, the following query extracts `<ip>` only if the original value for `ip` field is missing or is empty:

```logsql
_time:5m | extract_regexp 'ip=(?P<ip>([0-9]+[.]){3}[0-9]+)' keep_original_fields
```

By default `extract_regexp` writes empty matching fields to the output, which may overwrite existing values. Add `skip_empty_results` to the end of `extract_regexp ...`
in order to prevent overwriting the existing values for the corresponding fields with empty values.
For example, the following query preserves the original `ip` field value if the `foo` field doesn't contain the matching IP:

```logsql
_time:5m | extract_regexp 'ip=(?P<ip>([0-9]+[.]){3}[0-9]+)' from foo skip_empty_results
```

Performance tip: it is recommended using [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) instead of `extract_regexp` for achieving higher query performance.

See also:

- [Conditional `extract_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-extract_regexp)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)

#### Conditional extract_regexp

If some log entries must be skipped from [`extract_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract_regexp-pipe), then add `if (<filters>)` after the `extract_regexp` word.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query extracts `ip`
from [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) only
if the input [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) doesn't contain `ip` field or this field is empty:

```logsql
_time:5m | extract_regexp if (ip:"") "ip=(?P<ip>([0-9]+[.]){3}[0-9]+)"
```

An alternative approach is to add `keep_original_fields` to the end of `extract_regexp`, in order to keep the original non-empty values for the extracted fields.
For example, the following query is equivalent to the previous one:

```logsql
_time:5m | extract_regexp "ip=(?P<ip>([0-9]+[.]){3}[0-9]+)" keep_original_fields
```

### facets pipe

`<q> | facets` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the most frequent values for every seen [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax). It also returns an estimated number of hits for every returned `field=value` pair.

For example, the following query returns the most frequent values for every seen log field across logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) over the last hour:

```logsql
_time:1h error | facets
```

It is possible to specify the number of most frequently seen values to return for each log field by using the `facets N` syntax. For example,
the following query returns up to 3 most frequently seen values for each field across logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) over the last hour:

```logsql
_time:1h error | facets 3
```

By default `facets` pipe doesn't return log fields with too many unique values, since this may require a lot of additional memory to track.
The limit can be changed during the query via `max_values_per_field M` suffix. For example, the following query returns up to 15 most frequently seen
field values across fields with up to 100000 unique values:

```logsql
_time:1h error | facets 15 max_values_per_field 100000
```

By default `facets` pipe doesn't return log fields with too long values. The limit can be changed during query via `max_value_len K` suffix.
For example, the following query returns the most frequent values for all the log fields containing values no longer than 100 bytes:

```logsql
_time:1h error | facets max_value_len 100
```

By default `facets` pipe doesn't return log fields, which contain a single constant value across all the selected logs, since such facets aren't interesting in most cases.
Add `keep_const_fields` suffix to the `facets` pipe in order to get such fields:

```logsql
_time:1h error | facets keep_const_fields
```

See also:

- [`top`](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`field_names`](https://docs.victoriametrics.com/victorialogs/logsql/#field_names-pipe)
- [`field_values`](https://docs.victoriametrics.com/victorialogs/logsql/#field_values-pipe)

### field_names pipe

`<q> | field_names` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns all the names of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with an estimated number of logs for each field name returned from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query returns all the field names with the number of matching logs over the last 5 minutes:

```logsql
_time:5m | field_names
```

Field names are returned in arbitrary order. Use [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) in order to sort them if needed.

See also:

- [`field_values` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#field_values-pipe)
- [`facets` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)

### field_values pipe

`<q> | field_values field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns all the values for the given [`field_name` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the number of logs for each value returned from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
For example, the following query returns all the values with the number of matching logs for the field `level` over logs for the last 5 minutes:

```logsql
_time:5m | field_values level
```

It is possible to limit the number of returned values by adding `limit N` to the end of `field_values ...`. For example, the following query returns
up to 10 values for the field `user_id` over logs for the last 5 minutes:

```logsql
_time:5m | field_values user_id limit 10
```

If the limit is reached, then the set of returned values is random. Also the number of matching logs for each returned value is zeroed for performance reasons.

See also:

- [`field_names` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#field_names-pipe)
- [`facets` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)

### fields pipe

By default all the [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) are returned in the response.
It is possible to select the given set of log fields with `| fields field1, ..., fieldN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes). For example, the following query selects only `host`
and [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) fields from logs for the last 5 minutes:

```logsql
_time:5m | fields host, _msg
```

`keep` can be used instead of `fields` for convenience. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | keep host, _msg
```

It is possible to use wildcard prefixes in the list of fields to keep. For example, the following query keeps all the fields with names starting with `foo` prefix,
while drops the rest of the fields:

```logsql
_time:5m | fields foo*
```

See also:

- [`copy` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#copy-pipe)
- [`rename` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe)
- [`delete` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe)

### filter pipe

The `<q> | filter ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) filters logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) with the given [filter](https://docs.victoriametrics.com/victorialogs/logsql/#filters).

For example, the following query returns `host` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) values
if the number of log messages with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) for them over the last hour exceeds `1_000`:

```logsql
_time:1h error | stats by (host) count() logs_count | filter logs_count:> 1_000
```

It is allowed to use `where` prefix instead of `filter` prefix for convenience. For example, the following query is equivalent to the previous one:

```logsql
_time:1h error | stats by (host) count() logs_count | where logs_count:> 1_000
```

It is allowed to omit `filter` prefix if the used filters do not clash with [pipe names](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).
So the following query is equivalent to the previous one:

```logsql
_time:1h error | stats by (host) count() logs_count | logs_count:> 1_000
```

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

### first pipe

`<q> | first N by (fields)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the first `N` logs from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) after sorting them
by the given [`fields`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the first 10 logs with the smallest value of `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | first 10 by (request_duration)
```

It is possible to return up to `N` logs individually for each group of logs with the same set of [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
by enumerating the set of these fields in `partition by (...)`.
For example, the following query returns up to 3 logs with the smallest `request_duration` for each host over the last hour:

```logsql
_time:1h | first 3 by (request_duration) partition by (host)
```

See also:

- [`last` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

### format pipe

`<q> | format "pattern" as result_field` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) combines [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results according to the `pattern` and stores it into `result_field`.

For example, the following query stores `request from <ip>:<port>` text into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
by substituting `<ip>` and `<port>` with the corresponding [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) values:

```logsql
_time:5m | format "request from <ip>:<port>" as _msg
```

If the result of the `format` pattern is stored into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
then `as _msg` part can be omitted. The following query is equivalent to the previous one:

```logsql
_time:5m | format "request from <ip>:<port>"
```

String fields can be formatted with the following additional formatting rules:

- The number of seconds in the [duration value](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values) - add `duration_seconds:` in front of the corresponding field name.
  The formatted number is fractional if the duration value contains non-zero milliseconds, microseconds or nanoseconds.

- JSON-compatible quoted string - add `q:` in front of the corresponding field name.
  For example, the following query generates properly encoded JSON object from `_msg` and `stacktrace`
  [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) and stores it into `my_json` output field:

  ```logsql
  _time:5m | format '{"_msg":<q:_msg>,"stacktrace":<q:stacktrace>}' as my_json
  ```

- Uppercase and lowercase strings - add `uc:` or `lc:` in front of the corresponding field name.
  For example, the following query stores uppercase value of `foo` field and lowercase value of `bar` field in the `result` field:

  ```logsql
  _time:5m | format 'uppercase foo: <uc:foo>, lowercase bar: <lc:bar>' as result
  ```

- [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding) and decoding (aka `percent encoding`) - add `urlencode:` or `urldecode:`
  in front of the corresponding field name. For example, the following query properly encodes `user` field in the url query arg:

  ```logsql
  _time:5m | format 'url: http://foo.com/?user=<urlencode:user>'
  ```

- Hex encoding and decoding - add `hexencode:` or `hexdecode:` in front of the corresponding field name.
  For example, the following query hex-encodes `password` field:

  ```logsql
  _time:5m | format 'hex-encoded password: <hexencode:password>'
  ```

- [Base64 encoding](https://en.wikipedia.org/wiki/Base64) and decoding - add `base64encode:` or `base64decode:` in front of the corresponding
  field name. For example, the following query base64-encodes `password` field:

  ```logsql
  _time:5m | format 'base64-encoded password: <base64encode:password>'
  ```

- Converting of hexadecimal number to decimal number - add `hexnumdecode:` in front of the corresponding field name. For example, `format "num=<hexnumdecode:some_hex_field>"`.

Numeric fields can be transformed into the following string representation at `format` pipe:

- [RFC3339 time](https://www.rfc-editor.org/rfc/rfc3339) - by adding `time:` in front of the corresponding field name
  containing [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time).
  The numeric timestamp can be in seconds, milliseconds, microseconds, or nanoseconds — the precision is automatically detected based on the value.
  Both integer and floating-point values are supported.
  For example, `format "time=<time:timestamp>"`.

- Human-readable duration - by adding `duration:` in front of the corresponding numeric field name containing duration in nanoseconds.
  For example, `format "duration=<duration:duration_nsecs>"`. The duration can be converted into nanoseconds with the [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe).

- IPv4 - by adding `ipv4:` in front of the corresponding field name containing `uint32` representation of the IPv4 address.
  For example, `format "ip=<ipv4:ip_num>"`.

- Zero-padded 64-bit hex number - by adding `hexnumencode:` in front of the corresponding field name. For example, `format "hex_num=<hexnumencode:some_field>"`.

Add `keep_original_fields` to the end of `format ... as result_field` when the original non-empty value of the `result_field` must be preserved
instead of overwriting it with the `format` results. For example, the following query adds formatted result to `foo` field only if it was missing or empty:

```logsql
_time:5m | format 'some_text' as foo keep_original_fields
```

Add `skip_empty_results` to the end of `format ...` if empty results shouldn't be written to the output. For example, the following query adds formatted result to `foo` field
when at least `field1` or `field2` aren't empty, while preserving the original `foo` value:

```logsql
_time:5m | format "<field1><field2>" as foo skip_empty_results
```

Performance tip: it is recommended using more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries, which are passed to `format`.
See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional format](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-format)
- [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe)
- [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Conditional format

If the [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` just after the `format` word.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query stores the formatted result to `message` field
only if `ip` and `host` [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) aren't empty, otherwise the original `message` field isn't modified:

```logsql
_time:5m | format if (ip:* and host:*) "request from <ip>:<host>" as message
```

### generate_sequence pipe

The `<q> | generate_sequence <N>` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) skips all the `<q>` results and generates `<N>` output logs
with the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing integer sequence starting from 0 and ending at `N-1`.

This pipe is useful for testing and debugging of the LogsQL pipes. For example, the following query generates 1000 random integers in the range `[0..9]`
and collects the statistics on the number of hits for each random number:

```logsql
* | generate_sequence 1000
    | math round(rand()*10) as rand_num
    | stats by (rand_num) count() hits
    | sort by (rand_num)
```

See also:

- [`rand()` function from `math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)

### join pipe

The `<q1> | join by (<fields>) (<q2>)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) joins `<q1>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results with the `<q2>` results by the given set of comma-separated `<fields>`.
This pipe works in the following way:

1. It executes the `<q2>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) and remembers its results.
1. For each input row from `<q1>` it searches for matching rows in the `<q2>` results by the given `<fields>`.
1. If the `<q2>` results have no matching rows, then the input row is sent to the output as is.
1. If the `<q2>` results have matching rows, then for each matching row the input row is extended
   with new fields seen at the matching row, and the result is sent to the output.

This logic is similar to `LEFT JOIN` in SQL. For example, the following query returns the number of per-user logs across two applications — `app1` and `app2` (see
[stream filters](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter) for details on the `{...}` filter):

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  )
```

If you need results similar to `INNER JOIN` in SQL, then add `inner` suffix after the `join` pipe.
For example, the following query returns stats only for users, which exist in both applications `app1` and `app2`:

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  ) inner
```

It is possible to add a prefix to all the field names returned by the `<query>` by specifying the needed prefix after the `<query>`.
For example, the following query adds `app2.` prefix to all `<query>` log fields:

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  ) prefix "app2."
```

**Performance tips**:

- Make sure that the `<query>` in the `join` pipe returns relatively small number of results, since they are kept in RAM during execution of `join` pipe.
- [Conditional `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) is usually faster to execute.
  They usually require less RAM than the equivalent `join` pipe.

See also:

- [subquery filter](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [conditional `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters)
- [`filter` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe)

### json_array_len pipe

`<q> | json_array_len(field) as result_field` calculates the length of JSON array at the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
and stores it into the `result_field`, for every log entry returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query returns top 5 logs that contain [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with the biggest number of [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) across all the logs for the last 5 minutes:

```logsql
_time:5m | unpack_words _msg as words | json_array_len (words) as words_count | first 5 (words_count desc)
```

See also:

- [`len` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#len-pipe)
- [`unpack_words` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe)
- [`first` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)

### hash pipe

`<q> | hash(field) as result_field` calculates hash value for the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
and stores it into the `result_field`, for every log entry returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates the hash value over `user_id` field and stores it into `user_id_hash` field, across logs for the last 5 minutes:

```logsql
_time:5m | hash(user_id) as user_id_hash
```

See also:

- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`filter` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe)

### last pipe

`<q> | last N by (fields)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the last `N` logs from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) after sorting them
by the given [`fields`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the last 10 logs with the biggest value of `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | last 10 by (request_duration)
```

It is possible to return up to `N` logs individually for each group of logs with the same set of [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
by enumerating the set of these fields in `partition by (...)`.
For example, the following query returns up to 3 logs with the biggest `request_duration` for each host over the last hour:

```logsql
_time:1h | last 3 by (request_duration) partition by (host)
```

See also:

- [`first` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

### len pipe

`<q> | len(field) as result` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) stores byte length of the given `field` value into the `result` field
across all the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query shows top 5 log entries with the maximum byte length of `_msg` field across
logs for the last 5 minutes:

```logsql
_time:5m | len(_msg) as msg_len | sort by (msg_len desc) | limit 5
```

See also:

- [`json_array_len` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#json_array_len-pipe)
- [`sum_len` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#sum_len-stats)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)
- [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe)

### limit pipe

If only a subset of selected logs must be processed, then `| limit N` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used, where `N` can contain any [supported integer numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).
For example, the following query returns up to 100 logs over the last 5 minutes:

```logsql
_time:5m | limit 100
```

`head` keyword can be used instead of `limit` for convenience. For example, `_time:5m | head 100` is equivalent to `_time:5m | limit 100`.

The `N` in `head N` can be omitted - in this case up to 10 matching logs are returned:

```logsql
error | head
```

By default rows are selected in arbitrary order for performance reasons, so the query above can return different sets of logs every time it is executed.
[`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) can be used for making sure the logs are in the same order before applying `limit ...` to them.

See also:

- [`sample` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sample-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`offset` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#offset-pipe)

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

### offset pipe

If some selected logs must be skipped after [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe), then `| offset N` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used, where `N` can contain any [supported integer numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).
For example, the following query skips the first 100 logs over the last 5 minutes after sorting them by [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field):

```logsql
_time:5m | sort by (_time) | offset 100
```

`skip` keyword can be used instead of `offset` keyword for convenience. For example, `_time:5m | skip 10` is equivalent to `_time:5m | offset 10`.

Note that skipping rows without sorting makes little sense, since they can be returned in arbitrary order for performance reasons.
Rows can be sorted with [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).

See also:

- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

### pack_json pipe

`<q> | pack_json as field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) packs all the [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of every log
entry returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) into JSON object and stores it as a string in the given `field_name`.

For example, the following query packs all the fields into JSON object and stores it into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
for logs over the last 5 minutes:

```logsql
_time:5m | pack_json as _msg
```

The `as _msg` part can be omitted if packed JSON object is stored into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | pack_json
```

If only a subset of fields must be packed into JSON, then it must be listed inside `fields (...)` after `pack_json`. For example, the following query builds JSON with `foo` and `bar` fields
only and stores the result in `baz` field:

```logsql
_time:5m | pack_json fields (foo, bar) as baz
```

It is possible to pass field prefixes into `fields (...)` in order to pack only the fields, which start with the given prefixes.
For example, the following query builds JSON with all the fields, which start with either `foo.` or `bar.`:

```logsql
_time:5m | pack_json fields (foo.*, bar.*) as baz
```

The `pack_json` doesn't modify or delete other fields. If you do not need them, then add [`| fields ...`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) after the `pack_json` pipe. For example, the following query
leaves only the `foo` field with the original log fields packed into JSON:

```logsql
_time:5m | pack_json as foo | fields foo
```

See also:

- [`pack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_logfmt-pipe)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)

### pack_logfmt pipe

`<q> | pack_logfmt as field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) packs all the [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) for every log entry
returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) into [logfmt](https://brandur.org/logfmt) message and stores it as a string in the given `field_name`.

For example, the following query packs all the fields into [logfmt](https://brandur.org/logfmt) message and stores it
into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) for logs over the last 5 minutes:

```logsql
_time:5m | pack_logfmt as _msg
```

The `as _msg` part can be omitted if packed message is stored into [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | pack_logfmt
```

If only a subset of fields must be packed into [logfmt](https://brandur.org/logfmt), then it must be listed inside `fields (...)` after `pack_logfmt`.
For example, the following query builds [logfmt](https://brandur.org/logfmt) message with `foo` and `bar` fields only and stores the result in `baz` field:

```logsql
_time:5m | pack_logfmt fields (foo, bar) as baz
```

It is possible to pass field prefixes into `fields (...)` in order to pack only the fields, which start with the given prefixes.
For example, the following query builds `logfmt` message with all the fields, which start with either `foo.` or `bar.`:

```logsql
_time:5m | pack_logfmt fields (foo.*, bar.*) as baz
```

The `pack_logfmt` doesn't modify or delete other fields. If you do not need them, then add [`| fields ...`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) after the `pack_logfmt` pipe. For example, the following query
leaves only the `foo` field with the original log fields packed into [logfmt](https://brandur.org/logfmt):

```logsql
_time:5m | pack_logfmt as foo | fields foo
```

See also:

- [`pack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_json-pipe)
- [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)

### query_stats pipe

The `<q> | query_stats` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the following execution statistics for the given [query `<q>`](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax):

- `BytesReadColumnsHeaders` - the number of bytes read from disk for column headers. Use [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) for reducing the number of bytes read for column headers.
- `BytesReadColumnsHeaderIndexes` - the number of bytes read from disk for column header indexes.
- `BytesReadBloomFilters` - the number of bytes read from disk for bloom filters.
- `BytesReadValues` - the number of bytes read from disk for [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
   Use [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) for reducing the number of bytes read for log field values.
- `BytesReadTimestamps` - the number of bytes read from disk for [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).
- `BytesReadBlockHeaders` - the number of bytes read from disk for block headers.
- `BytesReadTotal` - the total number of bytes read from disk.
- `BlocksProcessed` - the number of data blocks processed during query execution. Use more narrow [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) and [log stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)
  for reducing the number of data blocks processed.
- `RowsProcessed` - the number of log entries processed during query execution. Use more narrow [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) and [log stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)
  for reducing the number of processed log entries.
- `RowsFound` - the number of log entries found by the query.
- `ValuesRead` - the number of [log field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) read during query processing.
  Use [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) for reducing the number of field values read.
- `TimestampsRead` - the number of [`_time` fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) read during query processing.
- `BytesProcessedUncompressedValues` - the number of uncompressed bytes for [log field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
  which are processed during query execution.
- `QueryDurationNsecs` - the duration of the query in nanoseconds. It can be used for calculating various rates over the query stats with the [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe).

This pipe is useful for investigation and optimizing slow queries.

See also:

- [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe)
- [query troubleshooting](https://docs.victoriametrics.com/victorialogs/logsql/#troubleshooting)

### rename pipe

If some [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) must be renamed, then `| rename src1 as dst1, ..., srcN as dstN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used.
For example, the following query renames `host` field to `server` for logs over the last 5 minutes, so the output contains `server` field instead of `host` field:

```logsql
_time:5m | rename host as server
```

Multiple fields can be renamed with a single `| rename ...` pipe. For example, the following query renames `host` to `instance` and `app` to `job`:

```logsql
_time:5m | rename host as instance, app as job
```

The `as` keyword is optional.

`mv` keyword can be used instead of `rename` keyword for convenience. For example, `_time:5m | mv foo bar` is equivalent to `_time:5m | rename foo as bar`.

It is possible to rename multiple fields with the given prefix to fields with another prefix. For example, the following query renames all the fields
starting with `foo` prefix to fields starting with `bar` prefix:

```logsql
_time:5m | rename foo* as bar*
```

It is also possible to remove the common prefix from some fields. For example, the following query removes the `foo` prefix from all the fields that start with `foo`:

```logsql
_time:5m | rename foo* as *
```

It is also possible to add a common prefix to all the fields. For example, the following query adds the `foo` prefix to all the fields:

```logsql
_time:5m | rename * as foo*
```

See also:

- [`copy` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#copy-pipe)
- [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe)
- [`delete` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe)

### replace pipe

`<q> | replace ("old", "new") at field` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) replaces all the occurrences of the `old` substring with the `new` substring
in the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) over all the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query replaces all the `secret-password` substrings with `***` in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
for logs over the last 5 minutes:

```logsql
_time:5m | replace ("secret-password", "***") at _msg
```

The `at _msg` part can be omitted if the replacement occurs in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | replace ("secret-password", "***")
```

The number of replacements can be limited with `limit N` at the end of `replace`. For example, the following query replaces only the first `foo` substring with `bar`
at the [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `baz`:

```logsql
_time:5m | replace ('foo', 'bar') at baz limit 1
```

Performance tip: it is recommended using more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries, which are passed to `replace`.
See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional replace](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-replace)
- [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe)
- [`collapse_nums`](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe)
- [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Conditional replace

If the [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `replace`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query replaces `secret` with `***` in the `password` field
only if the `user_type` field equals `admin`:

```logsql
_time:5m | replace if (user_type:=admin) ("secret", "***") at password
```

### replace_regexp pipe

`<q> | replace_regexp ("regexp", "replacement") at field` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) replaces all the substrings matching the given `regexp` with the given `replacement`
in the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) over all the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

The `regexp` must contain regular expression with [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
The `replacement` may contain `$N` or `${N}` placeholders, which are substituted with the `N-th` capturing group in the `regexp`.

For example, the following query replaces all the substrings starting with `host-` and ending with `-foo` with the contents between `host-` and `-foo` in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) for logs over the last 5 minutes:

```logsql
_time:5m | replace_regexp ("host-(.+?)-foo", "$1") at _msg
```

The `at _msg` part can be omitted if the replacement occurs in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | replace_regexp ("host-(.+?)-foo", "$1")
```

The number of replacements can be limited with `limit N` at the end of `replace_regexp`. For example, the following query replaces only the first `password: ...` substring
ending with whitespace with empty substring at the [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `baz`:

```logsql
_time:5m | replace_regexp ('password: [^ ]+', '') at baz limit 1
```

Performance tips:

- It is recommended to use the [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) instead of `replace_regexp` if possible, since it works faster.
- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `replace_regexp`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional replace_regexp](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-replace_regexp)
- [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe)
- [`collapse_nums` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe)
- [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`decolorize` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#decolorize-pipe)

#### Conditional replace_regexp

If the [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `replace_regexp`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query replaces `password: ...` substrings ending with whitespace
with `***` in the `foo` field only if the `user_type` field equals `admin`:

```logsql
_time:5m | replace_regexp if (user_type:=admin) ("password: [^ ]+", "***") at foo
```

### running_stats pipe

The `<q> | running_stats ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) calculates running stats (such as [running count](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats) or [running sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats))
over the specified [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)
and stores the stats in the specified log fields for each input log entry.

The running stats is calculated over the logs sorted by time, so the `<q>` must return the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field)
in order to properly calculate the running stats.

The `running_stats` pipe puts all the logs returned by `<q>` in memory, so make sure the `<q>` returns the limited number of logs in order to avoid high memory usage.

For example, the following LogsQL query calculates [running sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats) for the `hits` field over the logs for the last 5 minutes:

```logsql
_time:5m | running_stats sum(hits) as running_hits
```

The `| running_stats ...` pipe has the following basic format:

```logsql
... | running_stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Where `stats_func*` is any of the supported [running stats function](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions), while the `result_name*` is the name of the log field
to store the result of the corresponding stats function. The `as` keyword is optional.

For example, the following query calculates the following running stats for logs over the last 5 minutes:

- the number of logs with the help of [`count` function](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats);
- the sum of `hits` field with the help of [`sum` function](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats):

```logsql
_time:5m
    | running_stats
        count() as running_logs,
        sum(hits) as running_hits
```

It is allowed omitting the result name. In this case the result name equals the string representation of the used [running stats function](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions).
For example, the following query returns the same stats as the previous one, but gives `count()` and `sum(hits)` names for the returned fields:

```logsql
_time:5m | running_stats count(), sum(hits)
```

It is useful to combine `running_stats` with [stats by time buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets). For example, the following query returns per-hour number of logs over the last day,
plus running number of logs.

```logsql
_time:1d
    | stats by (_time:hour) count() as hits
    | running_stats sum(hits) as running_hits
```

See also:

- [`running_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions)
- [`running_stats` by fields](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-by-fields)
- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

#### running_stats by fields

The following LogsQL syntax can be used for calculating independent running stats per group of log fields:

```logsql
<q> | running_stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `(field1, ..., fieldM)` group of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
seen in the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates running number of logs and running number of `hits` over the last 5 minutes,
grouped by `(host, path)` fields:

```logsql
_time:5m
    | running_stats by (host, path)
        count() running_logs,
        sum(hits) running_hits
```

The `by` keyword can be skipped in `running_stats ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | running_stats (host, path) count() running_logs, sum(hits) running_hits
```

See also:

- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`running_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions)


### sample pipe

The `<q> | sample N` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns `1/N`th random sample of logs for the `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
For example, the following query returns ~1% (1/100th random sample) of logs over the last hour with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
_time:1h error | sample 100
```

See also:

- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)

### set_stream_fields pipe

The `| set_stream_fields field1, ..., fieldN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes)
sets the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
as [`_stream` fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).

For example, if the logs returned by `_time:5m` [filter](https://docs.victoriametrics.com/victorialogs/logsql/#filters) have `host="foo"` and `path="/bar"` fields,
then the following query sets `_stream` field to `{host="foo", path="/bar"}`:

```logsql
_time:5m | set_stream_fields host, path
```

See also:

- [conditional `set_stream_fields`](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-set_stream_fields)
- [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe)

#### Conditional set_stream_fields

The [`set_stream_fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#set_stream_fields-pipe) can be applied to a subset of input logs
which match the given [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters), by using `if (...)` after the `set_stream_fields`.
For example, the following query updates [`_stream` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
only for logs with the `host="foobar"` field, while leaving the original `_stream` value for the rest of the logs:

```logsql
_time:5m | set_stream_fields if (host:="foobar") host, app
```

### sort pipe

By default logs are selected in arbitrary order for performance reasons. If logs must be sorted, then `<q> | sort by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used
for sorting logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) by the given [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
using [natural sorting](https://en.wikipedia.org/wiki/Natural_sort_order).

For example, the following query returns logs for the last 5 minutes sorted by [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
and then by [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field):

```logsql
_time:5m | sort by (_stream, _time)
```

Add `desc` after the given log field in order to sort in reverse order of this field. For example, the following query sorts logs in reverse order of `request_duration_seconds` field:

```logsql
_time:5m | sort by (request_duration_seconds desc)
```

The reverse order can be applied globally via `desc` keyword after `by(...)` clause:

```logsql
_time:5m | sort by (foo, bar) desc
```

The `by` keyword can be skipped in `sort ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | sort (foo, bar) desc
```

The `order` alias can be used instead of `sort`, so the following query is equivalent to the previous one:

```logsql
_time:5m | order by (foo, bar) desc
```

Sorting a large number of logs can consume a lot of CPU time and memory. Sometimes it is enough to return the first `N` entries with the biggest
or the smallest values. This can be done by adding `limit N` to the end of `sort ...` pipe.
Such a query consumes less memory when sorting a large number of logs, since it keeps in memory only `N` log entries.
For example, the following query returns top 10 log entries with the biggest values
for the `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) during the last hour:

```logsql
_time:1h | sort by (request_duration desc) limit 10
```

This query is equivalent to the following one, which uses [`last` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe):

```logsql
_time:1h | last 10 by (request_duration)
```

If the first `N` sorted results must be skipped, then `offset N` can be added to `sort` pipe. For example,
the following query skips the first 10 logs with the biggest `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
and then returns the next 20 sorted logs for the last 5 minutes:

```logsql
_time:1h | sort by (request_duration desc) offset 10 limit 20
```

It is possible to sort the logs and apply the `limit` individually for each group of logs with the same set of [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
by enumerating the set of these fields in `partition by (...)`.
For example, the following query returns up to 3 logs with the biggest `request_duration` for each host over the last hour:

```logsql
_time:1h | sort by (request_duration desc) partition by (host) limit 3
```

It is possible to return a rank (sort order number) for every sorted log by adding `rank as <fieldName>` to the end of the `| sort ...` pipe.
For example, the following query stores rank for sorted by [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) logs
into `position` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
_time:5m | sort by (_time) rank as position
```

Note that sorting a large number of logs can be slow and can consume a lot of additional memory.
It is recommended to limit the number of logs before sorting with the following approaches:

- Adding `limit N` to the end of `sort ...` pipe.
- Reducing the selected time range with [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter).
- Using more specific [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters), so they select less logs.
- Limiting the number of selected [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) via [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe).

See also:

- [`first` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)
- [`last` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)
- [`offset` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#offset-pipe)

### split pipe

The `<q> | split <separator> from <src_field> as <dst_field>` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) splits `<src_field>` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
obtained from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `<dst_field>` as a JSON array, by using the given `<separator>`.

For example, the following query splits [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) by `,` and stores the results into `items` field:

```logsql
_time:5m | split "," from _msg as items
```

The `as <dst_field>` part is optional. If it is missing, then the result is stored in the `<src_field>` specified in `from <src_field>`.
For example, the following query stores the split result into `_msg` field:

```logsql
_time:5m | split "," from _msg
```

The `from <src_field>` part is optional. If it is missing, then the `_msg` field is used as a source field. The following query is equivalent to the previous one:

```logsql
_time:5m | split ","
```

It is convenient to use [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) for unrolling the JSON array with the split results.
For example, the following query returns top 5 most frequently seen comma-separated items across [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
for the last 5 minutes:

```logsql
_time:5m | split "," as items | unroll items | top 5 (items)
```

See also:

- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`unpack_words` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe)


### stats pipe

The `<q> | stats ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) calculates various stats over the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
For example, the following LogsQL query uses [`count` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats) for calculating the number of logs for the last 5 minutes:

```logsql
_time:5m | stats count() as logs_total
```

The `| stats ...` pipe has the following basic format:

```logsql
... | stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Where `stats_func*` is any of the supported [stats function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), while the `result_name*` is the name of the log field
to store the result of the corresponding stats function. The `as` keyword is optional.

For example, the following query calculates the following stats for logs over the last 5 minutes:

- the number of logs with the help of [`count` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats);
- the number of unique [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) with the help of [`count_uniq` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats):

```logsql
_time:5m | stats count() logs_total, count_uniq(_stream) streams_total
```

It is allowed omitting `stats` prefix for convenience. So the following query is equivalent to the previous one:

```logsql
_time:5m | count() logs_total, count_uniq(_stream) streams_total
```

It is allowed omitting the result name. In this case the result name equals the string representation of the used [stats function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions).
For example, the following query returns the same stats as the previous one, but gives `count()` and `count_uniq(_stream)` names for the returned fields:

```logsql
_time:5m | count(), count_uniq(_stream)
```

See also:

- [stats pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [stats by fields](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields)
- [stats by time buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets)
- [stats by time buckets with timezone offset](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets-with-timezone-offset)
- [stats by field buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-field-buckets)
- [stats by IPv4 buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-ipv4-buckets)
- [stats with additional filters](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters)
- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)

#### Stats by fields

The following LogsQL syntax can be used for calculating independent stats per group of log fields:

```logsql
<q> | stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `(field1, ..., fieldM)` group of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
seen in the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates the number of logs and unique IP addresses over the last 5 minutes,
grouped by `(host, path)` fields:

```logsql
_time:5m | stats by (host, path) count() logs_total, count_uniq(ip) ips_total
```

The `by` keyword can be skipped in `stats ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | stats (host, path) count() logs_total, count_uniq(ip) ips_total
```

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats)

#### Stats by time buckets

The following syntax can be used for calculating stats grouped by time buckets:

```logsql
<q> | stats by (_time:step)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `step` of the [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) field
across logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax). The `step` can have any [duration value](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
For example, the following LogsQL query returns per-minute number of logs and unique IP addresses over the last 5 minutes:

```logsql
_time:5m | stats by (_time:1m) count() logs_total, count_uniq(ip) ips_total
```

It might be useful to calculate running stats over the calculated per-time bucket stats, with the help of [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe).
For example, the following query adds the running number of logs to the `running_hits` field for the query above:

```logsql
_time:5m
    | stats by (_time:1m) count() as hits
    | running_stats sum(hits) as running_hits
```

It might be useful to calculate total stats over the calculated per-time bucket stats, with the help of [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe).
For example, the following query adds the total number of logs into `total_hits` field and then uses this field for calculating the per-minute percentage of hits
with the [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe):

```logsql
_time:5m
    | stats by (_time:1m) count() as hits
    | total_stats sum(hits) as total_hits
    | math round((hits / total_hits)*100) as hits_percent
```

Additionally, the following `step` values are supported:

- `nanosecond` - equals `1ns` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `microsecond` - equals `1µs` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `millisecond` - equals `1ms` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `second` - equals `1s` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `minute` - equals `1m` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `hour` - equals `1h` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `day` - equals `1d` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `week` - equals `1w` [duration](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).
- `month` - equals one month. It properly takes into account the number of days in each month.
- `year` - equals one year. It properly takes into account the number of days in each year.

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)

#### Stats by time buckets with timezone offset

VictoriaLogs stores [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) values as [Unix time](https://en.wikipedia.org/wiki/Unix_time)
in nanoseconds. This time corresponds to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) time zone. Sometimes it is needed calculating stats
grouped by days or weeks at non-UTC timezone. This is possible with the following syntax:

```logsql
<q> | stats by (_time:step offset timezone_offset) ...
```

For example, the following query calculates per-day number of logs over the last week, in `UTC+02:00` [time zone](https://en.wikipedia.org/wiki/Time_zone):

```logsql
_time:1w | stats by (_time:1d offset 2h) count() logs_total
```

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)

#### Stats by field buckets

Every log field inside `<q> | stats by (...)` can be bucketed in the same way as `_time` field in [this example](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets).
Any [numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values) can be used as `step` value for the bucket. For example, the following query calculates
the number of requests for the last hour, bucketed by 10KB of `request_size_bytes` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
_time:1h | stats by (request_size_bytes:10KB) count() requests
```

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)

#### Stats by IPv4 buckets

Stats can be bucketed by [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) containing [IPv4 addresses](https://en.wikipedia.org/wiki/IP_address)
via the `ip_field_name:/network_mask` syntax inside `by(...)` clause. For example, the following query returns the number of log entries per `/24` subnetwork
extracted from the `ip` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) during the last 5 minutes:

```logsql
_time:5m | stats by (ip:/24) count() requests_per_subnet
```

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`ipv4_range` filter](https://docs.victoriametrics.com/victorialogs/logsql/#ipv4-range-filter)

#### Stats with additional filters

Sometimes it is needed to calculate [stats](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) on different subsets of matching logs. This can be done by inserting an `if (<any_filters>)` condition
between the [stats function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) and `result_name`, where `any_filters` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters).
For example, the following query calculates individually the number of [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with `GET`, `POST` and `PUT` [words](https://docs.victoriametrics.com/victorialogs/logsql/#word), additionally to the total number of logs over the last 5 minutes:

```logsql
_time:5m | stats
  count() if (GET) gets,
  count() if (POST) posts,
  count() if (PUT) puts,
  count() total
```

If zero input rows match the given `if (...)` filter, then zero result is returned for the given stats function.

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)

### stream_context pipe

`<q> | stream_context ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) allows selecting surrounding logs in a [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
across the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) in the way similar to `grep -A` / `grep -B`.
The returned log chunks are delimited with `---` [log message](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) for easier investigation.

For example, the following query returns up to 10 additional logs after every log message with the `panic` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) across all the logs for the last 5 minutes:

```logsql
_time:5m panic | stream_context after 10
```

The following query returns up to 5 additional logs in front of every log message with the `stacktrace` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) across all the logs for the last 5 minutes:

```logsql
_time:5m stacktrace | stream_context before 5
```

The following query returns up to 2 logs in front of the log message with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) and up to 5 logs after this log message
across all the logs for the last 5 minutes:

```logsql
_time:5m error | stream_context before 2 after 5
```

By default `stream_context` pipe looks for surrounding logs in a one-hour window. This window can be changed via the `time_window` option at query time.
For example, the following query searches for surrounding logs in a one-week window:

```logsql
_time:5m error | stream_context before 10 time_window 1w
```

The `| stream_context` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) must go first just after the [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters).

See also:

- [stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)

### time_add pipe

`<q> | time_add <duration>` adds the given `<duration>` to the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).
The `<duration>` can be in any format described [here](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).

For example, the following query adds one hour to `_time` field in the selected logs:

```logsql
_time:5m | time_add 1h
```

Specify negative duration for subtracting it from the `_time` field:

```logsql
_time:5m | time_add -1h
```

Add `at <field_name>` to the end of the `time_add` pipe in order to add the given `<duration>` to the [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the given `<field_name>`. For example, the following query adds one week to the field `transaction_time`:

```logsql
_time:5m | time_add 1w at transaction_time
```

See also:

- [`_time` filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter).
- [`time_offset` option](https://docs.victoriametrics.com/victorialogs/logsql/#query-options).

### top pipe

`<q> | top N by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns top `N` sets for `(field1, ..., fieldN)` [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the maximum number of matching log entries across logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query returns top 7 [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
with the maximum number of log entries over the last 5 minutes. The number of entries is returned in the `hits` field:

```logsql
_time:5m | top 7 by (_stream)
```

The `N` is optional. If it is skipped, then top 10 entries are returned. For example, the following query returns top 10 values
for `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) seen in logs for the last 5 minutes:

```logsql
_time:5m | top by (ip)
```

It is possible to give another name for the `hits` field via `hits as <new_name>` syntax. For example, the following query returns top per-`path` hits in the `visits` field:

```logsql
_time:5m | top by (path) hits as visits
```

It is possible to set a `rank` field for each returned entry for the `top` pipe by adding `rank`. For example, the following query sets the `rank` field for each returned `ip`:

```logsql
_time:5m | top 10 by (ip) rank
```

The `rank` field can have other name. For example, the following query uses the `position` field name instead of `rank` field name in the output:

```logsql
_time:5m | top 10 by (ip) rank as position
```

See also:

- [`first` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)
- [`last` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe)
- [`facets` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`histogram` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#histogram-stats)

### total_stats pipe

The `<q> | total_stats ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) calculates total (global) stats (such as [global count](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats) or [global sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats))
over the specified [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)
and stores these stats in the specified log fields for each input log entry.

The total stats is calculated over the logs sorted by time, so the `<q>` must return the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field)
in order to properly calculate the total stats.

The `total_stats` pipe puts all the logs returned by `<q>` in memory, so make sure the `<q>` returns the limited number of logs in order to avoid high memory usage.

For example, the following LogsQL query calculates [total sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats) for the `hits` field over the logs for the last 5 minutes:

```logsql
_time:5m | total_stats sum(hits) as total_hits
```

The `| total_stats ...` pipe has the following basic format:

```logsql
... | total_stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Where `stats_func*` is any of the supported [total stats function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions), while the `result_name*` is the name of the log field
to store the result of the corresponding stats function. The `as` keyword is optional.

For example, the following query calculates the following total stats for logs over the last 5 minutes:

- the number of logs with the help of [`count` function](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats);
- the sum of `hits` field with the help of [`sum` function](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats):

```logsql
_time:5m
    | total_stats
        count() as total_logs,
        sum(hits) as total_hits
```

It is allowed omitting the result name. In this case the result name equals the string representation of the used [total stats function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions).
For example, the following query returns the same stats as the previous one, but gives `count()` and `sum(hits)` names for the returned fields:

```logsql
_time:5m | total_stats count(), sum(hits)
```

It is useful to combine `total_stats` with [stats by time buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets). For example, the following query returns per-hour number of logs over the last day,
plus the total number of logs, and then calculates the per-hour percent of hits over the daily hits.

```logsql
_time:1d
    | stats by (_time:hour) count() as hits
    | total_stats sum(hits) as total_hits
    | math round((hits / total_hits)*100) as hits_percent
```

See also:

- [`total_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions)
- [`total_stats` by fields](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-by-fields)
- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

#### total_stats by fields

The following LogsQL syntax can be used for calculating independent total stats per group of log fields:

```logsql
<q> | total_stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `(field1, ..., fieldM)` group of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
seen in the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates total number of logs and total number of `hits` over the last 5 minutes,
grouped by `(host, path)` fields:

```logsql
_time:5m
    | total_stats by (host, path)
        count() total_logs,
        sum(hits) total_hits
```

The `by` keyword can be skipped in `total_stats ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | total_stats (host, path) count() total_logs, sum(hits) total_hits
```

See also:

- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`total_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions)


### union pipe

`<q1> | union (<q2>)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns results of `<q1>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) followed by results of `<q2>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
It works similarly to `UNION ALL` in SQL. `<q1>` and `q2` may contain arbitrary [LogsQL queries](https://docs.victoriametrics.com/victorialogs/logsql/#logsql-tutorial).
For example, the following query returns logs with `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) for the last 5 minutes, plus logs with `panic` word for the last hour:

```logsql
_time:5m error | union (_time:1h panic)
```

See also:

- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)
- [subquery filter](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)

### uniq pipe

`<q> | uniq by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns unique values for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax). For example, the following LogsQL query
returns unique values for `ip` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | uniq by (ip)
```

It is possible to specify multiple fields inside `by(...)` clause. In this case all the unique sets for the given fields
are returned. For example, the following query returns all the unique `(host, path)` pairs for the logs over the last 5 minutes:

```logsql
_time:5m | uniq by (host, path)
```

The unique entries are returned in arbitrary order. Use [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) in order to sort them if needed.

Add `with hits` after `uniq by (...)` in order to return the number of matching logs for each field value:

```logsql
_time:5m | uniq by (host) with hits
```

Unique entries are stored in memory during query execution. Big number of unique selected entries may require a lot of memory.
Sometimes it is enough to return up to `N` unique entries. This can be done by adding `limit N` after `by (...)` clause.
This allows limiting memory usage. For example, the following query returns up to 100 unique `(host, path)` pairs for the logs over the last 5 minutes:

```logsql
_time:5m | uniq by (host, path) limit 100
```

If the `limit` is reached, then arbitrary subset of unique values can be returned. The `hits` calculation doesn't work when the `limit` is reached.

The `by` keyword can be skipped in `uniq ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | uniq (host, path) limit 100
```

See also:

- [`uniq_values` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)

### unpack_json pipe

`<q> | unpack_json from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks `{"k1":"v1", ..., "kN":"vN"}` JSON from the given [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `k1`, ... `kN` output field names with the corresponding `v1`, ..., `vN` values.
It overrides existing fields with names from the `k1`, ..., `kN` list. Other fields remain untouched.

Nested JSON is unpacked according to the rules defined [here](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query unpacks JSON fields from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) across logs for the last 5 minutes:

```logsql
_time:5m | unpack_json from _msg
```

The `from _msg` part can be omitted when JSON fields are unpacked from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_json
```

If only some fields must be extracted from JSON, then they can be enumerated inside `fields (...)`. For example, the following query unpacks only `foo` and `bar`
fields from JSON value stored in `my_json` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
_time:5m | unpack_json from my_json fields (foo, bar)
```

If it is needed to extract all the fields with some common prefix, then this can be done via `fields(prefix*)` syntax.

If it is needed to preserve the original non-empty field values, then add `keep_original_fields` to the end of `unpack_json ...`. For example,
the following query preserves the original non-empty values for `ip` and `host` fields instead of overwriting them with the unpacked values:

```logsql
_time:5m | unpack_json from foo fields (ip, host) keep_original_fields
```

Add `skip_empty_results` to the end of `unpack_json ...` if the original field values must be preserved when the corresponding unpacked values are empty.
For example, the following query preserves the original `ip` and `host` field values for empty unpacked values:

```logsql
_time:5m | unpack_json fields (ip, host) skip_empty_results
```

Performance tip: if you need to extract a single field from long JSON, it is faster to use the [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe). For example, the following query extracts the `"ip"` field from JSON
stored in [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) at the maximum speed:

```
_time:5m | extract '"ip":<ip>'
```

If you want to make sure that the unpacked JSON fields do not clash with the existing fields, then specify common prefix for all the fields extracted from JSON,
by adding `result_prefix "prefix_name"` to `unpack_json`. For example, the following query adds the `foo_` prefix for all the unpacked fields
from `foo`:

```logsql
_time:5m | unpack_json from foo result_prefix "foo_"
```

Performance tips:

- It is better from performance and resource usage PoV ingesting parsed JSON logs into VictoriaLogs
  according to the [supported data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of ingesting unparsed JSON lines into VictoriaLogs and then parsing them at query time with [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe).

- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `unpack_json`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional `unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-unpack_json)
- [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)
- [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`split` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#split-pipe)
- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`pack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_json-pipe)
- [`pack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pack_logfmt-pipe)

#### Conditional unpack_json

If the [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unpack_json`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unpacks JSON fields from `foo` field only if `ip` field in the current log entry isn't set or empty:

```logsql
_time:5m | unpack_json if (ip:"") from foo
```

### unpack_logfmt pipe

`<q> | unpack_logfmt from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks `k1=v1 ... kN=vN` [logfmt](https://brandur.org/logfmt) fields
from the given [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `k1`, ... `kN` field names
with the corresponding `v1`, ..., `vN` values. It overrides existing fields with names from the `k1`, ..., `kN` list. Other fields remain untouched.

For example, the following query unpacks [logfmt](https://brandur.org/logfmt) fields from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
across logs for the last 5 minutes:

```logsql
_time:5m | unpack_logfmt from _msg
```

The `from _msg` part can be omitted when [logfmt](https://brandur.org/logfmt) fields are unpacked from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_logfmt
```

If only some fields must be unpacked from logfmt, then they can be enumerated inside `fields (...)`. For example, the following query extracts only `foo` and `bar` fields
from logfmt stored in the `my_logfmt` field:

```logsql
_time:5m | unpack_logfmt from my_logfmt fields (foo, bar)
```

If it is needed to extract all the fields with some common prefix, then this can be done via `fields(prefix*)` syntax.

If it is needed to preserve the original non-empty field values, then add `keep_original_fields` to the end of `unpack_logfmt ...`. For example,
the following query preserves the original non-empty values for `ip` and `host` fields instead of overwriting them with the unpacked values:

```logsql
_time:5m | unpack_logfmt from foo fields (ip, host) keep_original_fields
```

Add `skip_empty_results` to the end of `unpack_logfmt ...` if the original field values must be preserved when the corresponding unpacked values are empty.
For example, the following query preserves the original `ip` and `host` field values for empty unpacked values:

```logsql
_time:5m | unpack_logfmt fields (ip, host) skip_empty_results
```

Performance tip: if you need to extract a single field from a long [logfmt](https://brandur.org/logfmt) line, it is faster to use the [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe).
For example, the following query extracts `"ip"` field from [logfmt](https://brandur.org/logfmt) line stored
in [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```
_time:5m | extract ' ip=<ip>'
```

If you want to make sure that the unpacked [logfmt](https://brandur.org/logfmt) fields do not clash with the existing fields, then specify common prefix for all the fields extracted from logfmt,
by adding `result_prefix "prefix_name"` to `unpack_logfmt`. For example, the following query adds `foo_` prefix for all the unpacked fields
from `foo` field:

```logsql
_time:5m | unpack_logfmt from foo result_prefix "foo_"
```

Performance tips:

- It is better from performance and resource usage PoV ingesting parsed [logfmt](https://brandur.org/logfmt) logs into VictoriaLogs
  according to the [supported data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of ingesting unparsed logfmt lines into VictoriaLogs and then parsing them at query time with [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe).

- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `unpack_logfmt`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional unpack_logfmt](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-unpack_logfmt)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
- [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Conditional unpack_logfmt

If the [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unpack_logfmt`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unpacks logfmt fields from `foo` field
only if `ip` field in the current log entry isn't set or empty:

```logsql
_time:5m | unpack_logfmt if (ip:"") from foo
```

### unpack_syslog pipe

`<q> | unpack_syslog from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks [syslog](https://en.wikipedia.org/wiki/Syslog) message
from the given [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results.
It understands the following Syslog formats:

- [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164) aka `<PRI>MMM DD hh:mm:ss HOSTNAME APP-NAME[PROCID]: MESSAGE`
- [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) aka `<PRI>1 TIMESTAMP HOSTNAME APP-NAME PROCID MSGID [STRUCTURED-DATA] MESSAGE`

The following fields are unpacked:

- `level` - obtained from `PRI`.
- `priority` - obtained from `PRI`.
- `facility` - calculated as `PRI / 8`.
- `facility_keyword` - string representation of the `facility` field according to [these docs](https://en.wikipedia.org/wiki/Syslog#Facility).
- `severity` - calculated as `PRI % 8`.
- `format` - either `rfc3164` or `rfc5424` depending on which Syslog format is unpacked.
- `timestamp` - timestamp in [ISO8601 format](https://en.wikipedia.org/wiki/ISO_8601). The `MMM DD hh:mm:ss` timestamp in [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164)
  is automatically converted into [ISO8601 format](https://en.wikipedia.org/wiki/ISO_8601) by assuming that the timestamp belongs to the last 12 months.
- `hostname`
- `app_name`
- `proc_id`
- `msg_id`
- `message`

The `<PRI>` part is optional. If it is missing, then `priority`, `facility` and `severity` fields aren't set.

The `[STRUCTURED-DATA]` is parsed into fields with the `SD-ID.param1`, `SD-ID.param2`, ..., `SD-ID.paramN` names and the corresponding values
according to [the specification](https://datatracker.ietf.org/doc/html/rfc5424#section-6.3).

If the `app_name` equals `CEF` and the `message` contains Common Event Format data for SIEM
aka [CEF for Syslog](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-8.3/cef-implementation-standard/Content/CEF/Chapter%201%20What%20is%20CEF.htm),
then it is automatically parsed into the following fields:

- `cef.version` - the CEF version
- `cef.device_vendor` - the device vendor field
- `cef.device_product` - the device product field
- `cef.device_version` - the device version field
- `cef.device_event_class_id` - the device event class id
- `cef.name` - the CEF name
- `cef.severity` - the severity field

Optional extension fields are parsed into `cef.extension.<key>=<value>` fields.

For example, the following query unpacks [syslog](https://en.wikipedia.org/wiki/Syslog) message from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
across logs for the last 5 minutes:

```logsql
_time:5m | unpack_syslog from _msg
```

The `from _msg` part can be omitted when [syslog](https://en.wikipedia.org/wiki/Syslog) message is unpacked
from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_syslog
```

By default timestamps in [RFC3164 format](https://datatracker.ietf.org/doc/html/rfc3164) are converted to local timezone. It is possible to change the timezone
offset via `offset` option. For example, the following query adds 5 hours and 30 minutes to unpacked `rfc3164` timestamps:

```logsql
_time:5m | unpack_syslog offset 5h30m
```

If it is needed to preserve the original non-empty field values, then add `keep_original_fields` to the end of `unpack_syslog ...`:

```logsql
_time:5m | unpack_syslog keep_original_fields
```

If you want to make sure that the unpacked [syslog](https://en.wikipedia.org/wiki/Syslog) fields do not clash with the existing fields,
then specify common prefix for all the fields extracted from syslog, by adding `result_prefix "prefix_name"` to `unpack_syslog`.
For example, the following query adds `foo_` prefix for all the unpacked fields from `foo` field:

```logsql
_time:5m | unpack_syslog from foo result_prefix "foo_"
```

Performance tips:

- It is better from performance and resource usage PoV ingesting parsed [syslog](https://en.wikipedia.org/wiki/Syslog) messages into VictoriaLogs
  according to the [supported data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of ingesting unparsed syslog lines into VictoriaLogs and then parsing them at query time with [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe).

- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `unpack_syslog`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional unpack_syslog](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-unpack_syslog)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
- [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Conditional unpack_syslog

If the [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unpack_syslog`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unpacks syslog message fields from `foo` field
only if `hostname` field in the current log entry isn't set or empty:

```logsql
_time:5m | unpack_syslog if (hostname:"") from foo
```

### unpack_words pipe

The `<q> | unpack_words from <src_field> as <dst_field>` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) from the given
`<src_field>` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `<dst_field>` as a JSON array.

For example, the following query unpacks words from [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) into `words` field:

```logsql
_time:5m | unpack_words from _msg as words
```

The `as <dst_field>` part is optional. If it is missing, then the result is stored in the `<src_field>` specified in `from <src_field>`.
For example, the following query stores the unpacked words into `_msg` field:

```logsql
_time:5m | unpack_words from _msg
```

The `from <src_field>` part is optional. If it is missing, then words are unpacked from the `_msg` field. The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_words
```

By default `unpack_words` pipe unpacks all the words, including duplicates, from the `<src_field>`. It is possible to drop duplicate words by adding `drop_duplicates` suffix to the pipe.
For example, the following query extracts only unique words from every `text` field:

```logsql
_time:5m | unpack_words from text as words drop_duplicates
```

It is convenient to use [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) for unrolling the JSON array with unpacked words from the destination field.
For example, the following query returns top 5 most frequently seen words across [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) for the last 5 minutes:

```logsql
_time:5m | unpack_words as words | unroll words | top 5 (words)
```

See also:

- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`split` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#split-pipe)

### unroll pipe

`<q> | unroll by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used for unrolling JSON arrays from `field1`, ..., `fieldN`
[log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into separate rows.

For example, the following query unrolls `timestamp` and `value` [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) from logs for the last 5 minutes:

```logsql
_time:5m | unroll (timestamp, value)
```

If the unrolled JSON array contains JSON objects, then it may be handy to use [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) for unpacking
the unrolled array items into separate fields for further processing.

See also:

- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
- [`unpack_words` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`uniq_values` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`values` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#values-stats)

#### Conditional unroll

If the [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unroll`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unrolls the `value` field only if the `value_type` field equals `json_array`:

```logsql
_time:5m | unroll if (value_type:="json_array") (value)
```

