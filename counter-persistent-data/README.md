# Counter

A simple example that shows how to store a counter as a flow variable for persistent data. Any state data can be set to a variable to be used in later instances. If the variable does not exist it is empty but is getting created the first time it will be stored.

[Counter Example](counter.yaml)

## Output
```json title="Output"
{
  "newCounter": 1,
  "var": {
    "counter": 0
  }
}
```