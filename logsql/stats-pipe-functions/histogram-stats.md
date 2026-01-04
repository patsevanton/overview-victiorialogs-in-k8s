### статистика гистограмм

Функция конвейера статистики `histogram(field)` (см. [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)) возвращает [бакеты гистограммы VictoriaMetrics](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350)
для заданного [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

Например, следующий запрос возвращает бакеты гистограммы для поля `response_size`, сгруппированные по полю `host`, по логам за последние 5 минут:

```logsql
_time:5m | stats by (host) histogram(response_size)
```

Если поле содержит [значение длительности](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values), то `histogram` нормализует его к наносекундам. Например, `1.25ms` будет нормализовано до `1_250_000`.

Если поле содержит [короткое числовое значение](https://docs.victoriametrics.com/victorialogs/logsql/#short-numeric-values), то `histogram` нормализует его к числовому значению без каких-либо суффиксов. Например, `1KiB` будет преобразовано в `1024`.

Бакеты гистограммы возвращаются в виде следующего JSON-массива:

```json
[{"vmrange":"...","hits":...},...,{"vmrange":"...","hits":...}]
```

Каждое значение `vmrange` содержит диапазон значений соответствующего [бакета гистограммы VictoriaMetrics](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350),
а `hits` содержит количество значений, попавших в данный бакет.

Иногда бывает удобно «развернуть» возвращаемые бакеты гистограммы для дальнейшей обработки прямо в запросе. Например, следующий запрос
строит гистограмму по [полю](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `response_size`,
а затем разворачивает её в отдельные строки с полями `vmrange` и `hits` с помощью конвейеров
[`unroll`](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) и
[`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe):

```logsql
_time:5m
  | stats histogram(response_size) as buckets
  | unroll (buckets)
  | unpack_json from buckets
```
