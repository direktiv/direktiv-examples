# Namespace Services

Direktiv can use namespace-wide services. These services have to be configured as individual files. In those files different attriubtes can bet set to change the behaviour of the service, e.g. environment variables. 


The avaiable attributes are available in the [specification](../spec/workflow-yaml/functions.md#namespacedknativefunctiondefinition)

[Service Definition](s1.yaml)

Multiple workflows can use this service in their function definition.

[Workflow](wf.yaml)