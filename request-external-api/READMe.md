<!-- ORDER=1 -->
# Greeting Example

This example shows how we can write a workflow to communicate with a external API service. In this workflow we will use the direktiv/request image to make a HTTP GET request to https://fakerapi.it/ and fetch the details of a fake person. A transform is also used to clean up the returned value from the action, but it can be commented out to see the full return value.

## Workflow YAML

```yaml
functions:
- id: get
  image: direktiv/request:v4
  type: knative-workflow

states:
  #
  # HTTP GET Fake person from fakerapi
  # Transform data to get data out of body
  #
  - id: get-fake-persons
    transform: "jq({person: .return.body.data[0]})" # This line can commented out to see complete action return
    type: action
    action:
      function: get
      input: 
        method: "GET"
        url: "https://fakerapi.it/api/v1/persons?_quantity=1"
```

## Output

The results of this action will contain a details of a fake person.

```json
{
  "person": {
    "address": {
      "buildingNumber": "8422",
      "city": "Ashleytown",
      "country": "Ethiopia",
      "county_code": "AD",
      "id": 0,
      "latitude": -21.509297,
      "longitude": -48.162169,
      "street": "47933 Kennedi View Apt. 395",
      "streetName": "Margie Stream",
      "zipcode": "44788"
    },
    "birthday": "1944-09-28",
    "email": "qmetz@gmail.com",
    "firstname": "Gabriella",
    "gender": "female",
    "id": 1,
    "image": "http://placeimg.com/640/480/people",
    "lastname": "Steuber",
    "phone": "+5542223225627",
    "website": "http://wiza.com"
  }
}
```

