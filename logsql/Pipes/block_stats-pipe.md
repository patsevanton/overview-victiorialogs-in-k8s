### Конвейер `block_stats`

Конвейер `<q> | block_stats` ([конвейеры](https://docs.victoriametrics.com/victorialogs/logsql/#pipes)) возвращает следующую статистику для каждого поля в каждом блоке данных, обработанном запросом `<q>` ([синтаксис запросов](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)):

- `field` — имя [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model);
- `rows` — количество строк для данного поля `field`;
- `type` — внутренний тип хранения для данного поля `field`;
- `values_bytes` — размер данных для данного поля `field` на диске;
- `bloom_bytes` — размер данных фильтра Блума для данного поля `field` на диске;
- `dict_bytes` — размер словарных данных для данного поля `field` на диске;
- `dict_items` — количество уникальных значений в словаре для данного поля `field`;
- `_stream` — [поток логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) для данного поля `field`;
- `part_path` — путь к части данных, где хранятся данные поля.

Конвейер `block_stats` в основном нужен для отладки.  
Например, см.:
- [как определить, какое поле логов занимает больше всего места на диске](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-fields-occupy-the-most-of-disk-space);
- [как определить, какой поток логов занимает больше всего места на диске](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-streams-occupy-the-most-of-disk-space).
