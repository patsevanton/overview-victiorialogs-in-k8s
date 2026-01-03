### Труба `decolorize`

Конструкция `<q> | decolorize <field>` [труба (pipe)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) удаляет [ANSI‑коды цветов](https://en.wikipedia.org/wiki/ANSI_escape_code) из указанного поля [`<field>`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) во всех логах, возвращённых запросом [`<q>`](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

Поле `<field>` можно опустить, если требуется удалить ANSI‑коды цветов из поля [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).

Например, следующий запрос удаляет ANSI‑коды цветов из всех полей `_msg` в логах за последние 5 минут:

```logsql
_time:5m | decolorize
```

Этот запрос эквивалентен такому:

```logsql
_time:5m | decolorize _msg
```

Рекомендуется удалять ANSI‑коды цветов на этапе приёма данных — см. [соответствующую документацию](https://docs.victoriametrics.com/victorialogs/data-ingestion/#decolorizing). Это упростит последующие запросы к логам: не придётся добавлять к ним трубу `| decolorize`.
