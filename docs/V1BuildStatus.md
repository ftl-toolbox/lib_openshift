# V1BuildStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | Phase is the point in the build lifecycle. | 
**cancelled** | **bool** | Cancelled describes if a cancel event was triggered for the build. | [optional] 
**reason** | **str** | Reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. | [optional] 
**message** | **str** | Message is a human-readable message indicating details about why the build has this status. | [optional] 
**start_timestamp** | **str** | StartTimestamp is a timestamp representing the server time when this Build started running in a Pod. It is represented in RFC3339 form and is in UTC. | [optional] 
**completion_timestamp** | **str** | CompletionTimestamp is a timestamp representing the server time when this Build was finished, whether that build failed or succeeded.  It reflects the time at which the Pod running the Build terminated. It is represented in RFC3339 form and is in UTC. | [optional] 
**duration** | [**TimeDuration**](TimeDuration.md) | Duration contains time.Duration object describing build time. | [optional] 
**output_docker_image_reference** | **str** | OutputDockerImageReference contains a reference to the Docker image that will be built by this build. Its value is computed from Build.Spec.Output.To, and should include the registry address, so that it can be used to push and pull the image. | [optional] 
**config** | [**V1ObjectReference**](V1ObjectReference.md) | Config is an ObjectReference to the BuildConfig this Build is based on. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


