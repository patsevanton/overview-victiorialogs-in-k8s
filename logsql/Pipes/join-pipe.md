## Труба join (соединение)

Соединяет результаты первого запроса с результатами второго по заданному набору полей. Работает как `LEFT JOIN` в SQL. Поддерживает `inner` для `INNER JOIN`, `prefix` для добавления префикса к полям.

**Примеры:**

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits | join by (user) (_time:1d {app="app2"} | stats by (user) count() app2_hits)
_time:1d {app="app1"} | stats by (user) count() app1_hits | join by (user) (_time:1d {app="app2"} | stats by (user) count() app2_hits) inner
_time:1d {app="app1"} | stats by (user) count() app1_hits | join by (user) (_time:1d {app="app2"} | stats by (user) count() app2_hits) prefix "app2."
```
