### unpack_syslog pipe

`<q> | unpack_syslog from field_name` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks [syslog](https://en.wikipedia.org/wiki/Syslog) message
from the given [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results.
It understands the following Syslog formats:

- [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164) aka `<PRI>MMM DD hh:mm:ss HOSTNAME APP-NAME[PROCID]: MESSAGE`
- [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) aka `<PRI>1 TIMESTAMP HOSTNAME APP-NAME PROCID MSGID [STRUCTURED-DATA] MESSAGE`

The following fields are unpacked:

- `level` - obtained from `PRI`.
- `priority` - obtained from `PRI`.
- `facility` - calculated as `PRI / 8`.
- `facility_keyword` - string representation of the `facility` field according to [these docs](https://en.wikipedia.org/wiki/Syslog#Facility).
- `severity` - calculated as `PRI % 8`.
- `format` - either `rfc3164` or `rfc5424` depending on which Syslog format is unpacked.
- `timestamp` - timestamp in [ISO8601 format](https://en.wikipedia.org/wiki/ISO_8601). The `MMM DD hh:mm:ss` timestamp in [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164)
  is automatically converted into [ISO8601 format](https://en.wikipedia.org/wiki/ISO_8601) by assuming that the timestamp belongs to the last 12 months.
- `hostname`
- `app_name`
- `proc_id`
- `msg_id`
- `message`

The `<PRI>` part is optional. If it is missing, then `priority`, `facility` and `severity` fields aren't set.

The `[STRUCTURED-DATA]` is parsed into fields with the `SD-ID.param1`, `SD-ID.param2`, ..., `SD-ID.paramN` names and the corresponding values
according to [the specification](https://datatracker.ietf.org/doc/html/rfc5424#section-6.3).

If the `app_name` equals `CEF` and the `message` contains Common Event Format data for SIEM
aka [CEF for Syslog](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-8.3/cef-implementation-standard/Content/CEF/Chapter%201%20What%20is%20CEF.htm),
then it is automatically parsed into the following fields:

- `cef.version` - the CEF version
- `cef.device_vendor` - the device vendor field
- `cef.device_product` - the device product field
- `cef.device_version` - the device version field
- `cef.device_event_class_id` - the device event class id
- `cef.name` - the CEF name
- `cef.severity` - the severity field

Optional extension fields are parsed into `cef.extension.<key>=<value>` fields.

For example, the following query unpacks [syslog](https://en.wikipedia.org/wiki/Syslog) message from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
across logs for the last 5 minutes:

```logsql
_time:5m | unpack_syslog from _msg
```

The `from _msg` part can be omitted when [syslog](https://en.wikipedia.org/wiki/Syslog) message is unpacked
from the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_syslog
```

By default timestamps in [RFC3164 format](https://datatracker.ietf.org/doc/html/rfc3164) are converted to local timezone. It is possible to change the timezone
offset via `offset` option. For example, the following query adds 5 hours and 30 minutes to unpacked `rfc3164` timestamps:

```logsql
_time:5m | unpack_syslog offset 5h30m
```

If it is needed to preserve the original non-empty field values, then add `keep_original_fields` to the end of `unpack_syslog ...`:

```logsql
_time:5m | unpack_syslog keep_original_fields
```

If you want to make sure that the unpacked [syslog](https://en.wikipedia.org/wiki/Syslog) fields do not clash with the existing fields,
then specify common prefix for all the fields extracted from syslog, by adding `result_prefix "prefix_name"` to `unpack_syslog`.
For example, the following query adds `foo_` prefix for all the unpacked fields from `foo` field:

```logsql
_time:5m | unpack_syslog from foo result_prefix "foo_"
```

Performance tips:

- It is better from performance and resource usage PoV ingesting parsed [syslog](https://en.wikipedia.org/wiki/Syslog) messages into VictoriaLogs
  according to the [supported data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of ingesting unparsed syslog lines into VictoriaLogs and then parsing them at query time with [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe).

- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `unpack_syslog`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional unpack_syslog](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-unpack_syslog)
- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
- [`unpack_logfmt` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Conditional unpack_syslog

If the [`unpack_syslog` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unpack_syslog`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unpacks syslog message fields from `foo` field
only if `hostname` field in the current log entry isn't set or empty:

```logsql
_time:5m | unpack_syslog if (hostname:"") from foo
```

