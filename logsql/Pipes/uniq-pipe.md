## Пайп uniq

Возвращает уникальные значения для указанных полей. Поддерживает `with hits` для подсчёта совпадений, `limit` для ограничения памяти. Ключевое слово `by` можно опустить.

**Примеры:**

```logsql
_time:5m | uniq by (ip)
_time:5m | uniq by (host, path)
_time:5m | uniq by (host) with hits
_time:5m | uniq by (host, path) limit 100
_time:5m | uniq (host, path) limit 100
```
