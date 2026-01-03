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

