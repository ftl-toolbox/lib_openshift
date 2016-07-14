# V1PersistentVolumeClaimStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | Phase represents the current phase of PersistentVolumeClaim. | [optional] 
**access_modes** | [**list[V1PersistentVolumeAccessMode]**](V1PersistentVolumeAccessMode.md) | AccessModes contains the actual access modes the volume backing the PVC has. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#access-modes-1 | [optional] 
**capacity** | **object** | Represents the actual resources of the underlying volume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


