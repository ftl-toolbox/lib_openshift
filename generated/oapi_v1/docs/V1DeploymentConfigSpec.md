# V1DeploymentConfigSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**V1DeploymentStrategy**](V1DeploymentStrategy.md) | Strategy describes how a deployment is executed. | 
**triggers** | [**list[V1DeploymentTriggerPolicy]**](V1DeploymentTriggerPolicy.md) | Triggers determine how updates to a DeploymentConfig result in new deployments. If no triggers are defined, a new deployment can only occur as a result of an explicit client update to the DeploymentConfig with a new LatestVersion. | 
**replicas** | **int** | Replicas is the number of desired replicas. | 
**test** | **bool** | Test ensures that this deployment config will have zero replicas except while a deployment is running. This allows the deployment config to be used as a continuous deployment test - triggering on images, running the deployment, and then succeeding or failing. Post strategy hooks and After actions can be used to integrate successful deployment with an action. | 
**selector** | **object** | Selector is a label query over pods that should match the Replicas count. | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | Template is the object that describes the pod that will be created if insufficient replicas are detected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


