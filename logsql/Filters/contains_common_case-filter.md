### contains_common_case filter

The `field_name:contains_common_case(phrase1, ..., phraseN)` filter searches for logs where the `field_name` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
contains the following [phrases](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) and [words](https://docs.victoriametrics.com/victorialogs/logsql/#word):

- the given phrases - `phrase1`, ..., `phraseN`
- uppercase and lowercase phrases
- individual phrases where every uppercase letter is independently replaced with the corresponding lowercase letter

For example, `_msg:contains_common_case("VictoriaMetrics")` finds logs where the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
contains at least one of the following [words](https://docs.victoriametrics.com/victorialogs/logsql/#word):

- VictoriaMetrics
- VICTORIAMETRICS
- victoriametrics
- Victoriametrics
- victoriaMetrics

The `contains_common_case(...)` usually works much faster than the [`i(...)`](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).

If you need to find logs with log fields equal to the common case words or phrases,
then use [`equals_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#equals_common_case-filter).

See also:

- [case-insensitive filter](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)
- [`equals_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#equals_common_case-filter)

