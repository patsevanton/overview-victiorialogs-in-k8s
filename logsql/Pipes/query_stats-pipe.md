### Конвейер `query_stats`

Конвейер `<q> | query_stats` ([pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes)) возвращает следующую статистику выполнения для заданного [запроса `<q>`](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax):

- `BytesReadColumnsHeaders` — количество байт, прочитанных с диска для заголовков колонок. Для уменьшения объёма читаемых данных используйте конвейер [`fields`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe).
- `BytesReadColumnsHeaderIndexes` — количество байт, прочитанных с диска для индексов заголовков колонок.
- `BytesReadBloomFilters` — количество байт, прочитанных с диска для фильтров Блума.
- `BytesReadValues` — количество байт, прочитанных с диска для [значений полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).  
  Для уменьшения объёма читаемых значений полей используйте конвейер [`fields`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe).
- `BytesReadTimestamps` — количество байт, прочитанных с диска для поля [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).
- `BytesReadBlockHeaders` — количество байт, прочитанных с диска для заголовков блоков.
- `BytesReadTotal` — общий объём байт, прочитанных с диска.
- `BlocksProcessed` — количество обработанных блоков данных во время выполнения запроса.  
  Чтобы уменьшить число обрабатываемых блоков, используйте более узкие [фильтр по времени](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) и [фильтр потока логов](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter).
- `RowsProcessed` — количество записей логов, обработанных во время выполнения запроса.  
  Чтобы уменьшить число обрабатываемых записей, используйте более узкие [фильтр по времени](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) и [фильтр потока логов](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter).
- `RowsFound` — количество записей логов, найденных запросом.
- `ValuesRead` — количество [значений полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), прочитанных в ходе обработки запроса.  
  Для уменьшения числа читаемых значений полей используйте конвейер [`fields`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe).
- `TimestampsRead` — количество полей [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field), прочитанных в ходе обработки запроса.
- `BytesProcessedUncompressedValues` — объём несжатых байт для [значений полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), обработанных во время выполнения запроса.
- `QueryDurationNsecs` — длительность выполнения запроса в наносекундах.  
  Может использоваться для расчёта различных показателей по статистике запроса с помощью конвейера [`math`](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe).

Этот конвейер полезен для анализа и оптимизации медленных запросов.
