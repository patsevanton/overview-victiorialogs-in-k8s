### Subquery filter

Sometimes it is needed to select logs with [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) matching values
selected by another [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) (aka subquery). LogsQL provides such an ability with the following filters:

- `field:in(<subquery>)` - it returns logs with `field` values matching the values returned by the `<subquery>`.
  For example, the following query selects all the logs for the last 5 minutes for users,
  who visited pages with `admin` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in the `path` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  during the last day:

  ```logsql
  _time:5m AND user_id:in(_time:1d AND path:admin | fields user_id)
  ```

- `field:contains_all(<subquery>)` - it returns logs with `field` values containing all the [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) and phrases returned by the `<subquery>`.
  For example, the following query selects all the logs for the last 5 minutes, which contain all the `user_id` values from admin logs over the last day
  in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

  ```logsql
  _time:5m _msg:contains_all(_time:1d is_admin:true | fields user_id)
  ```

- `field:contains_any(<subquery>)` - it returns logs with the `field` values containing at least one [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) or phrase returned by the `<subquery>`.
  For example, the following query selects all the logs for the last 5 minutes, which contain at least one `user_id` value from admin logs over the last day
  in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

  ```logsql
  _time:5m _msg:contains_any(_time:1d is_admin:true | fields user_id)
  ```

The `<subquery>` must end with either [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) or [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe) containing a single field name,
so VictoriaLogs could use values of this field for matching the given filter.

See also:

- [`in` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)
- [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)
- [`union` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#union-pipe)

