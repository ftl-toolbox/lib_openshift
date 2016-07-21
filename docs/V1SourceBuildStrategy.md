# V1SourceBuildStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled | 
**pull_secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | PullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Env contains additional environment variables you want to pass into a builder container | [optional] 
**scripts** | **str** | Scripts is the location of Source scripts | [optional] 
**incremental** | **bool** | Incremental flag forces the Source build to do incremental builds if true. | [optional] 
**force_pull** | **bool** | ForcePull describes if the builder should pull the images from registry prior to building. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


