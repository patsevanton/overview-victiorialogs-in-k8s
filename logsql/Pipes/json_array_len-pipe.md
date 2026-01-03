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

