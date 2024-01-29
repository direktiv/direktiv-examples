# Consumers

The concept of consumers is used in Direktiv's gateway. The following example uses two consumers and an endpoint requiring authentication. 

For auithentication the `key-auth` plugin is used where `key_name` defines the name of the API key. By default all consumers in Direktiv can access an endpoint. 

In this example there ius an additional ACL plugin configured which limits the access by groups. In this case only consumers with `group1` can access the route.

This request would be succesful because it is using the API key of `consumer1`.

```sh
curl --request GET \
  --url http://MYSERVER/ns/examples/consumer \
  --header 'mykey: apikey'
```

The second request would fail because although the user can be authenticated the ACL plugin denies the request because of the group membership.

```sh
curl --request GET \
  --url http://MYSERVER/ns/examples/consumer \
  --header 'mykey: apikey2'
```

[Route with Authentication](route.yaml)

[Consumer 1](consumer1.yaml)

[Consumer 2](consumer2.yaml)
