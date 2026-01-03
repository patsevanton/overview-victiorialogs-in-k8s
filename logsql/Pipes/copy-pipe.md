### Копирование полей (copy pipe)

Если необходимо скопировать некоторые [поля логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), можно использовать конвейер `| copy src1 as dst1, ..., srcN as dstN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).

Например, следующий запрос копирует поле `host` в поле `server` для логов за последние 5 минут. В результате в выводе будут присутствовать оба поля — `host` и `server`:

```logsql
_time:5m | copy host as server
```

С помощью одного конвейера `| copy …` можно скопировать несколько полей. Например, в следующем запросе:
- поле [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) копируется в `timestamp`;
- поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) — в `message`.

```logsql
_time:5m | copy _time as timestamp, _msg as message
```

Ключевое слово `as` необязательно.

Для удобства вместо `copy` можно использовать ключевое слово `cp`. Например, `_time:5m | cp foo bar` эквивалентно `_time:5m | copy foo as bar`.

Можно копировать несколько полей с одинаковым префиксом в поля с другим префиксом. Например, следующий запрос копирует все поля с префиксом `foo` в поля с префиксом `bar`:

```logsql
_time:5m | copy foo* as bar*
```

Смотрите также:

- конвейер [`rename`](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe);
- конвейер [`fields`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe);
- конвейер [`delete`](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe).
