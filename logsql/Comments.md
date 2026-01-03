## Comments

LogsQL query may contain comments at any place. The comment starts with `#` and continues until the end of the current line.
Example query with comments:

```logsql
error                               # find logs with `error` word
  | stats by (_stream) count() logs # then count the number of logs per `_stream` label
  | sort by (logs) desc             # then sort by the found logs in descending order
  | limit 5                         # and show top 5 streams with the biggest number of logs
```

