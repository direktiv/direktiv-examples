# Self-Destroying VM in GCP

This example shows how to create virtual machines (VM) in Google cloud and delete after a certain time. This can be used for build processes or creating test instances. This example requires a [service account JSON](https://cloud.google.com/iam/docs/keys-create-delete) key in Google Cloud.

It consist of three workflows. The 



[Create VM Flow](create.yaml)

[Delete Flow](deleter.yaml)

[Trigger Event Example](send-delete.yaml)