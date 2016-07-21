# V1SecurityContextConstraints

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**priority** | **int** | Priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields.  The higher the int, the higher priority.  If scores for multiple SCCs are equal they will be sorted by name. | 
**allow_privileged_container** | **bool** | AllowPrivilegedContainer determines if a container can request to be run as privileged. | 
**default_add_capabilities** | [**list[V1Capability]**](V1Capability.md) | DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities. | 
**required_drop_capabilities** | [**list[V1Capability]**](V1Capability.md) | RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added. | 
**allowed_capabilities** | [**list[V1Capability]**](V1Capability.md) | AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author&#39;s discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities. | 
**allow_host_dir_volume_plugin** | **bool** | AllowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin | 
**volumes** | [**list[V1FSType]**](V1FSType.md) |  | 
**allow_host_network** | **bool** | AllowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec. | 
**allow_host_ports** | **bool** | AllowHostPorts determines if the policy allows host ports in the containers. | 
**allow_host_pid** | **bool** | AllowHostPID determines if the policy allows host pid in the containers. | 
**allow_host_ipc** | **bool** | AllowHostIPC determines if the policy allows host ipc in the containers. | 
**se_linux_context** | [**V1SELinuxContextStrategyOptions**](V1SELinuxContextStrategyOptions.md) | SELinuxContext is the strategy that will dictate what labels will be set in the SecurityContext. | [optional] 
**run_as_user** | [**V1RunAsUserStrategyOptions**](V1RunAsUserStrategyOptions.md) | RunAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext. | [optional] 
**supplemental_groups** | [**V1SupplementalGroupsStrategyOptions**](V1SupplementalGroupsStrategyOptions.md) | SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext. | [optional] 
**fs_group** | [**V1FSGroupStrategyOptions**](V1FSGroupStrategyOptions.md) | FSGroup is the strategy that will dictate what fs group is used by the SecurityContext. | [optional] 
**read_only_root_filesystem** | **bool** | ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. | 
**users** | **list[str]** | The users who have permissions to use this security context constraints | [optional] 
**groups** | **list[str]** | The groups that have permission to use this security context constraints | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


