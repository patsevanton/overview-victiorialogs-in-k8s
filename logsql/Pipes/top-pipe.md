### Конвейер `top` (`top pipe`)

Конвейер  
```
<q> | top N by (field1, ..., fieldN)
```  
(см. [документацию по конвейерам](https://docs.victoriametrics.com/victorialogs/logsql/#pipes)) возвращает **топ‑`N`** наборов значений по полям `(field1, ..., fieldN)` (см. [поля логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)), которые встречаются в логах чаще всего — среди записей, отобранных запросом `<q>` (см. [синтаксис запросов](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)).

**Пример:** следующий запрос возвращает **топ‑7** [потоков логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) с наибольшим числом записей за последние 5 минут. Количество записей возвращается в поле `hits`:

```logsql
_time:5m | top 7 by (_stream)
```

Параметр `N` **необязателен**. Если он опущен, возвращается топ‑10 записей. Например, следующий запрос выдаёт топ‑10 значений поля `ip` (см. [модель данных](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)), встретившихся в логах за последние 5 минут:

```logsql
_time:5m | top by (ip)
```

Можно задать **другое имя для поля `hits`** с помощью синтаксиса `hits as <новое_имя>`. Например, следующий запрос возвращает топ‑значения по полю `path`, а количество записей — в поле `visits`:

```logsql
_time:5m | top by (path) hits as visits
```

Можно добавить **поле `rank`** для каждой возвращаемой записи — для этого достаточно указать `rank`. Например, следующий запрос добавляет поле `rank` для каждого IP‑адреса:

```logsql
_time:5m | top 10 by (ip) rank
```

Поле `rank` может иметь **другое имя**. Например, в следующем запросе вместо `rank` в выводе используется имя `position`:

```logsql
_time:5m | top 10 by (ip) rank as position
```
