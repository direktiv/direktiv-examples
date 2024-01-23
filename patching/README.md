# Patching Functions

Patcing functions is a simple way to use Kubernetes functionality, which is not supported by the default configuration in Direktiv. This can be extra annotations or metadata for the pod or values within the user container.

This example add an annotation and a label to the pod. Additionally it changes the CPU requests for that user function.

[Simple Patch](wf.yaml)

The following example uses annotations to enable container image builds on Direktiv. The annotation`/spec/template/metadata/annotations/container.apparmor.security.beta.kubernetes.io~1direktiv-container` change sthe apparmor settings for the container and an additional environment variable changes the filesystem for `buildah`. 

This function uses the helper command `/usr/share/direktiv/direktiv-cmd` which enables Direktiv to use standrad containers from registries. In this case it is the official `buildah` container. 

[Patch for Build](wf-build.yaml)
