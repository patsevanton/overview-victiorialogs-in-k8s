## Transformations

LogsQL supports the following transformations on the log entries selected with [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters):

- Extracting arbitrary text from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) according to the provided pattern.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) for details.
- Unpacking JSON fields from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model). See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe).
- Unpacking [logfmt](https://brandur.org/logfmt) fields from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model). See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe).
- Unpacking [Syslog](https://en.wikipedia.org/wiki/Syslog) messages from [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model). See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe).
- Creating a new field from existing [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) according to the provided format. See [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe).
- Replacing substrings in the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
  See [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) and [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe) docs.
- Creating a new field according to math calculations over existing [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model). See [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe).

See also [other pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes), which can be applied to the selected logs.

It is also possible to perform various transformations on the [selected log entries](https://docs.victoriametrics.com/victorialogs/logsql/#filters) at client side
with `jq`, `awk`, `cut`, etc. Unix commands according to [these docs](https://docs.victoriametrics.com/victorialogs/querying/#command-line).

