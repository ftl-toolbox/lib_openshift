# V1BuildConfigSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triggers** | [**list[V1BuildTriggerPolicy]**](V1BuildTriggerPolicy.md) | Triggers determine how new Builds can be launched from a BuildConfig. If no triggers are defined, a new build can only occur as a result of an explicit client build creation. | 
**service_account** | **str** | ServiceAccount is the name of the ServiceAccount to use to run the pod created by this build. The pod will be allowed to use secrets referenced by the ServiceAccount | [optional] 
**source** | [**V1BuildSource**](V1BuildSource.md) | Source describes the SCM in use. | [optional] 
**revision** | [**V1SourceRevision**](V1SourceRevision.md) | Revision is the information from the source for a specific repo snapshot. This is optional. | [optional] 
**strategy** | [**V1BuildStrategy**](V1BuildStrategy.md) | Strategy defines how to perform a build. | 
**output** | [**V1BuildOutput**](V1BuildOutput.md) | Output describes the Docker image the Strategy should produce. | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Compute resource requirements to execute the build | [optional] 
**post_commit** | [**V1BuildPostCommitSpec**](V1BuildPostCommitSpec.md) | PostCommit is a build hook executed after the build output image is committed, before it is pushed to a registry. | [optional] 
**completion_deadline_seconds** | **int** | Optional duration in seconds, counted from the time when a build pod gets scheduled in the system, that the build may be active on a node before the system actively tries to terminate the build; value must be positive integer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


