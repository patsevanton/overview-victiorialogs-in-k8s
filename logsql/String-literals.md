## String literals

LogsQL supports the following string literals:

- `"double quoted"`. Double quote and backslash inside such a string must be escaped with `\`: `"escape\"doublequote and \\ backslash"`.
  Double-quoted strings may contain special sequences such as `\n`, `\t`, `\f`, `\x8c`, etc. They are decoded according to [these docs](https://go.dev/ref/spec#String_literals).
- `'single quoted'`. Single quote and backslash inside such a string must be escaped with `\`: `'escape\'singlequote and \\ backslash'`.
- ``` `backtick quoted` ```. Strings with backslashes, double quotes and single quotes shouldn't be escaped inside backtick-quoted strings.

