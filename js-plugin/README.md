# Javascript Plugin

This example uses the Javascript and Request converter plugin. The first plugin adds a header and the request converter sends the whole request split into an object to the flow.

The flow receiving that request will have an additional header called `Header1`.

[Javascript Route](jsroute.yaml)

[Simple Workflow](wf.yaml)

## Advanced Example

This example uses a path parameter and a bit more complex Javascript. 
