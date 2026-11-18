# Find the length of a month: implementation

## What the example does

calendar.monthrange handles leap years and returns the first weekday plus the number of days. Month numbers are one-based.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  2024,
  2
]
```

Expected result:

```json
29
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
