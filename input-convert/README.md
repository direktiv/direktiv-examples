# Convert Input

This example show how to handleinput which is not JSON. This example uses a XLSX file and converts it to JSON to be used in the workflow. 

If Direktiv gets non-JSON input, in this case a binary file, it encodes it as Base64 and starts the workflow with a an `input` variable containing the binary file. 


```console
curl -XPOST --data-binary @data.xlsx http://MYSERVER/api/namespaces/direktiv-examples/tree/input-convert/workflow?op=wait
```