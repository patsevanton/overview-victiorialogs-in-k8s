## Фильтр сопоставления с шаблоном

Фильтрует логи по шаблонам с плейсхолдерами: `<N>` (число), `<UUID>`, `<IP4>`, `<TIME>`, `<DATE>`, `<DATETIME>`, `<W>` (слово). По умолчанию применяется к полю `_msg`.

**Примеры:**

```logsql
pattern_match("user_id=<N>, ip=<IP4>, time=<DATETIME>")
pattern_match_full("шаблон")
поле_лога:pattern_match("шаблон")
```
