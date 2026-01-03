### Substring filter

If it is needed to find logs with some substring, then `*substring*` filter can be used. The substring can be put in quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals) if needed.
For example, the following query matches log entries, which contain `ampl` text in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
*ampl*
```

It matches the following messages:

- `Example message`
- `This is a sample`

It doesn't match `EXAMPLE message`, since `AMPL` substring here is in uppercase. Use [`~"(?i)ampl"` filter](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) instead. Note that case-insensitive filter
may be much slower than case-sensitive one.

Performance tip: prefer using [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter), since substring filter may be quite slow.

See also:

- [Pattern match filter](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Regexp filter](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter)

