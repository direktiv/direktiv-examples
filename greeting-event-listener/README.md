# Event-based Workflow

This example demonstrates a flow that waits for a cloud event with type `greetingcloudevent`. When the event is received, a state will be triggered using the data provided by the event. Because this flow has a start of type event, directly executing this flow is not necessary. 

To trigger the listener flow, a second flow will be created to generate the cloud event. 


The `generate-greeting` flow generates the `greetingcloudevent` that the `eventbased-greeting` flow is waiting for.

[Listener Workflow](greeting-listener.yaml)

```json title="Output"
{
    "return": {
        "greeting": "Welcome to Direktiv, World!"
    }
}
```

[Generator Workflow](greeting-generate.yaml)
