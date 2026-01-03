## LogsQL tutorial

If you aren't familiar with VictoriaLogs, then start with [key concepts docs](https://docs.victoriametrics.com/victorialogs/keyconcepts/).

Then follow these docs:

- [How to run VictoriaLogs](https://docs.victoriametrics.com/victorialogs/quickstart/).
- [how to ingest data into VictoriaLogs](https://docs.victoriametrics.com/victorialogs/data-ingestion/).
- [How to query VictoriaLogs](https://docs.victoriametrics.com/victorialogs/querying/).

The simplest LogsQL query is just a [word](https://docs.victoriametrics.com/victorialogs/logsql/#word), which must be found in the [log message](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
For example, the following query finds all the logs with `error` word:

```logsql
error
```

It is recommended to use [vlogscli](https://docs.victoriametrics.com/victorialogs/querying/vlogscli/) for querying VictoriaLogs.

If the queried [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) clashes with LogsQL keywords, then just wrap it into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query finds all the log messages with `and` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word):

```logsql
"and"
```

It is OK to wrap any word into quotes. For example:

```logsql
"error"
```

Moreover, it is possible to wrap phrases containing multiple words in quotes. For example, the following query
finds log messages with the `error: cannot find file` phrase:

```logsql
"error: cannot find file"
```

Queries above match logs with any [timestamp](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field),
e.g. they may return logs from the previous year alongside recently ingested logs.

Usually logs from the previous year aren't as interesting as the recently ingested logs.
So it is recommended to add a [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) to the query.
For example, the following query returns logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word),
which were ingested into VictoriaLogs during the last 5 minutes:

```logsql
error AND _time:5m
```

This query consists of two [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) joined with `AND` [operator](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter):

- The filter on the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word).
- The filter on the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).

The `AND` operator means that the [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) must match both filters in order to be selected.

Typical LogsQL query consists of multiple [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) joined with `AND` operator. It may be tiresome typing and then reading all these `AND` words.
So LogsQL allows omitting `AND` words. For example, the following query is equivalent to the query above:

```logsql
_time:5m error
```

The query returns logs in arbitrary order because sorting a large number of logs may require non-trivial amounts of CPU and RAM.
The number of logs with the `error` word over the last 5 minutes isn't usually too big (e.g., less than a few million), so it is OK to sort them with the [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).
The following query sorts the selected logs by [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) field:

```logsql
_time:5m error | sort by (_time)
```

It is unlikely you are going to investigate more than a few hundred logs returned by the query above. So you can limit the number of returned logs
with [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe). The following query returns the last 10 logs with the `error` word over the last 5 minutes:

```logsql
_time:5m error | sort by (_time) desc | limit 10
```

By default VictoriaLogs returns all the [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
If you need only the given set of fields, then add [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) to the end of the query. For example, the following query returns only
[`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field), [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
and [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) fields:

```logsql
error _time:5m | fields _time, _stream, _msg
```

Suppose the query above selects too many rows because some buggy app pushes invalid error logs to VictoriaLogs. Suppose the app adds `buggy_app` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) to every log line.
Then the following query removes all the logs from the buggy app, allowing us paying attention to the real errors:

```logsql
_time:5m error NOT buggy_app
```

This query uses `NOT` [operator](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for removing log lines from the buggy app. The `NOT` operator is used frequently, so it can be substituted with `-` or `!` char
(the `!` must be used instead of `-` in front of [`=`](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
and [`~`](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) filters like `!=` and `!~`).
The following query is equivalent to the previous one:

```logsql
_time:5m error -buggy_app
```

Suppose another buggy app starts pushing invalid error logs to VictoriaLogs - it adds `foobar` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) to every emitted log line.
No problems - just add `-foobar` to the query in order to remove these buggy logs:

```logsql
_time:5m error -buggy_app -foobar
```

This query can be rewritten to more clear query with the `OR` [operator](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) inside parentheses:

```logsql
_time:5m error -(buggy_app OR foobar)
```

The parentheses are **required** here, since otherwise the query won't return the expected results.
The query `error -buggy_app OR foobar` is interpreted as `(error AND NOT buggy_app) OR foobar` according to [priorities for AND, OR and NOT operator](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
This query returns logs with `foobar` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word), even if they do not contain `error` word or contain `buggy_app` word.
So it is recommended wrapping the needed query parts into explicit parentheses if you are unsure in priority rules.
As an additional bonus, explicit parentheses make queries easier to read and maintain.

Queries above assume that the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) is stored in the [log message](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
If this word is stored in other [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) such as `log.level`, then add `log.level:` prefix
in front of the `error` word:

```logsql
_time:5m log.level:error -(buggy_app OR foobar)
```

The field name can be wrapped into quotes if it contains special chars or keywords, which may clash with LogsQL syntax.
Any [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) also can be wrapped into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals). So the following query is equivalent to the previous one:

```logsql
"_time":"5m" "log.level":"error" -("buggy_app" OR "foobar")
```

What if the application identifier - such as `buggy_app` and `foobar` - is stored in the `app` field? Correct - just add `app:` prefix in front of `buggy_app` and `foobar`:

```logsql
_time:5m log.level:error -(app:buggy_app OR app:foobar)
```

The query can be simplified by moving the `app:` prefix outside the parentheses:

```logsql
_time:5m log.level:error -app:(buggy_app OR foobar)
```

The `app` field uniquely identifies the application instance if a single instance runs for each unique `app`.
In this case it is recommended associating the `app` field with [log stream fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
during [data ingestion](https://docs.victoriametrics.com/victorialogs/data-ingestion/). This usually improves both compression rate
and query performance when querying the needed streams via [`_stream` filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter).
If the `app` field is associated with the log stream, then the query above can be rewritten to more performant one:

```logsql
_time:5m log.level:error {app!~"buggy_app|foobar"}
```

This query skips scanning for [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) from `buggy_app` and `foobar` apps.
It inspects only `log.level` and [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) labels.
This significantly reduces disk read IO and CPU time needed for performing the query.

LogsQL also provides [functions for statistics calculation](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) over the selected logs. For example, the following query returns the number of logs
with the `error` word for the last 5 minutes:

```logsql
_time:5m error | stats count() logs_with_error
```

Finally, it is recommended reading [performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

Now you are familiar with LogsQL basics. See [LogsQL examples](https://docs.victoriametrics.com/victorialogs/logsql-examples/) and [query syntax](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)
if you want to continue learning LogsQL.

### Key concepts

#### Word

LogsQL splits all the [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) into words
delimited by non-word chars such as whitespace, parens, punctuation chars, etc. For example, the `foo: (bar,"тест")!` string
is split into `foo`, `bar` and `тест` words. Words can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8) chars.
These words are taken into account by full-text search filters such as
[word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter), [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) and [prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter).

#### Query syntax

LogsQL query must contain at least a single [filter](https://docs.victoriametrics.com/victorialogs/logsql/#filters) for selecting the matching logs.
For example, the following query selects all the logs for the last 5 minutes by using [`_time` filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter):

```logsql
_time:5m
```

Tip: try [`*` filter](https://docs.victoriametrics.com/victorialogs/logsql/#any-value-filter), which selects all the logs stored in VictoriaLogs.
Do not worry - this doesn't crash VictoriaLogs, even if the query selects trillions of logs. See [these docs](https://docs.victoriametrics.com/victorialogs/querying/#command-line)
if you are curious why.

Additionally to filters, LogsQL query may contain arbitrary mix of optional actions for processing the selected logs. These actions are delimited by `|` and are known as [`pipes`](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).
For example, the following query uses [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) for returning the number of [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) for the last 5 minutes:

```logsql
_time:5m error | stats count() errors
```

See [the list of supported pipes in LogsQL](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).

