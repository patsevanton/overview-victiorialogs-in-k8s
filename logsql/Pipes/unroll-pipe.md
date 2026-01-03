### Pipe `unroll`

Pipe [`<q> | unroll by (field1, ..., fieldN)`](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) можно использовать для разворачивания JSON-массивов из [полей лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `field1`, …, `fieldN` в результатах [запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) `<q>` в отдельные строки.

Например, следующий запрос разворачивает [поля лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `timestamp` и `value` из логов за последние 5 минут:

```logsql
_time:5m | unroll (timestamp, value)
```

Если разворачиваемый JSON-массив содержит JSON-объекты, то может быть удобно использовать pipe [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) для распаковки элементов массива в отдельные поля для дальнейшей обработки.

См. также:

* pipe [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
* pipe [`unpack_words`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe)
* pipe [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
* статистическая функция [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
* статистическая функция [`values`](https://docs.victoriametrics.com/victorialogs/logsql/#values-stats)

---

### Условный `unroll`

Если pipe [`unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) нужно применять только к некоторым [записям лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), то после `unroll` добавляется `if (<filters>)`.

`<filters>` может содержать произвольные [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters). Например, следующий запрос разворачивает поле `value` только в том случае, если поле `value_type` равно `json_array`:

```logsql
_time:5m | unroll if (value_type:="json_array") (value)
```
