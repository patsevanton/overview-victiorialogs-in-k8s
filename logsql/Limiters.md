## Ограничители (Limiters)

LogsQL предоставляет следующие **конвейеры** (*pipes*), позволяющие ограничивать объём возвращаемых записей журнала:

- Конвейеры [`fields`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) и [`delete`](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe) позволяют ограничить набор **полей журнала** (*log fields*), которые будут возвращены в результате запроса.  
  *(Пояснение: поля журнала — это отдельные атрибуты каждой записи, например `timestamp`, `level`, `message`, `service_name` и т. д.)*

- Конвейер [`limit`](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe) позволяет ограничить **количество** возвращаемых записей журнала.
