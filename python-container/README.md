# Python Container

With Direktiv's special command it is easy to use a standard Python container from Docker Hub. In the following example the flow uses one of those containers and uses the special command `/usr/share/direktiv/direktiv-cmd`
to use it in Direktiv. 

This special command eanbles the user to pass in files as well. Thisd can be done with the standard files in Direktiv's filesystem or on-demand like in this example. The file `script.py` is getting created when the function 
runs and can be executed because the permission is set to `0755`. These scripts can contain flow variables and secrets as well if required. 

[Python Container](wf.yaml)