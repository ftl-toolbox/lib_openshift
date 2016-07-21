# V1Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata | 
**involved_object** | [**V1ObjectReference**](V1ObjectReference.md) | The object that this event is about. | 
**reason** | **str** | This should be a short, machine understandable string that gives the reason for the transition into the object&#39;s current status. | [optional] 
**message** | **str** | A human-readable description of the status of this operation. | [optional] 
**source** | [**V1EventSource**](V1EventSource.md) | The component reporting this event. Should be a short machine understandable string. | [optional] 
**first_timestamp** | **str** | The time at which the event was first recorded. (Time of server receipt is in TypeMeta.) | [optional] 
**last_timestamp** | **str** | The time at which the most recent occurrence of this event was recorded. | [optional] 
**count** | **int** | The number of times this event has occurred. | [optional] 
**type** | **str** | Type of this event (Normal, Warning), new types could be added in the future | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


