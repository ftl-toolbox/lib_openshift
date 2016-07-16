# V1TLSConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**termination** | **str** | Termination indicates termination type. | 
**certificate** | **str** | Certificate provides certificate contents | [optional] 
**key** | **str** | Key provides key file contents | [optional] 
**ca_certificate** | **str** | CACertificate provides the cert authority certificate contents | [optional] 
**destination_ca_certificate** | **str** | DestinationCACertificate provides the contents of the ca certificate of the final destination.  When using reencrypt termination this file should be provided in order to have routers use it for health checks on the secure connection | [optional] 
**insecure_edge_termination_policy** | **str** | InsecureEdgeTerminationPolicy indicates the desired behavior for insecure connections to an edge-terminated route:   disable, allow or redirect | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


