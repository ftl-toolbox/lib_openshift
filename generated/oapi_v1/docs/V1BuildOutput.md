# V1BuildOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**V1ObjectReference**](V1ObjectReference.md) | To defines an optional location to push the output of this build to. Kind must be one of &#39;ImageStreamTag&#39; or &#39;DockerImage&#39;. This value will be used to look up a Docker image repository to push to. In the case of an ImageStreamTag, the ImageStreamTag will be looked for in the namespace of the build unless Namespace is specified. | [optional] 
**push_secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | PushSecret is the name of a Secret that would be used for setting up the authentication for executing the Docker push to authentication enabled Docker Registry (or Docker Hub). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


