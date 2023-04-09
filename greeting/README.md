# Greeting Example

This simple example flow uses a single `action` state to call the `hello-world` action, which 'greets' the user specified in the `"name"` field of the input provided to the flow. The validate state ensures the input is valid.

[Greeter Flow](greeting.yaml)


```json title="Input"
{
    "name": "World"
}
```

The results of this action will contain a greeting addressed to the provided name.

```json title="Output"
{
  "greeting": "Hello World"
}
```

