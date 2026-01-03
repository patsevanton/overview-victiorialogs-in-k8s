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

