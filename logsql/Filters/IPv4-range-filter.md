### IPv4 range filter

If you need to filter log message by some field containing only [IPv4](https://en.wikipedia.org/wiki/Internet_Protocol_version_4) addresses such as `1.2.3.4`,
then the `ipv4_range()` filter can be used. For example, the following query matches log entries with `user.ip` address in the range `[127.0.0.0 - 127.255.255.255]`:

```logsql
user.ip:ipv4_range(127.0.0.0, 127.255.255.255)
```

The `ipv4_range()` accepts also IPv4 subnetworks in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).
For example, the following query is equivalent to the query above:

```logsql
user.ip:ipv4_range("127.0.0.0/8")
```

If you need matching a single IPv4 address, then just put it inside `ipv4_range()`. For example, the following query matches `1.2.3.4` IP
at `user.ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
user.ip:ipv4_range("1.2.3.4")
```

Note that the `ipv4_range()` doesn't match a string with IPv4 address if this string contains other text. For example, `ipv4_range("127.0.0.0/24")`
doesn't match `request from 127.0.0.1: done` [log message](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
since the `127.0.0.1` ip is surrounded by other text. Extract the IP from the message with [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
and then apply the `ipv4_range()` [filter pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe) to the extracted field.

Hints:

- If you need to search for [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing the given `X.Y.Z.Q` IPv4 address,
  then `"X.Y.Z.Q"` query can be used. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) for details.
- If you need to search for [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing
  at least a single IPv4 address out of the given list, then `"ip1" OR "ip2" ... OR "ipN"` query can be used. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- If you need to find log entries with the `ip` field in multiple ranges, then use `ip:(ipv4_range(range1) OR ipv4_range(range2) ... OR ipv4_range(rangeN))` query.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.

Performance tips:

- It is better querying pure IPv4 [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
  instead of extracting IPv4 from text field via [transformations](https://docs.victoriametrics.com/victorialogs/logsql/#transformations) at query time.
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Range filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter)
- [String range filter](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter)
- [Length range filter](https://docs.victoriametrics.com/victorialogs/logsql/#length-range-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

