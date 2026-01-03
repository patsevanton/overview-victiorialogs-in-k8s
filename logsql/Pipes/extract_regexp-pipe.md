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

