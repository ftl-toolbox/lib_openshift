# V1DeploymentConfigRollbackSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From points to a ReplicationController which is a deployment. | 
**include_triggers** | **bool** | IncludeTriggers specifies whether to include config Triggers. | 
**include_template** | **bool** | IncludeTemplate specifies whether to include the PodTemplateSpec. | 
**include_replication_meta** | **bool** | IncludeReplicationMeta specifies whether to include the replica count and selector. | 
**include_strategy** | **bool** | IncludeStrategy specifies whether to include the deployment Strategy. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


