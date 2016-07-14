# V1DeploymentStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type is the name of a deployment strategy. | [optional] 
**custom_params** | [**V1CustomDeploymentStrategyParams**](V1CustomDeploymentStrategyParams.md) | CustomParams are the input to the Custom deployment strategy. | [optional] 
**recreate_params** | [**V1RecreateDeploymentStrategyParams**](V1RecreateDeploymentStrategyParams.md) | RecreateParams are the input to the Recreate deployment strategy. | [optional] 
**rolling_params** | [**V1RollingDeploymentStrategyParams**](V1RollingDeploymentStrategyParams.md) | RollingParams are the input to the Rolling deployment strategy. | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources contains resource requirements to execute the deployment and any hooks | [optional] 
**labels** | **object** | Labels is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods. | [optional] 
**annotations** | **object** | Annotations is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


