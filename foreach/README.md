# Foreach 

The `foreach` state requires the `array` attribute to loop over. The difference to other states is that the data in the action of the `foreach` function is not getting the state data of the flow but the values provided in the array. 

## Simple Foreach

This is the most basic example. It shows that each action call in the foreach loop has it's own object during execution. In the flow scope there is a variable `.names`. But the `array` definition uses jq to iterate through `.names` and creates a list of JSON objects with the variable `name`. This means that each action only sees an object with the value `name` and has no access to `names`.

[Simple Foreach](printer.yaml)

The output for this flow should be something like the following:

```json title="Output"
{
  "names": [
    "hello",
    "world",
    "goodbye"
  ],
  "return": [
    {
      "name": "hello"
    },
    {
      "name": "world"
    },
    {
      "name": "goodbye"
    }
  ]
}
```

## Foreach with JQ

This examples shows how to use JQ for a more complex foreach scenario. It generates an array based on `.data` in the first state. The JQ command is storing the state data `.otherdata` in the variable `od`. This result will be piped into the actual array generation with `.data[]`. In this case it is more obvious how each `foreach` action gets it's own JSON object. In this case the JQ command sets the `name` to the name in the array, `time` to the actual time with the JQ `time` function. The last attribute `otherdata` passes the original value from the flow state data into the action.

[JQ Foreach](foreach-jq.yaml)

```json title="Output"
{
  "data": [
    {
      "name": "key1",
      "value": "value1"
    },
    {
      "name": "key2",
      "value": "value2"
    },
    {
      "name": "key3",
      "value": "value3"
    }
  ],
  "otherdata": "somedata",
  "return": [
    {
      "name": "key1",
      "otherdata": "somedata",
      "time": 1680972341.2246315
    },
    {
      "name": "key2",
      "otherdata": "somedata",
      "time": 1680972341.224634
    },
    {
      "name": "key3",
      "otherdata": "somedata",
      "time": 1680972341.2246354
    }
  ]
}
```

## Foreach with JS

This example uses Javascript to achieve the same outcome. If data structures are getting too complex it might be better to use Javascript for readability. If Javascript is used Direktiv passes in an object `data` which contains the flow state. Data can be accessed in the usual way like `data["otherdata"]`. In the case of a `foreach` the Javascript function needs to return an array.

[JS Foreach](foreach-js.yaml)