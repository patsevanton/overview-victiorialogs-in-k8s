### Статистика `values`

Функция конвейера статистики [`values(field1, ..., fieldN)`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) возвращает все значения (включая пустые значения)
для указанных [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Возвращаемые значения кодируются в виде JSON-массива.

Например, следующий запрос возвращает все значения поля [`ip`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
по логам за последние 5 минут:

```logsql
_time:5m | stats values(ip) ips
```

Возвращённые IP-адреса можно развернуть в отдельные записи логов с помощью
[конвейера `unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

Также можно получить значения для всех полей с общим префиксом, используя синтаксис `values(prefix*)`.
