# Dependency Schedule

Earliest finish calculation for task dependency networks.

A depth-first traversal memoizes finish times and detects missing dependencies and cycles. Durations are non-negative integers.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
