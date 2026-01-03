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

