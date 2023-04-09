# Variable Mime Type Example

All variables have an associated mime type to distinguish the content type of its value. This example will show two examples, and the special behaviour that happens when mimeType is `text/plain` or `application/octet-stream`. 

## Storing a string as a raw plaintext variable.

By default (mimeType=application/json) all variables are treated as JSON values. So this means even if you store a string in a variable, it's value is stored with quotes wrapped around it.

[JSON String Data](variable-string-json.yaml)

```json title="JSON String Variable"
"hello\nworld"
```

If the data is YAML it will be converted to JSON in the variable.

[JSON Data](variable-json.yaml)

```json title="JSON Variable"
[{"key":"value"}]
```

There are certain scenarios where you would not want to store the variable with its quotes. To do this all need to do is simply set the mimeType to `text/plain` or `text/plain; charset=utf-8`. This will store the variable as a raw string without quotes. 

[Plain Text](variable-string-plaintext.yaml)

### Variable - StringVar Value
``` title="Plain Text Variable"
hello
world
```

## Auto-Decoding Base64 string

Another special behaviour is that it's also possible to auto decode a base64 string by setting the `mimeType` to `application/octet-stream`. This is used for binaries like Excel files, images etc.

[Base64 Variable](variable-base64.yaml)


### Variable - MessageVar Value
```json title="Binary Data"
hello from direktiv
```

These are the only two mime types with special behaviour. Any other `mimeType` will be treated internally by the default `JSON` behaviour. The default value for mimeType is `application/json`