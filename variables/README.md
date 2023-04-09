# Variable Scopes

Variable can be set on different scopes. Later in the flow they can be accessed within the same scope. The following scopes are available.

- instance: Only valid during the execution of the flow
- workflow: Stored as workflow variable and can be accessed from every intsance of the flow
- namespace: Namespace global scope and every workflow in the namespace can access it

This example uses a setter state to set a variable in the `instance` scope. The second state set a workflow variable with the special output folder `out` in actions. Values can be stored in `out/<SCOPE>` and will be set after executing the action. The last state uses a `transform` to return the variables.

[Set Variables](workflow-scope.yaml)