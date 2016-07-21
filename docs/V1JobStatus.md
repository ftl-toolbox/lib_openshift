# V1JobStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1JobCondition]**](V1JobCondition.md) | Conditions represent the latest available observations of an object&#39;s current state. More info: http://releases.k8s.io/release-1.2/docs/user-guide/jobs.md | [optional] 
**start_time** | **str** | StartTime represents time when the job was acknowledged by the Job Manager. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. | [optional] 
**completion_time** | **str** | CompletionTime represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. | [optional] 
**active** | **int** | Active is the number of actively running pods. | [optional] 
**succeeded** | **int** | Succeeded is the number of pods which reached Phase Succeeded. | [optional] 
**failed** | **int** | Failed is the number of pods which reached Phase Failed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


