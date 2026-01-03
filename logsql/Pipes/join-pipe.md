### Труба `join` (соединение)

Конструкция `<q1> | join by (<поля>) (<q2>)` [труба](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) соединяет результаты запроса `<q1>` [запрос](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) с результатами `<q2>` по заданному набору полей (перечисляются через запятую в `<поля>`).

Эта труба работает следующим образом:

1. Выполняется запрос `<q2>` [запрос](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), и его результаты сохраняются.
2. Для каждой входной строки из `<q1>` выполняется поиск совпадающих строк в результатах `<q2>` по указанным полям `<поля>`.
3. Если в результатах `<q2>` нет совпадающих строк, входная строка передаётся на выход без изменений.
4. Если в результатах `<q2>` найдены совпадающие строки, то для каждой такой строки входная строка дополняется новыми полями, присутствующими в совпадающей строке, и результат передаётся на выход.

Эта логика аналогична операции `LEFT JOIN` в SQL. Например, следующий запрос возвращает количество логов на пользователя для двух приложений — `app1` и `app2` (подробнее о фильтре `{...}` см. [фильтры потоков](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)):

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  )
```

Если вам нужны результаты, аналогичные `INNER JOIN` в SQL, добавьте суффикс `inner` после трубы `join`.  
Например, следующий запрос возвращает статистику только для пользователей, которые есть в обоих приложениях `app1` и `app2`:

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  ) inner
```

Можно добавить префикс ко всем именам полей, возвращаемым запросом `<query>`, указав нужный префикс после `<query>`.  
Например, следующий запрос добавляет префикс `app2.` ко всем полям логов из `<query>`:

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  ) prefix "app2."
```

**Советы по производительности**:

- Убедитесь, что запрос `<query>` в трубе `join` возвращает относительно небольшое число результатов, поскольку они хранятся в оперативной памяти (RAM) во время выполнения трубы `join`.
- [Условные `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) обычно выполняются быстрее.  
  Как правило, они требуют меньше оперативной памяти, чем эквивалентная труба `join`.

См. также:

- [фильтр подзапроса](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)
- [труба `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [условные `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters)
- [труба `filter`](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe)
