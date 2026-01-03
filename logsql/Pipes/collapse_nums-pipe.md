## Конвейер `collapse_nums`

Конвейер `<q> | collapse_nums at <field>` заменяет все десятичные и шестнадцатеричные числа в указанном поле [`<field>`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), возвращаемом запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), на заполнитель `<N>`.

**Пример:** если поле `_msg` содержит строку `2024-10-20T12:34:56Z request duration 1.34s`, то после выполнения следующего запроса:

```logsql
_time:5m | collapse_nums at _msg
```

она будет преобразована в `<N>-<N>-<N>T<N>:<N>:<N>Z request duration <N>.<N>s`.

Суффикс `at ...` можно опустить, если `collapse_nums` применяется к полю [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field). Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | collapse_nums
```

Эта функциональность полезна для поиска наиболее часто встречающихся шаблонов логов среди сообщений с различными числовыми значениями. К таким сущностям относятся:
- временные метки (timestamps),
- IP‑адреса,
- длительность запросов (request durations),
- размеры ответов (response sizes),
- [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier),
- идентификаторы трассировки (trace IDs),
- идентификаторы пользователей (user IDs) и т. д.

После применения конвейера `collapse_nums` сообщения с такими сущностями становятся идентичными, что позволяет использовать конвейер [`top`](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe) для выявления самых частых шаблонов. Например, следующий запрос возвращает **5 самых частых шаблонов** логов за последний час:

```logsql
_time:1h | collapse_nums | top 5 by (_msg)
```

### Улучшенное форматирование с `prettify`

Если к конвейеру `collapse_nums` добавить суффикс `prettify`, он сможет распознавать определённые шаблоны в сжатых числах и заменять их соответствующими заполнителями:

- `<N>-<N>-<N>-<N>-<N>` → `<UUID>`
- `<N>.<N>.<N>.<N>` → `<IP4>`
- `<N>:<N>:<N>` → `<TIME>` (дробные секунды опционально включаются в `<TIME>`)
- `<N>-<N>-<N>` и `<N>/<N>/<N>` → `<DATE>`
- `<N>-<N>-<N>T<N>:<N>:<N>` и `<N>-<N>-<N> <N>:<N>:<N>` → `<DATETIME>` (часовой пояс опционально включается в `<DATETIME>`)

**Пример:** сообщение лога  
`2edfed59-3e98-4073-bbb2-28d321ca71a7 - [2024/12/08 15:21:02] 10.71.20.32 GET /foo 200`  
после выполнения запроса

```logsql
_time:1h | collapse_nums prettify
```

преобразуется в `<UUID> - [<DATETIME>] <IP4> GET /foo <N>`.

Шаблоны, полученные с помощью `collapse_nums prettify`, можно использовать в [фильтре по шаблону](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter).

### Условный `collapse_nums`

Если конвейер `collapse_nums` нужно применить лишь к части записей лога, добавьте условие `if (<filters>)` после `collapse_nums`. В `<filters>` могут быть любые [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters).

**Пример:** следующий запрос сжимает числа в поле `foo` только для записей, где поле `user_type` равно `admin`:

```logsql
_time:5m | collapse_nums if (user_type:=admin) at foo
```

**Примечание:** `collapse_nums` может пропустить некоторые числа или сжать неожиданные значения. В таких случаях рекомендуется использовать **условный `collapse_nums`** либо предварительно обработать данные с помощью конвейера [`replace_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe).
