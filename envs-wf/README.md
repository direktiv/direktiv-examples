# Environment Variables

Direktiv allows to add environment variabels when using functions and services. In both cases the syntax is similar. 

```
envs:
- name: MYVAR
  value: my-value
- name: MYOTHERVAR
  value: my-other-value
```

These values will be set when executing the user function. If those values change the service will be redeployed by Direktiv.

The following services is an example how to use environment variabels in namespace services.

[Service With Environment Variables](svc.yaml)

Environment variabels can be used in flow functions as well. This flow is using a namespace service and a flow function with environment variables and adds the return of the functions to the final output of the flow. 

[Function with Environment Variables](wf.yaml)
