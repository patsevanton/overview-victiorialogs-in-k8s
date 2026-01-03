## Преобразования

LogsQL поддерживает следующие преобразования для записей журнала, отобранных с помощью [фильтров](https://docs.victoriametrics.com/victorialogs/logsql/#filters):

- **Извлечение произвольного текста** из [полей журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) по заданному шаблону.  
  Подробнее см. в [документации по оператору `extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe).

- **Распаковка полей JSON** из [полей журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).  
  См. [документацию по оператору `unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe).

- **Распаковка полей в формате logfmt** из [полей журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).  
  См. [документацию по оператору `unpack_logfmt`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe).

- **Распаковка сообщений Syslog** из [полей журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).  
  См. [документацию по оператору `unpack_syslog`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe).

- **Создание нового поля** на основе существующих [полей журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) по заданному формату.  
  См. оператор [`format`](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe).

- **Замена подстрок** в указанном [поле журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).  
  См. документацию по операторам [`replace`](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) и [`replace_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe).

- **Создание нового поля** на основе математических вычислений над существующими [полями журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).  
  См. оператор [`math`](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe).

Также см. [другие операторы (pipes)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes), которые можно применять к отобранным записям журнала.

Кроме того, можно выполнять различные преобразования **на стороне клиента** для [отобранных записей журнала](https://docs.victoriametrics.com/victorialogs/logsql/#filters) с помощью утилит командной строки Unix: `jq`, `awk`, `cut` и др.  
Подробнее см. в [разделе о запросах из командной строки](https://docs.victoriametrics.com/victorialogs/querying/#command-line).
