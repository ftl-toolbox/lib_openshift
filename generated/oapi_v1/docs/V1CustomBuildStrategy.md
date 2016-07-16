# V1CustomBuildStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled | 
**pull_secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | PullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Env contains additional environment variables you want to pass into a builder container | [optional] 
**expose_docker_socket** | **bool** | ExposeDockerSocket will allow running Docker commands (and build Docker images) from inside the Docker container. | [optional] 
**force_pull** | **bool** | ForcePull describes if the controller should configure the build pod to always pull the images for the builder or only pull if it is not present locally | [optional] 
**secrets** | [**list[V1SecretSpec]**](V1SecretSpec.md) | Secrets is a list of additional secrets that will be included in the build pod | [optional] 
**build_api_version** | **str** | BuildAPIVersion is the requested API version for the Build object serialized and passed to the custom builder | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


