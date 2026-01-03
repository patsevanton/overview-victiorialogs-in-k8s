### Фильтр по подстроке

Если требуется найти логи, содержащие определённую подстроку, можно использовать фильтр `*подстрока*`. При необходимости подстроку можно заключить в кавычки — см. [документацию](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).

Например, следующий запрос отбирает записи логов, в которых в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) встречается текст `ampl`:

```logsql
*ampl*
```

Этот фильтр подойдёт для таких сообщений:

- `Example message`
- `This is a sample`

Но он **не подойдёт** для `EXAMPLE message`, поскольку подстрока `AMPL` здесь записана заглавными буквами. В таком случае используйте фильтр [`~"(?i)ampl"`](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) — он учитывает регистр нечувствительно. Обратите внимание, что фильтр без учёта регистра может работать значительно медленнее, чем чувствительный к регистру.

**Совет по производительности:** отдавайте предпочтение [фильтру по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) и [фильтру по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter), поскольку фильтр по подстроке может работать довольно медленно.
