# V1HTTPGetAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to access on the HTTP server. | [optional] 
**port** | **str** | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 
**host** | **str** | Host name to connect to, defaults to the pod IP. You probably want to set \&quot;Host\&quot; in httpHeaders instead. | [optional] 
**scheme** | **str** | Scheme to use for connecting to the host. Defaults to HTTP. | [optional] 
**http_headers** | [**list[V1HTTPHeader]**](V1HTTPHeader.md) | Custom headers to set in the request. HTTP allows repeated headers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


