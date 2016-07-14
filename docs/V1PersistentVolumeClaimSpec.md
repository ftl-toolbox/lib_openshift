# V1PersistentVolumeClaimSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | [**list[V1PersistentVolumeAccessMode]**](V1PersistentVolumeAccessMode.md) | AccessModes contains the desired access modes the volume should have. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#access-modes-1 | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources represents the minimum resources the volume should have. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#resources | [optional] 
**volume_name** | **str** | VolumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


