### Конвейер `json_array_len`

Конструкция  
```
<q> | json_array_len(поле) as результирующее_поле
```  
вычисляет длину JSON‑массива в указанном поле (`поле`) для каждой записи журнала, возвращённой запросом `<q>`, и сохраняет результат в поле `результирующее_поле`.

Подробнее о модели данных см. в разделе [«Модель данных»](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), а о синтаксисе запросов — в разделе [«Синтаксис запросов»](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

**Пример.** Следующий запрос возвращает 5 лучших записей журнала (за последние 5 минут), содержащих сообщения с наибольшим числом слов:

```logsql
_time:5m | unpack_words _msg as words | json_array_len(words) as words_count | first 5 (words_count desc)
```

Пояснение:
- `_time:5m` — отбор записей за последние 5 минут;
- `unpack_words _msg as words` — разбиение текста сообщения `_msg` на слова и сохранение результата в поле `words` (см. конвейер [`unpack_words`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe));
- `json_array_len(words) as words_count` — вычисление числа элементов в массиве `words` и сохранение в `words_count`;
- `first 5 (words_count desc)` — отбор первых 5 записей с максимальным значением `words_count` (см. конвейер [`first`](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)).
