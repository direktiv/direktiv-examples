# Conditional State

This example demonstrates the use of a switch state to conditional transition to different states based on a jq expression.  To show this, the example below is a flow that either approves or rejects a loan depending on the provided credit score and required minimum credit score.

[Simple Switch Statement](check-credit.yaml)

```json title="Input"
{
  "creditMinRequired": 500,
  "creditScore": 600
}
```

```json title="Output"
{
  "msg": "You have been approved for this loan"
}
```

