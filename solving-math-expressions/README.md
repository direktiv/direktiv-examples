<!-- ORDER=3 -->

# Solving Math Expressions Example

This example shows how we can iterate over data using the [ForEach](../../specification#foreachstate) state. Which executes an action that solves a math expression. The workflow data input are the expressions you want to solve as a string array.

The example demonstrates the use of an action isolate to solve a number of mathematical expressions using a `foreach` state. For each expression in the input array, the isolate will be run once. 

## Solver Workflow YAML

```yaml
functions:
- id: solve-math-expression
  image: direktiv/solve:v3
  type: knative-workflow

states:
- id: validate-input
  type: validate
  schema:
    type: object
    required:
    - expressions
    properties:
      expressions:
        type: array
        description: expressions to solve
        title: Expressions
        items:
          type: string
  transition: solve

#
# Execute solve action.
#
- id: solve
  type: foreach
  array: 'jq([.expressions[] | { expression: . }])'
  action:
    function: solve-math-expression
    input: 'jq({ x: .expression })'
  transform: 'jq({ solved: .return })'
```

## Input

```json
{
  "expressions": [
    "4+10",
    "15-14",
    "100*3",
    "200/2"
  ]
}
```

## Output

The results of this foreach loop will be a json array of strings that have the solved answers.

```json
{
  "solved": [
    "14",
    "1",
    "300",
    "100"
  ]
}
```

Note: The array for a foreach state must be passed as an array of objects. This is why to iterate over the `expressions` string array, we must pipe it and construct a new array of objects using `[.expressions[] | { expression: . }]`.

### jq: `.expressions`
```json
[
  "4+10",
  "15-14",
  "100*3",
  "200/2"
]
```

### jq: `[.expressions[] | { expression: . }]`
```json
[
  {
    "expression": "4+10"
  },
  {
    "expression": "15-14"
  },
  {
    "expression": "100*3"
  },
  {
    "expression": "200/2"
  }
]

```
