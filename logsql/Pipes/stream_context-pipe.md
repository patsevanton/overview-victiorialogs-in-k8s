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

