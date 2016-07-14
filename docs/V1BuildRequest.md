# V1BuildRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**revision** | [**V1SourceRevision**](V1SourceRevision.md) | Revision is the information from the source for a specific repo snapshot. | [optional] 
**triggered_by_image** | [**V1ObjectReference**](V1ObjectReference.md) | TriggeredByImage is the Image that triggered this build. | [optional] 
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From is the reference to the ImageStreamTag that triggered the build. | [optional] 
**binary** | [**V1BinaryBuildSource**](V1BinaryBuildSource.md) | Binary indicates a request to build from a binary provided to the builder | [optional] 
**last_version** | **int** | LastVersion (optional) is the LastVersion of the BuildConfig that was used to generate the build. If the BuildConfig in the generator doesn&#39;t match, a build will not be generated. | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Env contains additional environment variables you want to pass into a builder container | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


