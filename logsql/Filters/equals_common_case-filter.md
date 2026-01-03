### Фильтр equals_common_case

Фильтр `field_name:equals_common_case(phrase1, ..., phraseN)` ищет логи, в которых [поле лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `field_name`
равно следующим [фразам](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) и [словам](https://docs.victoriametrics.com/victorialogs/logsql/#word):

* заданным фразам — `phrase1`, …, `phraseN`
* фразам в верхнем и нижнем регистре
* отдельным фразам, в которых каждая заглавная буква независимо заменена на соответствующую строчную

Например, `_msg:equals_common_case("VictoriaMetrics")` находит логи, в которых
[поле `_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
равно одному из следующих [слов](https://docs.victoriametrics.com/victorialogs/logsql/#word):

* VictoriaMetrics
* VICTORIAMETRICS
* victoriametrics
* Victoriametrics
* victoriaMetrics

Фильтр `equals_common_case(...)` обычно работает значительно быстрее, чем
[регистронезависимый фильтр `i(...)`](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).

Если вам нужно найти логи, в которых поля лога **содержат** слова или фразы с «обычным регистром»,
используйте фильтр [`contains_common_case`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter).
