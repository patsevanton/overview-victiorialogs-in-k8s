### Фильтр contains_common_case

Фильтр `field_name:contains_common_case(phrase1, ..., phraseN)` ищет логи, в которых [поле лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `field_name`
содержит следующие [фразы](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) и [слова](https://docs.victoriametrics.com/victorialogs/logsql/#word):

* заданные фразы — `phrase1`, …, `phraseN`
* фразы в верхнем и нижнем регистре
* варианты фраз, в которых каждая заглавная буква независимо заменена на соответствующую строчную

Например, `_msg:contains_common_case("VictoriaMetrics")` находит логи, в которых [поле `_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
содержит хотя бы одно из следующих [слов](https://docs.victoriametrics.com/victorialogs/logsql/#word):

* VictoriaMetrics
* VICTORIAMETRICS
* victoriametrics
* Victoriametrics
* victoriaMetrics

Фильтр `contains_common_case(...)` обычно работает значительно быстрее, чем
[регистронезависимый фильтр `i(...)`](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).

Если вам нужно найти логи, в которых поля лога **равны** словам или фразам с общим регистром,
используйте фильтр [`equals_common_case`](https://docs.victoriametrics.com/victorialogs/logsql/#equals_common_case-filter).
