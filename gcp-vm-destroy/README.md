# Self-Destroying VM in GCP

This example shows how to create virtual machines (VM) in Google cloud and delete after a certain time. This can be used for build processes or creating test instances. This example requires a [service account JSON](https://cloud.google.com/iam/docs/keys-create-delete) key in Google Cloud.

It consist of three workflows. The create flow is responsible for creating the virtual machine. This example uses a Google Cloud VM but conceptually it works with every cloud provider. This flow returns all the important information about the created machine. At the end it starts a subflow which waits for an event to delete the virtual machine. If that event does not arrive and times out, the delete process starts even in the absence of that event. 

This flow has a validate state at the beginning and a transform to set defaults for the virtual machine creation.

[Create VM Flow](create.yaml)

The `timeout` defines how long that flow waits before it starts to delete the virtual machine. 

[Delete Flow](deleter.yaml)

The virtual machine can be deleted by sending an event. This can come from outside via an API call or within a flow with the `generateEvent` state.

[Trigger Event Example](send-delete.yaml)