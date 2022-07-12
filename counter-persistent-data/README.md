<!-- ORDER=1 -->
# Counter Example

A simple example that shows how to store a counter as a workflow variable for persistent data. Any state data can be set to a variable to be used in later instances.

## Workflow YAML

```yaml
states:
  #
  # Get workflow counter variable and increment value
  #
  - id: counter-get
    type: getter 
    transition: counter-set
    variables:
    - key: ExampleVariableCounter
      scope: workflow
    transform: 'jq(. += {"newCounter": (.var.ExampleVariableCounter + 1)})'

  #
  # Set workflow counter variable
  #
  - id: counter-set
    type: setter
    variables:
      - key: ExampleVariableCounter
        scope: workflow 
        value: 'jq(.newCounter)'
```

## Output
```json
{
  "newCounter": 1,
  "var": {
    "counter": 0
  }
}
```