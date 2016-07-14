# V1ResourceQuotaSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | **object** | Hard is the set of desired hard limits for each named resource. More info: http://releases.k8s.io/release-1.2/docs/design/admission_control_resource_quota.md#admissioncontrol-plugin-resourcequota | [optional] 
**scopes** | [**list[V1ResourceQuotaScope]**](V1ResourceQuotaScope.md) | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


