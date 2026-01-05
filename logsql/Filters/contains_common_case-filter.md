### Фильтр contains_common_case

Фильтр `field_name:contains_common_case(phrase1, ..., phraseN)` ищет логи, в которых `поле лога` `field_name`
содержит следующие `фразы` и `слова`:

* заданные фразы — `phrase1`, …, `phraseN`
* фразы в верхнем и нижнем регистре
* варианты фраз, в которых каждая заглавная буква независимо заменена на соответствующую строчную

Например, `_msg:contains_common_case("VictoriaMetrics")` находит логи, в которых `поле `_msg``
содержит хотя бы одно из следующих `слов`:

* VictoriaMetrics
* VICTORIAMETRICS
* victoriametrics
* Victoriametrics
* victoriaMetrics

Фильтр `contains_common_case(...)` обычно работает значительно быстрее, чем
`регистронезависимый фильтр `i(...)``.

Если вам нужно найти логи, в которых поля лога **равны** словам или фразам с общим регистром,
используйте фильтр ``equals_common_case``.
