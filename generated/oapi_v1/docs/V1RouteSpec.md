# V1RouteSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host is an alias/DNS that points to the service. Optional Must follow DNS952 subdomain conventions. | 
**path** | **str** | Path that the router watches for, to route traffic for to the service. Optional | [optional] 
**to** | [**V1ObjectReference**](V1ObjectReference.md) | To is an object the route points to. Only the Service kind is allowed, and it will be defaulted to Service. | 
**port** | [**V1RoutePort**](V1RoutePort.md) | If specified, the port to be used by the router. Most routers will use all endpoints exposed by the service by default - set this value to instruct routers which port to use. | [optional] 
**tls** | [**V1TLSConfig**](V1TLSConfig.md) | TLS provides the ability to configure certificates and termination for the route | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


