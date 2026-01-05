### Фильтр equals_common_case

Фильтр `field_name:equals_common_case(phrase1, ..., phraseN)` ищет логи, в которых `поле лога` `field_name`
равно следующим `фразам` и `словам`:

* заданным фразам — `phrase1`, …, `phraseN`
* фразам в верхнем и нижнем регистре
* отдельным фразам, в которых каждая заглавная буква независимо заменена на соответствующую строчную

Например, `_msg:equals_common_case("VictoriaMetrics")` находит логи, в которых
`поле `_msg``
равно одному из следующих `слов`:

* VictoriaMetrics
* VICTORIAMETRICS
* victoriametrics
* Victoriametrics
* victoriaMetrics

Фильтр `equals_common_case(...)` обычно работает значительно быстрее, чем
`регистронезависимый фильтр `i(...)``.

Если вам нужно найти логи, в которых поля лога **содержат** слова или фразы с «обычным регистром»,
используйте фильтр ``contains_common_case``.
