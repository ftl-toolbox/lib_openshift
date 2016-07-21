# lib_openshift.ApiV1

All URIs are relative to *https://localhost:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_binding**](ApiV1.md#create_binding) | **POST** /api/v1/bindings | create a Binding
[**create_config_map**](ApiV1.md#create_config_map) | **POST** /api/v1/configmaps | create a ConfigMap
[**create_endpoints**](ApiV1.md#create_endpoints) | **POST** /api/v1/endpoints | create a Endpoints
[**create_event**](ApiV1.md#create_event) | **POST** /api/v1/events | create a Event
[**create_limit_range**](ApiV1.md#create_limit_range) | **POST** /api/v1/limitranges | create a LimitRange
[**create_namespaced_binding**](ApiV1.md#create_namespaced_binding) | **POST** /api/v1/namespaces/{namespace}/bindings | create a Binding
[**create_namespaced_binding_binding**](ApiV1.md#create_namespaced_binding_binding) | **POST** /api/v1/namespaces/{namespace}/pods/{name}/binding | create binding of a Binding
[**create_namespaced_config_map**](ApiV1.md#create_namespaced_config_map) | **POST** /api/v1/namespaces/{namespace}/configmaps | create a ConfigMap
[**create_namespaced_endpoints**](ApiV1.md#create_namespaced_endpoints) | **POST** /api/v1/namespaces/{namespace}/endpoints | create a Endpoints
[**create_namespaced_event**](ApiV1.md#create_namespaced_event) | **POST** /api/v1/namespaces/{namespace}/events | create a Event
[**create_namespaced_limit_range**](ApiV1.md#create_namespaced_limit_range) | **POST** /api/v1/namespaces/{namespace}/limitranges | create a LimitRange
[**create_namespaced_namespace**](ApiV1.md#create_namespaced_namespace) | **POST** /api/v1/namespaces | create a Namespace
[**create_namespaced_node**](ApiV1.md#create_namespaced_node) | **POST** /api/v1/nodes | create a Node
[**create_namespaced_persistent_volume**](ApiV1.md#create_namespaced_persistent_volume) | **POST** /api/v1/persistentvolumes | create a PersistentVolume
[**create_namespaced_persistent_volume_claim**](ApiV1.md#create_namespaced_persistent_volume_claim) | **POST** /api/v1/namespaces/{namespace}/persistentvolumeclaims | create a PersistentVolumeClaim
[**create_namespaced_pod**](ApiV1.md#create_namespaced_pod) | **POST** /api/v1/namespaces/{namespace}/pods | create a Pod
[**create_namespaced_pod_template**](ApiV1.md#create_namespaced_pod_template) | **POST** /api/v1/namespaces/{namespace}/podtemplates | create a PodTemplate
[**create_namespaced_replication_controller**](ApiV1.md#create_namespaced_replication_controller) | **POST** /api/v1/namespaces/{namespace}/replicationcontrollers | create a ReplicationController
[**create_namespaced_resource_quota**](ApiV1.md#create_namespaced_resource_quota) | **POST** /api/v1/namespaces/{namespace}/resourcequotas | create a ResourceQuota
[**create_namespaced_secret**](ApiV1.md#create_namespaced_secret) | **POST** /api/v1/namespaces/{namespace}/secrets | create a Secret
[**create_namespaced_security_context_constraints**](ApiV1.md#create_namespaced_security_context_constraints) | **POST** /api/v1/securitycontextconstraints | create a SecurityContextConstraints
[**create_namespaced_service**](ApiV1.md#create_namespaced_service) | **POST** /api/v1/namespaces/{namespace}/services | create a Service
[**create_namespaced_service_account**](ApiV1.md#create_namespaced_service_account) | **POST** /api/v1/namespaces/{namespace}/serviceaccounts | create a ServiceAccount
[**create_persistent_volume_claim**](ApiV1.md#create_persistent_volume_claim) | **POST** /api/v1/persistentvolumeclaims | create a PersistentVolumeClaim
[**create_pod**](ApiV1.md#create_pod) | **POST** /api/v1/pods | create a Pod
[**create_pod_template**](ApiV1.md#create_pod_template) | **POST** /api/v1/podtemplates | create a PodTemplate
[**create_replication_controller**](ApiV1.md#create_replication_controller) | **POST** /api/v1/replicationcontrollers | create a ReplicationController
[**create_resource_quota**](ApiV1.md#create_resource_quota) | **POST** /api/v1/resourcequotas | create a ResourceQuota
[**create_secret**](ApiV1.md#create_secret) | **POST** /api/v1/secrets | create a Secret
[**create_service**](ApiV1.md#create_service) | **POST** /api/v1/services | create a Service
[**create_service_account**](ApiV1.md#create_service_account) | **POST** /api/v1/serviceaccounts | create a ServiceAccount
[**delete_namespaced_config_map**](ApiV1.md#delete_namespaced_config_map) | **DELETE** /api/v1/namespaces/{namespace}/configmaps/{name} | delete a ConfigMap
[**delete_namespaced_endpoints**](ApiV1.md#delete_namespaced_endpoints) | **DELETE** /api/v1/namespaces/{namespace}/endpoints/{name} | delete a Endpoints
[**delete_namespaced_event**](ApiV1.md#delete_namespaced_event) | **DELETE** /api/v1/namespaces/{namespace}/events/{name} | delete a Event
[**delete_namespaced_limit_range**](ApiV1.md#delete_namespaced_limit_range) | **DELETE** /api/v1/namespaces/{namespace}/limitranges/{name} | delete a LimitRange
[**delete_namespaced_namespace**](ApiV1.md#delete_namespaced_namespace) | **DELETE** /api/v1/namespaces/{name} | delete a Namespace
[**delete_namespaced_node**](ApiV1.md#delete_namespaced_node) | **DELETE** /api/v1/nodes/{name} | delete a Node
[**delete_namespaced_node_proxy**](ApiV1.md#delete_namespaced_node_proxy) | **DELETE** /api/v1/nodes/{name}/proxy | connect DELETE requests to proxy of Node
[**delete_namespaced_node_proxy_0**](ApiV1.md#delete_namespaced_node_proxy_0) | **DELETE** /api/v1/nodes/{name}/proxy/{path} | connect DELETE requests to proxy of Node
[**delete_namespaced_persistent_volume**](ApiV1.md#delete_namespaced_persistent_volume) | **DELETE** /api/v1/persistentvolumes/{name} | delete a PersistentVolume
[**delete_namespaced_persistent_volume_claim**](ApiV1.md#delete_namespaced_persistent_volume_claim) | **DELETE** /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name} | delete a PersistentVolumeClaim
[**delete_namespaced_pod**](ApiV1.md#delete_namespaced_pod) | **DELETE** /api/v1/namespaces/{namespace}/pods/{name} | delete a Pod
[**delete_namespaced_pod_proxy**](ApiV1.md#delete_namespaced_pod_proxy) | **DELETE** /api/v1/namespaces/{namespace}/pods/{name}/proxy | connect DELETE requests to proxy of Pod
[**delete_namespaced_pod_proxy_0**](ApiV1.md#delete_namespaced_pod_proxy_0) | **DELETE** /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path} | connect DELETE requests to proxy of Pod
[**delete_namespaced_pod_template**](ApiV1.md#delete_namespaced_pod_template) | **DELETE** /api/v1/namespaces/{namespace}/podtemplates/{name} | delete a PodTemplate
[**delete_namespaced_replication_controller**](ApiV1.md#delete_namespaced_replication_controller) | **DELETE** /api/v1/namespaces/{namespace}/replicationcontrollers/{name} | delete a ReplicationController
[**delete_namespaced_resource_quota**](ApiV1.md#delete_namespaced_resource_quota) | **DELETE** /api/v1/namespaces/{namespace}/resourcequotas/{name} | delete a ResourceQuota
[**delete_namespaced_secret**](ApiV1.md#delete_namespaced_secret) | **DELETE** /api/v1/namespaces/{namespace}/secrets/{name} | delete a Secret
[**delete_namespaced_security_context_constraints**](ApiV1.md#delete_namespaced_security_context_constraints) | **DELETE** /api/v1/securitycontextconstraints/{name} | delete a SecurityContextConstraints
[**delete_namespaced_service**](ApiV1.md#delete_namespaced_service) | **DELETE** /api/v1/namespaces/{namespace}/services/{name} | delete a Service
[**delete_namespaced_service_account**](ApiV1.md#delete_namespaced_service_account) | **DELETE** /api/v1/namespaces/{namespace}/serviceaccounts/{name} | delete a ServiceAccount
[**delete_namespaced_service_proxy**](ApiV1.md#delete_namespaced_service_proxy) | **DELETE** /api/v1/namespaces/{namespace}/services/{name}/proxy | connect DELETE requests to proxy of Service
[**delete_namespaced_service_proxy_0**](ApiV1.md#delete_namespaced_service_proxy_0) | **DELETE** /api/v1/namespaces/{namespace}/services/{name}/proxy/{path} | connect DELETE requests to proxy of Service
[**deletecollection_namespaced_config_map**](ApiV1.md#deletecollection_namespaced_config_map) | **DELETE** /api/v1/namespaces/{namespace}/configmaps | delete collection of ConfigMap
[**deletecollection_namespaced_endpoints**](ApiV1.md#deletecollection_namespaced_endpoints) | **DELETE** /api/v1/namespaces/{namespace}/endpoints | delete collection of Endpoints
[**deletecollection_namespaced_event**](ApiV1.md#deletecollection_namespaced_event) | **DELETE** /api/v1/namespaces/{namespace}/events | delete collection of Event
[**deletecollection_namespaced_limit_range**](ApiV1.md#deletecollection_namespaced_limit_range) | **DELETE** /api/v1/namespaces/{namespace}/limitranges | delete collection of LimitRange
[**deletecollection_namespaced_namespace**](ApiV1.md#deletecollection_namespaced_namespace) | **DELETE** /api/v1/namespaces | delete collection of Namespace
[**deletecollection_namespaced_node**](ApiV1.md#deletecollection_namespaced_node) | **DELETE** /api/v1/nodes | delete collection of Node
[**deletecollection_namespaced_persistent_volume**](ApiV1.md#deletecollection_namespaced_persistent_volume) | **DELETE** /api/v1/persistentvolumes | delete collection of PersistentVolume
[**deletecollection_namespaced_persistent_volume_claim**](ApiV1.md#deletecollection_namespaced_persistent_volume_claim) | **DELETE** /api/v1/namespaces/{namespace}/persistentvolumeclaims | delete collection of PersistentVolumeClaim
[**deletecollection_namespaced_pod**](ApiV1.md#deletecollection_namespaced_pod) | **DELETE** /api/v1/namespaces/{namespace}/pods | delete collection of Pod
[**deletecollection_namespaced_pod_template**](ApiV1.md#deletecollection_namespaced_pod_template) | **DELETE** /api/v1/namespaces/{namespace}/podtemplates | delete collection of PodTemplate
[**deletecollection_namespaced_replication_controller**](ApiV1.md#deletecollection_namespaced_replication_controller) | **DELETE** /api/v1/namespaces/{namespace}/replicationcontrollers | delete collection of ReplicationController
[**deletecollection_namespaced_resource_quota**](ApiV1.md#deletecollection_namespaced_resource_quota) | **DELETE** /api/v1/namespaces/{namespace}/resourcequotas | delete collection of ResourceQuota
[**deletecollection_namespaced_secret**](ApiV1.md#deletecollection_namespaced_secret) | **DELETE** /api/v1/namespaces/{namespace}/secrets | delete collection of Secret
[**deletecollection_namespaced_security_context_constraints**](ApiV1.md#deletecollection_namespaced_security_context_constraints) | **DELETE** /api/v1/securitycontextconstraints | delete collection of SecurityContextConstraints
[**deletecollection_namespaced_service_account**](ApiV1.md#deletecollection_namespaced_service_account) | **DELETE** /api/v1/namespaces/{namespace}/serviceaccounts | delete collection of ServiceAccount
[**get_api_resources**](ApiV1.md#get_api_resources) | **GET** /api/v1 | get available resources
[**get_namespaced_node_proxy**](ApiV1.md#get_namespaced_node_proxy) | **GET** /api/v1/nodes/{name}/proxy | connect GET requests to proxy of Node
[**get_namespaced_node_proxy_0**](ApiV1.md#get_namespaced_node_proxy_0) | **GET** /api/v1/nodes/{name}/proxy/{path} | connect GET requests to proxy of Node
[**get_namespaced_pod_attach**](ApiV1.md#get_namespaced_pod_attach) | **GET** /api/v1/namespaces/{namespace}/pods/{name}/attach | connect GET requests to attach of Pod
[**get_namespaced_pod_exec**](ApiV1.md#get_namespaced_pod_exec) | **GET** /api/v1/namespaces/{namespace}/pods/{name}/exec | connect GET requests to exec of Pod
[**get_namespaced_pod_portforward**](ApiV1.md#get_namespaced_pod_portforward) | **GET** /api/v1/namespaces/{namespace}/pods/{name}/portforward | connect GET requests to portforward of Pod
[**get_namespaced_pod_proxy**](ApiV1.md#get_namespaced_pod_proxy) | **GET** /api/v1/namespaces/{namespace}/pods/{name}/proxy | connect GET requests to proxy of Pod
[**get_namespaced_pod_proxy_0**](ApiV1.md#get_namespaced_pod_proxy_0) | **GET** /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path} | connect GET requests to proxy of Pod
[**get_namespaced_service_proxy**](ApiV1.md#get_namespaced_service_proxy) | **GET** /api/v1/namespaces/{namespace}/services/{name}/proxy | connect GET requests to proxy of Service
[**get_namespaced_service_proxy_0**](ApiV1.md#get_namespaced_service_proxy_0) | **GET** /api/v1/namespaces/{namespace}/services/{name}/proxy/{path} | connect GET requests to proxy of Service
[**head_namespaced_node_proxy**](ApiV1.md#head_namespaced_node_proxy) | **HEAD** /api/v1/nodes/{name}/proxy | connect HEAD requests to proxy of Node
[**head_namespaced_node_proxy_0**](ApiV1.md#head_namespaced_node_proxy_0) | **HEAD** /api/v1/nodes/{name}/proxy/{path} | connect HEAD requests to proxy of Node
[**head_namespaced_pod_proxy**](ApiV1.md#head_namespaced_pod_proxy) | **HEAD** /api/v1/namespaces/{namespace}/pods/{name}/proxy | connect HEAD requests to proxy of Pod
[**head_namespaced_pod_proxy_0**](ApiV1.md#head_namespaced_pod_proxy_0) | **HEAD** /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path} | connect HEAD requests to proxy of Pod
[**head_namespaced_service_proxy**](ApiV1.md#head_namespaced_service_proxy) | **HEAD** /api/v1/namespaces/{namespace}/services/{name}/proxy | connect HEAD requests to proxy of Service
[**head_namespaced_service_proxy_0**](ApiV1.md#head_namespaced_service_proxy_0) | **HEAD** /api/v1/namespaces/{namespace}/services/{name}/proxy/{path} | connect HEAD requests to proxy of Service
[**list_config_map**](ApiV1.md#list_config_map) | **GET** /api/v1/configmaps | list or watch objects of kind ConfigMap
[**list_endpoints**](ApiV1.md#list_endpoints) | **GET** /api/v1/endpoints | list or watch objects of kind Endpoints
[**list_event**](ApiV1.md#list_event) | **GET** /api/v1/events | list or watch objects of kind Event
[**list_limit_range**](ApiV1.md#list_limit_range) | **GET** /api/v1/limitranges | list or watch objects of kind LimitRange
[**list_namespaced_component_status**](ApiV1.md#list_namespaced_component_status) | **GET** /api/v1/componentstatuses | list objects of kind ComponentStatus
[**list_namespaced_config_map**](ApiV1.md#list_namespaced_config_map) | **GET** /api/v1/namespaces/{namespace}/configmaps | list or watch objects of kind ConfigMap
[**list_namespaced_endpoints**](ApiV1.md#list_namespaced_endpoints) | **GET** /api/v1/namespaces/{namespace}/endpoints | list or watch objects of kind Endpoints
[**list_namespaced_event**](ApiV1.md#list_namespaced_event) | **GET** /api/v1/namespaces/{namespace}/events | list or watch objects of kind Event
[**list_namespaced_limit_range**](ApiV1.md#list_namespaced_limit_range) | **GET** /api/v1/namespaces/{namespace}/limitranges | list or watch objects of kind LimitRange
[**list_namespaced_namespace**](ApiV1.md#list_namespaced_namespace) | **GET** /api/v1/namespaces | list or watch objects of kind Namespace
[**list_namespaced_node**](ApiV1.md#list_namespaced_node) | **GET** /api/v1/nodes | list or watch objects of kind Node
[**list_namespaced_persistent_volume**](ApiV1.md#list_namespaced_persistent_volume) | **GET** /api/v1/persistentvolumes | list or watch objects of kind PersistentVolume
[**list_namespaced_persistent_volume_claim**](ApiV1.md#list_namespaced_persistent_volume_claim) | **GET** /api/v1/namespaces/{namespace}/persistentvolumeclaims | list or watch objects of kind PersistentVolumeClaim
[**list_namespaced_pod**](ApiV1.md#list_namespaced_pod) | **GET** /api/v1/namespaces/{namespace}/pods | list or watch objects of kind Pod
[**list_namespaced_pod_template**](ApiV1.md#list_namespaced_pod_template) | **GET** /api/v1/namespaces/{namespace}/podtemplates | list or watch objects of kind PodTemplate
[**list_namespaced_replication_controller**](ApiV1.md#list_namespaced_replication_controller) | **GET** /api/v1/namespaces/{namespace}/replicationcontrollers | list or watch objects of kind ReplicationController
[**list_namespaced_resource_quota**](ApiV1.md#list_namespaced_resource_quota) | **GET** /api/v1/namespaces/{namespace}/resourcequotas | list or watch objects of kind ResourceQuota
[**list_namespaced_secret**](ApiV1.md#list_namespaced_secret) | **GET** /api/v1/namespaces/{namespace}/secrets | list or watch objects of kind Secret
[**list_namespaced_security_context_constraints**](ApiV1.md#list_namespaced_security_context_constraints) | **GET** /api/v1/securitycontextconstraints | list or watch objects of kind SecurityContextConstraints
[**list_namespaced_service**](ApiV1.md#list_namespaced_service) | **GET** /api/v1/namespaces/{namespace}/services | list or watch objects of kind Service
[**list_namespaced_service_account**](ApiV1.md#list_namespaced_service_account) | **GET** /api/v1/namespaces/{namespace}/serviceaccounts | list or watch objects of kind ServiceAccount
[**list_persistent_volume_claim**](ApiV1.md#list_persistent_volume_claim) | **GET** /api/v1/persistentvolumeclaims | list or watch objects of kind PersistentVolumeClaim
[**list_pod**](ApiV1.md#list_pod) | **GET** /api/v1/pods | list or watch objects of kind Pod
[**list_pod_template**](ApiV1.md#list_pod_template) | **GET** /api/v1/podtemplates | list or watch objects of kind PodTemplate
[**list_replication_controller**](ApiV1.md#list_replication_controller) | **GET** /api/v1/replicationcontrollers | list or watch objects of kind ReplicationController
[**list_resource_quota**](ApiV1.md#list_resource_quota) | **GET** /api/v1/resourcequotas | list or watch objects of kind ResourceQuota
[**list_secret**](ApiV1.md#list_secret) | **GET** /api/v1/secrets | list or watch objects of kind Secret
[**list_service**](ApiV1.md#list_service) | **GET** /api/v1/services | list or watch objects of kind Service
[**list_service_account**](ApiV1.md#list_service_account) | **GET** /api/v1/serviceaccounts | list or watch objects of kind ServiceAccount
[**options_namespaced_node_proxy**](ApiV1.md#options_namespaced_node_proxy) | **OPTIONS** /api/v1/nodes/{name}/proxy | connect OPTIONS requests to proxy of Node
[**options_namespaced_node_proxy_0**](ApiV1.md#options_namespaced_node_proxy_0) | **OPTIONS** /api/v1/nodes/{name}/proxy/{path} | connect OPTIONS requests to proxy of Node
[**options_namespaced_pod_proxy**](ApiV1.md#options_namespaced_pod_proxy) | **OPTIONS** /api/v1/namespaces/{namespace}/pods/{name}/proxy | connect OPTIONS requests to proxy of Pod
[**options_namespaced_pod_proxy_0**](ApiV1.md#options_namespaced_pod_proxy_0) | **OPTIONS** /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path} | connect OPTIONS requests to proxy of Pod
[**options_namespaced_service_proxy**](ApiV1.md#options_namespaced_service_proxy) | **OPTIONS** /api/v1/namespaces/{namespace}/services/{name}/proxy | connect OPTIONS requests to proxy of Service
[**options_namespaced_service_proxy_0**](ApiV1.md#options_namespaced_service_proxy_0) | **OPTIONS** /api/v1/namespaces/{namespace}/services/{name}/proxy/{path} | connect OPTIONS requests to proxy of Service
[**patch_namespaced_config_map**](ApiV1.md#patch_namespaced_config_map) | **PATCH** /api/v1/namespaces/{namespace}/configmaps/{name} | partially update the specified ConfigMap
[**patch_namespaced_endpoints**](ApiV1.md#patch_namespaced_endpoints) | **PATCH** /api/v1/namespaces/{namespace}/endpoints/{name} | partially update the specified Endpoints
[**patch_namespaced_event**](ApiV1.md#patch_namespaced_event) | **PATCH** /api/v1/namespaces/{namespace}/events/{name} | partially update the specified Event
[**patch_namespaced_limit_range**](ApiV1.md#patch_namespaced_limit_range) | **PATCH** /api/v1/namespaces/{namespace}/limitranges/{name} | partially update the specified LimitRange
[**patch_namespaced_namespace**](ApiV1.md#patch_namespaced_namespace) | **PATCH** /api/v1/namespaces/{name} | partially update the specified Namespace
[**patch_namespaced_node**](ApiV1.md#patch_namespaced_node) | **PATCH** /api/v1/nodes/{name} | partially update the specified Node
[**patch_namespaced_persistent_volume**](ApiV1.md#patch_namespaced_persistent_volume) | **PATCH** /api/v1/persistentvolumes/{name} | partially update the specified PersistentVolume
[**patch_namespaced_persistent_volume_claim**](ApiV1.md#patch_namespaced_persistent_volume_claim) | **PATCH** /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name} | partially update the specified PersistentVolumeClaim
[**patch_namespaced_pod**](ApiV1.md#patch_namespaced_pod) | **PATCH** /api/v1/namespaces/{namespace}/pods/{name} | partially update the specified Pod
[**patch_namespaced_pod_template**](ApiV1.md#patch_namespaced_pod_template) | **PATCH** /api/v1/namespaces/{namespace}/podtemplates/{name} | partially update the specified PodTemplate
[**patch_namespaced_replication_controller**](ApiV1.md#patch_namespaced_replication_controller) | **PATCH** /api/v1/namespaces/{namespace}/replicationcontrollers/{name} | partially update the specified ReplicationController
[**patch_namespaced_resource_quota**](ApiV1.md#patch_namespaced_resource_quota) | **PATCH** /api/v1/namespaces/{namespace}/resourcequotas/{name} | partially update the specified ResourceQuota
[**patch_namespaced_scale_scale**](ApiV1.md#patch_namespaced_scale_scale) | **PATCH** /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale | partially update scale of the specified Scale
[**patch_namespaced_secret**](ApiV1.md#patch_namespaced_secret) | **PATCH** /api/v1/namespaces/{namespace}/secrets/{name} | partially update the specified Secret
[**patch_namespaced_security_context_constraints**](ApiV1.md#patch_namespaced_security_context_constraints) | **PATCH** /api/v1/securitycontextconstraints/{name} | partially update the specified SecurityContextConstraints
[**patch_namespaced_service**](ApiV1.md#patch_namespaced_service) | **PATCH** /api/v1/namespaces/{namespace}/services/{name} | partially update the specified Service
[**patch_namespaced_service_account**](ApiV1.md#patch_namespaced_service_account) | **PATCH** /api/v1/namespaces/{namespace}/serviceaccounts/{name} | partially update the specified ServiceAccount
[**post_namespaced_node_proxy**](ApiV1.md#post_namespaced_node_proxy) | **POST** /api/v1/nodes/{name}/proxy | connect POST requests to proxy of Node
[**post_namespaced_node_proxy_0**](ApiV1.md#post_namespaced_node_proxy_0) | **POST** /api/v1/nodes/{name}/proxy/{path} | connect POST requests to proxy of Node
[**post_namespaced_pod_attach**](ApiV1.md#post_namespaced_pod_attach) | **POST** /api/v1/namespaces/{namespace}/pods/{name}/attach | connect POST requests to attach of Pod
[**post_namespaced_pod_exec**](ApiV1.md#post_namespaced_pod_exec) | **POST** /api/v1/namespaces/{namespace}/pods/{name}/exec | connect POST requests to exec of Pod
[**post_namespaced_pod_portforward**](ApiV1.md#post_namespaced_pod_portforward) | **POST** /api/v1/namespaces/{namespace}/pods/{name}/portforward | connect POST requests to portforward of Pod
[**post_namespaced_pod_proxy**](ApiV1.md#post_namespaced_pod_proxy) | **POST** /api/v1/namespaces/{namespace}/pods/{name}/proxy | connect POST requests to proxy of Pod
[**post_namespaced_pod_proxy_0**](ApiV1.md#post_namespaced_pod_proxy_0) | **POST** /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path} | connect POST requests to proxy of Pod
[**post_namespaced_service_proxy**](ApiV1.md#post_namespaced_service_proxy) | **POST** /api/v1/namespaces/{namespace}/services/{name}/proxy | connect POST requests to proxy of Service
[**post_namespaced_service_proxy_0**](ApiV1.md#post_namespaced_service_proxy_0) | **POST** /api/v1/namespaces/{namespace}/services/{name}/proxy/{path} | connect POST requests to proxy of Service
[**proxy_delete_namespaced_node**](ApiV1.md#proxy_delete_namespaced_node) | **DELETE** /api/v1/proxy/nodes/{name} | proxy DELETE requests to Node
[**proxy_delete_namespaced_node_0**](ApiV1.md#proxy_delete_namespaced_node_0) | **DELETE** /api/v1/proxy/nodes/{name}/{path} | proxy DELETE requests to Node
[**proxy_delete_namespaced_pod**](ApiV1.md#proxy_delete_namespaced_pod) | **DELETE** /api/v1/proxy/namespaces/{namespace}/pods/{name} | proxy DELETE requests to Pod
[**proxy_delete_namespaced_pod_0**](ApiV1.md#proxy_delete_namespaced_pod_0) | **DELETE** /api/v1/proxy/namespaces/{namespace}/pods/{name}/{path} | proxy DELETE requests to Pod
[**proxy_delete_namespaced_service**](ApiV1.md#proxy_delete_namespaced_service) | **DELETE** /api/v1/proxy/namespaces/{namespace}/services/{name} | proxy DELETE requests to Service
[**proxy_delete_namespaced_service_0**](ApiV1.md#proxy_delete_namespaced_service_0) | **DELETE** /api/v1/proxy/namespaces/{namespace}/services/{name}/{path} | proxy DELETE requests to Service
[**proxy_get_namespaced_node**](ApiV1.md#proxy_get_namespaced_node) | **GET** /api/v1/proxy/nodes/{name} | proxy GET requests to Node
[**proxy_get_namespaced_node_0**](ApiV1.md#proxy_get_namespaced_node_0) | **GET** /api/v1/proxy/nodes/{name}/{path} | proxy GET requests to Node
[**proxy_get_namespaced_pod**](ApiV1.md#proxy_get_namespaced_pod) | **GET** /api/v1/proxy/namespaces/{namespace}/pods/{name} | proxy GET requests to Pod
[**proxy_get_namespaced_pod_0**](ApiV1.md#proxy_get_namespaced_pod_0) | **GET** /api/v1/proxy/namespaces/{namespace}/pods/{name}/{path} | proxy GET requests to Pod
[**proxy_get_namespaced_service**](ApiV1.md#proxy_get_namespaced_service) | **GET** /api/v1/proxy/namespaces/{namespace}/services/{name} | proxy GET requests to Service
[**proxy_get_namespaced_service_0**](ApiV1.md#proxy_get_namespaced_service_0) | **GET** /api/v1/proxy/namespaces/{namespace}/services/{name}/{path} | proxy GET requests to Service
[**proxy_head_namespaced_node**](ApiV1.md#proxy_head_namespaced_node) | **HEAD** /api/v1/proxy/nodes/{name} | proxy HEAD requests to Node
[**proxy_head_namespaced_node_0**](ApiV1.md#proxy_head_namespaced_node_0) | **HEAD** /api/v1/proxy/nodes/{name}/{path} | proxy HEAD requests to Node
[**proxy_head_namespaced_pod**](ApiV1.md#proxy_head_namespaced_pod) | **HEAD** /api/v1/proxy/namespaces/{namespace}/pods/{name} | proxy HEAD requests to Pod
[**proxy_head_namespaced_pod_0**](ApiV1.md#proxy_head_namespaced_pod_0) | **HEAD** /api/v1/proxy/namespaces/{namespace}/pods/{name}/{path} | proxy HEAD requests to Pod
[**proxy_head_namespaced_service**](ApiV1.md#proxy_head_namespaced_service) | **HEAD** /api/v1/proxy/namespaces/{namespace}/services/{name} | proxy HEAD requests to Service
[**proxy_head_namespaced_service_0**](ApiV1.md#proxy_head_namespaced_service_0) | **HEAD** /api/v1/proxy/namespaces/{namespace}/services/{name}/{path} | proxy HEAD requests to Service
[**proxy_options_namespaced_node**](ApiV1.md#proxy_options_namespaced_node) | **OPTIONS** /api/v1/proxy/nodes/{name} | proxy OPTIONS requests to Node
[**proxy_options_namespaced_node_0**](ApiV1.md#proxy_options_namespaced_node_0) | **OPTIONS** /api/v1/proxy/nodes/{name}/{path} | proxy OPTIONS requests to Node
[**proxy_options_namespaced_pod**](ApiV1.md#proxy_options_namespaced_pod) | **OPTIONS** /api/v1/proxy/namespaces/{namespace}/pods/{name} | proxy OPTIONS requests to Pod
[**proxy_options_namespaced_pod_0**](ApiV1.md#proxy_options_namespaced_pod_0) | **OPTIONS** /api/v1/proxy/namespaces/{namespace}/pods/{name}/{path} | proxy OPTIONS requests to Pod
[**proxy_options_namespaced_service**](ApiV1.md#proxy_options_namespaced_service) | **OPTIONS** /api/v1/proxy/namespaces/{namespace}/services/{name} | proxy OPTIONS requests to Service
[**proxy_options_namespaced_service_0**](ApiV1.md#proxy_options_namespaced_service_0) | **OPTIONS** /api/v1/proxy/namespaces/{namespace}/services/{name}/{path} | proxy OPTIONS requests to Service
[**proxy_post_namespaced_node**](ApiV1.md#proxy_post_namespaced_node) | **POST** /api/v1/proxy/nodes/{name} | proxy POST requests to Node
[**proxy_post_namespaced_node_0**](ApiV1.md#proxy_post_namespaced_node_0) | **POST** /api/v1/proxy/nodes/{name}/{path} | proxy POST requests to Node
[**proxy_post_namespaced_pod**](ApiV1.md#proxy_post_namespaced_pod) | **POST** /api/v1/proxy/namespaces/{namespace}/pods/{name} | proxy POST requests to Pod
[**proxy_post_namespaced_pod_0**](ApiV1.md#proxy_post_namespaced_pod_0) | **POST** /api/v1/proxy/namespaces/{namespace}/pods/{name}/{path} | proxy POST requests to Pod
[**proxy_post_namespaced_service**](ApiV1.md#proxy_post_namespaced_service) | **POST** /api/v1/proxy/namespaces/{namespace}/services/{name} | proxy POST requests to Service
[**proxy_post_namespaced_service_0**](ApiV1.md#proxy_post_namespaced_service_0) | **POST** /api/v1/proxy/namespaces/{namespace}/services/{name}/{path} | proxy POST requests to Service
[**proxy_put_namespaced_node**](ApiV1.md#proxy_put_namespaced_node) | **PUT** /api/v1/proxy/nodes/{name} | proxy PUT requests to Node
[**proxy_put_namespaced_node_0**](ApiV1.md#proxy_put_namespaced_node_0) | **PUT** /api/v1/proxy/nodes/{name}/{path} | proxy PUT requests to Node
[**proxy_put_namespaced_pod**](ApiV1.md#proxy_put_namespaced_pod) | **PUT** /api/v1/proxy/namespaces/{namespace}/pods/{name} | proxy PUT requests to Pod
[**proxy_put_namespaced_pod_0**](ApiV1.md#proxy_put_namespaced_pod_0) | **PUT** /api/v1/proxy/namespaces/{namespace}/pods/{name}/{path} | proxy PUT requests to Pod
[**proxy_put_namespaced_service**](ApiV1.md#proxy_put_namespaced_service) | **PUT** /api/v1/proxy/namespaces/{namespace}/services/{name} | proxy PUT requests to Service
[**proxy_put_namespaced_service_0**](ApiV1.md#proxy_put_namespaced_service_0) | **PUT** /api/v1/proxy/namespaces/{namespace}/services/{name}/{path} | proxy PUT requests to Service
[**put_namespaced_node_proxy**](ApiV1.md#put_namespaced_node_proxy) | **PUT** /api/v1/nodes/{name}/proxy | connect PUT requests to proxy of Node
[**put_namespaced_node_proxy_0**](ApiV1.md#put_namespaced_node_proxy_0) | **PUT** /api/v1/nodes/{name}/proxy/{path} | connect PUT requests to proxy of Node
[**put_namespaced_pod_proxy**](ApiV1.md#put_namespaced_pod_proxy) | **PUT** /api/v1/namespaces/{namespace}/pods/{name}/proxy | connect PUT requests to proxy of Pod
[**put_namespaced_pod_proxy_0**](ApiV1.md#put_namespaced_pod_proxy_0) | **PUT** /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path} | connect PUT requests to proxy of Pod
[**put_namespaced_service_proxy**](ApiV1.md#put_namespaced_service_proxy) | **PUT** /api/v1/namespaces/{namespace}/services/{name}/proxy | connect PUT requests to proxy of Service
[**put_namespaced_service_proxy_0**](ApiV1.md#put_namespaced_service_proxy_0) | **PUT** /api/v1/namespaces/{namespace}/services/{name}/proxy/{path} | connect PUT requests to proxy of Service
[**read_namespaced_component_status**](ApiV1.md#read_namespaced_component_status) | **GET** /api/v1/componentstatuses/{name} | read the specified ComponentStatus
[**read_namespaced_config_map**](ApiV1.md#read_namespaced_config_map) | **GET** /api/v1/namespaces/{namespace}/configmaps/{name} | read the specified ConfigMap
[**read_namespaced_endpoints**](ApiV1.md#read_namespaced_endpoints) | **GET** /api/v1/namespaces/{namespace}/endpoints/{name} | read the specified Endpoints
[**read_namespaced_event**](ApiV1.md#read_namespaced_event) | **GET** /api/v1/namespaces/{namespace}/events/{name} | read the specified Event
[**read_namespaced_limit_range**](ApiV1.md#read_namespaced_limit_range) | **GET** /api/v1/namespaces/{namespace}/limitranges/{name} | read the specified LimitRange
[**read_namespaced_namespace**](ApiV1.md#read_namespaced_namespace) | **GET** /api/v1/namespaces/{name} | read the specified Namespace
[**read_namespaced_node**](ApiV1.md#read_namespaced_node) | **GET** /api/v1/nodes/{name} | read the specified Node
[**read_namespaced_persistent_volume**](ApiV1.md#read_namespaced_persistent_volume) | **GET** /api/v1/persistentvolumes/{name} | read the specified PersistentVolume
[**read_namespaced_persistent_volume_claim**](ApiV1.md#read_namespaced_persistent_volume_claim) | **GET** /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name} | read the specified PersistentVolumeClaim
[**read_namespaced_pod**](ApiV1.md#read_namespaced_pod) | **GET** /api/v1/namespaces/{namespace}/pods/{name} | read the specified Pod
[**read_namespaced_pod_log**](ApiV1.md#read_namespaced_pod_log) | **GET** /api/v1/namespaces/{namespace}/pods/{name}/log | read log of the specified Pod
[**read_namespaced_pod_template**](ApiV1.md#read_namespaced_pod_template) | **GET** /api/v1/namespaces/{namespace}/podtemplates/{name} | read the specified PodTemplate
[**read_namespaced_replication_controller**](ApiV1.md#read_namespaced_replication_controller) | **GET** /api/v1/namespaces/{namespace}/replicationcontrollers/{name} | read the specified ReplicationController
[**read_namespaced_resource_quota**](ApiV1.md#read_namespaced_resource_quota) | **GET** /api/v1/namespaces/{namespace}/resourcequotas/{name} | read the specified ResourceQuota
[**read_namespaced_scale_scale**](ApiV1.md#read_namespaced_scale_scale) | **GET** /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale | read scale of the specified Scale
[**read_namespaced_secret**](ApiV1.md#read_namespaced_secret) | **GET** /api/v1/namespaces/{namespace}/secrets/{name} | read the specified Secret
[**read_namespaced_security_context_constraints**](ApiV1.md#read_namespaced_security_context_constraints) | **GET** /api/v1/securitycontextconstraints/{name} | read the specified SecurityContextConstraints
[**read_namespaced_service**](ApiV1.md#read_namespaced_service) | **GET** /api/v1/namespaces/{namespace}/services/{name} | read the specified Service
[**read_namespaced_service_account**](ApiV1.md#read_namespaced_service_account) | **GET** /api/v1/namespaces/{namespace}/serviceaccounts/{name} | read the specified ServiceAccount
[**replace_namespaced_config_map**](ApiV1.md#replace_namespaced_config_map) | **PUT** /api/v1/namespaces/{namespace}/configmaps/{name} | replace the specified ConfigMap
[**replace_namespaced_endpoints**](ApiV1.md#replace_namespaced_endpoints) | **PUT** /api/v1/namespaces/{namespace}/endpoints/{name} | replace the specified Endpoints
[**replace_namespaced_event**](ApiV1.md#replace_namespaced_event) | **PUT** /api/v1/namespaces/{namespace}/events/{name} | replace the specified Event
[**replace_namespaced_limit_range**](ApiV1.md#replace_namespaced_limit_range) | **PUT** /api/v1/namespaces/{namespace}/limitranges/{name} | replace the specified LimitRange
[**replace_namespaced_namespace**](ApiV1.md#replace_namespaced_namespace) | **PUT** /api/v1/namespaces/{name} | replace the specified Namespace
[**replace_namespaced_namespace_finalize**](ApiV1.md#replace_namespaced_namespace_finalize) | **PUT** /api/v1/namespaces/{name}/finalize | replace finalize of the specified Namespace
[**replace_namespaced_namespace_status**](ApiV1.md#replace_namespaced_namespace_status) | **PUT** /api/v1/namespaces/{name}/status | replace status of the specified Namespace
[**replace_namespaced_node**](ApiV1.md#replace_namespaced_node) | **PUT** /api/v1/nodes/{name} | replace the specified Node
[**replace_namespaced_node_status**](ApiV1.md#replace_namespaced_node_status) | **PUT** /api/v1/nodes/{name}/status | replace status of the specified Node
[**replace_namespaced_persistent_volume**](ApiV1.md#replace_namespaced_persistent_volume) | **PUT** /api/v1/persistentvolumes/{name} | replace the specified PersistentVolume
[**replace_namespaced_persistent_volume_claim**](ApiV1.md#replace_namespaced_persistent_volume_claim) | **PUT** /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name} | replace the specified PersistentVolumeClaim
[**replace_namespaced_persistent_volume_claim_status**](ApiV1.md#replace_namespaced_persistent_volume_claim_status) | **PUT** /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status | replace status of the specified PersistentVolumeClaim
[**replace_namespaced_persistent_volume_status**](ApiV1.md#replace_namespaced_persistent_volume_status) | **PUT** /api/v1/persistentvolumes/{name}/status | replace status of the specified PersistentVolume
[**replace_namespaced_pod**](ApiV1.md#replace_namespaced_pod) | **PUT** /api/v1/namespaces/{namespace}/pods/{name} | replace the specified Pod
[**replace_namespaced_pod_status**](ApiV1.md#replace_namespaced_pod_status) | **PUT** /api/v1/namespaces/{namespace}/pods/{name}/status | replace status of the specified Pod
[**replace_namespaced_pod_template**](ApiV1.md#replace_namespaced_pod_template) | **PUT** /api/v1/namespaces/{namespace}/podtemplates/{name} | replace the specified PodTemplate
[**replace_namespaced_replication_controller**](ApiV1.md#replace_namespaced_replication_controller) | **PUT** /api/v1/namespaces/{namespace}/replicationcontrollers/{name} | replace the specified ReplicationController
[**replace_namespaced_replication_controller_status**](ApiV1.md#replace_namespaced_replication_controller_status) | **PUT** /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status | replace status of the specified ReplicationController
[**replace_namespaced_resource_quota**](ApiV1.md#replace_namespaced_resource_quota) | **PUT** /api/v1/namespaces/{namespace}/resourcequotas/{name} | replace the specified ResourceQuota
[**replace_namespaced_resource_quota_status**](ApiV1.md#replace_namespaced_resource_quota_status) | **PUT** /api/v1/namespaces/{namespace}/resourcequotas/{name}/status | replace status of the specified ResourceQuota
[**replace_namespaced_scale_scale**](ApiV1.md#replace_namespaced_scale_scale) | **PUT** /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale | replace scale of the specified Scale
[**replace_namespaced_secret**](ApiV1.md#replace_namespaced_secret) | **PUT** /api/v1/namespaces/{namespace}/secrets/{name} | replace the specified Secret
[**replace_namespaced_security_context_constraints**](ApiV1.md#replace_namespaced_security_context_constraints) | **PUT** /api/v1/securitycontextconstraints/{name} | replace the specified SecurityContextConstraints
[**replace_namespaced_service**](ApiV1.md#replace_namespaced_service) | **PUT** /api/v1/namespaces/{namespace}/services/{name} | replace the specified Service
[**replace_namespaced_service_account**](ApiV1.md#replace_namespaced_service_account) | **PUT** /api/v1/namespaces/{namespace}/serviceaccounts/{name} | replace the specified ServiceAccount
[**replace_namespaced_service_status**](ApiV1.md#replace_namespaced_service_status) | **PUT** /api/v1/namespaces/{namespace}/services/{name}/status | replace status of the specified Service
[**watch_config_map_list**](ApiV1.md#watch_config_map_list) | **GET** /api/v1/watch/configmaps | watch individual changes to a list of ConfigMap
[**watch_endpoints_list**](ApiV1.md#watch_endpoints_list) | **GET** /api/v1/watch/endpoints | watch individual changes to a list of Endpoints
[**watch_event_list**](ApiV1.md#watch_event_list) | **GET** /api/v1/watch/events | watch individual changes to a list of Event
[**watch_limit_range_list**](ApiV1.md#watch_limit_range_list) | **GET** /api/v1/watch/limitranges | watch individual changes to a list of LimitRange
[**watch_namespaced_config_map**](ApiV1.md#watch_namespaced_config_map) | **GET** /api/v1/watch/namespaces/{namespace}/configmaps/{name} | watch changes to an object of kind ConfigMap
[**watch_namespaced_config_map_list**](ApiV1.md#watch_namespaced_config_map_list) | **GET** /api/v1/watch/namespaces/{namespace}/configmaps | watch individual changes to a list of ConfigMap
[**watch_namespaced_endpoints**](ApiV1.md#watch_namespaced_endpoints) | **GET** /api/v1/watch/namespaces/{namespace}/endpoints/{name} | watch changes to an object of kind Endpoints
[**watch_namespaced_endpoints_list**](ApiV1.md#watch_namespaced_endpoints_list) | **GET** /api/v1/watch/namespaces/{namespace}/endpoints | watch individual changes to a list of Endpoints
[**watch_namespaced_event**](ApiV1.md#watch_namespaced_event) | **GET** /api/v1/watch/namespaces/{namespace}/events/{name} | watch changes to an object of kind Event
[**watch_namespaced_event_list**](ApiV1.md#watch_namespaced_event_list) | **GET** /api/v1/watch/namespaces/{namespace}/events | watch individual changes to a list of Event
[**watch_namespaced_limit_range**](ApiV1.md#watch_namespaced_limit_range) | **GET** /api/v1/watch/namespaces/{namespace}/limitranges/{name} | watch changes to an object of kind LimitRange
[**watch_namespaced_limit_range_list**](ApiV1.md#watch_namespaced_limit_range_list) | **GET** /api/v1/watch/namespaces/{namespace}/limitranges | watch individual changes to a list of LimitRange
[**watch_namespaced_namespace**](ApiV1.md#watch_namespaced_namespace) | **GET** /api/v1/watch/namespaces/{name} | watch changes to an object of kind Namespace
[**watch_namespaced_namespace_list**](ApiV1.md#watch_namespaced_namespace_list) | **GET** /api/v1/watch/namespaces | watch individual changes to a list of Namespace
[**watch_namespaced_node**](ApiV1.md#watch_namespaced_node) | **GET** /api/v1/watch/nodes/{name} | watch changes to an object of kind Node
[**watch_namespaced_node_list**](ApiV1.md#watch_namespaced_node_list) | **GET** /api/v1/watch/nodes | watch individual changes to a list of Node
[**watch_namespaced_persistent_volume**](ApiV1.md#watch_namespaced_persistent_volume) | **GET** /api/v1/watch/persistentvolumes/{name} | watch changes to an object of kind PersistentVolume
[**watch_namespaced_persistent_volume_claim**](ApiV1.md#watch_namespaced_persistent_volume_claim) | **GET** /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name} | watch changes to an object of kind PersistentVolumeClaim
[**watch_namespaced_persistent_volume_claim_list**](ApiV1.md#watch_namespaced_persistent_volume_claim_list) | **GET** /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims | watch individual changes to a list of PersistentVolumeClaim
[**watch_namespaced_persistent_volume_list**](ApiV1.md#watch_namespaced_persistent_volume_list) | **GET** /api/v1/watch/persistentvolumes | watch individual changes to a list of PersistentVolume
[**watch_namespaced_pod**](ApiV1.md#watch_namespaced_pod) | **GET** /api/v1/watch/namespaces/{namespace}/pods/{name} | watch changes to an object of kind Pod
[**watch_namespaced_pod_list**](ApiV1.md#watch_namespaced_pod_list) | **GET** /api/v1/watch/namespaces/{namespace}/pods | watch individual changes to a list of Pod
[**watch_namespaced_pod_template**](ApiV1.md#watch_namespaced_pod_template) | **GET** /api/v1/watch/namespaces/{namespace}/podtemplates/{name} | watch changes to an object of kind PodTemplate
[**watch_namespaced_pod_template_list**](ApiV1.md#watch_namespaced_pod_template_list) | **GET** /api/v1/watch/namespaces/{namespace}/podtemplates | watch individual changes to a list of PodTemplate
[**watch_namespaced_replication_controller**](ApiV1.md#watch_namespaced_replication_controller) | **GET** /api/v1/watch/namespaces/{namespace}/replicationcontrollers/{name} | watch changes to an object of kind ReplicationController
[**watch_namespaced_replication_controller_list**](ApiV1.md#watch_namespaced_replication_controller_list) | **GET** /api/v1/watch/namespaces/{namespace}/replicationcontrollers | watch individual changes to a list of ReplicationController
[**watch_namespaced_resource_quota**](ApiV1.md#watch_namespaced_resource_quota) | **GET** /api/v1/watch/namespaces/{namespace}/resourcequotas/{name} | watch changes to an object of kind ResourceQuota
[**watch_namespaced_resource_quota_list**](ApiV1.md#watch_namespaced_resource_quota_list) | **GET** /api/v1/watch/namespaces/{namespace}/resourcequotas | watch individual changes to a list of ResourceQuota
[**watch_namespaced_secret**](ApiV1.md#watch_namespaced_secret) | **GET** /api/v1/watch/namespaces/{namespace}/secrets/{name} | watch changes to an object of kind Secret
[**watch_namespaced_secret_list**](ApiV1.md#watch_namespaced_secret_list) | **GET** /api/v1/watch/namespaces/{namespace}/secrets | watch individual changes to a list of Secret
[**watch_namespaced_security_context_constraints**](ApiV1.md#watch_namespaced_security_context_constraints) | **GET** /api/v1/watch/securitycontextconstraints/{name} | watch changes to an object of kind SecurityContextConstraints
[**watch_namespaced_security_context_constraints_list**](ApiV1.md#watch_namespaced_security_context_constraints_list) | **GET** /api/v1/watch/securitycontextconstraints | watch individual changes to a list of SecurityContextConstraints
[**watch_namespaced_service**](ApiV1.md#watch_namespaced_service) | **GET** /api/v1/watch/namespaces/{namespace}/services/{name} | watch changes to an object of kind Service
[**watch_namespaced_service_account**](ApiV1.md#watch_namespaced_service_account) | **GET** /api/v1/watch/namespaces/{namespace}/serviceaccounts/{name} | watch changes to an object of kind ServiceAccount
[**watch_namespaced_service_account_list**](ApiV1.md#watch_namespaced_service_account_list) | **GET** /api/v1/watch/namespaces/{namespace}/serviceaccounts | watch individual changes to a list of ServiceAccount
[**watch_namespaced_service_list**](ApiV1.md#watch_namespaced_service_list) | **GET** /api/v1/watch/namespaces/{namespace}/services | watch individual changes to a list of Service
[**watch_persistent_volume_claim_list**](ApiV1.md#watch_persistent_volume_claim_list) | **GET** /api/v1/watch/persistentvolumeclaims | watch individual changes to a list of PersistentVolumeClaim
[**watch_pod_list**](ApiV1.md#watch_pod_list) | **GET** /api/v1/watch/pods | watch individual changes to a list of Pod
[**watch_pod_template_list**](ApiV1.md#watch_pod_template_list) | **GET** /api/v1/watch/podtemplates | watch individual changes to a list of PodTemplate
[**watch_replication_controller_list**](ApiV1.md#watch_replication_controller_list) | **GET** /api/v1/watch/replicationcontrollers | watch individual changes to a list of ReplicationController
[**watch_resource_quota_list**](ApiV1.md#watch_resource_quota_list) | **GET** /api/v1/watch/resourcequotas | watch individual changes to a list of ResourceQuota
[**watch_secret_list**](ApiV1.md#watch_secret_list) | **GET** /api/v1/watch/secrets | watch individual changes to a list of Secret
[**watch_service_account_list**](ApiV1.md#watch_service_account_list) | **GET** /api/v1/watch/serviceaccounts | watch individual changes to a list of ServiceAccount
[**watch_service_list**](ApiV1.md#watch_service_list) | **GET** /api/v1/watch/services | watch individual changes to a list of Service


# **create_binding**
> V1Binding create_binding(body, pretty=pretty)

create a Binding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Binding() # V1Binding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Binding
    api_response = api_instance.create_binding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Binding**](V1Binding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Binding**](V1Binding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_config_map**
> V1ConfigMap create_config_map(body, pretty=pretty)

create a ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ConfigMap() # V1ConfigMap | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ConfigMap
    api_response = api_instance.create_config_map(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ConfigMap**](V1ConfigMap.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ConfigMap**](V1ConfigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoints**
> V1Endpoints create_endpoints(body, pretty=pretty)

create a Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Endpoints() # V1Endpoints | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Endpoints
    api_response = api_instance.create_endpoints(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Endpoints**](V1Endpoints.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Endpoints**](V1Endpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event**
> V1Event create_event(body, pretty=pretty)

create a Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Event() # V1Event | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Event
    api_response = api_instance.create_event(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Event**](V1Event.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Event**](V1Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_limit_range**
> V1LimitRange create_limit_range(body, pretty=pretty)

create a LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1LimitRange() # V1LimitRange | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LimitRange
    api_response = api_instance.create_limit_range(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LimitRange**](V1LimitRange.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LimitRange**](V1LimitRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_binding**
> V1Binding create_namespaced_binding(body, namespace, pretty=pretty)

create a Binding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Binding() # V1Binding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Binding
    api_response = api_instance.create_namespaced_binding(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Binding**](V1Binding.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Binding**](V1Binding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_binding_binding**
> V1Binding create_namespaced_binding_binding(body, namespace, name, pretty=pretty)

create binding of a Binding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Binding() # V1Binding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Binding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create binding of a Binding
    api_response = api_instance.create_namespaced_binding_binding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_binding_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Binding**](V1Binding.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Binding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Binding**](V1Binding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_config_map**
> V1ConfigMap create_namespaced_config_map(body, namespace, pretty=pretty)

create a ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ConfigMap() # V1ConfigMap | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ConfigMap
    api_response = api_instance.create_namespaced_config_map(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ConfigMap**](V1ConfigMap.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ConfigMap**](V1ConfigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_endpoints**
> V1Endpoints create_namespaced_endpoints(body, namespace, pretty=pretty)

create a Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Endpoints() # V1Endpoints | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Endpoints
    api_response = api_instance.create_namespaced_endpoints(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Endpoints**](V1Endpoints.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Endpoints**](V1Endpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_event**
> V1Event create_namespaced_event(body, namespace, pretty=pretty)

create a Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Event() # V1Event | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Event
    api_response = api_instance.create_namespaced_event(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Event**](V1Event.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Event**](V1Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_limit_range**
> V1LimitRange create_namespaced_limit_range(body, namespace, pretty=pretty)

create a LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1LimitRange() # V1LimitRange | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LimitRange
    api_response = api_instance.create_namespaced_limit_range(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LimitRange**](V1LimitRange.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LimitRange**](V1LimitRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_namespace**
> V1Namespace create_namespaced_namespace(body, pretty=pretty)

create a Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Namespace() # V1Namespace | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Namespace
    api_response = api_instance.create_namespaced_namespace(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Namespace**](V1Namespace.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Namespace**](V1Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_node**
> V1Node create_namespaced_node(body, pretty=pretty)

create a Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Node() # V1Node | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Node
    api_response = api_instance.create_namespaced_node(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Node**](V1Node.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Node**](V1Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_persistent_volume**
> V1PersistentVolume create_namespaced_persistent_volume(body, pretty=pretty)

create a PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PersistentVolume() # V1PersistentVolume | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PersistentVolume
    api_response = api_instance.create_namespaced_persistent_volume(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PersistentVolume**](V1PersistentVolume.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolume**](V1PersistentVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_persistent_volume_claim**
> V1PersistentVolumeClaim create_namespaced_persistent_volume_claim(body, namespace, pretty=pretty)

create a PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PersistentVolumeClaim() # V1PersistentVolumeClaim | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PersistentVolumeClaim
    api_response = api_instance.create_namespaced_persistent_volume_claim(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_pod**
> V1Pod create_namespaced_pod(body, namespace, pretty=pretty)

create a Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Pod() # V1Pod | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Pod
    api_response = api_instance.create_namespaced_pod(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Pod**](V1Pod.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Pod**](V1Pod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_pod_template**
> V1PodTemplate create_namespaced_pod_template(body, namespace, pretty=pretty)

create a PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PodTemplate() # V1PodTemplate | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PodTemplate
    api_response = api_instance.create_namespaced_pod_template(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodTemplate**](V1PodTemplate.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodTemplate**](V1PodTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_replication_controller**
> V1ReplicationController create_namespaced_replication_controller(body, namespace, pretty=pretty)

create a ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ReplicationController() # V1ReplicationController | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ReplicationController
    api_response = api_instance.create_namespaced_replication_controller(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ReplicationController**](V1ReplicationController.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ReplicationController**](V1ReplicationController.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_resource_quota**
> V1ResourceQuota create_namespaced_resource_quota(body, namespace, pretty=pretty)

create a ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ResourceQuota() # V1ResourceQuota | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ResourceQuota
    api_response = api_instance.create_namespaced_resource_quota(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ResourceQuota**](V1ResourceQuota.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ResourceQuota**](V1ResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_secret**
> V1Secret create_namespaced_secret(body, namespace, pretty=pretty)

create a Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Secret() # V1Secret | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Secret
    api_response = api_instance.create_namespaced_secret(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Secret**](V1Secret.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Secret**](V1Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_security_context_constraints**
> V1SecurityContextConstraints create_namespaced_security_context_constraints(body, pretty=pretty)

create a SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1SecurityContextConstraints() # V1SecurityContextConstraints | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a SecurityContextConstraints
    api_response = api_instance.create_namespaced_security_context_constraints(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SecurityContextConstraints**](V1SecurityContextConstraints.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SecurityContextConstraints**](V1SecurityContextConstraints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_service**
> V1Service create_namespaced_service(body, namespace, pretty=pretty)

create a Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Service() # V1Service | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Service
    api_response = api_instance.create_namespaced_service(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Service**](V1Service.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Service**](V1Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_service_account**
> V1ServiceAccount create_namespaced_service_account(body, namespace, pretty=pretty)

create a ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ServiceAccount() # V1ServiceAccount | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ServiceAccount
    api_response = api_instance.create_namespaced_service_account(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ServiceAccount**](V1ServiceAccount.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ServiceAccount**](V1ServiceAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_persistent_volume_claim**
> V1PersistentVolumeClaim create_persistent_volume_claim(body, pretty=pretty)

create a PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PersistentVolumeClaim() # V1PersistentVolumeClaim | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PersistentVolumeClaim
    api_response = api_instance.create_persistent_volume_claim(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pod**
> V1Pod create_pod(body, pretty=pretty)

create a Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Pod() # V1Pod | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Pod
    api_response = api_instance.create_pod(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Pod**](V1Pod.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Pod**](V1Pod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pod_template**
> V1PodTemplate create_pod_template(body, pretty=pretty)

create a PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PodTemplate() # V1PodTemplate | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PodTemplate
    api_response = api_instance.create_pod_template(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodTemplate**](V1PodTemplate.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodTemplate**](V1PodTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_replication_controller**
> V1ReplicationController create_replication_controller(body, pretty=pretty)

create a ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ReplicationController() # V1ReplicationController | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ReplicationController
    api_response = api_instance.create_replication_controller(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ReplicationController**](V1ReplicationController.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ReplicationController**](V1ReplicationController.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resource_quota**
> V1ResourceQuota create_resource_quota(body, pretty=pretty)

create a ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ResourceQuota() # V1ResourceQuota | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ResourceQuota
    api_response = api_instance.create_resource_quota(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ResourceQuota**](V1ResourceQuota.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ResourceQuota**](V1ResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret**
> V1Secret create_secret(body, pretty=pretty)

create a Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Secret() # V1Secret | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Secret
    api_response = api_instance.create_secret(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Secret**](V1Secret.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Secret**](V1Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service**
> V1Service create_service(body, pretty=pretty)

create a Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Service() # V1Service | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Service
    api_response = api_instance.create_service(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Service**](V1Service.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Service**](V1Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account**
> V1ServiceAccount create_service_account(body, pretty=pretty)

create a ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ServiceAccount() # V1ServiceAccount | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ServiceAccount
    api_response = api_instance.create_service_account(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->create_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ServiceAccount**](V1ServiceAccount.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ServiceAccount**](V1ServiceAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_config_map**
> UnversionedStatus delete_namespaced_config_map(body, namespace, name, pretty=pretty)

delete a ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ConfigMap
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ConfigMap
    api_response = api_instance.delete_namespaced_config_map(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ConfigMap | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_endpoints**
> UnversionedStatus delete_namespaced_endpoints(body, namespace, name, pretty=pretty)

delete a Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Endpoints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Endpoints
    api_response = api_instance.delete_namespaced_endpoints(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Endpoints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_event**
> UnversionedStatus delete_namespaced_event(body, namespace, name, pretty=pretty)

delete a Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Event
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Event
    api_response = api_instance.delete_namespaced_event(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Event | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_limit_range**
> UnversionedStatus delete_namespaced_limit_range(body, namespace, name, pretty=pretty)

delete a LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the LimitRange
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a LimitRange
    api_response = api_instance.delete_namespaced_limit_range(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the LimitRange | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_namespace**
> UnversionedStatus delete_namespaced_namespace(body, name, pretty=pretty)

delete a Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Namespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Namespace
    api_response = api_instance.delete_namespaced_namespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the Namespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_node**
> UnversionedStatus delete_namespaced_node(body, name, pretty=pretty)

delete a Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Node
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Node
    api_response = api_instance.delete_namespaced_node(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the Node | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_node_proxy**
> str delete_namespaced_node_proxy(name, path=path)

connect DELETE requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect DELETE requests to proxy of Node
    api_response = api_instance.delete_namespaced_node_proxy(name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_node_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_node_proxy_0**
> str delete_namespaced_node_proxy_0(name, path2, path=path)

connect DELETE requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect DELETE requests to proxy of Node
    api_response = api_instance.delete_namespaced_node_proxy_0(name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_node_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_persistent_volume**
> UnversionedStatus delete_namespaced_persistent_volume(body, name, pretty=pretty)

delete a PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the PersistentVolume
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a PersistentVolume
    api_response = api_instance.delete_namespaced_persistent_volume(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the PersistentVolume | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_persistent_volume_claim**
> UnversionedStatus delete_namespaced_persistent_volume_claim(body, namespace, name, pretty=pretty)

delete a PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PersistentVolumeClaim
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a PersistentVolumeClaim
    api_response = api_instance.delete_namespaced_persistent_volume_claim(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PersistentVolumeClaim | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_pod**
> UnversionedStatus delete_namespaced_pod(body, namespace, name, pretty=pretty)

delete a Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Pod
    api_response = api_instance.delete_namespaced_pod(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_pod_proxy**
> str delete_namespaced_pod_proxy(namespace, name, path=path)

connect DELETE requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect DELETE requests to proxy of Pod
    api_response = api_instance.delete_namespaced_pod_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_pod_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_pod_proxy_0**
> str delete_namespaced_pod_proxy_0(namespace, name, path2, path=path)

connect DELETE requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect DELETE requests to proxy of Pod
    api_response = api_instance.delete_namespaced_pod_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_pod_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_pod_template**
> UnversionedStatus delete_namespaced_pod_template(body, namespace, name, pretty=pretty)

delete a PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PodTemplate
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a PodTemplate
    api_response = api_instance.delete_namespaced_pod_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PodTemplate | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_replication_controller**
> UnversionedStatus delete_namespaced_replication_controller(body, namespace, name, pretty=pretty)

delete a ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicationController
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ReplicationController
    api_response = api_instance.delete_namespaced_replication_controller(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicationController | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_resource_quota**
> UnversionedStatus delete_namespaced_resource_quota(body, namespace, name, pretty=pretty)

delete a ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ResourceQuota
    api_response = api_instance.delete_namespaced_resource_quota(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_secret**
> UnversionedStatus delete_namespaced_secret(body, namespace, name, pretty=pretty)

delete a Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Secret
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Secret
    api_response = api_instance.delete_namespaced_secret(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Secret | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_security_context_constraints**
> UnversionedStatus delete_namespaced_security_context_constraints(body, name, pretty=pretty)

delete a SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the SecurityContextConstraints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a SecurityContextConstraints
    api_response = api_instance.delete_namespaced_security_context_constraints(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the SecurityContextConstraints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_service**
> UnversionedStatus delete_namespaced_service(namespace, name, pretty=pretty)

delete a Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Service
    api_response = api_instance.delete_namespaced_service(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_service_account**
> UnversionedStatus delete_namespaced_service_account(body, namespace, name, pretty=pretty)

delete a ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ServiceAccount
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ServiceAccount
    api_response = api_instance.delete_namespaced_service_account(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ServiceAccount | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_service_proxy**
> str delete_namespaced_service_proxy(namespace, name, path=path)

connect DELETE requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect DELETE requests to proxy of Service
    api_response = api_instance.delete_namespaced_service_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_service_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_service_proxy_0**
> str delete_namespaced_service_proxy_0(namespace, name, path2, path=path)

connect DELETE requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect DELETE requests to proxy of Service
    api_response = api_instance.delete_namespaced_service_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->delete_namespaced_service_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_config_map**
> UnversionedStatus deletecollection_namespaced_config_map(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ConfigMap
    api_response = api_instance.deletecollection_namespaced_config_map(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_endpoints**
> UnversionedStatus deletecollection_namespaced_endpoints(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Endpoints
    api_response = api_instance.deletecollection_namespaced_endpoints(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_event**
> UnversionedStatus deletecollection_namespaced_event(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Event
    api_response = api_instance.deletecollection_namespaced_event(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_limit_range**
> UnversionedStatus deletecollection_namespaced_limit_range(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of LimitRange
    api_response = api_instance.deletecollection_namespaced_limit_range(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_namespace**
> UnversionedStatus deletecollection_namespaced_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Namespace
    api_response = api_instance.deletecollection_namespaced_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_node**
> UnversionedStatus deletecollection_namespaced_node(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Node
    api_response = api_instance.deletecollection_namespaced_node(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_persistent_volume**
> UnversionedStatus deletecollection_namespaced_persistent_volume(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of PersistentVolume
    api_response = api_instance.deletecollection_namespaced_persistent_volume(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_persistent_volume_claim**
> UnversionedStatus deletecollection_namespaced_persistent_volume_claim(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of PersistentVolumeClaim
    api_response = api_instance.deletecollection_namespaced_persistent_volume_claim(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_pod**
> UnversionedStatus deletecollection_namespaced_pod(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Pod
    api_response = api_instance.deletecollection_namespaced_pod(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_pod_template**
> UnversionedStatus deletecollection_namespaced_pod_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of PodTemplate
    api_response = api_instance.deletecollection_namespaced_pod_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_replication_controller**
> UnversionedStatus deletecollection_namespaced_replication_controller(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ReplicationController
    api_response = api_instance.deletecollection_namespaced_replication_controller(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_resource_quota**
> UnversionedStatus deletecollection_namespaced_resource_quota(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ResourceQuota
    api_response = api_instance.deletecollection_namespaced_resource_quota(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_secret**
> UnversionedStatus deletecollection_namespaced_secret(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Secret
    api_response = api_instance.deletecollection_namespaced_secret(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_security_context_constraints**
> UnversionedStatus deletecollection_namespaced_security_context_constraints(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of SecurityContextConstraints
    api_response = api_instance.deletecollection_namespaced_security_context_constraints(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_service_account**
> UnversionedStatus deletecollection_namespaced_service_account(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ServiceAccount
    api_response = api_instance.deletecollection_namespaced_service_account(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->deletecollection_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> get_api_resources()

get available resources

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()

try: 
    # get available resources
    api_instance.get_api_resources()
except ApiException as e:
    print "Exception when calling ApiV1->get_api_resources: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_node_proxy**
> str get_namespaced_node_proxy(name, path=path)

connect GET requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect GET requests to proxy of Node
    api_response = api_instance.get_namespaced_node_proxy(name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_node_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_node_proxy_0**
> str get_namespaced_node_proxy_0(name, path2, path=path)

connect GET requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect GET requests to proxy of Node
    api_response = api_instance.get_namespaced_node_proxy_0(name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_node_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_pod_attach**
> str get_namespaced_pod_attach(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container)

connect GET requests to attach of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
stdin = true # bool | Stdin if true, redirects the standard input stream of the pod for this call. Defaults to false. (optional)
stdout = true # bool | Stdout if true indicates that stdout is to be redirected for the attach call. Defaults to true. (optional)
stderr = true # bool | Stderr if true indicates that stderr is to be redirected for the attach call. Defaults to true. (optional)
tty = true # bool | TTY if true indicates that a tty will be allocated for the attach call. This is passed through the container runtime so the tty is allocated on the worker node by the container runtime. Defaults to false. (optional)
container = 'container_example' # str | The container in which to execute the command. Defaults to only container if there is only one container in the pod. (optional)

try: 
    # connect GET requests to attach of Pod
    api_response = api_instance.get_namespaced_pod_attach(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_pod_attach: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **stdin** | **bool**| Stdin if true, redirects the standard input stream of the pod for this call. Defaults to false. | [optional] 
 **stdout** | **bool**| Stdout if true indicates that stdout is to be redirected for the attach call. Defaults to true. | [optional] 
 **stderr** | **bool**| Stderr if true indicates that stderr is to be redirected for the attach call. Defaults to true. | [optional] 
 **tty** | **bool**| TTY if true indicates that a tty will be allocated for the attach call. This is passed through the container runtime so the tty is allocated on the worker node by the container runtime. Defaults to false. | [optional] 
 **container** | **str**| The container in which to execute the command. Defaults to only container if there is only one container in the pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_pod_exec**
> str get_namespaced_pod_exec(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container, command=command)

connect GET requests to exec of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
stdin = true # bool | Redirect the standard input stream of the pod for this call. Defaults to false. (optional)
stdout = true # bool | Redirect the standard output stream of the pod for this call. Defaults to true. (optional)
stderr = true # bool | Redirect the standard error stream of the pod for this call. Defaults to true. (optional)
tty = true # bool | TTY if true indicates that a tty will be allocated for the exec call. Defaults to false. (optional)
container = 'container_example' # str | Container in which to execute the command. Defaults to only container if there is only one container in the pod. (optional)
command = 'command_example' # str | Command is the remote command to execute. argv array. Not executed within a shell. (optional)

try: 
    # connect GET requests to exec of Pod
    api_response = api_instance.get_namespaced_pod_exec(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container, command=command)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_pod_exec: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **stdin** | **bool**| Redirect the standard input stream of the pod for this call. Defaults to false. | [optional] 
 **stdout** | **bool**| Redirect the standard output stream of the pod for this call. Defaults to true. | [optional] 
 **stderr** | **bool**| Redirect the standard error stream of the pod for this call. Defaults to true. | [optional] 
 **tty** | **bool**| TTY if true indicates that a tty will be allocated for the exec call. Defaults to false. | [optional] 
 **container** | **str**| Container in which to execute the command. Defaults to only container if there is only one container in the pod. | [optional] 
 **command** | **str**| Command is the remote command to execute. argv array. Not executed within a shell. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_pod_portforward**
> str get_namespaced_pod_portforward(namespace, name)

connect GET requests to portforward of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # connect GET requests to portforward of Pod
    api_response = api_instance.get_namespaced_pod_portforward(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_pod_portforward: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_pod_proxy**
> str get_namespaced_pod_proxy(namespace, name, path=path)

connect GET requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect GET requests to proxy of Pod
    api_response = api_instance.get_namespaced_pod_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_pod_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_pod_proxy_0**
> str get_namespaced_pod_proxy_0(namespace, name, path2, path=path)

connect GET requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect GET requests to proxy of Pod
    api_response = api_instance.get_namespaced_pod_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_pod_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_service_proxy**
> str get_namespaced_service_proxy(namespace, name, path=path)

connect GET requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect GET requests to proxy of Service
    api_response = api_instance.get_namespaced_service_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_service_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_service_proxy_0**
> str get_namespaced_service_proxy_0(namespace, name, path2, path=path)

connect GET requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect GET requests to proxy of Service
    api_response = api_instance.get_namespaced_service_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->get_namespaced_service_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_namespaced_node_proxy**
> str head_namespaced_node_proxy(name, path=path)

connect HEAD requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect HEAD requests to proxy of Node
    api_response = api_instance.head_namespaced_node_proxy(name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->head_namespaced_node_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_namespaced_node_proxy_0**
> str head_namespaced_node_proxy_0(name, path2, path=path)

connect HEAD requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect HEAD requests to proxy of Node
    api_response = api_instance.head_namespaced_node_proxy_0(name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->head_namespaced_node_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_namespaced_pod_proxy**
> str head_namespaced_pod_proxy(namespace, name, path=path)

connect HEAD requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect HEAD requests to proxy of Pod
    api_response = api_instance.head_namespaced_pod_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->head_namespaced_pod_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_namespaced_pod_proxy_0**
> str head_namespaced_pod_proxy_0(namespace, name, path2, path=path)

connect HEAD requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect HEAD requests to proxy of Pod
    api_response = api_instance.head_namespaced_pod_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->head_namespaced_pod_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_namespaced_service_proxy**
> str head_namespaced_service_proxy(namespace, name, path=path)

connect HEAD requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect HEAD requests to proxy of Service
    api_response = api_instance.head_namespaced_service_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->head_namespaced_service_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_namespaced_service_proxy_0**
> str head_namespaced_service_proxy_0(namespace, name, path2, path=path)

connect HEAD requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect HEAD requests to proxy of Service
    api_response = api_instance.head_namespaced_service_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->head_namespaced_service_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_map**
> V1ConfigMapList list_config_map(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ConfigMap
    api_response = api_instance.list_config_map(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ConfigMapList**](V1ConfigMapList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_endpoints**
> V1EndpointsList list_endpoints(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Endpoints
    api_response = api_instance.list_endpoints(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1EndpointsList**](V1EndpointsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event**
> V1EventList list_event(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Event
    api_response = api_instance.list_event(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1EventList**](V1EventList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_limit_range**
> V1LimitRangeList list_limit_range(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind LimitRange
    api_response = api_instance.list_limit_range(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1LimitRangeList**](V1LimitRangeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_component_status**
> V1ComponentStatusList list_namespaced_component_status(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ComponentStatus

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ComponentStatus
    api_response = api_instance.list_namespaced_component_status(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_component_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ComponentStatusList**](V1ComponentStatusList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_config_map**
> V1ConfigMapList list_namespaced_config_map(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ConfigMap
    api_response = api_instance.list_namespaced_config_map(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ConfigMapList**](V1ConfigMapList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_endpoints**
> V1EndpointsList list_namespaced_endpoints(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Endpoints
    api_response = api_instance.list_namespaced_endpoints(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1EndpointsList**](V1EndpointsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_event**
> V1EventList list_namespaced_event(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Event
    api_response = api_instance.list_namespaced_event(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1EventList**](V1EventList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_limit_range**
> V1LimitRangeList list_namespaced_limit_range(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind LimitRange
    api_response = api_instance.list_namespaced_limit_range(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1LimitRangeList**](V1LimitRangeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_namespace**
> V1NamespaceList list_namespaced_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Namespace
    api_response = api_instance.list_namespaced_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1NamespaceList**](V1NamespaceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_node**
> V1NodeList list_namespaced_node(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Node
    api_response = api_instance.list_namespaced_node(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1NodeList**](V1NodeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_persistent_volume**
> V1PersistentVolumeList list_namespaced_persistent_volume(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PersistentVolume
    api_response = api_instance.list_namespaced_persistent_volume(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1PersistentVolumeList**](V1PersistentVolumeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_persistent_volume_claim**
> V1PersistentVolumeClaimList list_namespaced_persistent_volume_claim(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PersistentVolumeClaim
    api_response = api_instance.list_namespaced_persistent_volume_claim(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1PersistentVolumeClaimList**](V1PersistentVolumeClaimList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_pod**
> V1PodList list_namespaced_pod(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Pod
    api_response = api_instance.list_namespaced_pod(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1PodList**](V1PodList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_pod_template**
> V1PodTemplateList list_namespaced_pod_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PodTemplate
    api_response = api_instance.list_namespaced_pod_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1PodTemplateList**](V1PodTemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_replication_controller**
> V1ReplicationControllerList list_namespaced_replication_controller(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ReplicationController
    api_response = api_instance.list_namespaced_replication_controller(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ReplicationControllerList**](V1ReplicationControllerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_resource_quota**
> V1ResourceQuotaList list_namespaced_resource_quota(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ResourceQuota
    api_response = api_instance.list_namespaced_resource_quota(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ResourceQuotaList**](V1ResourceQuotaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_secret**
> V1SecretList list_namespaced_secret(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Secret
    api_response = api_instance.list_namespaced_secret(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1SecretList**](V1SecretList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_security_context_constraints**
> V1SecurityContextConstraintsList list_namespaced_security_context_constraints(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind SecurityContextConstraints
    api_response = api_instance.list_namespaced_security_context_constraints(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1SecurityContextConstraintsList**](V1SecurityContextConstraintsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_service**
> V1ServiceList list_namespaced_service(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Service
    api_response = api_instance.list_namespaced_service(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ServiceList**](V1ServiceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_service_account**
> V1ServiceAccountList list_namespaced_service_account(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ServiceAccount
    api_response = api_instance.list_namespaced_service_account(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ServiceAccountList**](V1ServiceAccountList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_persistent_volume_claim**
> V1PersistentVolumeClaimList list_persistent_volume_claim(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PersistentVolumeClaim
    api_response = api_instance.list_persistent_volume_claim(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1PersistentVolumeClaimList**](V1PersistentVolumeClaimList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pod**
> V1PodList list_pod(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Pod
    api_response = api_instance.list_pod(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1PodList**](V1PodList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pod_template**
> V1PodTemplateList list_pod_template(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PodTemplate
    api_response = api_instance.list_pod_template(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1PodTemplateList**](V1PodTemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_controller**
> V1ReplicationControllerList list_replication_controller(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ReplicationController
    api_response = api_instance.list_replication_controller(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ReplicationControllerList**](V1ReplicationControllerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_quota**
> V1ResourceQuotaList list_resource_quota(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ResourceQuota
    api_response = api_instance.list_resource_quota(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ResourceQuotaList**](V1ResourceQuotaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secret**
> V1SecretList list_secret(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Secret
    api_response = api_instance.list_secret(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1SecretList**](V1SecretList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service**
> V1ServiceList list_service(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Service
    api_response = api_instance.list_service(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ServiceList**](V1ServiceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_account**
> V1ServiceAccountList list_service_account(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ServiceAccount
    api_response = api_instance.list_service_account(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->list_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1ServiceAccountList**](V1ServiceAccountList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_namespaced_node_proxy**
> str options_namespaced_node_proxy(name, path=path)

connect OPTIONS requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect OPTIONS requests to proxy of Node
    api_response = api_instance.options_namespaced_node_proxy(name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->options_namespaced_node_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_namespaced_node_proxy_0**
> str options_namespaced_node_proxy_0(name, path2, path=path)

connect OPTIONS requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect OPTIONS requests to proxy of Node
    api_response = api_instance.options_namespaced_node_proxy_0(name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->options_namespaced_node_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_namespaced_pod_proxy**
> str options_namespaced_pod_proxy(namespace, name, path=path)

connect OPTIONS requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect OPTIONS requests to proxy of Pod
    api_response = api_instance.options_namespaced_pod_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->options_namespaced_pod_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_namespaced_pod_proxy_0**
> str options_namespaced_pod_proxy_0(namespace, name, path2, path=path)

connect OPTIONS requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect OPTIONS requests to proxy of Pod
    api_response = api_instance.options_namespaced_pod_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->options_namespaced_pod_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_namespaced_service_proxy**
> str options_namespaced_service_proxy(namespace, name, path=path)

connect OPTIONS requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect OPTIONS requests to proxy of Service
    api_response = api_instance.options_namespaced_service_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->options_namespaced_service_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_namespaced_service_proxy_0**
> str options_namespaced_service_proxy_0(namespace, name, path2, path=path)

connect OPTIONS requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect OPTIONS requests to proxy of Service
    api_response = api_instance.options_namespaced_service_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->options_namespaced_service_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_config_map**
> V1ConfigMap patch_namespaced_config_map(body, namespace, name, pretty=pretty)

partially update the specified ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ConfigMap
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ConfigMap
    api_response = api_instance.patch_namespaced_config_map(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ConfigMap | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ConfigMap**](V1ConfigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_endpoints**
> V1Endpoints patch_namespaced_endpoints(body, namespace, name, pretty=pretty)

partially update the specified Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Endpoints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Endpoints
    api_response = api_instance.patch_namespaced_endpoints(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Endpoints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Endpoints**](V1Endpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_event**
> V1Event patch_namespaced_event(body, namespace, name, pretty=pretty)

partially update the specified Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Event
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Event
    api_response = api_instance.patch_namespaced_event(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Event | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Event**](V1Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_limit_range**
> V1LimitRange patch_namespaced_limit_range(body, namespace, name, pretty=pretty)

partially update the specified LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the LimitRange
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified LimitRange
    api_response = api_instance.patch_namespaced_limit_range(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the LimitRange | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LimitRange**](V1LimitRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_namespace**
> V1Namespace patch_namespaced_namespace(body, name, pretty=pretty)

partially update the specified Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Namespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Namespace
    api_response = api_instance.patch_namespaced_namespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the Namespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Namespace**](V1Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_node**
> V1Node patch_namespaced_node(body, name, pretty=pretty)

partially update the specified Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Node
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Node
    api_response = api_instance.patch_namespaced_node(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the Node | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Node**](V1Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_persistent_volume**
> V1PersistentVolume patch_namespaced_persistent_volume(body, name, pretty=pretty)

partially update the specified PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the PersistentVolume
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified PersistentVolume
    api_response = api_instance.patch_namespaced_persistent_volume(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the PersistentVolume | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolume**](V1PersistentVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_persistent_volume_claim**
> V1PersistentVolumeClaim patch_namespaced_persistent_volume_claim(body, namespace, name, pretty=pretty)

partially update the specified PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PersistentVolumeClaim
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified PersistentVolumeClaim
    api_response = api_instance.patch_namespaced_persistent_volume_claim(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PersistentVolumeClaim | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_pod**
> V1Pod patch_namespaced_pod(body, namespace, name, pretty=pretty)

partially update the specified Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Pod
    api_response = api_instance.patch_namespaced_pod(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Pod**](V1Pod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_pod_template**
> V1PodTemplate patch_namespaced_pod_template(body, namespace, name, pretty=pretty)

partially update the specified PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PodTemplate
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified PodTemplate
    api_response = api_instance.patch_namespaced_pod_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PodTemplate | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodTemplate**](V1PodTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replication_controller**
> V1ReplicationController patch_namespaced_replication_controller(body, namespace, name, pretty=pretty)

partially update the specified ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicationController
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ReplicationController
    api_response = api_instance.patch_namespaced_replication_controller(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicationController | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ReplicationController**](V1ReplicationController.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_resource_quota**
> V1ResourceQuota patch_namespaced_resource_quota(body, namespace, name, pretty=pretty)

partially update the specified ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ResourceQuota
    api_response = api_instance.patch_namespaced_resource_quota(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ResourceQuota**](V1ResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_scale_scale**
> V1Scale patch_namespaced_scale_scale(body, namespace, name, pretty=pretty)

partially update scale of the specified Scale

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update scale of the specified Scale
    api_response = api_instance.patch_namespaced_scale_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Scale**](V1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_secret**
> V1Secret patch_namespaced_secret(body, namespace, name, pretty=pretty)

partially update the specified Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Secret
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Secret
    api_response = api_instance.patch_namespaced_secret(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Secret | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Secret**](V1Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_security_context_constraints**
> V1SecurityContextConstraints patch_namespaced_security_context_constraints(body, name, pretty=pretty)

partially update the specified SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the SecurityContextConstraints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified SecurityContextConstraints
    api_response = api_instance.patch_namespaced_security_context_constraints(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the SecurityContextConstraints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SecurityContextConstraints**](V1SecurityContextConstraints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_service**
> V1Service patch_namespaced_service(body, namespace, name, pretty=pretty)

partially update the specified Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Service
    api_response = api_instance.patch_namespaced_service(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Service**](V1Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_service_account**
> V1ServiceAccount patch_namespaced_service_account(body, namespace, name, pretty=pretty)

partially update the specified ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ServiceAccount
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ServiceAccount
    api_response = api_instance.patch_namespaced_service_account(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->patch_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ServiceAccount | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ServiceAccount**](V1ServiceAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_node_proxy**
> str post_namespaced_node_proxy(name, path=path)

connect POST requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect POST requests to proxy of Node
    api_response = api_instance.post_namespaced_node_proxy(name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_node_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_node_proxy_0**
> str post_namespaced_node_proxy_0(name, path2, path=path)

connect POST requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect POST requests to proxy of Node
    api_response = api_instance.post_namespaced_node_proxy_0(name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_node_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_pod_attach**
> str post_namespaced_pod_attach(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container)

connect POST requests to attach of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
stdin = true # bool | Stdin if true, redirects the standard input stream of the pod for this call. Defaults to false. (optional)
stdout = true # bool | Stdout if true indicates that stdout is to be redirected for the attach call. Defaults to true. (optional)
stderr = true # bool | Stderr if true indicates that stderr is to be redirected for the attach call. Defaults to true. (optional)
tty = true # bool | TTY if true indicates that a tty will be allocated for the attach call. This is passed through the container runtime so the tty is allocated on the worker node by the container runtime. Defaults to false. (optional)
container = 'container_example' # str | The container in which to execute the command. Defaults to only container if there is only one container in the pod. (optional)

try: 
    # connect POST requests to attach of Pod
    api_response = api_instance.post_namespaced_pod_attach(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_pod_attach: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **stdin** | **bool**| Stdin if true, redirects the standard input stream of the pod for this call. Defaults to false. | [optional] 
 **stdout** | **bool**| Stdout if true indicates that stdout is to be redirected for the attach call. Defaults to true. | [optional] 
 **stderr** | **bool**| Stderr if true indicates that stderr is to be redirected for the attach call. Defaults to true. | [optional] 
 **tty** | **bool**| TTY if true indicates that a tty will be allocated for the attach call. This is passed through the container runtime so the tty is allocated on the worker node by the container runtime. Defaults to false. | [optional] 
 **container** | **str**| The container in which to execute the command. Defaults to only container if there is only one container in the pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_pod_exec**
> str post_namespaced_pod_exec(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container, command=command)

connect POST requests to exec of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
stdin = true # bool | Redirect the standard input stream of the pod for this call. Defaults to false. (optional)
stdout = true # bool | Redirect the standard output stream of the pod for this call. Defaults to true. (optional)
stderr = true # bool | Redirect the standard error stream of the pod for this call. Defaults to true. (optional)
tty = true # bool | TTY if true indicates that a tty will be allocated for the exec call. Defaults to false. (optional)
container = 'container_example' # str | Container in which to execute the command. Defaults to only container if there is only one container in the pod. (optional)
command = 'command_example' # str | Command is the remote command to execute. argv array. Not executed within a shell. (optional)

try: 
    # connect POST requests to exec of Pod
    api_response = api_instance.post_namespaced_pod_exec(namespace, name, stdin=stdin, stdout=stdout, stderr=stderr, tty=tty, container=container, command=command)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_pod_exec: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **stdin** | **bool**| Redirect the standard input stream of the pod for this call. Defaults to false. | [optional] 
 **stdout** | **bool**| Redirect the standard output stream of the pod for this call. Defaults to true. | [optional] 
 **stderr** | **bool**| Redirect the standard error stream of the pod for this call. Defaults to true. | [optional] 
 **tty** | **bool**| TTY if true indicates that a tty will be allocated for the exec call. Defaults to false. | [optional] 
 **container** | **str**| Container in which to execute the command. Defaults to only container if there is only one container in the pod. | [optional] 
 **command** | **str**| Command is the remote command to execute. argv array. Not executed within a shell. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_pod_portforward**
> str post_namespaced_pod_portforward(namespace, name)

connect POST requests to portforward of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # connect POST requests to portforward of Pod
    api_response = api_instance.post_namespaced_pod_portforward(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_pod_portforward: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_pod_proxy**
> str post_namespaced_pod_proxy(namespace, name, path=path)

connect POST requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect POST requests to proxy of Pod
    api_response = api_instance.post_namespaced_pod_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_pod_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_pod_proxy_0**
> str post_namespaced_pod_proxy_0(namespace, name, path2, path=path)

connect POST requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect POST requests to proxy of Pod
    api_response = api_instance.post_namespaced_pod_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_pod_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_service_proxy**
> str post_namespaced_service_proxy(namespace, name, path=path)

connect POST requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect POST requests to proxy of Service
    api_response = api_instance.post_namespaced_service_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_service_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_service_proxy_0**
> str post_namespaced_service_proxy_0(namespace, name, path2, path=path)

connect POST requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect POST requests to proxy of Service
    api_response = api_instance.post_namespaced_service_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->post_namespaced_service_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_delete_namespaced_node**
> str proxy_delete_namespaced_node(name)

proxy DELETE requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node

try: 
    # proxy DELETE requests to Node
    api_response = api_instance.proxy_delete_namespaced_node(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_delete_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_delete_namespaced_node_0**
> str proxy_delete_namespaced_node_0(name, path)

proxy DELETE requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | path to the resource

try: 
    # proxy DELETE requests to Node
    api_response = api_instance.proxy_delete_namespaced_node_0(name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_delete_namespaced_node_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_delete_namespaced_pod**
> str proxy_delete_namespaced_pod(namespace, name)

proxy DELETE requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # proxy DELETE requests to Pod
    api_response = api_instance.proxy_delete_namespaced_pod(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_delete_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_delete_namespaced_pod_0**
> str proxy_delete_namespaced_pod_0(namespace, name, path)

proxy DELETE requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | path to the resource

try: 
    # proxy DELETE requests to Pod
    api_response = api_instance.proxy_delete_namespaced_pod_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_delete_namespaced_pod_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_delete_namespaced_service**
> str proxy_delete_namespaced_service(namespace, name)

proxy DELETE requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service

try: 
    # proxy DELETE requests to Service
    api_response = api_instance.proxy_delete_namespaced_service(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_delete_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_delete_namespaced_service_0**
> str proxy_delete_namespaced_service_0(namespace, name, path)

proxy DELETE requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | path to the resource

try: 
    # proxy DELETE requests to Service
    api_response = api_instance.proxy_delete_namespaced_service_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_delete_namespaced_service_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_get_namespaced_node**
> str proxy_get_namespaced_node(name)

proxy GET requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node

try: 
    # proxy GET requests to Node
    api_response = api_instance.proxy_get_namespaced_node(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_get_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_get_namespaced_node_0**
> str proxy_get_namespaced_node_0(name, path)

proxy GET requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | path to the resource

try: 
    # proxy GET requests to Node
    api_response = api_instance.proxy_get_namespaced_node_0(name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_get_namespaced_node_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_get_namespaced_pod**
> str proxy_get_namespaced_pod(namespace, name)

proxy GET requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # proxy GET requests to Pod
    api_response = api_instance.proxy_get_namespaced_pod(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_get_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_get_namespaced_pod_0**
> str proxy_get_namespaced_pod_0(namespace, name, path)

proxy GET requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | path to the resource

try: 
    # proxy GET requests to Pod
    api_response = api_instance.proxy_get_namespaced_pod_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_get_namespaced_pod_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_get_namespaced_service**
> str proxy_get_namespaced_service(namespace, name)

proxy GET requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service

try: 
    # proxy GET requests to Service
    api_response = api_instance.proxy_get_namespaced_service(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_get_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_get_namespaced_service_0**
> str proxy_get_namespaced_service_0(namespace, name, path)

proxy GET requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | path to the resource

try: 
    # proxy GET requests to Service
    api_response = api_instance.proxy_get_namespaced_service_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_get_namespaced_service_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_head_namespaced_node**
> str proxy_head_namespaced_node(name)

proxy HEAD requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node

try: 
    # proxy HEAD requests to Node
    api_response = api_instance.proxy_head_namespaced_node(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_head_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_head_namespaced_node_0**
> str proxy_head_namespaced_node_0(name, path)

proxy HEAD requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | path to the resource

try: 
    # proxy HEAD requests to Node
    api_response = api_instance.proxy_head_namespaced_node_0(name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_head_namespaced_node_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_head_namespaced_pod**
> str proxy_head_namespaced_pod(namespace, name)

proxy HEAD requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # proxy HEAD requests to Pod
    api_response = api_instance.proxy_head_namespaced_pod(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_head_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_head_namespaced_pod_0**
> str proxy_head_namespaced_pod_0(namespace, name, path)

proxy HEAD requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | path to the resource

try: 
    # proxy HEAD requests to Pod
    api_response = api_instance.proxy_head_namespaced_pod_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_head_namespaced_pod_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_head_namespaced_service**
> str proxy_head_namespaced_service(namespace, name)

proxy HEAD requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service

try: 
    # proxy HEAD requests to Service
    api_response = api_instance.proxy_head_namespaced_service(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_head_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_head_namespaced_service_0**
> str proxy_head_namespaced_service_0(namespace, name, path)

proxy HEAD requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | path to the resource

try: 
    # proxy HEAD requests to Service
    api_response = api_instance.proxy_head_namespaced_service_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_head_namespaced_service_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_options_namespaced_node**
> str proxy_options_namespaced_node(name)

proxy OPTIONS requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node

try: 
    # proxy OPTIONS requests to Node
    api_response = api_instance.proxy_options_namespaced_node(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_options_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_options_namespaced_node_0**
> str proxy_options_namespaced_node_0(name, path)

proxy OPTIONS requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | path to the resource

try: 
    # proxy OPTIONS requests to Node
    api_response = api_instance.proxy_options_namespaced_node_0(name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_options_namespaced_node_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_options_namespaced_pod**
> str proxy_options_namespaced_pod(namespace, name)

proxy OPTIONS requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # proxy OPTIONS requests to Pod
    api_response = api_instance.proxy_options_namespaced_pod(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_options_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_options_namespaced_pod_0**
> str proxy_options_namespaced_pod_0(namespace, name, path)

proxy OPTIONS requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | path to the resource

try: 
    # proxy OPTIONS requests to Pod
    api_response = api_instance.proxy_options_namespaced_pod_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_options_namespaced_pod_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_options_namespaced_service**
> str proxy_options_namespaced_service(namespace, name)

proxy OPTIONS requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service

try: 
    # proxy OPTIONS requests to Service
    api_response = api_instance.proxy_options_namespaced_service(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_options_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_options_namespaced_service_0**
> str proxy_options_namespaced_service_0(namespace, name, path)

proxy OPTIONS requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | path to the resource

try: 
    # proxy OPTIONS requests to Service
    api_response = api_instance.proxy_options_namespaced_service_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_options_namespaced_service_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_post_namespaced_node**
> str proxy_post_namespaced_node(name)

proxy POST requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node

try: 
    # proxy POST requests to Node
    api_response = api_instance.proxy_post_namespaced_node(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_post_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_post_namespaced_node_0**
> str proxy_post_namespaced_node_0(name, path)

proxy POST requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | path to the resource

try: 
    # proxy POST requests to Node
    api_response = api_instance.proxy_post_namespaced_node_0(name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_post_namespaced_node_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_post_namespaced_pod**
> str proxy_post_namespaced_pod(namespace, name)

proxy POST requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # proxy POST requests to Pod
    api_response = api_instance.proxy_post_namespaced_pod(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_post_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_post_namespaced_pod_0**
> str proxy_post_namespaced_pod_0(namespace, name, path)

proxy POST requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | path to the resource

try: 
    # proxy POST requests to Pod
    api_response = api_instance.proxy_post_namespaced_pod_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_post_namespaced_pod_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_post_namespaced_service**
> str proxy_post_namespaced_service(namespace, name)

proxy POST requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service

try: 
    # proxy POST requests to Service
    api_response = api_instance.proxy_post_namespaced_service(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_post_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_post_namespaced_service_0**
> str proxy_post_namespaced_service_0(namespace, name, path)

proxy POST requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | path to the resource

try: 
    # proxy POST requests to Service
    api_response = api_instance.proxy_post_namespaced_service_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_post_namespaced_service_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_put_namespaced_node**
> str proxy_put_namespaced_node(name)

proxy PUT requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node

try: 
    # proxy PUT requests to Node
    api_response = api_instance.proxy_put_namespaced_node(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_put_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_put_namespaced_node_0**
> str proxy_put_namespaced_node_0(name, path)

proxy PUT requests to Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | path to the resource

try: 
    # proxy PUT requests to Node
    api_response = api_instance.proxy_put_namespaced_node_0(name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_put_namespaced_node_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_put_namespaced_pod**
> str proxy_put_namespaced_pod(namespace, name)

proxy PUT requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod

try: 
    # proxy PUT requests to Pod
    api_response = api_instance.proxy_put_namespaced_pod(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_put_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_put_namespaced_pod_0**
> str proxy_put_namespaced_pod_0(namespace, name, path)

proxy PUT requests to Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | path to the resource

try: 
    # proxy PUT requests to Pod
    api_response = api_instance.proxy_put_namespaced_pod_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_put_namespaced_pod_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_put_namespaced_service**
> str proxy_put_namespaced_service(namespace, name)

proxy PUT requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service

try: 
    # proxy PUT requests to Service
    api_response = api_instance.proxy_put_namespaced_service(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_put_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_put_namespaced_service_0**
> str proxy_put_namespaced_service_0(namespace, name, path)

proxy PUT requests to Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | path to the resource

try: 
    # proxy PUT requests to Service
    api_response = api_instance.proxy_put_namespaced_service_0(namespace, name, path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->proxy_put_namespaced_service_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| path to the resource | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespaced_node_proxy**
> str put_namespaced_node_proxy(name, path=path)

connect PUT requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect PUT requests to proxy of Node
    api_response = api_instance.put_namespaced_node_proxy(name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->put_namespaced_node_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespaced_node_proxy_0**
> str put_namespaced_node_proxy_0(name, path2, path=path)

connect PUT requests to proxy of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to node. (optional)

try: 
    # connect PUT requests to proxy of Node
    api_response = api_instance.put_namespaced_node_proxy_0(name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->put_namespaced_node_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to node. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespaced_pod_proxy**
> str put_namespaced_pod_proxy(namespace, name, path=path)

connect PUT requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect PUT requests to proxy of Pod
    api_response = api_instance.put_namespaced_pod_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->put_namespaced_pod_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespaced_pod_proxy_0**
> str put_namespaced_pod_proxy_0(namespace, name, path2, path=path)

connect PUT requests to proxy of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect PUT requests to proxy of Pod
    api_response = api_instance.put_namespaced_pod_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->put_namespaced_pod_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespaced_service_proxy**
> str put_namespaced_service_proxy(namespace, name, path=path)

connect PUT requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect PUT requests to proxy of Service
    api_response = api_instance.put_namespaced_service_proxy(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->put_namespaced_service_proxy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespaced_service_proxy_0**
> str put_namespaced_service_proxy_0(namespace, name, path2, path=path)

connect PUT requests to proxy of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q=user:kimchy. Path is _search?q=user:kimchy. (optional)

try: 
    # connect PUT requests to proxy of Service
    api_response = api_instance.put_namespaced_service_proxy_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->put_namespaced_service_proxy_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **path2** | **str**| path to the resource | 
 **path** | **str**| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_component_status**
> V1ComponentStatus read_namespaced_component_status(name, pretty=pretty)

read the specified ComponentStatus

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the ComponentStatus
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ComponentStatus
    api_response = api_instance.read_namespaced_component_status(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_component_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ComponentStatus | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ComponentStatus**](V1ComponentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_config_map**
> V1ConfigMap read_namespaced_config_map(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ConfigMap
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ConfigMap
    api_response = api_instance.read_namespaced_config_map(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ConfigMap | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ConfigMap**](V1ConfigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_endpoints**
> V1Endpoints read_namespaced_endpoints(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Endpoints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Endpoints
    api_response = api_instance.read_namespaced_endpoints(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Endpoints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Endpoints**](V1Endpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_event**
> V1Event read_namespaced_event(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Event
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Event
    api_response = api_instance.read_namespaced_event(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Event | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Event**](V1Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_limit_range**
> V1LimitRange read_namespaced_limit_range(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the LimitRange
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified LimitRange
    api_response = api_instance.read_namespaced_limit_range(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the LimitRange | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1LimitRange**](V1LimitRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_namespace**
> V1Namespace read_namespaced_namespace(name, pretty=pretty, export=export, exact=exact)

read the specified Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Namespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Namespace
    api_response = api_instance.read_namespaced_namespace(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Namespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Namespace**](V1Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_node**
> V1Node read_namespaced_node(name, pretty=pretty, export=export, exact=exact)

read the specified Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Node
    api_response = api_instance.read_namespaced_node(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Node**](V1Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_persistent_volume**
> V1PersistentVolume read_namespaced_persistent_volume(name, pretty=pretty, export=export, exact=exact)

read the specified PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the PersistentVolume
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified PersistentVolume
    api_response = api_instance.read_namespaced_persistent_volume(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PersistentVolume | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1PersistentVolume**](V1PersistentVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_persistent_volume_claim**
> V1PersistentVolumeClaim read_namespaced_persistent_volume_claim(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PersistentVolumeClaim
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified PersistentVolumeClaim
    api_response = api_instance.read_namespaced_persistent_volume_claim(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PersistentVolumeClaim | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_pod**
> V1Pod read_namespaced_pod(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Pod
    api_response = api_instance.read_namespaced_pod(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Pod**](V1Pod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_pod_log**
> V1Pod read_namespaced_pod_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes)

read log of the specified Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
container = 'container_example' # str | The container for which to stream logs. Defaults to only container if there is one container in the pod. (optional)
follow = true # bool | Follow the log stream of the pod. Defaults to false. (optional)
previous = true # bool | Return previous terminated container logs. Defaults to false. (optional)
since_seconds = 56 # int | A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
since_time = 'since_time_example' # str | An RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
timestamps = true # bool | If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. (optional)
tail_lines = 56 # int | If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime (optional)
limit_bytes = 56 # int | If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. (optional)

try: 
    # read log of the specified Pod
    api_response = api_instance.read_namespaced_pod_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_pod_log: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **container** | **str**| The container for which to stream logs. Defaults to only container if there is one container in the pod. | [optional] 
 **follow** | **bool**| Follow the log stream of the pod. Defaults to false. | [optional] 
 **previous** | **bool**| Return previous terminated container logs. Defaults to false. | [optional] 
 **since_seconds** | **int**| A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **since_time** | **str**| An RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **timestamps** | **bool**| If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. | [optional] 
 **tail_lines** | **int**| If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime | [optional] 
 **limit_bytes** | **int**| If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. | [optional] 

### Return type

[**V1Pod**](V1Pod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_pod_template**
> V1PodTemplate read_namespaced_pod_template(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PodTemplate
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified PodTemplate
    api_response = api_instance.read_namespaced_pod_template(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PodTemplate | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1PodTemplate**](V1PodTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replication_controller**
> V1ReplicationController read_namespaced_replication_controller(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicationController
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ReplicationController
    api_response = api_instance.read_namespaced_replication_controller(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicationController | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ReplicationController**](V1ReplicationController.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_resource_quota**
> V1ResourceQuota read_namespaced_resource_quota(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ResourceQuota
    api_response = api_instance.read_namespaced_resource_quota(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ResourceQuota**](V1ResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_scale_scale**
> V1Scale read_namespaced_scale_scale(namespace, name, pretty=pretty)

read scale of the specified Scale

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read scale of the specified Scale
    api_response = api_instance.read_namespaced_scale_scale(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Scale**](V1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_secret**
> V1Secret read_namespaced_secret(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Secret
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Secret
    api_response = api_instance.read_namespaced_secret(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Secret | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Secret**](V1Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_security_context_constraints**
> V1SecurityContextConstraints read_namespaced_security_context_constraints(name, pretty=pretty, export=export, exact=exact)

read the specified SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the SecurityContextConstraints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified SecurityContextConstraints
    api_response = api_instance.read_namespaced_security_context_constraints(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the SecurityContextConstraints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1SecurityContextConstraints**](V1SecurityContextConstraints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_service**
> V1Service read_namespaced_service(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Service
    api_response = api_instance.read_namespaced_service(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Service**](V1Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_service_account**
> V1ServiceAccount read_namespaced_service_account(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ServiceAccount
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ServiceAccount
    api_response = api_instance.read_namespaced_service_account(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->read_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ServiceAccount | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ServiceAccount**](V1ServiceAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_config_map**
> V1ConfigMap replace_namespaced_config_map(body, namespace, name, pretty=pretty)

replace the specified ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ConfigMap() # V1ConfigMap | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ConfigMap
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ConfigMap
    api_response = api_instance.replace_namespaced_config_map(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ConfigMap**](V1ConfigMap.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ConfigMap | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ConfigMap**](V1ConfigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_endpoints**
> V1Endpoints replace_namespaced_endpoints(body, namespace, name, pretty=pretty)

replace the specified Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Endpoints() # V1Endpoints | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Endpoints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Endpoints
    api_response = api_instance.replace_namespaced_endpoints(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Endpoints**](V1Endpoints.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Endpoints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Endpoints**](V1Endpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_event**
> V1Event replace_namespaced_event(body, namespace, name, pretty=pretty)

replace the specified Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Event() # V1Event | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Event
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Event
    api_response = api_instance.replace_namespaced_event(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Event**](V1Event.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Event | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Event**](V1Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_limit_range**
> V1LimitRange replace_namespaced_limit_range(body, namespace, name, pretty=pretty)

replace the specified LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1LimitRange() # V1LimitRange | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the LimitRange
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified LimitRange
    api_response = api_instance.replace_namespaced_limit_range(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LimitRange**](V1LimitRange.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the LimitRange | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LimitRange**](V1LimitRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_namespace**
> V1Namespace replace_namespaced_namespace(body, name, pretty=pretty)

replace the specified Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Namespace() # V1Namespace | 
name = 'name_example' # str | name of the Namespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Namespace
    api_response = api_instance.replace_namespaced_namespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Namespace**](V1Namespace.md)|  | 
 **name** | **str**| name of the Namespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Namespace**](V1Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_namespace_finalize**
> V1Namespace replace_namespaced_namespace_finalize(body, name, pretty=pretty)

replace finalize of the specified Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Namespace() # V1Namespace | 
name = 'name_example' # str | name of the Namespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace finalize of the specified Namespace
    api_response = api_instance.replace_namespaced_namespace_finalize(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_namespace_finalize: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Namespace**](V1Namespace.md)|  | 
 **name** | **str**| name of the Namespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Namespace**](V1Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_namespace_status**
> V1Namespace replace_namespaced_namespace_status(body, name, pretty=pretty)

replace status of the specified Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Namespace() # V1Namespace | 
name = 'name_example' # str | name of the Namespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Namespace
    api_response = api_instance.replace_namespaced_namespace_status(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_namespace_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Namespace**](V1Namespace.md)|  | 
 **name** | **str**| name of the Namespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Namespace**](V1Namespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_node**
> V1Node replace_namespaced_node(body, name, pretty=pretty)

replace the specified Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Node() # V1Node | 
name = 'name_example' # str | name of the Node
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Node
    api_response = api_instance.replace_namespaced_node(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Node**](V1Node.md)|  | 
 **name** | **str**| name of the Node | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Node**](V1Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_node_status**
> V1Node replace_namespaced_node_status(body, name, pretty=pretty)

replace status of the specified Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Node() # V1Node | 
name = 'name_example' # str | name of the Node
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Node
    api_response = api_instance.replace_namespaced_node_status(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_node_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Node**](V1Node.md)|  | 
 **name** | **str**| name of the Node | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Node**](V1Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_persistent_volume**
> V1PersistentVolume replace_namespaced_persistent_volume(body, name, pretty=pretty)

replace the specified PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PersistentVolume() # V1PersistentVolume | 
name = 'name_example' # str | name of the PersistentVolume
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified PersistentVolume
    api_response = api_instance.replace_namespaced_persistent_volume(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PersistentVolume**](V1PersistentVolume.md)|  | 
 **name** | **str**| name of the PersistentVolume | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolume**](V1PersistentVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_persistent_volume_claim**
> V1PersistentVolumeClaim replace_namespaced_persistent_volume_claim(body, namespace, name, pretty=pretty)

replace the specified PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PersistentVolumeClaim() # V1PersistentVolumeClaim | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PersistentVolumeClaim
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified PersistentVolumeClaim
    api_response = api_instance.replace_namespaced_persistent_volume_claim(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PersistentVolumeClaim | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_persistent_volume_claim_status**
> V1PersistentVolumeClaim replace_namespaced_persistent_volume_claim_status(body, namespace, name, pretty=pretty)

replace status of the specified PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PersistentVolumeClaim() # V1PersistentVolumeClaim | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PersistentVolumeClaim
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified PersistentVolumeClaim
    api_response = api_instance.replace_namespaced_persistent_volume_claim_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_persistent_volume_claim_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PersistentVolumeClaim | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_persistent_volume_status**
> V1PersistentVolume replace_namespaced_persistent_volume_status(body, name, pretty=pretty)

replace status of the specified PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PersistentVolume() # V1PersistentVolume | 
name = 'name_example' # str | name of the PersistentVolume
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified PersistentVolume
    api_response = api_instance.replace_namespaced_persistent_volume_status(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_persistent_volume_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PersistentVolume**](V1PersistentVolume.md)|  | 
 **name** | **str**| name of the PersistentVolume | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PersistentVolume**](V1PersistentVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_pod**
> V1Pod replace_namespaced_pod(body, namespace, name, pretty=pretty)

replace the specified Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Pod() # V1Pod | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Pod
    api_response = api_instance.replace_namespaced_pod(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Pod**](V1Pod.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Pod**](V1Pod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_pod_status**
> V1Pod replace_namespaced_pod_status(body, namespace, name, pretty=pretty)

replace status of the specified Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Pod() # V1Pod | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Pod
    api_response = api_instance.replace_namespaced_pod_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_pod_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Pod**](V1Pod.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Pod**](V1Pod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_pod_template**
> V1PodTemplate replace_namespaced_pod_template(body, namespace, name, pretty=pretty)

replace the specified PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1PodTemplate() # V1PodTemplate | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PodTemplate
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified PodTemplate
    api_response = api_instance.replace_namespaced_pod_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodTemplate**](V1PodTemplate.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PodTemplate | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodTemplate**](V1PodTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replication_controller**
> V1ReplicationController replace_namespaced_replication_controller(body, namespace, name, pretty=pretty)

replace the specified ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ReplicationController() # V1ReplicationController | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicationController
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ReplicationController
    api_response = api_instance.replace_namespaced_replication_controller(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ReplicationController**](V1ReplicationController.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicationController | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ReplicationController**](V1ReplicationController.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replication_controller_status**
> V1ReplicationController replace_namespaced_replication_controller_status(body, namespace, name, pretty=pretty)

replace status of the specified ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ReplicationController() # V1ReplicationController | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicationController
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified ReplicationController
    api_response = api_instance.replace_namespaced_replication_controller_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_replication_controller_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ReplicationController**](V1ReplicationController.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicationController | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ReplicationController**](V1ReplicationController.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_resource_quota**
> V1ResourceQuota replace_namespaced_resource_quota(body, namespace, name, pretty=pretty)

replace the specified ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ResourceQuota() # V1ResourceQuota | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ResourceQuota
    api_response = api_instance.replace_namespaced_resource_quota(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ResourceQuota**](V1ResourceQuota.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ResourceQuota**](V1ResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_resource_quota_status**
> V1ResourceQuota replace_namespaced_resource_quota_status(body, namespace, name, pretty=pretty)

replace status of the specified ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ResourceQuota() # V1ResourceQuota | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified ResourceQuota
    api_response = api_instance.replace_namespaced_resource_quota_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_resource_quota_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ResourceQuota**](V1ResourceQuota.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ResourceQuota**](V1ResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_scale_scale**
> V1Scale replace_namespaced_scale_scale(body, namespace, name, pretty=pretty)

replace scale of the specified Scale

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Scale() # V1Scale | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace scale of the specified Scale
    api_response = api_instance.replace_namespaced_scale_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Scale**](V1Scale.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Scale**](V1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_secret**
> V1Secret replace_namespaced_secret(body, namespace, name, pretty=pretty)

replace the specified Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Secret() # V1Secret | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Secret
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Secret
    api_response = api_instance.replace_namespaced_secret(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Secret**](V1Secret.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Secret | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Secret**](V1Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_security_context_constraints**
> V1SecurityContextConstraints replace_namespaced_security_context_constraints(body, name, pretty=pretty)

replace the specified SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1SecurityContextConstraints() # V1SecurityContextConstraints | 
name = 'name_example' # str | name of the SecurityContextConstraints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified SecurityContextConstraints
    api_response = api_instance.replace_namespaced_security_context_constraints(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SecurityContextConstraints**](V1SecurityContextConstraints.md)|  | 
 **name** | **str**| name of the SecurityContextConstraints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SecurityContextConstraints**](V1SecurityContextConstraints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_service**
> V1Service replace_namespaced_service(body, namespace, name, pretty=pretty)

replace the specified Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Service() # V1Service | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Service
    api_response = api_instance.replace_namespaced_service(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Service**](V1Service.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Service**](V1Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_service_account**
> V1ServiceAccount replace_namespaced_service_account(body, namespace, name, pretty=pretty)

replace the specified ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1ServiceAccount() # V1ServiceAccount | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ServiceAccount
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ServiceAccount
    api_response = api_instance.replace_namespaced_service_account(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ServiceAccount**](V1ServiceAccount.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ServiceAccount | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ServiceAccount**](V1ServiceAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_service_status**
> V1Service replace_namespaced_service_status(body, namespace, name, pretty=pretty)

replace status of the specified Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
body = lib_openshift.V1Service() # V1Service | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Service
    api_response = api_instance.replace_namespaced_service_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->replace_namespaced_service_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Service**](V1Service.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Service**](V1Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_config_map_list**
> JsonWatchEvent watch_config_map_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ConfigMap
    api_response = api_instance.watch_config_map_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_config_map_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_endpoints_list**
> JsonWatchEvent watch_endpoints_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Endpoints
    api_response = api_instance.watch_endpoints_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_endpoints_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_event_list**
> JsonWatchEvent watch_event_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Event
    api_response = api_instance.watch_event_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_event_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_limit_range_list**
> JsonWatchEvent watch_limit_range_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of LimitRange
    api_response = api_instance.watch_limit_range_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_limit_range_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_config_map**
> JsonWatchEvent watch_namespaced_config_map(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ConfigMap
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ConfigMap
    api_response = api_instance.watch_namespaced_config_map(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_config_map: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ConfigMap | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_config_map_list**
> JsonWatchEvent watch_namespaced_config_map_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ConfigMap

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ConfigMap
    api_response = api_instance.watch_namespaced_config_map_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_config_map_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_endpoints**
> JsonWatchEvent watch_namespaced_endpoints(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Endpoints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Endpoints
    api_response = api_instance.watch_namespaced_endpoints(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_endpoints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Endpoints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_endpoints_list**
> JsonWatchEvent watch_namespaced_endpoints_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Endpoints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Endpoints
    api_response = api_instance.watch_namespaced_endpoints_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_endpoints_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_event**
> JsonWatchEvent watch_namespaced_event(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Event
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Event
    api_response = api_instance.watch_namespaced_event(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Event | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_event_list**
> JsonWatchEvent watch_namespaced_event_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Event

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Event
    api_response = api_instance.watch_namespaced_event_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_event_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_limit_range**
> JsonWatchEvent watch_namespaced_limit_range(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the LimitRange
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind LimitRange
    api_response = api_instance.watch_namespaced_limit_range(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_limit_range: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the LimitRange | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_limit_range_list**
> JsonWatchEvent watch_namespaced_limit_range_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of LimitRange

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of LimitRange
    api_response = api_instance.watch_namespaced_limit_range_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_limit_range_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_namespace**
> JsonWatchEvent watch_namespaced_namespace(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Namespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Namespace
    api_response = api_instance.watch_namespaced_namespace(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Namespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_namespace_list**
> JsonWatchEvent watch_namespaced_namespace_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Namespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Namespace
    api_response = api_instance.watch_namespaced_namespace_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_namespace_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_node**
> JsonWatchEvent watch_namespaced_node(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the Node
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Node
    api_response = api_instance.watch_namespaced_node(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Node | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_node_list**
> JsonWatchEvent watch_namespaced_node_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Node

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Node
    api_response = api_instance.watch_namespaced_node_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_node_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_persistent_volume**
> JsonWatchEvent watch_namespaced_persistent_volume(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the PersistentVolume
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind PersistentVolume
    api_response = api_instance.watch_namespaced_persistent_volume(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_persistent_volume: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PersistentVolume | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_persistent_volume_claim**
> JsonWatchEvent watch_namespaced_persistent_volume_claim(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PersistentVolumeClaim
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind PersistentVolumeClaim
    api_response = api_instance.watch_namespaced_persistent_volume_claim(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_persistent_volume_claim: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PersistentVolumeClaim | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_persistent_volume_claim_list**
> JsonWatchEvent watch_namespaced_persistent_volume_claim_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PersistentVolumeClaim
    api_response = api_instance.watch_namespaced_persistent_volume_claim_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_persistent_volume_claim_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_persistent_volume_list**
> JsonWatchEvent watch_namespaced_persistent_volume_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PersistentVolume

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PersistentVolume
    api_response = api_instance.watch_namespaced_persistent_volume_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_persistent_volume_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_pod**
> JsonWatchEvent watch_namespaced_pod(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Pod
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Pod
    api_response = api_instance.watch_namespaced_pod(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_pod: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Pod | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_pod_list**
> JsonWatchEvent watch_namespaced_pod_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Pod
    api_response = api_instance.watch_namespaced_pod_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_pod_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_pod_template**
> JsonWatchEvent watch_namespaced_pod_template(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PodTemplate
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind PodTemplate
    api_response = api_instance.watch_namespaced_pod_template(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_pod_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PodTemplate | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_pod_template_list**
> JsonWatchEvent watch_namespaced_pod_template_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PodTemplate
    api_response = api_instance.watch_namespaced_pod_template_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_pod_template_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_replication_controller**
> JsonWatchEvent watch_namespaced_replication_controller(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicationController
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ReplicationController
    api_response = api_instance.watch_namespaced_replication_controller(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_replication_controller: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicationController | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_replication_controller_list**
> JsonWatchEvent watch_namespaced_replication_controller_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ReplicationController
    api_response = api_instance.watch_namespaced_replication_controller_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_replication_controller_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_resource_quota**
> JsonWatchEvent watch_namespaced_resource_quota(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ResourceQuota
    api_response = api_instance.watch_namespaced_resource_quota(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_resource_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_resource_quota_list**
> JsonWatchEvent watch_namespaced_resource_quota_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ResourceQuota
    api_response = api_instance.watch_namespaced_resource_quota_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_resource_quota_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_secret**
> JsonWatchEvent watch_namespaced_secret(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Secret
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Secret
    api_response = api_instance.watch_namespaced_secret(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Secret | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_secret_list**
> JsonWatchEvent watch_namespaced_secret_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Secret
    api_response = api_instance.watch_namespaced_secret_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_secret_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_security_context_constraints**
> JsonWatchEvent watch_namespaced_security_context_constraints(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
name = 'name_example' # str | name of the SecurityContextConstraints
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind SecurityContextConstraints
    api_response = api_instance.watch_namespaced_security_context_constraints(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_security_context_constraints: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the SecurityContextConstraints | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_security_context_constraints_list**
> JsonWatchEvent watch_namespaced_security_context_constraints_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of SecurityContextConstraints

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of SecurityContextConstraints
    api_response = api_instance.watch_namespaced_security_context_constraints_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_security_context_constraints_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_service**
> JsonWatchEvent watch_namespaced_service(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Service
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Service
    api_response = api_instance.watch_namespaced_service(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_service: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Service | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_service_account**
> JsonWatchEvent watch_namespaced_service_account(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ServiceAccount
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ServiceAccount
    api_response = api_instance.watch_namespaced_service_account(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_service_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ServiceAccount | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_service_account_list**
> JsonWatchEvent watch_namespaced_service_account_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ServiceAccount
    api_response = api_instance.watch_namespaced_service_account_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_service_account_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_service_list**
> JsonWatchEvent watch_namespaced_service_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Service
    api_response = api_instance.watch_namespaced_service_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_namespaced_service_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_persistent_volume_claim_list**
> JsonWatchEvent watch_persistent_volume_claim_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PersistentVolumeClaim

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PersistentVolumeClaim
    api_response = api_instance.watch_persistent_volume_claim_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_persistent_volume_claim_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_pod_list**
> JsonWatchEvent watch_pod_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Pod

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Pod
    api_response = api_instance.watch_pod_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_pod_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_pod_template_list**
> JsonWatchEvent watch_pod_template_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PodTemplate

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PodTemplate
    api_response = api_instance.watch_pod_template_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_pod_template_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_replication_controller_list**
> JsonWatchEvent watch_replication_controller_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ReplicationController

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ReplicationController
    api_response = api_instance.watch_replication_controller_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_replication_controller_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_resource_quota_list**
> JsonWatchEvent watch_resource_quota_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ResourceQuota

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ResourceQuota
    api_response = api_instance.watch_resource_quota_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_resource_quota_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_secret_list**
> JsonWatchEvent watch_secret_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Secret

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Secret
    api_response = api_instance.watch_secret_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_secret_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_service_account_list**
> JsonWatchEvent watch_service_account_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ServiceAccount

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ServiceAccount
    api_response = api_instance.watch_service_account_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_service_account_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_service_list**
> JsonWatchEvent watch_service_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Service

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Service
    api_response = api_instance.watch_service_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiV1->watch_service_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**JsonWatchEvent**](JsonWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

