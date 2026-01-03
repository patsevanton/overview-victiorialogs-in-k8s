### Фильтр `_stream_id`

Каждый [поток логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) в VictoriaLogs однозначно идентифицируется полем `_stream_id`.

Фильтр `_stream_id:...` позволяет быстро выбрать все логи, принадлежащие конкретному потоку.

Например, следующий запрос выбирает все логи, которые относятся к [потоку логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) с `_stream_id`, равным `0000007b000001c850d9950ea6196b1a4812081265faa1c7`:

```logsql
_stream_id:0000007b000001c850d9950ea6196b1a4812081265faa1c7
```

Если поток логов содержит слишком много записей, рекомендуется ограничить количество возвращаемых логов с помощью [фильтра по времени](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter). Например, следующий запрос выбирает логи для заданного потока за последний час:

```logsql
_time:1h _stream_id:0000007b000001c850d9950ea6196b1a4812081265faa1c7
```

Фильтр `_stream_id` поддерживает указание нескольких значений `_stream_id` с помощью синтаксиса `_stream_id:in(...)`. Например:

```logsql
_stream_id:in(0000007b000001c850d9950ea6196b1a4812081265faa1c7, 1230007b456701c850d9950ea6196b1a4812081265fff2a9)
```

Также внутри `in(...)` можно указать подзапрос, который выберет нужные значения `_stream_id`. Например, следующий запрос возвращает логи для [потоков логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields), содержащих слово `error` в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) за последние 5 минут:

```logsql
_stream_id:in(_time:5m error | fields _stream_id)
```
