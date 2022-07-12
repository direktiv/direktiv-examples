<!-- ORDER=2 -->

# Event-based Greeting Example

This example demonstrates a workflow that waits for a cloud event with type `greetingcloudevent`. When the event is received, a state will be triggered using the data provided by the event. Because this workflow has a start of type event, directly executing this workflow is not necessary. 

To trigger the listener workflow,  a second workflow will be created to generate the cloud event. 


The `generate-greeting` workflow generates the `greetingcloudevent` that the `eventbased-greeting` workflow is waiting for.

## Event Listener Workflow YAML 

```yaml
start:
  type: event
  state: greeter
  event:
    type: greetingcloudevent

functions:
- id: greeter
  image: direktiv/greeting:v4
  type: knative-workflow
  
states:
- id: greeter
  type: action
  action: 
    function: greeter
    input: jq(.greetingcloudevent)
  transform: 'jq({ "greeting": .return.greeting })'
```

##  Event Listener Workflow Input
### This is a cloud event generated from GenerateGreeting
```json
{
  "greetingcloudevent": {
    "data": {
      "name": "Trent"
    },
    "datacontenttype": "application/json",
    "id": "2638e2d6-754e-409f-9038-f725e0d9d0af",
    "source": "Direktiv",
    "specversion": "1.0",
    "type": "greetingcloudevent"
  }
}
```

##  Event Listener Workflow Output
```json
{
    "return": {
        "greeting": "Welcome to Direktiv, Trent!"
    }
}
```

## GenerateGreeting Workflow YAML
```yaml
id: generate-greeting
description: "Generate greeting event" 
states:
- id: gen
  type: generateEvent
  event:
    type: greetingcloudevent
    source: Direktiv
    data:
      name: "Trent"
```
