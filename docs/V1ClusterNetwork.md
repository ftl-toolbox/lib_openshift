# V1ClusterNetwork

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**network** | **str** | Network is a CIDR string to specify the global overlay network&#39;s L3 space | 
**hostsubnetlength** | **int** | HostSubnetLength is the number of bits to allocate to each host&#39;s subnet e.g. 8 would mean a /24 network on the host | 
**service_network** | **str** | ServiceNetwork is the CIDR string to specify the service network | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

