# V1ServiceSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | [**list[V1ServicePort]**](V1ServicePort.md) | The list of ports that are exposed by this service. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies | 
**selector** | **object** | This service will route traffic to pods having labels matching this selector. Label keys and values that must match in order to receive traffic for this service. If empty, all pods are selected, if not specified, endpoints must be manually specified. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#overview | [optional] 
**portal_ip** | **str** | The IP Address of the service. Deprecated: Use clusterIP instead. | [optional] 
**cluster_ip** | **str** | ClusterIP is usually assigned by the master and is the IP address of the service. If specified, it will be allocated to the service if it is unused or else creation of the service will fail. Valid values are None, empty string (\&quot;\&quot;), or a valid IP address. &#39;None&#39; can be specified for a headless service when proxying is not required. Cannot be updated. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies | [optional] 
**type** | **str** | Type of exposed service. Must be ClusterIP, NodePort, or LoadBalancer. Defaults to ClusterIP. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#external-services | [optional] 
**external_i_ps** | **list[str]** | externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  A previous form of this functionality exists as the deprecatedPublicIPs field.  When using this field, callers should also clear the deprecatedPublicIPs field. | [optional] 
**deprecated_public_i_ps** | **list[str]** | deprecatedPublicIPs is deprecated and replaced by the externalIPs field with almost the exact same semantics.  This field is retained in the v1 API for compatibility until at least 8/20/2016.  It will be removed from any new API revisions.  If both deprecatedPublicIPs *and* externalIPs are set, deprecatedPublicIPs is used. | [optional] 
**session_affinity** | **str** | Supports \&quot;ClientIP\&quot; and \&quot;None\&quot;. Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies | [optional] 
**load_balancer_ip** | **str** | Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


