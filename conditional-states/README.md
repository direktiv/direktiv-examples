<!-- ORDER=1 -->
# Conditional State Example

This example demonstrates the use of a switch state to conditional transition to different states based on a jq expression.  To show this, the example below is a workflow that either approves or rejects a loan depending on the inputted credit score and required minimum credit score.

## Workflow YAML

```yaml
states:
  - id: validate-input
    type: validate
    schema:
      type: object
      required:
      - creditScore
      - creditMinRequired
      properties:
        creditMinRequired:
          type: number
          title: Minimum credit score
          description: minimum credit score required for approval 
          default: 500
        creditScore:
          type: number
          description: credit score of user
          title: Credit Score
    transition: check-credit

    #
    # Check if the user's threshold is above minimum credit requirements.
    # If credit score meets requirements transition to approve-loan. Otherwise
    # transition to reject-loan.
    #
  - id: check-credit
    type: switch
    conditions:
    - condition: jq(.creditScore > .creditMinRequired)
      transition: approve-loan
    defaultTransition: reject-loan
  - id: reject-loan
    type: noop
    transform: 'jq({ "msg": "You have been rejected for this loan" })'
  - id: approve-loan
    type: noop
    transform: 'jq({ "msg": "You have been approved for this loan" })'
```

## Input

```json
{
  "creditMinRequired": 500,
  "creditScore": 600
}
```

## Output

```json
{
  "msg": "You have been approved for this loan"
}
```

