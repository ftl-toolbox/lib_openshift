# oapi_v1.Oapiv1Api

All URIs are relative to *https://localhost:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_build**](Oapiv1Api.md#create_build) | **POST** /oapi/v1/builds | create a Build
[**create_build_config**](Oapiv1Api.md#create_build_config) | **POST** /oapi/v1/buildconfigs | create a BuildConfig
[**create_deployment_config**](Oapiv1Api.md#create_deployment_config) | **POST** /oapi/v1/deploymentconfigs | create a DeploymentConfig
[**create_deployment_config_rollback**](Oapiv1Api.md#create_deployment_config_rollback) | **POST** /oapi/v1/deploymentconfigrollbacks | create a DeploymentConfigRollback
[**create_image_stream**](Oapiv1Api.md#create_image_stream) | **POST** /oapi/v1/imagestreams | create a ImageStream
[**create_image_stream_import**](Oapiv1Api.md#create_image_stream_import) | **POST** /oapi/v1/imagestreamimports | create a ImageStreamImport
[**create_image_stream_mapping**](Oapiv1Api.md#create_image_stream_mapping) | **POST** /oapi/v1/imagestreammappings | create a ImageStreamMapping
[**create_local_resource_access_review**](Oapiv1Api.md#create_local_resource_access_review) | **POST** /oapi/v1/localresourceaccessreviews | create a LocalResourceAccessReview
[**create_local_subject_access_review**](Oapiv1Api.md#create_local_subject_access_review) | **POST** /oapi/v1/localsubjectaccessreviews | create a LocalSubjectAccessReview
[**create_namespaced_build**](Oapiv1Api.md#create_namespaced_build) | **POST** /oapi/v1/namespaces/{namespace}/builds | create a Build
[**create_namespaced_build_config**](Oapiv1Api.md#create_namespaced_build_config) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs | create a BuildConfig
[**create_namespaced_build_request_clone**](Oapiv1Api.md#create_namespaced_build_request_clone) | **POST** /oapi/v1/namespaces/{namespace}/builds/{name}/clone | create clone of a BuildRequest
[**create_namespaced_build_request_instantiate**](Oapiv1Api.md#create_namespaced_build_request_instantiate) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/instantiate | create instantiate of a BuildRequest
[**create_namespaced_cluster_network**](Oapiv1Api.md#create_namespaced_cluster_network) | **POST** /oapi/v1/clusternetworks | create a ClusterNetwork
[**create_namespaced_cluster_policy**](Oapiv1Api.md#create_namespaced_cluster_policy) | **POST** /oapi/v1/clusterpolicies | create a ClusterPolicy
[**create_namespaced_cluster_policy_binding**](Oapiv1Api.md#create_namespaced_cluster_policy_binding) | **POST** /oapi/v1/clusterpolicybindings | create a ClusterPolicyBinding
[**create_namespaced_cluster_role**](Oapiv1Api.md#create_namespaced_cluster_role) | **POST** /oapi/v1/clusterroles | create a ClusterRole
[**create_namespaced_cluster_role_binding**](Oapiv1Api.md#create_namespaced_cluster_role_binding) | **POST** /oapi/v1/clusterrolebindings | create a ClusterRoleBinding
[**create_namespaced_deployment_config**](Oapiv1Api.md#create_namespaced_deployment_config) | **POST** /oapi/v1/namespaces/{namespace}/deploymentconfigs | create a DeploymentConfig
[**create_namespaced_deployment_config_rollback**](Oapiv1Api.md#create_namespaced_deployment_config_rollback) | **POST** /oapi/v1/namespaces/{namespace}/deploymentconfigrollbacks | create a DeploymentConfigRollback
[**create_namespaced_group**](Oapiv1Api.md#create_namespaced_group) | **POST** /oapi/v1/groups | create a Group
[**create_namespaced_host_subnet**](Oapiv1Api.md#create_namespaced_host_subnet) | **POST** /oapi/v1/hostsubnets | create a HostSubnet
[**create_namespaced_identity**](Oapiv1Api.md#create_namespaced_identity) | **POST** /oapi/v1/identities | create a Identity
[**create_namespaced_image**](Oapiv1Api.md#create_namespaced_image) | **POST** /oapi/v1/images | create a Image
[**create_namespaced_image_stream**](Oapiv1Api.md#create_namespaced_image_stream) | **POST** /oapi/v1/namespaces/{namespace}/imagestreams | create a ImageStream
[**create_namespaced_image_stream_import**](Oapiv1Api.md#create_namespaced_image_stream_import) | **POST** /oapi/v1/namespaces/{namespace}/imagestreamimports | create a ImageStreamImport
[**create_namespaced_image_stream_mapping**](Oapiv1Api.md#create_namespaced_image_stream_mapping) | **POST** /oapi/v1/namespaces/{namespace}/imagestreammappings | create a ImageStreamMapping
[**create_namespaced_local_resource_access_review**](Oapiv1Api.md#create_namespaced_local_resource_access_review) | **POST** /oapi/v1/namespaces/{namespace}/localresourceaccessreviews | create a LocalResourceAccessReview
[**create_namespaced_local_subject_access_review**](Oapiv1Api.md#create_namespaced_local_subject_access_review) | **POST** /oapi/v1/namespaces/{namespace}/localsubjectaccessreviews | create a LocalSubjectAccessReview
[**create_namespaced_net_namespace**](Oapiv1Api.md#create_namespaced_net_namespace) | **POST** /oapi/v1/netnamespaces | create a NetNamespace
[**create_namespaced_o_auth_access_token**](Oapiv1Api.md#create_namespaced_o_auth_access_token) | **POST** /oapi/v1/oauthaccesstokens | create a OAuthAccessToken
[**create_namespaced_o_auth_authorize_token**](Oapiv1Api.md#create_namespaced_o_auth_authorize_token) | **POST** /oapi/v1/oauthauthorizetokens | create a OAuthAuthorizeToken
[**create_namespaced_o_auth_client**](Oapiv1Api.md#create_namespaced_o_auth_client) | **POST** /oapi/v1/oauthclients | create a OAuthClient
[**create_namespaced_o_auth_client_authorization**](Oapiv1Api.md#create_namespaced_o_auth_client_authorization) | **POST** /oapi/v1/oauthclientauthorizations | create a OAuthClientAuthorization
[**create_namespaced_policy**](Oapiv1Api.md#create_namespaced_policy) | **POST** /oapi/v1/namespaces/{namespace}/policies | create a Policy
[**create_namespaced_policy_binding**](Oapiv1Api.md#create_namespaced_policy_binding) | **POST** /oapi/v1/namespaces/{namespace}/policybindings | create a PolicyBinding
[**create_namespaced_project**](Oapiv1Api.md#create_namespaced_project) | **POST** /oapi/v1/projects | create a Project
[**create_namespaced_project_request**](Oapiv1Api.md#create_namespaced_project_request) | **POST** /oapi/v1/projectrequests | create a ProjectRequest
[**create_namespaced_resource_access_review**](Oapiv1Api.md#create_namespaced_resource_access_review) | **POST** /oapi/v1/namespaces/{namespace}/resourceaccessreviews | create a ResourceAccessReview
[**create_namespaced_role**](Oapiv1Api.md#create_namespaced_role) | **POST** /oapi/v1/namespaces/{namespace}/roles | create a Role
[**create_namespaced_role_binding**](Oapiv1Api.md#create_namespaced_role_binding) | **POST** /oapi/v1/namespaces/{namespace}/rolebindings | create a RoleBinding
[**create_namespaced_route**](Oapiv1Api.md#create_namespaced_route) | **POST** /oapi/v1/namespaces/{namespace}/routes | create a Route
[**create_namespaced_subject_access_review**](Oapiv1Api.md#create_namespaced_subject_access_review) | **POST** /oapi/v1/namespaces/{namespace}/subjectaccessreviews | create a SubjectAccessReview
[**create_namespaced_template**](Oapiv1Api.md#create_namespaced_template) | **POST** /oapi/v1/namespaces/{namespace}/processedtemplates | create a Template
[**create_namespaced_template_0**](Oapiv1Api.md#create_namespaced_template_0) | **POST** /oapi/v1/namespaces/{namespace}/templates | create a Template
[**create_namespaced_user**](Oapiv1Api.md#create_namespaced_user) | **POST** /oapi/v1/users | create a User
[**create_namespaced_user_identity_mapping**](Oapiv1Api.md#create_namespaced_user_identity_mapping) | **POST** /oapi/v1/useridentitymappings | create a UserIdentityMapping
[**create_policy**](Oapiv1Api.md#create_policy) | **POST** /oapi/v1/policies | create a Policy
[**create_policy_binding**](Oapiv1Api.md#create_policy_binding) | **POST** /oapi/v1/policybindings | create a PolicyBinding
[**create_resource_access_review**](Oapiv1Api.md#create_resource_access_review) | **POST** /oapi/v1/resourceaccessreviews | create a ResourceAccessReview
[**create_role**](Oapiv1Api.md#create_role) | **POST** /oapi/v1/roles | create a Role
[**create_role_binding**](Oapiv1Api.md#create_role_binding) | **POST** /oapi/v1/rolebindings | create a RoleBinding
[**create_route**](Oapiv1Api.md#create_route) | **POST** /oapi/v1/routes | create a Route
[**create_subject_access_review**](Oapiv1Api.md#create_subject_access_review) | **POST** /oapi/v1/subjectaccessreviews | create a SubjectAccessReview
[**create_template**](Oapiv1Api.md#create_template) | **POST** /oapi/v1/processedtemplates | create a Template
[**create_template_0**](Oapiv1Api.md#create_template_0) | **POST** /oapi/v1/templates | create a Template
[**delete_namespaced_build**](Oapiv1Api.md#delete_namespaced_build) | **DELETE** /oapi/v1/namespaces/{namespace}/builds/{name} | delete a Build
[**delete_namespaced_build_config**](Oapiv1Api.md#delete_namespaced_build_config) | **DELETE** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | delete a BuildConfig
[**delete_namespaced_cluster_network**](Oapiv1Api.md#delete_namespaced_cluster_network) | **DELETE** /oapi/v1/clusternetworks/{name} | delete a ClusterNetwork
[**delete_namespaced_cluster_policy**](Oapiv1Api.md#delete_namespaced_cluster_policy) | **DELETE** /oapi/v1/clusterpolicies/{name} | delete a ClusterPolicy
[**delete_namespaced_cluster_policy_binding**](Oapiv1Api.md#delete_namespaced_cluster_policy_binding) | **DELETE** /oapi/v1/clusterpolicybindings/{name} | delete a ClusterPolicyBinding
[**delete_namespaced_cluster_role**](Oapiv1Api.md#delete_namespaced_cluster_role) | **DELETE** /oapi/v1/clusterroles/{name} | delete a ClusterRole
[**delete_namespaced_cluster_role_binding**](Oapiv1Api.md#delete_namespaced_cluster_role_binding) | **DELETE** /oapi/v1/clusterrolebindings/{name} | delete a ClusterRoleBinding
[**delete_namespaced_deployment_config**](Oapiv1Api.md#delete_namespaced_deployment_config) | **DELETE** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | delete a DeploymentConfig
[**delete_namespaced_group**](Oapiv1Api.md#delete_namespaced_group) | **DELETE** /oapi/v1/groups/{name} | delete a Group
[**delete_namespaced_host_subnet**](Oapiv1Api.md#delete_namespaced_host_subnet) | **DELETE** /oapi/v1/hostsubnets/{name} | delete a HostSubnet
[**delete_namespaced_identity**](Oapiv1Api.md#delete_namespaced_identity) | **DELETE** /oapi/v1/identities/{name} | delete a Identity
[**delete_namespaced_image**](Oapiv1Api.md#delete_namespaced_image) | **DELETE** /oapi/v1/images/{name} | delete a Image
[**delete_namespaced_image_stream**](Oapiv1Api.md#delete_namespaced_image_stream) | **DELETE** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | delete a ImageStream
[**delete_namespaced_image_stream_tag**](Oapiv1Api.md#delete_namespaced_image_stream_tag) | **DELETE** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | delete a ImageStreamTag
[**delete_namespaced_net_namespace**](Oapiv1Api.md#delete_namespaced_net_namespace) | **DELETE** /oapi/v1/netnamespaces/{name} | delete a NetNamespace
[**delete_namespaced_o_auth_access_token**](Oapiv1Api.md#delete_namespaced_o_auth_access_token) | **DELETE** /oapi/v1/oauthaccesstokens/{name} | delete a OAuthAccessToken
[**delete_namespaced_o_auth_authorize_token**](Oapiv1Api.md#delete_namespaced_o_auth_authorize_token) | **DELETE** /oapi/v1/oauthauthorizetokens/{name} | delete a OAuthAuthorizeToken
[**delete_namespaced_o_auth_client**](Oapiv1Api.md#delete_namespaced_o_auth_client) | **DELETE** /oapi/v1/oauthclients/{name} | delete a OAuthClient
[**delete_namespaced_o_auth_client_authorization**](Oapiv1Api.md#delete_namespaced_o_auth_client_authorization) | **DELETE** /oapi/v1/oauthclientauthorizations/{name} | delete a OAuthClientAuthorization
[**delete_namespaced_policy**](Oapiv1Api.md#delete_namespaced_policy) | **DELETE** /oapi/v1/namespaces/{namespace}/policies/{name} | delete a Policy
[**delete_namespaced_policy_binding**](Oapiv1Api.md#delete_namespaced_policy_binding) | **DELETE** /oapi/v1/namespaces/{namespace}/policybindings/{name} | delete a PolicyBinding
[**delete_namespaced_project**](Oapiv1Api.md#delete_namespaced_project) | **DELETE** /oapi/v1/projects/{name} | delete a Project
[**delete_namespaced_role**](Oapiv1Api.md#delete_namespaced_role) | **DELETE** /oapi/v1/namespaces/{namespace}/roles/{name} | delete a Role
[**delete_namespaced_role_binding**](Oapiv1Api.md#delete_namespaced_role_binding) | **DELETE** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | delete a RoleBinding
[**delete_namespaced_route**](Oapiv1Api.md#delete_namespaced_route) | **DELETE** /oapi/v1/namespaces/{namespace}/routes/{name} | delete a Route
[**delete_namespaced_template**](Oapiv1Api.md#delete_namespaced_template) | **DELETE** /oapi/v1/namespaces/{namespace}/templates/{name} | delete a Template
[**delete_namespaced_user**](Oapiv1Api.md#delete_namespaced_user) | **DELETE** /oapi/v1/users/{name} | delete a User
[**delete_namespaced_user_identity_mapping**](Oapiv1Api.md#delete_namespaced_user_identity_mapping) | **DELETE** /oapi/v1/useridentitymappings/{name} | delete a UserIdentityMapping
[**deletecollection_namespaced_build**](Oapiv1Api.md#deletecollection_namespaced_build) | **DELETE** /oapi/v1/namespaces/{namespace}/builds | delete collection of Build
[**deletecollection_namespaced_build_config**](Oapiv1Api.md#deletecollection_namespaced_build_config) | **DELETE** /oapi/v1/namespaces/{namespace}/buildconfigs | delete collection of BuildConfig
[**deletecollection_namespaced_cluster_network**](Oapiv1Api.md#deletecollection_namespaced_cluster_network) | **DELETE** /oapi/v1/clusternetworks | delete collection of ClusterNetwork
[**deletecollection_namespaced_cluster_policy**](Oapiv1Api.md#deletecollection_namespaced_cluster_policy) | **DELETE** /oapi/v1/clusterpolicies | delete collection of ClusterPolicy
[**deletecollection_namespaced_cluster_policy_binding**](Oapiv1Api.md#deletecollection_namespaced_cluster_policy_binding) | **DELETE** /oapi/v1/clusterpolicybindings | delete collection of ClusterPolicyBinding
[**deletecollection_namespaced_deployment_config**](Oapiv1Api.md#deletecollection_namespaced_deployment_config) | **DELETE** /oapi/v1/namespaces/{namespace}/deploymentconfigs | delete collection of DeploymentConfig
[**deletecollection_namespaced_group**](Oapiv1Api.md#deletecollection_namespaced_group) | **DELETE** /oapi/v1/groups | delete collection of Group
[**deletecollection_namespaced_host_subnet**](Oapiv1Api.md#deletecollection_namespaced_host_subnet) | **DELETE** /oapi/v1/hostsubnets | delete collection of HostSubnet
[**deletecollection_namespaced_identity**](Oapiv1Api.md#deletecollection_namespaced_identity) | **DELETE** /oapi/v1/identities | delete collection of Identity
[**deletecollection_namespaced_image**](Oapiv1Api.md#deletecollection_namespaced_image) | **DELETE** /oapi/v1/images | delete collection of Image
[**deletecollection_namespaced_image_stream**](Oapiv1Api.md#deletecollection_namespaced_image_stream) | **DELETE** /oapi/v1/namespaces/{namespace}/imagestreams | delete collection of ImageStream
[**deletecollection_namespaced_net_namespace**](Oapiv1Api.md#deletecollection_namespaced_net_namespace) | **DELETE** /oapi/v1/netnamespaces | delete collection of NetNamespace
[**deletecollection_namespaced_o_auth_client**](Oapiv1Api.md#deletecollection_namespaced_o_auth_client) | **DELETE** /oapi/v1/oauthclients | delete collection of OAuthClient
[**deletecollection_namespaced_o_auth_client_authorization**](Oapiv1Api.md#deletecollection_namespaced_o_auth_client_authorization) | **DELETE** /oapi/v1/oauthclientauthorizations | delete collection of OAuthClientAuthorization
[**deletecollection_namespaced_policy**](Oapiv1Api.md#deletecollection_namespaced_policy) | **DELETE** /oapi/v1/namespaces/{namespace}/policies | delete collection of Policy
[**deletecollection_namespaced_policy_binding**](Oapiv1Api.md#deletecollection_namespaced_policy_binding) | **DELETE** /oapi/v1/namespaces/{namespace}/policybindings | delete collection of PolicyBinding
[**deletecollection_namespaced_route**](Oapiv1Api.md#deletecollection_namespaced_route) | **DELETE** /oapi/v1/namespaces/{namespace}/routes | delete collection of Route
[**deletecollection_namespaced_template**](Oapiv1Api.md#deletecollection_namespaced_template) | **DELETE** /oapi/v1/namespaces/{namespace}/templates | delete collection of Template
[**deletecollection_namespaced_user**](Oapiv1Api.md#deletecollection_namespaced_user) | **DELETE** /oapi/v1/users | delete collection of User
[**get_api_resources**](Oapiv1Api.md#get_api_resources) | **GET** /oapi/v1 | get available resources
[**list_build**](Oapiv1Api.md#list_build) | **GET** /oapi/v1/builds | list or watch objects of kind Build
[**list_build_config**](Oapiv1Api.md#list_build_config) | **GET** /oapi/v1/buildconfigs | list or watch objects of kind BuildConfig
[**list_deployment_config**](Oapiv1Api.md#list_deployment_config) | **GET** /oapi/v1/deploymentconfigs | list or watch objects of kind DeploymentConfig
[**list_image_stream**](Oapiv1Api.md#list_image_stream) | **GET** /oapi/v1/imagestreams | list or watch objects of kind ImageStream
[**list_image_stream_tag**](Oapiv1Api.md#list_image_stream_tag) | **GET** /oapi/v1/imagestreamtags | list objects of kind ImageStreamTag
[**list_namespaced_build**](Oapiv1Api.md#list_namespaced_build) | **GET** /oapi/v1/namespaces/{namespace}/builds | list or watch objects of kind Build
[**list_namespaced_build_config**](Oapiv1Api.md#list_namespaced_build_config) | **GET** /oapi/v1/namespaces/{namespace}/buildconfigs | list or watch objects of kind BuildConfig
[**list_namespaced_cluster_network**](Oapiv1Api.md#list_namespaced_cluster_network) | **GET** /oapi/v1/clusternetworks | list or watch objects of kind ClusterNetwork
[**list_namespaced_cluster_policy**](Oapiv1Api.md#list_namespaced_cluster_policy) | **GET** /oapi/v1/clusterpolicies | list or watch objects of kind ClusterPolicy
[**list_namespaced_cluster_policy_binding**](Oapiv1Api.md#list_namespaced_cluster_policy_binding) | **GET** /oapi/v1/clusterpolicybindings | list or watch objects of kind ClusterPolicyBinding
[**list_namespaced_cluster_role**](Oapiv1Api.md#list_namespaced_cluster_role) | **GET** /oapi/v1/clusterroles | list objects of kind ClusterRole
[**list_namespaced_cluster_role_binding**](Oapiv1Api.md#list_namespaced_cluster_role_binding) | **GET** /oapi/v1/clusterrolebindings | list objects of kind ClusterRoleBinding
[**list_namespaced_deployment_config**](Oapiv1Api.md#list_namespaced_deployment_config) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs | list or watch objects of kind DeploymentConfig
[**list_namespaced_group**](Oapiv1Api.md#list_namespaced_group) | **GET** /oapi/v1/groups | list or watch objects of kind Group
[**list_namespaced_host_subnet**](Oapiv1Api.md#list_namespaced_host_subnet) | **GET** /oapi/v1/hostsubnets | list or watch objects of kind HostSubnet
[**list_namespaced_identity**](Oapiv1Api.md#list_namespaced_identity) | **GET** /oapi/v1/identities | list or watch objects of kind Identity
[**list_namespaced_image**](Oapiv1Api.md#list_namespaced_image) | **GET** /oapi/v1/images | list or watch objects of kind Image
[**list_namespaced_image_stream**](Oapiv1Api.md#list_namespaced_image_stream) | **GET** /oapi/v1/namespaces/{namespace}/imagestreams | list or watch objects of kind ImageStream
[**list_namespaced_image_stream_tag**](Oapiv1Api.md#list_namespaced_image_stream_tag) | **GET** /oapi/v1/namespaces/{namespace}/imagestreamtags | list objects of kind ImageStreamTag
[**list_namespaced_net_namespace**](Oapiv1Api.md#list_namespaced_net_namespace) | **GET** /oapi/v1/netnamespaces | list or watch objects of kind NetNamespace
[**list_namespaced_o_auth_access_token**](Oapiv1Api.md#list_namespaced_o_auth_access_token) | **GET** /oapi/v1/oauthaccesstokens | list objects of kind OAuthAccessToken
[**list_namespaced_o_auth_authorize_token**](Oapiv1Api.md#list_namespaced_o_auth_authorize_token) | **GET** /oapi/v1/oauthauthorizetokens | list objects of kind OAuthAuthorizeToken
[**list_namespaced_o_auth_client**](Oapiv1Api.md#list_namespaced_o_auth_client) | **GET** /oapi/v1/oauthclients | list or watch objects of kind OAuthClient
[**list_namespaced_o_auth_client_authorization**](Oapiv1Api.md#list_namespaced_o_auth_client_authorization) | **GET** /oapi/v1/oauthclientauthorizations | list or watch objects of kind OAuthClientAuthorization
[**list_namespaced_policy**](Oapiv1Api.md#list_namespaced_policy) | **GET** /oapi/v1/namespaces/{namespace}/policies | list or watch objects of kind Policy
[**list_namespaced_policy_binding**](Oapiv1Api.md#list_namespaced_policy_binding) | **GET** /oapi/v1/namespaces/{namespace}/policybindings | list or watch objects of kind PolicyBinding
[**list_namespaced_project**](Oapiv1Api.md#list_namespaced_project) | **GET** /oapi/v1/projects | list objects of kind Project
[**list_namespaced_project_request**](Oapiv1Api.md#list_namespaced_project_request) | **GET** /oapi/v1/projectrequests | list objects of kind ProjectRequest
[**list_namespaced_role**](Oapiv1Api.md#list_namespaced_role) | **GET** /oapi/v1/namespaces/{namespace}/roles | list objects of kind Role
[**list_namespaced_role_binding**](Oapiv1Api.md#list_namespaced_role_binding) | **GET** /oapi/v1/namespaces/{namespace}/rolebindings | list objects of kind RoleBinding
[**list_namespaced_route**](Oapiv1Api.md#list_namespaced_route) | **GET** /oapi/v1/namespaces/{namespace}/routes | list or watch objects of kind Route
[**list_namespaced_template**](Oapiv1Api.md#list_namespaced_template) | **GET** /oapi/v1/namespaces/{namespace}/templates | list or watch objects of kind Template
[**list_namespaced_user**](Oapiv1Api.md#list_namespaced_user) | **GET** /oapi/v1/users | list or watch objects of kind User
[**list_policy**](Oapiv1Api.md#list_policy) | **GET** /oapi/v1/policies | list or watch objects of kind Policy
[**list_policy_binding**](Oapiv1Api.md#list_policy_binding) | **GET** /oapi/v1/policybindings | list or watch objects of kind PolicyBinding
[**list_role**](Oapiv1Api.md#list_role) | **GET** /oapi/v1/roles | list objects of kind Role
[**list_role_binding**](Oapiv1Api.md#list_role_binding) | **GET** /oapi/v1/rolebindings | list objects of kind RoleBinding
[**list_route**](Oapiv1Api.md#list_route) | **GET** /oapi/v1/routes | list or watch objects of kind Route
[**list_template**](Oapiv1Api.md#list_template) | **GET** /oapi/v1/templates | list or watch objects of kind Template
[**patch_namespaced_build**](Oapiv1Api.md#patch_namespaced_build) | **PATCH** /oapi/v1/namespaces/{namespace}/builds/{name} | partially update the specified Build
[**patch_namespaced_build_config**](Oapiv1Api.md#patch_namespaced_build_config) | **PATCH** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | partially update the specified BuildConfig
[**patch_namespaced_cluster_network**](Oapiv1Api.md#patch_namespaced_cluster_network) | **PATCH** /oapi/v1/clusternetworks/{name} | partially update the specified ClusterNetwork
[**patch_namespaced_cluster_policy**](Oapiv1Api.md#patch_namespaced_cluster_policy) | **PATCH** /oapi/v1/clusterpolicies/{name} | partially update the specified ClusterPolicy
[**patch_namespaced_cluster_policy_binding**](Oapiv1Api.md#patch_namespaced_cluster_policy_binding) | **PATCH** /oapi/v1/clusterpolicybindings/{name} | partially update the specified ClusterPolicyBinding
[**patch_namespaced_cluster_role**](Oapiv1Api.md#patch_namespaced_cluster_role) | **PATCH** /oapi/v1/clusterroles/{name} | partially update the specified ClusterRole
[**patch_namespaced_cluster_role_binding**](Oapiv1Api.md#patch_namespaced_cluster_role_binding) | **PATCH** /oapi/v1/clusterrolebindings/{name} | partially update the specified ClusterRoleBinding
[**patch_namespaced_deployment_config**](Oapiv1Api.md#patch_namespaced_deployment_config) | **PATCH** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | partially update the specified DeploymentConfig
[**patch_namespaced_group**](Oapiv1Api.md#patch_namespaced_group) | **PATCH** /oapi/v1/groups/{name} | partially update the specified Group
[**patch_namespaced_host_subnet**](Oapiv1Api.md#patch_namespaced_host_subnet) | **PATCH** /oapi/v1/hostsubnets/{name} | partially update the specified HostSubnet
[**patch_namespaced_identity**](Oapiv1Api.md#patch_namespaced_identity) | **PATCH** /oapi/v1/identities/{name} | partially update the specified Identity
[**patch_namespaced_image**](Oapiv1Api.md#patch_namespaced_image) | **PATCH** /oapi/v1/images/{name} | partially update the specified Image
[**patch_namespaced_image_stream**](Oapiv1Api.md#patch_namespaced_image_stream) | **PATCH** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | partially update the specified ImageStream
[**patch_namespaced_image_stream_tag**](Oapiv1Api.md#patch_namespaced_image_stream_tag) | **PATCH** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | partially update the specified ImageStreamTag
[**patch_namespaced_net_namespace**](Oapiv1Api.md#patch_namespaced_net_namespace) | **PATCH** /oapi/v1/netnamespaces/{name} | partially update the specified NetNamespace
[**patch_namespaced_o_auth_client**](Oapiv1Api.md#patch_namespaced_o_auth_client) | **PATCH** /oapi/v1/oauthclients/{name} | partially update the specified OAuthClient
[**patch_namespaced_o_auth_client_authorization**](Oapiv1Api.md#patch_namespaced_o_auth_client_authorization) | **PATCH** /oapi/v1/oauthclientauthorizations/{name} | partially update the specified OAuthClientAuthorization
[**patch_namespaced_policy**](Oapiv1Api.md#patch_namespaced_policy) | **PATCH** /oapi/v1/namespaces/{namespace}/policies/{name} | partially update the specified Policy
[**patch_namespaced_policy_binding**](Oapiv1Api.md#patch_namespaced_policy_binding) | **PATCH** /oapi/v1/namespaces/{namespace}/policybindings/{name} | partially update the specified PolicyBinding
[**patch_namespaced_project**](Oapiv1Api.md#patch_namespaced_project) | **PATCH** /oapi/v1/projects/{name} | partially update the specified Project
[**patch_namespaced_role**](Oapiv1Api.md#patch_namespaced_role) | **PATCH** /oapi/v1/namespaces/{namespace}/roles/{name} | partially update the specified Role
[**patch_namespaced_role_binding**](Oapiv1Api.md#patch_namespaced_role_binding) | **PATCH** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | partially update the specified RoleBinding
[**patch_namespaced_route**](Oapiv1Api.md#patch_namespaced_route) | **PATCH** /oapi/v1/namespaces/{namespace}/routes/{name} | partially update the specified Route
[**patch_namespaced_scale_scale**](Oapiv1Api.md#patch_namespaced_scale_scale) | **PATCH** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | partially update scale of the specified Scale
[**patch_namespaced_template**](Oapiv1Api.md#patch_namespaced_template) | **PATCH** /oapi/v1/namespaces/{namespace}/templates/{name} | partially update the specified Template
[**patch_namespaced_user**](Oapiv1Api.md#patch_namespaced_user) | **PATCH** /oapi/v1/users/{name} | partially update the specified User
[**patch_namespaced_user_identity_mapping**](Oapiv1Api.md#patch_namespaced_user_identity_mapping) | **PATCH** /oapi/v1/useridentitymappings/{name} | partially update the specified UserIdentityMapping
[**post_namespaced_binary_build_request_options_instantiatebinary**](Oapiv1Api.md#post_namespaced_binary_build_request_options_instantiatebinary) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/instantiatebinary | connect POST requests to instantiatebinary of BinaryBuildRequestOptions
[**post_namespaced_status_webhooks**](Oapiv1Api.md#post_namespaced_status_webhooks) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks | connect POST requests to webhooks of Status
[**post_namespaced_status_webhooks_0**](Oapiv1Api.md#post_namespaced_status_webhooks_0) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks/{path} | connect POST requests to webhooks of Status
[**read_namespaced_build**](Oapiv1Api.md#read_namespaced_build) | **GET** /oapi/v1/namespaces/{namespace}/builds/{name} | read the specified Build
[**read_namespaced_build_config**](Oapiv1Api.md#read_namespaced_build_config) | **GET** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | read the specified BuildConfig
[**read_namespaced_build_log_log**](Oapiv1Api.md#read_namespaced_build_log_log) | **GET** /oapi/v1/namespaces/{namespace}/builds/{name}/log | read log of the specified BuildLog
[**read_namespaced_cluster_network**](Oapiv1Api.md#read_namespaced_cluster_network) | **GET** /oapi/v1/clusternetworks/{name} | read the specified ClusterNetwork
[**read_namespaced_cluster_policy**](Oapiv1Api.md#read_namespaced_cluster_policy) | **GET** /oapi/v1/clusterpolicies/{name} | read the specified ClusterPolicy
[**read_namespaced_cluster_policy_binding**](Oapiv1Api.md#read_namespaced_cluster_policy_binding) | **GET** /oapi/v1/clusterpolicybindings/{name} | read the specified ClusterPolicyBinding
[**read_namespaced_cluster_role**](Oapiv1Api.md#read_namespaced_cluster_role) | **GET** /oapi/v1/clusterroles/{name} | read the specified ClusterRole
[**read_namespaced_cluster_role_binding**](Oapiv1Api.md#read_namespaced_cluster_role_binding) | **GET** /oapi/v1/clusterrolebindings/{name} | read the specified ClusterRoleBinding
[**read_namespaced_deployment_config**](Oapiv1Api.md#read_namespaced_deployment_config) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | read the specified DeploymentConfig
[**read_namespaced_deployment_config_0**](Oapiv1Api.md#read_namespaced_deployment_config_0) | **GET** /oapi/v1/namespaces/{namespace}/generatedeploymentconfigs/{name} | read the specified DeploymentConfig
[**read_namespaced_deployment_log_log**](Oapiv1Api.md#read_namespaced_deployment_log_log) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/log | read log of the specified DeploymentLog
[**read_namespaced_group**](Oapiv1Api.md#read_namespaced_group) | **GET** /oapi/v1/groups/{name} | read the specified Group
[**read_namespaced_host_subnet**](Oapiv1Api.md#read_namespaced_host_subnet) | **GET** /oapi/v1/hostsubnets/{name} | read the specified HostSubnet
[**read_namespaced_identity**](Oapiv1Api.md#read_namespaced_identity) | **GET** /oapi/v1/identities/{name} | read the specified Identity
[**read_namespaced_image**](Oapiv1Api.md#read_namespaced_image) | **GET** /oapi/v1/images/{name} | read the specified Image
[**read_namespaced_image_stream**](Oapiv1Api.md#read_namespaced_image_stream) | **GET** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | read the specified ImageStream
[**read_namespaced_image_stream_image**](Oapiv1Api.md#read_namespaced_image_stream_image) | **GET** /oapi/v1/namespaces/{namespace}/imagestreamimages/{name} | read the specified ImageStreamImage
[**read_namespaced_image_stream_tag**](Oapiv1Api.md#read_namespaced_image_stream_tag) | **GET** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | read the specified ImageStreamTag
[**read_namespaced_net_namespace**](Oapiv1Api.md#read_namespaced_net_namespace) | **GET** /oapi/v1/netnamespaces/{name} | read the specified NetNamespace
[**read_namespaced_o_auth_access_token**](Oapiv1Api.md#read_namespaced_o_auth_access_token) | **GET** /oapi/v1/oauthaccesstokens/{name} | read the specified OAuthAccessToken
[**read_namespaced_o_auth_authorize_token**](Oapiv1Api.md#read_namespaced_o_auth_authorize_token) | **GET** /oapi/v1/oauthauthorizetokens/{name} | read the specified OAuthAuthorizeToken
[**read_namespaced_o_auth_client**](Oapiv1Api.md#read_namespaced_o_auth_client) | **GET** /oapi/v1/oauthclients/{name} | read the specified OAuthClient
[**read_namespaced_o_auth_client_authorization**](Oapiv1Api.md#read_namespaced_o_auth_client_authorization) | **GET** /oapi/v1/oauthclientauthorizations/{name} | read the specified OAuthClientAuthorization
[**read_namespaced_policy**](Oapiv1Api.md#read_namespaced_policy) | **GET** /oapi/v1/namespaces/{namespace}/policies/{name} | read the specified Policy
[**read_namespaced_policy_binding**](Oapiv1Api.md#read_namespaced_policy_binding) | **GET** /oapi/v1/namespaces/{namespace}/policybindings/{name} | read the specified PolicyBinding
[**read_namespaced_project**](Oapiv1Api.md#read_namespaced_project) | **GET** /oapi/v1/projects/{name} | read the specified Project
[**read_namespaced_role**](Oapiv1Api.md#read_namespaced_role) | **GET** /oapi/v1/namespaces/{namespace}/roles/{name} | read the specified Role
[**read_namespaced_role_binding**](Oapiv1Api.md#read_namespaced_role_binding) | **GET** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | read the specified RoleBinding
[**read_namespaced_route**](Oapiv1Api.md#read_namespaced_route) | **GET** /oapi/v1/namespaces/{namespace}/routes/{name} | read the specified Route
[**read_namespaced_scale_scale**](Oapiv1Api.md#read_namespaced_scale_scale) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | read scale of the specified Scale
[**read_namespaced_secret_list_secrets**](Oapiv1Api.md#read_namespaced_secret_list_secrets) | **GET** /oapi/v1/namespaces/{namespace}/imagestreams/{name}/secrets | read secrets of the specified SecretList
[**read_namespaced_template**](Oapiv1Api.md#read_namespaced_template) | **GET** /oapi/v1/namespaces/{namespace}/templates/{name} | read the specified Template
[**read_namespaced_user**](Oapiv1Api.md#read_namespaced_user) | **GET** /oapi/v1/users/{name} | read the specified User
[**read_namespaced_user_identity_mapping**](Oapiv1Api.md#read_namespaced_user_identity_mapping) | **GET** /oapi/v1/useridentitymappings/{name} | read the specified UserIdentityMapping
[**replace_namespaced_build**](Oapiv1Api.md#replace_namespaced_build) | **PUT** /oapi/v1/namespaces/{namespace}/builds/{name} | replace the specified Build
[**replace_namespaced_build_config**](Oapiv1Api.md#replace_namespaced_build_config) | **PUT** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | replace the specified BuildConfig
[**replace_namespaced_build_details**](Oapiv1Api.md#replace_namespaced_build_details) | **PUT** /oapi/v1/namespaces/{namespace}/builds/{name}/details | replace details of the specified Build
[**replace_namespaced_cluster_network**](Oapiv1Api.md#replace_namespaced_cluster_network) | **PUT** /oapi/v1/clusternetworks/{name} | replace the specified ClusterNetwork
[**replace_namespaced_cluster_policy**](Oapiv1Api.md#replace_namespaced_cluster_policy) | **PUT** /oapi/v1/clusterpolicies/{name} | replace the specified ClusterPolicy
[**replace_namespaced_cluster_policy_binding**](Oapiv1Api.md#replace_namespaced_cluster_policy_binding) | **PUT** /oapi/v1/clusterpolicybindings/{name} | replace the specified ClusterPolicyBinding
[**replace_namespaced_cluster_role**](Oapiv1Api.md#replace_namespaced_cluster_role) | **PUT** /oapi/v1/clusterroles/{name} | replace the specified ClusterRole
[**replace_namespaced_cluster_role_binding**](Oapiv1Api.md#replace_namespaced_cluster_role_binding) | **PUT** /oapi/v1/clusterrolebindings/{name} | replace the specified ClusterRoleBinding
[**replace_namespaced_deployment_config**](Oapiv1Api.md#replace_namespaced_deployment_config) | **PUT** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | replace the specified DeploymentConfig
[**replace_namespaced_group**](Oapiv1Api.md#replace_namespaced_group) | **PUT** /oapi/v1/groups/{name} | replace the specified Group
[**replace_namespaced_host_subnet**](Oapiv1Api.md#replace_namespaced_host_subnet) | **PUT** /oapi/v1/hostsubnets/{name} | replace the specified HostSubnet
[**replace_namespaced_identity**](Oapiv1Api.md#replace_namespaced_identity) | **PUT** /oapi/v1/identities/{name} | replace the specified Identity
[**replace_namespaced_image**](Oapiv1Api.md#replace_namespaced_image) | **PUT** /oapi/v1/images/{name} | replace the specified Image
[**replace_namespaced_image_stream**](Oapiv1Api.md#replace_namespaced_image_stream) | **PUT** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | replace the specified ImageStream
[**replace_namespaced_image_stream_status**](Oapiv1Api.md#replace_namespaced_image_stream_status) | **PUT** /oapi/v1/namespaces/{namespace}/imagestreams/{name}/status | replace status of the specified ImageStream
[**replace_namespaced_image_stream_tag**](Oapiv1Api.md#replace_namespaced_image_stream_tag) | **PUT** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | replace the specified ImageStreamTag
[**replace_namespaced_net_namespace**](Oapiv1Api.md#replace_namespaced_net_namespace) | **PUT** /oapi/v1/netnamespaces/{name} | replace the specified NetNamespace
[**replace_namespaced_o_auth_client**](Oapiv1Api.md#replace_namespaced_o_auth_client) | **PUT** /oapi/v1/oauthclients/{name} | replace the specified OAuthClient
[**replace_namespaced_o_auth_client_authorization**](Oapiv1Api.md#replace_namespaced_o_auth_client_authorization) | **PUT** /oapi/v1/oauthclientauthorizations/{name} | replace the specified OAuthClientAuthorization
[**replace_namespaced_policy**](Oapiv1Api.md#replace_namespaced_policy) | **PUT** /oapi/v1/namespaces/{namespace}/policies/{name} | replace the specified Policy
[**replace_namespaced_policy_binding**](Oapiv1Api.md#replace_namespaced_policy_binding) | **PUT** /oapi/v1/namespaces/{namespace}/policybindings/{name} | replace the specified PolicyBinding
[**replace_namespaced_project**](Oapiv1Api.md#replace_namespaced_project) | **PUT** /oapi/v1/projects/{name} | replace the specified Project
[**replace_namespaced_role**](Oapiv1Api.md#replace_namespaced_role) | **PUT** /oapi/v1/namespaces/{namespace}/roles/{name} | replace the specified Role
[**replace_namespaced_role_binding**](Oapiv1Api.md#replace_namespaced_role_binding) | **PUT** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | replace the specified RoleBinding
[**replace_namespaced_route**](Oapiv1Api.md#replace_namespaced_route) | **PUT** /oapi/v1/namespaces/{namespace}/routes/{name} | replace the specified Route
[**replace_namespaced_route_status**](Oapiv1Api.md#replace_namespaced_route_status) | **PUT** /oapi/v1/namespaces/{namespace}/routes/{name}/status | replace status of the specified Route
[**replace_namespaced_scale_scale**](Oapiv1Api.md#replace_namespaced_scale_scale) | **PUT** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | replace scale of the specified Scale
[**replace_namespaced_template**](Oapiv1Api.md#replace_namespaced_template) | **PUT** /oapi/v1/namespaces/{namespace}/templates/{name} | replace the specified Template
[**replace_namespaced_user**](Oapiv1Api.md#replace_namespaced_user) | **PUT** /oapi/v1/users/{name} | replace the specified User
[**replace_namespaced_user_identity_mapping**](Oapiv1Api.md#replace_namespaced_user_identity_mapping) | **PUT** /oapi/v1/useridentitymappings/{name} | replace the specified UserIdentityMapping
[**watch_build_config_list**](Oapiv1Api.md#watch_build_config_list) | **GET** /oapi/v1/watch/buildconfigs | watch individual changes to a list of BuildConfig
[**watch_build_list**](Oapiv1Api.md#watch_build_list) | **GET** /oapi/v1/watch/builds | watch individual changes to a list of Build
[**watch_deployment_config_list**](Oapiv1Api.md#watch_deployment_config_list) | **GET** /oapi/v1/watch/deploymentconfigs | watch individual changes to a list of DeploymentConfig
[**watch_image_stream_list**](Oapiv1Api.md#watch_image_stream_list) | **GET** /oapi/v1/watch/imagestreams | watch individual changes to a list of ImageStream
[**watch_namespaced_build**](Oapiv1Api.md#watch_namespaced_build) | **GET** /oapi/v1/watch/namespaces/{namespace}/builds/{name} | watch changes to an object of kind Build
[**watch_namespaced_build_config**](Oapiv1Api.md#watch_namespaced_build_config) | **GET** /oapi/v1/watch/namespaces/{namespace}/buildconfigs/{name} | watch changes to an object of kind BuildConfig
[**watch_namespaced_build_config_list**](Oapiv1Api.md#watch_namespaced_build_config_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/buildconfigs | watch individual changes to a list of BuildConfig
[**watch_namespaced_build_list**](Oapiv1Api.md#watch_namespaced_build_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/builds | watch individual changes to a list of Build
[**watch_namespaced_cluster_network**](Oapiv1Api.md#watch_namespaced_cluster_network) | **GET** /oapi/v1/watch/clusternetworks/{name} | watch changes to an object of kind ClusterNetwork
[**watch_namespaced_cluster_network_list**](Oapiv1Api.md#watch_namespaced_cluster_network_list) | **GET** /oapi/v1/watch/clusternetworks | watch individual changes to a list of ClusterNetwork
[**watch_namespaced_cluster_policy**](Oapiv1Api.md#watch_namespaced_cluster_policy) | **GET** /oapi/v1/watch/clusterpolicies/{name} | watch changes to an object of kind ClusterPolicy
[**watch_namespaced_cluster_policy_binding**](Oapiv1Api.md#watch_namespaced_cluster_policy_binding) | **GET** /oapi/v1/watch/clusterpolicybindings/{name} | watch changes to an object of kind ClusterPolicyBinding
[**watch_namespaced_cluster_policy_binding_list**](Oapiv1Api.md#watch_namespaced_cluster_policy_binding_list) | **GET** /oapi/v1/watch/clusterpolicybindings | watch individual changes to a list of ClusterPolicyBinding
[**watch_namespaced_cluster_policy_list**](Oapiv1Api.md#watch_namespaced_cluster_policy_list) | **GET** /oapi/v1/watch/clusterpolicies | watch individual changes to a list of ClusterPolicy
[**watch_namespaced_deployment_config**](Oapiv1Api.md#watch_namespaced_deployment_config) | **GET** /oapi/v1/watch/namespaces/{namespace}/deploymentconfigs/{name} | watch changes to an object of kind DeploymentConfig
[**watch_namespaced_deployment_config_list**](Oapiv1Api.md#watch_namespaced_deployment_config_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/deploymentconfigs | watch individual changes to a list of DeploymentConfig
[**watch_namespaced_group**](Oapiv1Api.md#watch_namespaced_group) | **GET** /oapi/v1/watch/groups/{name} | watch changes to an object of kind Group
[**watch_namespaced_group_list**](Oapiv1Api.md#watch_namespaced_group_list) | **GET** /oapi/v1/watch/groups | watch individual changes to a list of Group
[**watch_namespaced_host_subnet**](Oapiv1Api.md#watch_namespaced_host_subnet) | **GET** /oapi/v1/watch/hostsubnets/{name} | watch changes to an object of kind HostSubnet
[**watch_namespaced_host_subnet_list**](Oapiv1Api.md#watch_namespaced_host_subnet_list) | **GET** /oapi/v1/watch/hostsubnets | watch individual changes to a list of HostSubnet
[**watch_namespaced_identity**](Oapiv1Api.md#watch_namespaced_identity) | **GET** /oapi/v1/watch/identities/{name} | watch changes to an object of kind Identity
[**watch_namespaced_identity_list**](Oapiv1Api.md#watch_namespaced_identity_list) | **GET** /oapi/v1/watch/identities | watch individual changes to a list of Identity
[**watch_namespaced_image**](Oapiv1Api.md#watch_namespaced_image) | **GET** /oapi/v1/watch/images/{name} | watch changes to an object of kind Image
[**watch_namespaced_image_list**](Oapiv1Api.md#watch_namespaced_image_list) | **GET** /oapi/v1/watch/images | watch individual changes to a list of Image
[**watch_namespaced_image_stream**](Oapiv1Api.md#watch_namespaced_image_stream) | **GET** /oapi/v1/watch/namespaces/{namespace}/imagestreams/{name} | watch changes to an object of kind ImageStream
[**watch_namespaced_image_stream_list**](Oapiv1Api.md#watch_namespaced_image_stream_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/imagestreams | watch individual changes to a list of ImageStream
[**watch_namespaced_net_namespace**](Oapiv1Api.md#watch_namespaced_net_namespace) | **GET** /oapi/v1/watch/netnamespaces/{name} | watch changes to an object of kind NetNamespace
[**watch_namespaced_net_namespace_list**](Oapiv1Api.md#watch_namespaced_net_namespace_list) | **GET** /oapi/v1/watch/netnamespaces | watch individual changes to a list of NetNamespace
[**watch_namespaced_o_auth_client**](Oapiv1Api.md#watch_namespaced_o_auth_client) | **GET** /oapi/v1/watch/oauthclients/{name} | watch changes to an object of kind OAuthClient
[**watch_namespaced_o_auth_client_authorization**](Oapiv1Api.md#watch_namespaced_o_auth_client_authorization) | **GET** /oapi/v1/watch/oauthclientauthorizations/{name} | watch changes to an object of kind OAuthClientAuthorization
[**watch_namespaced_o_auth_client_authorization_list**](Oapiv1Api.md#watch_namespaced_o_auth_client_authorization_list) | **GET** /oapi/v1/watch/oauthclientauthorizations | watch individual changes to a list of OAuthClientAuthorization
[**watch_namespaced_o_auth_client_list**](Oapiv1Api.md#watch_namespaced_o_auth_client_list) | **GET** /oapi/v1/watch/oauthclients | watch individual changes to a list of OAuthClient
[**watch_namespaced_policy**](Oapiv1Api.md#watch_namespaced_policy) | **GET** /oapi/v1/watch/namespaces/{namespace}/policies/{name} | watch changes to an object of kind Policy
[**watch_namespaced_policy_binding**](Oapiv1Api.md#watch_namespaced_policy_binding) | **GET** /oapi/v1/watch/namespaces/{namespace}/policybindings/{name} | watch changes to an object of kind PolicyBinding
[**watch_namespaced_policy_binding_list**](Oapiv1Api.md#watch_namespaced_policy_binding_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/policybindings | watch individual changes to a list of PolicyBinding
[**watch_namespaced_policy_list**](Oapiv1Api.md#watch_namespaced_policy_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/policies | watch individual changes to a list of Policy
[**watch_namespaced_route**](Oapiv1Api.md#watch_namespaced_route) | **GET** /oapi/v1/watch/namespaces/{namespace}/routes/{name} | watch changes to an object of kind Route
[**watch_namespaced_route_list**](Oapiv1Api.md#watch_namespaced_route_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/routes | watch individual changes to a list of Route
[**watch_namespaced_template**](Oapiv1Api.md#watch_namespaced_template) | **GET** /oapi/v1/watch/namespaces/{namespace}/templates/{name} | watch changes to an object of kind Template
[**watch_namespaced_template_list**](Oapiv1Api.md#watch_namespaced_template_list) | **GET** /oapi/v1/watch/namespaces/{namespace}/templates | watch individual changes to a list of Template
[**watch_namespaced_user**](Oapiv1Api.md#watch_namespaced_user) | **GET** /oapi/v1/watch/users/{name} | watch changes to an object of kind User
[**watch_namespaced_user_list**](Oapiv1Api.md#watch_namespaced_user_list) | **GET** /oapi/v1/watch/users | watch individual changes to a list of User
[**watch_policy_binding_list**](Oapiv1Api.md#watch_policy_binding_list) | **GET** /oapi/v1/watch/policybindings | watch individual changes to a list of PolicyBinding
[**watch_policy_list**](Oapiv1Api.md#watch_policy_list) | **GET** /oapi/v1/watch/policies | watch individual changes to a list of Policy
[**watch_route_list**](Oapiv1Api.md#watch_route_list) | **GET** /oapi/v1/watch/routes | watch individual changes to a list of Route
[**watch_template_list**](Oapiv1Api.md#watch_template_list) | **GET** /oapi/v1/watch/templates | watch individual changes to a list of Template


# **create_build**
> V1Build create_build(body, pretty=pretty)

create a Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Build() # V1Build | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Build
    api_response = api_instance.create_build(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_build: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Build**](V1Build.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_config**
> V1BuildConfig create_build_config(body, pretty=pretty)

create a BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1BuildConfig() # V1BuildConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a BuildConfig
    api_response = api_instance.create_build_config(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_build_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildConfig**](V1BuildConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment_config**
> V1DeploymentConfig create_deployment_config(body, pretty=pretty)

create a DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeploymentConfig() # V1DeploymentConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfig
    api_response = api_instance.create_deployment_config(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_deployment_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentConfig**](V1DeploymentConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment_config_rollback**
> V1DeploymentConfigRollback create_deployment_config_rollback(body, pretty=pretty)

create a DeploymentConfigRollback

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeploymentConfigRollback() # V1DeploymentConfigRollback | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfigRollback
    api_response = api_instance.create_deployment_config_rollback(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_deployment_config_rollback: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentConfigRollback**](V1DeploymentConfigRollback.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfigRollback**](V1DeploymentConfigRollback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_stream**
> V1ImageStream create_image_stream(body, pretty=pretty)

create a ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStream() # V1ImageStream | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStream
    api_response = api_instance.create_image_stream(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_image_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_stream_import**
> V1ImageStreamImport create_image_stream_import(body, pretty=pretty)

create a ImageStreamImport

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStreamImport() # V1ImageStreamImport | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamImport
    api_response = api_instance.create_image_stream_import(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_image_stream_import: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamImport**](V1ImageStreamImport.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamImport**](V1ImageStreamImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_stream_mapping**
> V1ImageStreamMapping create_image_stream_mapping(body, pretty=pretty)

create a ImageStreamMapping

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStreamMapping() # V1ImageStreamMapping | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamMapping
    api_response = api_instance.create_image_stream_mapping(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_image_stream_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamMapping**](V1ImageStreamMapping.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamMapping**](V1ImageStreamMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_local_resource_access_review**
> V1LocalResourceAccessReview create_local_resource_access_review(body, pretty=pretty)

create a LocalResourceAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1LocalResourceAccessReview() # V1LocalResourceAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalResourceAccessReview
    api_response = api_instance.create_local_resource_access_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_local_resource_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LocalResourceAccessReview**](V1LocalResourceAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LocalResourceAccessReview**](V1LocalResourceAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_local_subject_access_review**
> V1LocalSubjectAccessReview create_local_subject_access_review(body, pretty=pretty)

create a LocalSubjectAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1LocalSubjectAccessReview() # V1LocalSubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalSubjectAccessReview
    api_response = api_instance.create_local_subject_access_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_local_subject_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_build**
> V1Build create_namespaced_build(body, namespace, pretty=pretty)

create a Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Build() # V1Build | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Build
    api_response = api_instance.create_namespaced_build(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_build: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Build**](V1Build.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_build_config**
> V1BuildConfig create_namespaced_build_config(body, namespace, pretty=pretty)

create a BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1BuildConfig() # V1BuildConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a BuildConfig
    api_response = api_instance.create_namespaced_build_config(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_build_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildConfig**](V1BuildConfig.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_build_request_clone**
> V1BuildRequest create_namespaced_build_request_clone(body, namespace, name, pretty=pretty)

create clone of a BuildRequest

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1BuildRequest() # V1BuildRequest | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildRequest
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create clone of a BuildRequest
    api_response = api_instance.create_namespaced_build_request_clone(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_build_request_clone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildRequest**](V1BuildRequest.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildRequest | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildRequest**](V1BuildRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_build_request_instantiate**
> V1BuildRequest create_namespaced_build_request_instantiate(body, namespace, name, pretty=pretty)

create instantiate of a BuildRequest

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1BuildRequest() # V1BuildRequest | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildRequest
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create instantiate of a BuildRequest
    api_response = api_instance.create_namespaced_build_request_instantiate(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_build_request_instantiate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildRequest**](V1BuildRequest.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildRequest | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildRequest**](V1BuildRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_cluster_network**
> V1ClusterNetwork create_namespaced_cluster_network(body, pretty=pretty)

create a ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterNetwork() # V1ClusterNetwork | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterNetwork
    api_response = api_instance.create_namespaced_cluster_network(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_cluster_network: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterNetwork**](V1ClusterNetwork.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_cluster_policy**
> V1ClusterPolicy create_namespaced_cluster_policy(body, pretty=pretty)

create a ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterPolicy() # V1ClusterPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterPolicy
    api_response = api_instance.create_namespaced_cluster_policy(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_cluster_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterPolicy**](V1ClusterPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterPolicy**](V1ClusterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_cluster_policy_binding**
> V1ClusterPolicyBinding create_namespaced_cluster_policy_binding(body, pretty=pretty)

create a ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterPolicyBinding() # V1ClusterPolicyBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterPolicyBinding
    api_response = api_instance.create_namespaced_cluster_policy_binding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_cluster_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterPolicyBinding**](V1ClusterPolicyBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterPolicyBinding**](V1ClusterPolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_cluster_role**
> V1ClusterRole create_namespaced_cluster_role(body, pretty=pretty)

create a ClusterRole

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterRole() # V1ClusterRole | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterRole
    api_response = api_instance.create_namespaced_cluster_role(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_cluster_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterRole**](V1ClusterRole.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRole**](V1ClusterRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_cluster_role_binding**
> V1ClusterRoleBinding create_namespaced_cluster_role_binding(body, pretty=pretty)

create a ClusterRoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterRoleBinding() # V1ClusterRoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterRoleBinding
    api_response = api_instance.create_namespaced_cluster_role_binding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_cluster_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterRoleBinding**](V1ClusterRoleBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRoleBinding**](V1ClusterRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment_config**
> V1DeploymentConfig create_namespaced_deployment_config(body, namespace, pretty=pretty)

create a DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeploymentConfig() # V1DeploymentConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfig
    api_response = api_instance.create_namespaced_deployment_config(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_deployment_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentConfig**](V1DeploymentConfig.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment_config_rollback**
> V1DeploymentConfigRollback create_namespaced_deployment_config_rollback(body, namespace, pretty=pretty)

create a DeploymentConfigRollback

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeploymentConfigRollback() # V1DeploymentConfigRollback | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfigRollback
    api_response = api_instance.create_namespaced_deployment_config_rollback(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_deployment_config_rollback: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentConfigRollback**](V1DeploymentConfigRollback.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfigRollback**](V1DeploymentConfigRollback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_group**
> V1Group create_namespaced_group(body, pretty=pretty)

create a Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Group() # V1Group | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Group
    api_response = api_instance.create_namespaced_group(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Group**](V1Group.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Group**](V1Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_host_subnet**
> V1HostSubnet create_namespaced_host_subnet(body, pretty=pretty)

create a HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1HostSubnet() # V1HostSubnet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a HostSubnet
    api_response = api_instance.create_namespaced_host_subnet(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_host_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HostSubnet**](V1HostSubnet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_identity**
> V1Identity create_namespaced_identity(body, pretty=pretty)

create a Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Identity() # V1Identity | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Identity
    api_response = api_instance.create_namespaced_identity(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_identity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Identity**](V1Identity.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Identity**](V1Identity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_image**
> V1Image create_namespaced_image(body, pretty=pretty)

create a Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Image() # V1Image | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Image
    api_response = api_instance.create_namespaced_image(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Image**](V1Image.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_image_stream**
> V1ImageStream create_namespaced_image_stream(body, namespace, pretty=pretty)

create a ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStream() # V1ImageStream | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStream
    api_response = api_instance.create_namespaced_image_stream(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_image_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_image_stream_import**
> V1ImageStreamImport create_namespaced_image_stream_import(body, namespace, pretty=pretty)

create a ImageStreamImport

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStreamImport() # V1ImageStreamImport | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamImport
    api_response = api_instance.create_namespaced_image_stream_import(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_image_stream_import: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamImport**](V1ImageStreamImport.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamImport**](V1ImageStreamImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_image_stream_mapping**
> V1ImageStreamMapping create_namespaced_image_stream_mapping(body, namespace, pretty=pretty)

create a ImageStreamMapping

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStreamMapping() # V1ImageStreamMapping | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamMapping
    api_response = api_instance.create_namespaced_image_stream_mapping(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_image_stream_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamMapping**](V1ImageStreamMapping.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamMapping**](V1ImageStreamMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_local_resource_access_review**
> V1LocalResourceAccessReview create_namespaced_local_resource_access_review(body, namespace, pretty=pretty)

create a LocalResourceAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1LocalResourceAccessReview() # V1LocalResourceAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalResourceAccessReview
    api_response = api_instance.create_namespaced_local_resource_access_review(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_local_resource_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LocalResourceAccessReview**](V1LocalResourceAccessReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LocalResourceAccessReview**](V1LocalResourceAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_local_subject_access_review**
> V1LocalSubjectAccessReview create_namespaced_local_subject_access_review(body, namespace, pretty=pretty)

create a LocalSubjectAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1LocalSubjectAccessReview() # V1LocalSubjectAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalSubjectAccessReview
    api_response = api_instance.create_namespaced_local_subject_access_review(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_local_subject_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_net_namespace**
> V1NetNamespace create_namespaced_net_namespace(body, pretty=pretty)

create a NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1NetNamespace() # V1NetNamespace | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a NetNamespace
    api_response = api_instance.create_namespaced_net_namespace(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_net_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetNamespace**](V1NetNamespace.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_o_auth_access_token**
> V1OAuthAccessToken create_namespaced_o_auth_access_token(body, pretty=pretty)

create a OAuthAccessToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1OAuthAccessToken() # V1OAuthAccessToken | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthAccessToken
    api_response = api_instance.create_namespaced_o_auth_access_token(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_o_auth_access_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1OAuthAccessToken**](V1OAuthAccessToken.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthAccessToken**](V1OAuthAccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_o_auth_authorize_token**
> V1OAuthAuthorizeToken create_namespaced_o_auth_authorize_token(body, pretty=pretty)

create a OAuthAuthorizeToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1OAuthAuthorizeToken() # V1OAuthAuthorizeToken | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthAuthorizeToken
    api_response = api_instance.create_namespaced_o_auth_authorize_token(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_o_auth_authorize_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1OAuthAuthorizeToken**](V1OAuthAuthorizeToken.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthAuthorizeToken**](V1OAuthAuthorizeToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_o_auth_client**
> V1OAuthClient create_namespaced_o_auth_client(body, pretty=pretty)

create a OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1OAuthClient() # V1OAuthClient | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthClient
    api_response = api_instance.create_namespaced_o_auth_client(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_o_auth_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1OAuthClient**](V1OAuthClient.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthClient**](V1OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_o_auth_client_authorization**
> V1OAuthClientAuthorization create_namespaced_o_auth_client_authorization(body, pretty=pretty)

create a OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1OAuthClientAuthorization() # V1OAuthClientAuthorization | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthClientAuthorization
    api_response = api_instance.create_namespaced_o_auth_client_authorization(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_o_auth_client_authorization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1OAuthClientAuthorization**](V1OAuthClientAuthorization.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthClientAuthorization**](V1OAuthClientAuthorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_policy**
> V1Policy create_namespaced_policy(body, namespace, pretty=pretty)

create a Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Policy() # V1Policy | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Policy
    api_response = api_instance.create_namespaced_policy(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Policy**](V1Policy.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Policy**](V1Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_policy_binding**
> V1PolicyBinding create_namespaced_policy_binding(body, namespace, pretty=pretty)

create a PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1PolicyBinding() # V1PolicyBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PolicyBinding
    api_response = api_instance.create_namespaced_policy_binding(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PolicyBinding**](V1PolicyBinding.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PolicyBinding**](V1PolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_project**
> V1Project create_namespaced_project(body, pretty=pretty)

create a Project

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Project() # V1Project | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Project
    api_response = api_instance.create_namespaced_project(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_project: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Project**](V1Project.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_project_request**
> V1ProjectRequest create_namespaced_project_request(body, pretty=pretty)

create a ProjectRequest

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ProjectRequest() # V1ProjectRequest | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ProjectRequest
    api_response = api_instance.create_namespaced_project_request(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_project_request: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ProjectRequest**](V1ProjectRequest.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ProjectRequest**](V1ProjectRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_resource_access_review**
> V1ResourceAccessReview create_namespaced_resource_access_review(body, namespace, pretty=pretty)

create a ResourceAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ResourceAccessReview() # V1ResourceAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ResourceAccessReview
    api_response = api_instance.create_namespaced_resource_access_review(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_resource_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ResourceAccessReview**](V1ResourceAccessReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ResourceAccessReview**](V1ResourceAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_role**
> V1Role create_namespaced_role(body, namespace, pretty=pretty)

create a Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Role() # V1Role | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Role
    api_response = api_instance.create_namespaced_role(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Role**](V1Role.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Role**](V1Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_role_binding**
> V1RoleBinding create_namespaced_role_binding(body, namespace, pretty=pretty)

create a RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1RoleBinding() # V1RoleBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a RoleBinding
    api_response = api_instance.create_namespaced_role_binding(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RoleBinding**](V1RoleBinding.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1RoleBinding**](V1RoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_route**
> V1Route create_namespaced_route(body, namespace, pretty=pretty)

create a Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Route() # V1Route | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Route
    api_response = api_instance.create_namespaced_route(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Route**](V1Route.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Route**](V1Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_subject_access_review**
> V1SubjectAccessReview create_namespaced_subject_access_review(body, namespace, pretty=pretty)

create a SubjectAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1SubjectAccessReview() # V1SubjectAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a SubjectAccessReview
    api_response = api_instance.create_namespaced_subject_access_review(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_subject_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SubjectAccessReview**](V1SubjectAccessReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SubjectAccessReview**](V1SubjectAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_template**
> V1Template create_namespaced_template(body, namespace, pretty=pretty)

create a Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Template() # V1Template | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_namespaced_template(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Template**](V1Template.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_template_0**
> V1Template create_namespaced_template_0(body, namespace, pretty=pretty)

create a Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Template() # V1Template | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_namespaced_template_0(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_template_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Template**](V1Template.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_user**
> V1User create_namespaced_user(body, pretty=pretty)

create a User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1User() # V1User | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a User
    api_response = api_instance.create_namespaced_user(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1User**](V1User.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_user_identity_mapping**
> V1UserIdentityMapping create_namespaced_user_identity_mapping(body, pretty=pretty)

create a UserIdentityMapping

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1UserIdentityMapping() # V1UserIdentityMapping | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a UserIdentityMapping
    api_response = api_instance.create_namespaced_user_identity_mapping(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_namespaced_user_identity_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UserIdentityMapping**](V1UserIdentityMapping.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1UserIdentityMapping**](V1UserIdentityMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> V1Policy create_policy(body, pretty=pretty)

create a Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Policy() # V1Policy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Policy
    api_response = api_instance.create_policy(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Policy**](V1Policy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Policy**](V1Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_binding**
> V1PolicyBinding create_policy_binding(body, pretty=pretty)

create a PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1PolicyBinding() # V1PolicyBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PolicyBinding
    api_response = api_instance.create_policy_binding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PolicyBinding**](V1PolicyBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PolicyBinding**](V1PolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resource_access_review**
> V1ResourceAccessReview create_resource_access_review(body, pretty=pretty)

create a ResourceAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ResourceAccessReview() # V1ResourceAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ResourceAccessReview
    api_response = api_instance.create_resource_access_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_resource_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ResourceAccessReview**](V1ResourceAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ResourceAccessReview**](V1ResourceAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> V1Role create_role(body, pretty=pretty)

create a Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Role() # V1Role | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Role
    api_response = api_instance.create_role(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Role**](V1Role.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Role**](V1Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_binding**
> V1RoleBinding create_role_binding(body, pretty=pretty)

create a RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1RoleBinding() # V1RoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a RoleBinding
    api_response = api_instance.create_role_binding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RoleBinding**](V1RoleBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1RoleBinding**](V1RoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route**
> V1Route create_route(body, pretty=pretty)

create a Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Route() # V1Route | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Route
    api_response = api_instance.create_route(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Route**](V1Route.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Route**](V1Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subject_access_review**
> V1SubjectAccessReview create_subject_access_review(body, pretty=pretty)

create a SubjectAccessReview

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1SubjectAccessReview() # V1SubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a SubjectAccessReview
    api_response = api_instance.create_subject_access_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_subject_access_review: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SubjectAccessReview**](V1SubjectAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SubjectAccessReview**](V1SubjectAccessReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> V1Template create_template(body, pretty=pretty)

create a Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Template() # V1Template | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_template(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Template**](V1Template.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_0**
> V1Template create_template_0(body, pretty=pretty)

create a Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Template() # V1Template | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_template_0(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->create_template_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Template**](V1Template.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_build**
> UnversionedStatus delete_namespaced_build(body, namespace, name, pretty=pretty)

delete a Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Build
    api_response = api_instance.delete_namespaced_build(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_build: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Build | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_build_config**
> UnversionedStatus delete_namespaced_build_config(body, namespace, name, pretty=pretty)

delete a BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a BuildConfig
    api_response = api_instance.delete_namespaced_build_config(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_build_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cluster_network**
> UnversionedStatus delete_namespaced_cluster_network(body, name, pretty=pretty)

delete a ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterNetwork
    api_response = api_instance.delete_namespaced_cluster_network(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_cluster_network: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the ClusterNetwork | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cluster_policy**
> UnversionedStatus delete_namespaced_cluster_policy(body, name, pretty=pretty)

delete a ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterPolicy
    api_response = api_instance.delete_namespaced_cluster_policy(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_cluster_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the ClusterPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cluster_policy_binding**
> UnversionedStatus delete_namespaced_cluster_policy_binding(body, name, pretty=pretty)

delete a ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterPolicyBinding
    api_response = api_instance.delete_namespaced_cluster_policy_binding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_cluster_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the ClusterPolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cluster_role**
> UnversionedStatus delete_namespaced_cluster_role(body, name, pretty=pretty)

delete a ClusterRole

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterRole
    api_response = api_instance.delete_namespaced_cluster_role(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_cluster_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the ClusterRole | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cluster_role_binding**
> UnversionedStatus delete_namespaced_cluster_role_binding(body, name, pretty=pretty)

delete a ClusterRoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterRoleBinding
    api_response = api_instance.delete_namespaced_cluster_role_binding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_cluster_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the ClusterRoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_deployment_config**
> UnversionedStatus delete_namespaced_deployment_config(body, namespace, name, pretty=pretty)

delete a DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a DeploymentConfig
    api_response = api_instance.delete_namespaced_deployment_config(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_deployment_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_group**
> UnversionedStatus delete_namespaced_group(body, name, pretty=pretty)

delete a Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Group
    api_response = api_instance.delete_namespaced_group(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the Group | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_host_subnet**
> UnversionedStatus delete_namespaced_host_subnet(body, name, pretty=pretty)

delete a HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a HostSubnet
    api_response = api_instance.delete_namespaced_host_subnet(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_host_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the HostSubnet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_identity**
> UnversionedStatus delete_namespaced_identity(body, name, pretty=pretty)

delete a Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Identity
    api_response = api_instance.delete_namespaced_identity(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_identity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the Identity | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_image**
> UnversionedStatus delete_namespaced_image(body, name, pretty=pretty)

delete a Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Image
    api_response = api_instance.delete_namespaced_image(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the Image | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_image_stream**
> UnversionedStatus delete_namespaced_image_stream(body, namespace, name, pretty=pretty)

delete a ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ImageStream
    api_response = api_instance.delete_namespaced_image_stream(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_image_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStream | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_image_stream_tag**
> UnversionedStatus delete_namespaced_image_stream_tag(namespace, name, pretty=pretty)

delete a ImageStreamTag

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ImageStreamTag
    api_response = api_instance.delete_namespaced_image_stream_tag(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_image_stream_tag: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStreamTag | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_net_namespace**
> UnversionedStatus delete_namespaced_net_namespace(body, name, pretty=pretty)

delete a NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a NetNamespace
    api_response = api_instance.delete_namespaced_net_namespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_net_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the NetNamespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_o_auth_access_token**
> UnversionedStatus delete_namespaced_o_auth_access_token(body, name, pretty=pretty)

delete a OAuthAccessToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthAccessToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthAccessToken
    api_response = api_instance.delete_namespaced_o_auth_access_token(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_o_auth_access_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the OAuthAccessToken | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_o_auth_authorize_token**
> UnversionedStatus delete_namespaced_o_auth_authorize_token(body, name, pretty=pretty)

delete a OAuthAuthorizeToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthAuthorizeToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthAuthorizeToken
    api_response = api_instance.delete_namespaced_o_auth_authorize_token(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_o_auth_authorize_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the OAuthAuthorizeToken | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_o_auth_client**
> UnversionedStatus delete_namespaced_o_auth_client(body, name, pretty=pretty)

delete a OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthClient
    api_response = api_instance.delete_namespaced_o_auth_client(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_o_auth_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the OAuthClient | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_o_auth_client_authorization**
> UnversionedStatus delete_namespaced_o_auth_client_authorization(body, name, pretty=pretty)

delete a OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthClientAuthorization
    api_response = api_instance.delete_namespaced_o_auth_client_authorization(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_o_auth_client_authorization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the OAuthClientAuthorization | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_policy**
> UnversionedStatus delete_namespaced_policy(body, namespace, name, pretty=pretty)

delete a Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Policy
    api_response = api_instance.delete_namespaced_policy(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Policy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_policy_binding**
> UnversionedStatus delete_namespaced_policy_binding(body, namespace, name, pretty=pretty)

delete a PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a PolicyBinding
    api_response = api_instance.delete_namespaced_policy_binding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_project**
> UnversionedStatus delete_namespaced_project(name, pretty=pretty)

delete a Project

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Project
    api_response = api_instance.delete_namespaced_project(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_project: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Project | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_role**
> UnversionedStatus delete_namespaced_role(body, namespace, name, pretty=pretty)

delete a Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Role
    api_response = api_instance.delete_namespaced_role(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Role | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_role_binding**
> UnversionedStatus delete_namespaced_role_binding(body, namespace, name, pretty=pretty)

delete a RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a RoleBinding
    api_response = api_instance.delete_namespaced_role_binding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the RoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_route**
> UnversionedStatus delete_namespaced_route(body, namespace, name, pretty=pretty)

delete a Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Route
    api_response = api_instance.delete_namespaced_route(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Route | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_template**
> UnversionedStatus delete_namespaced_template(body, namespace, name, pretty=pretty)

delete a Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Template
    api_response = api_instance.delete_namespaced_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Template | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_user**
> UnversionedStatus delete_namespaced_user(body, name, pretty=pretty)

delete a User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a User
    api_response = api_instance.delete_namespaced_user(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the User | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_user_identity_mapping**
> UnversionedStatus delete_namespaced_user_identity_mapping(name, pretty=pretty)

delete a UserIdentityMapping

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a UserIdentityMapping
    api_response = api_instance.delete_namespaced_user_identity_mapping(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->delete_namespaced_user_identity_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the UserIdentityMapping | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_build**
> UnversionedStatus deletecollection_namespaced_build(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Build
    api_response = api_instance.deletecollection_namespaced_build(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_build: %s\n" % e
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

# **deletecollection_namespaced_build_config**
> UnversionedStatus deletecollection_namespaced_build_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of BuildConfig
    api_response = api_instance.deletecollection_namespaced_build_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_build_config: %s\n" % e
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

# **deletecollection_namespaced_cluster_network**
> UnversionedStatus deletecollection_namespaced_cluster_network(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ClusterNetwork
    api_response = api_instance.deletecollection_namespaced_cluster_network(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_cluster_network: %s\n" % e
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

# **deletecollection_namespaced_cluster_policy**
> UnversionedStatus deletecollection_namespaced_cluster_policy(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ClusterPolicy
    api_response = api_instance.deletecollection_namespaced_cluster_policy(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_cluster_policy: %s\n" % e
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

# **deletecollection_namespaced_cluster_policy_binding**
> UnversionedStatus deletecollection_namespaced_cluster_policy_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ClusterPolicyBinding
    api_response = api_instance.deletecollection_namespaced_cluster_policy_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_cluster_policy_binding: %s\n" % e
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

# **deletecollection_namespaced_deployment_config**
> UnversionedStatus deletecollection_namespaced_deployment_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of DeploymentConfig
    api_response = api_instance.deletecollection_namespaced_deployment_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_deployment_config: %s\n" % e
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

# **deletecollection_namespaced_group**
> UnversionedStatus deletecollection_namespaced_group(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Group
    api_response = api_instance.deletecollection_namespaced_group(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_group: %s\n" % e
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

# **deletecollection_namespaced_host_subnet**
> UnversionedStatus deletecollection_namespaced_host_subnet(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of HostSubnet
    api_response = api_instance.deletecollection_namespaced_host_subnet(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_host_subnet: %s\n" % e
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

# **deletecollection_namespaced_identity**
> UnversionedStatus deletecollection_namespaced_identity(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Identity
    api_response = api_instance.deletecollection_namespaced_identity(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_identity: %s\n" % e
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

# **deletecollection_namespaced_image**
> UnversionedStatus deletecollection_namespaced_image(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Image
    api_response = api_instance.deletecollection_namespaced_image(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_image: %s\n" % e
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

# **deletecollection_namespaced_image_stream**
> UnversionedStatus deletecollection_namespaced_image_stream(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ImageStream
    api_response = api_instance.deletecollection_namespaced_image_stream(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_image_stream: %s\n" % e
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

# **deletecollection_namespaced_net_namespace**
> UnversionedStatus deletecollection_namespaced_net_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of NetNamespace
    api_response = api_instance.deletecollection_namespaced_net_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_net_namespace: %s\n" % e
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

# **deletecollection_namespaced_o_auth_client**
> UnversionedStatus deletecollection_namespaced_o_auth_client(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of OAuthClient
    api_response = api_instance.deletecollection_namespaced_o_auth_client(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_o_auth_client: %s\n" % e
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

# **deletecollection_namespaced_o_auth_client_authorization**
> UnversionedStatus deletecollection_namespaced_o_auth_client_authorization(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of OAuthClientAuthorization
    api_response = api_instance.deletecollection_namespaced_o_auth_client_authorization(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_o_auth_client_authorization: %s\n" % e
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

# **deletecollection_namespaced_policy**
> UnversionedStatus deletecollection_namespaced_policy(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Policy
    api_response = api_instance.deletecollection_namespaced_policy(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_policy: %s\n" % e
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

# **deletecollection_namespaced_policy_binding**
> UnversionedStatus deletecollection_namespaced_policy_binding(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of PolicyBinding
    api_response = api_instance.deletecollection_namespaced_policy_binding(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_policy_binding: %s\n" % e
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

# **deletecollection_namespaced_route**
> UnversionedStatus deletecollection_namespaced_route(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Route
    api_response = api_instance.deletecollection_namespaced_route(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_route: %s\n" % e
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

# **deletecollection_namespaced_template**
> UnversionedStatus deletecollection_namespaced_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Template
    api_response = api_instance.deletecollection_namespaced_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_template: %s\n" % e
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

# **deletecollection_namespaced_user**
> UnversionedStatus deletecollection_namespaced_user(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of User
    api_response = api_instance.deletecollection_namespaced_user(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->deletecollection_namespaced_user: %s\n" % e
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

# **get_api_resources**
> get_api_resources()

get available resources

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()

try: 
    # get available resources
    api_instance.get_api_resources()
except ApiException as e:
    print "Exception when calling Oapiv1Api->get_api_resources: %s\n" % e
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

# **list_build**
> V1BuildList list_build(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Build
    api_response = api_instance.list_build(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_build: %s\n" % e
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

[**V1BuildList**](V1BuildList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_config**
> V1BuildConfigList list_build_config(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind BuildConfig
    api_response = api_instance.list_build_config(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_build_config: %s\n" % e
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

[**V1BuildConfigList**](V1BuildConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployment_config**
> V1DeploymentConfigList list_deployment_config(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind DeploymentConfig
    api_response = api_instance.list_deployment_config(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_deployment_config: %s\n" % e
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

[**V1DeploymentConfigList**](V1DeploymentConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_stream**
> V1ImageStreamList list_image_stream(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ImageStream
    api_response = api_instance.list_image_stream(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_image_stream: %s\n" % e
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

[**V1ImageStreamList**](V1ImageStreamList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_stream_tag**
> V1ImageStreamTagList list_image_stream_tag(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ImageStreamTag

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ImageStreamTag
    api_response = api_instance.list_image_stream_tag(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_image_stream_tag: %s\n" % e
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

[**V1ImageStreamTagList**](V1ImageStreamTagList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_build**
> V1BuildList list_namespaced_build(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Build
    api_response = api_instance.list_namespaced_build(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_build: %s\n" % e
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

[**V1BuildList**](V1BuildList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_build_config**
> V1BuildConfigList list_namespaced_build_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind BuildConfig
    api_response = api_instance.list_namespaced_build_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_build_config: %s\n" % e
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

[**V1BuildConfigList**](V1BuildConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cluster_network**
> V1ClusterNetworkList list_namespaced_cluster_network(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ClusterNetwork
    api_response = api_instance.list_namespaced_cluster_network(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_cluster_network: %s\n" % e
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

[**V1ClusterNetworkList**](V1ClusterNetworkList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cluster_policy**
> V1ClusterPolicyList list_namespaced_cluster_policy(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ClusterPolicy
    api_response = api_instance.list_namespaced_cluster_policy(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_cluster_policy: %s\n" % e
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

[**V1ClusterPolicyList**](V1ClusterPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cluster_policy_binding**
> V1ClusterPolicyBindingList list_namespaced_cluster_policy_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ClusterPolicyBinding
    api_response = api_instance.list_namespaced_cluster_policy_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_cluster_policy_binding: %s\n" % e
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

[**V1ClusterPolicyBindingList**](V1ClusterPolicyBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cluster_role**
> V1ClusterRoleList list_namespaced_cluster_role(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ClusterRole

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ClusterRole
    api_response = api_instance.list_namespaced_cluster_role(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_cluster_role: %s\n" % e
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

[**V1ClusterRoleList**](V1ClusterRoleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cluster_role_binding**
> V1ClusterRoleBindingList list_namespaced_cluster_role_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ClusterRoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ClusterRoleBinding
    api_response = api_instance.list_namespaced_cluster_role_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_cluster_role_binding: %s\n" % e
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

[**V1ClusterRoleBindingList**](V1ClusterRoleBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_deployment_config**
> V1DeploymentConfigList list_namespaced_deployment_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind DeploymentConfig
    api_response = api_instance.list_namespaced_deployment_config(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_deployment_config: %s\n" % e
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

[**V1DeploymentConfigList**](V1DeploymentConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_group**
> V1GroupList list_namespaced_group(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Group
    api_response = api_instance.list_namespaced_group(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_group: %s\n" % e
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

[**V1GroupList**](V1GroupList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_host_subnet**
> V1HostSubnetList list_namespaced_host_subnet(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind HostSubnet
    api_response = api_instance.list_namespaced_host_subnet(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_host_subnet: %s\n" % e
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

[**V1HostSubnetList**](V1HostSubnetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_identity**
> V1IdentityList list_namespaced_identity(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Identity
    api_response = api_instance.list_namespaced_identity(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_identity: %s\n" % e
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

[**V1IdentityList**](V1IdentityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_image**
> V1ImageList list_namespaced_image(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Image
    api_response = api_instance.list_namespaced_image(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_image: %s\n" % e
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

[**V1ImageList**](V1ImageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_image_stream**
> V1ImageStreamList list_namespaced_image_stream(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ImageStream
    api_response = api_instance.list_namespaced_image_stream(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_image_stream: %s\n" % e
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

[**V1ImageStreamList**](V1ImageStreamList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_image_stream_tag**
> V1ImageStreamTagList list_namespaced_image_stream_tag(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ImageStreamTag

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ImageStreamTag
    api_response = api_instance.list_namespaced_image_stream_tag(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_image_stream_tag: %s\n" % e
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

[**V1ImageStreamTagList**](V1ImageStreamTagList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_net_namespace**
> V1NetNamespaceList list_namespaced_net_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind NetNamespace
    api_response = api_instance.list_namespaced_net_namespace(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_net_namespace: %s\n" % e
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

[**V1NetNamespaceList**](V1NetNamespaceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_o_auth_access_token**
> V1OAuthAccessTokenList list_namespaced_o_auth_access_token(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind OAuthAccessToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind OAuthAccessToken
    api_response = api_instance.list_namespaced_o_auth_access_token(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_o_auth_access_token: %s\n" % e
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

[**V1OAuthAccessTokenList**](V1OAuthAccessTokenList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_o_auth_authorize_token**
> V1OAuthAuthorizeTokenList list_namespaced_o_auth_authorize_token(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind OAuthAuthorizeToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind OAuthAuthorizeToken
    api_response = api_instance.list_namespaced_o_auth_authorize_token(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_o_auth_authorize_token: %s\n" % e
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

[**V1OAuthAuthorizeTokenList**](V1OAuthAuthorizeTokenList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_o_auth_client**
> V1OAuthClientList list_namespaced_o_auth_client(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind OAuthClient
    api_response = api_instance.list_namespaced_o_auth_client(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_o_auth_client: %s\n" % e
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

[**V1OAuthClientList**](V1OAuthClientList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_o_auth_client_authorization**
> V1OAuthClientAuthorizationList list_namespaced_o_auth_client_authorization(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind OAuthClientAuthorization
    api_response = api_instance.list_namespaced_o_auth_client_authorization(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_o_auth_client_authorization: %s\n" % e
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

[**V1OAuthClientAuthorizationList**](V1OAuthClientAuthorizationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_policy**
> V1PolicyList list_namespaced_policy(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Policy
    api_response = api_instance.list_namespaced_policy(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_policy: %s\n" % e
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

[**V1PolicyList**](V1PolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_policy_binding**
> V1PolicyBindingList list_namespaced_policy_binding(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PolicyBinding
    api_response = api_instance.list_namespaced_policy_binding(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_policy_binding: %s\n" % e
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

[**V1PolicyBindingList**](V1PolicyBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_project**
> V1ProjectList list_namespaced_project(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind Project

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind Project
    api_response = api_instance.list_namespaced_project(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_project: %s\n" % e
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

[**V1ProjectList**](V1ProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_project_request**
> UnversionedStatus list_namespaced_project_request(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ProjectRequest

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ProjectRequest
    api_response = api_instance.list_namespaced_project_request(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_project_request: %s\n" % e
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

# **list_namespaced_role**
> V1RoleList list_namespaced_role(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind Role
    api_response = api_instance.list_namespaced_role(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_role: %s\n" % e
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

[**V1RoleList**](V1RoleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_role_binding**
> V1RoleBindingList list_namespaced_role_binding(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind RoleBinding
    api_response = api_instance.list_namespaced_role_binding(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_role_binding: %s\n" % e
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

[**V1RoleBindingList**](V1RoleBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_route**
> V1RouteList list_namespaced_route(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Route
    api_response = api_instance.list_namespaced_route(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_route: %s\n" % e
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

[**V1RouteList**](V1RouteList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_template**
> V1TemplateList list_namespaced_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Template
    api_response = api_instance.list_namespaced_template(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_template: %s\n" % e
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

[**V1TemplateList**](V1TemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_user**
> V1UserList list_namespaced_user(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind User
    api_response = api_instance.list_namespaced_user(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_namespaced_user: %s\n" % e
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

[**V1UserList**](V1UserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policy**
> V1PolicyList list_policy(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Policy
    api_response = api_instance.list_policy(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_policy: %s\n" % e
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

[**V1PolicyList**](V1PolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policy_binding**
> V1PolicyBindingList list_policy_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PolicyBinding
    api_response = api_instance.list_policy_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_policy_binding: %s\n" % e
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

[**V1PolicyBindingList**](V1PolicyBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role**
> V1RoleList list_role(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind Role
    api_response = api_instance.list_role(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_role: %s\n" % e
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

[**V1RoleList**](V1RoleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_binding**
> V1RoleBindingList list_role_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind RoleBinding
    api_response = api_instance.list_role_binding(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_role_binding: %s\n" % e
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

[**V1RoleBindingList**](V1RoleBindingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_route**
> V1RouteList list_route(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Route
    api_response = api_instance.list_route(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_route: %s\n" % e
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

[**V1RouteList**](V1RouteList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template**
> V1TemplateList list_template(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Template
    api_response = api_instance.list_template(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->list_template: %s\n" % e
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

[**V1TemplateList**](V1TemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_build**
> V1Build patch_namespaced_build(body, namespace, name, pretty=pretty)

partially update the specified Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Build
    api_response = api_instance.patch_namespaced_build(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_build: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Build | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_build_config**
> V1BuildConfig patch_namespaced_build_config(body, namespace, name, pretty=pretty)

partially update the specified BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified BuildConfig
    api_response = api_instance.patch_namespaced_build_config(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_build_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cluster_network**
> V1ClusterNetwork patch_namespaced_cluster_network(body, name, pretty=pretty)

partially update the specified ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterNetwork
    api_response = api_instance.patch_namespaced_cluster_network(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_cluster_network: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the ClusterNetwork | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cluster_policy**
> V1ClusterPolicy patch_namespaced_cluster_policy(body, name, pretty=pretty)

partially update the specified ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterPolicy
    api_response = api_instance.patch_namespaced_cluster_policy(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_cluster_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the ClusterPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterPolicy**](V1ClusterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cluster_policy_binding**
> V1ClusterPolicyBinding patch_namespaced_cluster_policy_binding(body, name, pretty=pretty)

partially update the specified ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterPolicyBinding
    api_response = api_instance.patch_namespaced_cluster_policy_binding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_cluster_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the ClusterPolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterPolicyBinding**](V1ClusterPolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cluster_role**
> V1ClusterRole patch_namespaced_cluster_role(body, name, pretty=pretty)

partially update the specified ClusterRole

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterRole
    api_response = api_instance.patch_namespaced_cluster_role(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_cluster_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the ClusterRole | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRole**](V1ClusterRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cluster_role_binding**
> V1ClusterRoleBinding patch_namespaced_cluster_role_binding(body, name, pretty=pretty)

partially update the specified ClusterRoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterRoleBinding
    api_response = api_instance.patch_namespaced_cluster_role_binding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_cluster_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the ClusterRoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRoleBinding**](V1ClusterRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployment_config**
> V1DeploymentConfig patch_namespaced_deployment_config(body, namespace, name, pretty=pretty)

partially update the specified DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified DeploymentConfig
    api_response = api_instance.patch_namespaced_deployment_config(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_deployment_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_group**
> V1Group patch_namespaced_group(body, name, pretty=pretty)

partially update the specified Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Group
    api_response = api_instance.patch_namespaced_group(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the Group | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Group**](V1Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_host_subnet**
> V1HostSubnet patch_namespaced_host_subnet(body, name, pretty=pretty)

partially update the specified HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified HostSubnet
    api_response = api_instance.patch_namespaced_host_subnet(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_host_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the HostSubnet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_identity**
> V1Identity patch_namespaced_identity(body, name, pretty=pretty)

partially update the specified Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Identity
    api_response = api_instance.patch_namespaced_identity(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_identity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the Identity | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Identity**](V1Identity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_image**
> V1Image patch_namespaced_image(body, name, pretty=pretty)

partially update the specified Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Image
    api_response = api_instance.patch_namespaced_image(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the Image | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_image_stream**
> V1ImageStream patch_namespaced_image_stream(body, namespace, name, pretty=pretty)

partially update the specified ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ImageStream
    api_response = api_instance.patch_namespaced_image_stream(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_image_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStream | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_image_stream_tag**
> V1ImageStreamTag patch_namespaced_image_stream_tag(body, namespace, name, pretty=pretty)

partially update the specified ImageStreamTag

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ImageStreamTag
    api_response = api_instance.patch_namespaced_image_stream_tag(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_image_stream_tag: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStreamTag | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_net_namespace**
> V1NetNamespace patch_namespaced_net_namespace(body, name, pretty=pretty)

partially update the specified NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified NetNamespace
    api_response = api_instance.patch_namespaced_net_namespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_net_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the NetNamespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_o_auth_client**
> V1OAuthClient patch_namespaced_o_auth_client(body, name, pretty=pretty)

partially update the specified OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified OAuthClient
    api_response = api_instance.patch_namespaced_o_auth_client(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_o_auth_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the OAuthClient | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthClient**](V1OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_o_auth_client_authorization**
> V1OAuthClientAuthorization patch_namespaced_o_auth_client_authorization(body, name, pretty=pretty)

partially update the specified OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified OAuthClientAuthorization
    api_response = api_instance.patch_namespaced_o_auth_client_authorization(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_o_auth_client_authorization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the OAuthClientAuthorization | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthClientAuthorization**](V1OAuthClientAuthorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_policy**
> V1Policy patch_namespaced_policy(body, namespace, name, pretty=pretty)

partially update the specified Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Policy
    api_response = api_instance.patch_namespaced_policy(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Policy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Policy**](V1Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_policy_binding**
> V1PolicyBinding patch_namespaced_policy_binding(body, namespace, name, pretty=pretty)

partially update the specified PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified PolicyBinding
    api_response = api_instance.patch_namespaced_policy_binding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PolicyBinding**](V1PolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_project**
> V1Project patch_namespaced_project(body, name, pretty=pretty)

partially update the specified Project

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Project
    api_response = api_instance.patch_namespaced_project(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_project: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the Project | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_role**
> V1Role patch_namespaced_role(body, namespace, name, pretty=pretty)

partially update the specified Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Role
    api_response = api_instance.patch_namespaced_role(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Role | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Role**](V1Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_role_binding**
> V1RoleBinding patch_namespaced_role_binding(body, namespace, name, pretty=pretty)

partially update the specified RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified RoleBinding
    api_response = api_instance.patch_namespaced_role_binding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the RoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1RoleBinding**](V1RoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_route**
> V1Route patch_namespaced_route(body, namespace, name, pretty=pretty)

partially update the specified Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Route
    api_response = api_instance.patch_namespaced_route(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Route | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Route**](V1Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_scale_scale**
> V1beta1Scale patch_namespaced_scale_scale(body, namespace, name, pretty=pretty)

partially update scale of the specified Scale

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update scale of the specified Scale
    api_response = api_instance.patch_namespaced_scale_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_template**
> V1Template patch_namespaced_template(body, namespace, name, pretty=pretty)

partially update the specified Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Template
    api_response = api_instance.patch_namespaced_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Template | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_user**
> V1User patch_namespaced_user(body, name, pretty=pretty)

partially update the specified User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified User
    api_response = api_instance.patch_namespaced_user(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the User | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_user_identity_mapping**
> V1UserIdentityMapping patch_namespaced_user_identity_mapping(body, name, pretty=pretty)

partially update the specified UserIdentityMapping

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified UserIdentityMapping
    api_response = api_instance.patch_namespaced_user_identity_mapping(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->patch_namespaced_user_identity_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the UserIdentityMapping | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1UserIdentityMapping**](V1UserIdentityMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_binary_build_request_options_instantiatebinary**
> str post_namespaced_binary_build_request_options_instantiatebinary(namespace, name, as_file=as_file, revision_commit=revision_commit, revision_message=revision_message, revision_author_name=revision_author_name, revision_author_email=revision_author_email, revision_committer_name=revision_committer_name, revision_committer_email=revision_committer_email)

connect POST requests to instantiatebinary of BinaryBuildRequestOptions

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BinaryBuildRequestOptions
as_file = 'as_file_example' # str | AsFile determines if the binary should be created as a file within the source rather than extracted as an archive (optional)
revision_commit = 'revision_commit_example' # str | Commit is the value identifying a specific commit (optional)
revision_message = 'revision_message_example' # str | Message is the description of a specific commit (optional)
revision_author_name = 'revision_author_name_example' # str | AuthorName of the source control user (optional)
revision_author_email = 'revision_author_email_example' # str | AuthorEmail of the source control user (optional)
revision_committer_name = 'revision_committer_name_example' # str | CommitterName of the source control user (optional)
revision_committer_email = 'revision_committer_email_example' # str | CommitterEmail of the source control user (optional)

try: 
    # connect POST requests to instantiatebinary of BinaryBuildRequestOptions
    api_response = api_instance.post_namespaced_binary_build_request_options_instantiatebinary(namespace, name, as_file=as_file, revision_commit=revision_commit, revision_message=revision_message, revision_author_name=revision_author_name, revision_author_email=revision_author_email, revision_committer_name=revision_committer_name, revision_committer_email=revision_committer_email)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->post_namespaced_binary_build_request_options_instantiatebinary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BinaryBuildRequestOptions | 
 **as_file** | **str**| AsFile determines if the binary should be created as a file within the source rather than extracted as an archive | [optional] 
 **revision_commit** | **str**| Commit is the value identifying a specific commit | [optional] 
 **revision_message** | **str**| Message is the description of a specific commit | [optional] 
 **revision_author_name** | **str**| AuthorName of the source control user | [optional] 
 **revision_author_email** | **str**| AuthorEmail of the source control user | [optional] 
 **revision_committer_name** | **str**| CommitterName of the source control user | [optional] 
 **revision_committer_email** | **str**| CommitterEmail of the source control user | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_status_webhooks**
> str post_namespaced_status_webhooks(namespace, name, path=path)

connect POST requests to webhooks of Status

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Status
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect POST requests to webhooks of Status
    api_response = api_instance.post_namespaced_status_webhooks(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->post_namespaced_status_webhooks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Status | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespaced_status_webhooks_0**
> str post_namespaced_status_webhooks_0(namespace, name, path2, path=path)

connect POST requests to webhooks of Status

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Status
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect POST requests to webhooks of Status
    api_response = api_instance.post_namespaced_status_webhooks_0(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->post_namespaced_status_webhooks_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Status | 
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

# **read_namespaced_build**
> V1Build read_namespaced_build(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Build
    api_response = api_instance.read_namespaced_build(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_build: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Build | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_build_config**
> V1BuildConfig read_namespaced_build_config(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified BuildConfig
    api_response = api_instance.read_namespaced_build_config(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_build_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_build_log_log**
> V1BuildLog read_namespaced_build_log_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)

read log of the specified BuildLog

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildLog
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
container = 'container_example' # str | The container for which to stream logs. Defaults to only container if there is one container in the pod. (optional)
follow = true # bool | Follow if true indicates that the build log should be streamed until the build terminates. (optional)
previous = true # bool | Return previous build logs. Defaults to false. (optional)
since_seconds = 56 # int | A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
since_time = 'since_time_example' # str | An RFC3339 timestamp from which to show logs. If this value preceeds the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
timestamps = true # bool | If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. (optional)
tail_lines = 56 # int | If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime (optional)
limit_bytes = 56 # int | If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. (optional)
nowait = true # bool | NoWait if true causes the call to return immediately even if the build is not available yet. Otherwise the server will wait until the build has started. (optional)
version = 56 # int | Version of the build for which to view logs. (optional)

try: 
    # read log of the specified BuildLog
    api_response = api_instance.read_namespaced_build_log_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_build_log_log: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildLog | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **container** | **str**| The container for which to stream logs. Defaults to only container if there is one container in the pod. | [optional] 
 **follow** | **bool**| Follow if true indicates that the build log should be streamed until the build terminates. | [optional] 
 **previous** | **bool**| Return previous build logs. Defaults to false. | [optional] 
 **since_seconds** | **int**| A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **since_time** | **str**| An RFC3339 timestamp from which to show logs. If this value preceeds the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **timestamps** | **bool**| If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. | [optional] 
 **tail_lines** | **int**| If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime | [optional] 
 **limit_bytes** | **int**| If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. | [optional] 
 **nowait** | **bool**| NoWait if true causes the call to return immediately even if the build is not available yet. Otherwise the server will wait until the build has started. | [optional] 
 **version** | **int**| Version of the build for which to view logs. | [optional] 

### Return type

[**V1BuildLog**](V1BuildLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cluster_network**
> V1ClusterNetwork read_namespaced_cluster_network(name, pretty=pretty, export=export, exact=exact)

read the specified ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ClusterNetwork
    api_response = api_instance.read_namespaced_cluster_network(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_cluster_network: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterNetwork | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cluster_policy**
> V1ClusterPolicy read_namespaced_cluster_policy(name, pretty=pretty, export=export, exact=exact)

read the specified ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ClusterPolicy
    api_response = api_instance.read_namespaced_cluster_policy(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_cluster_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ClusterPolicy**](V1ClusterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cluster_policy_binding**
> V1ClusterPolicyBinding read_namespaced_cluster_policy_binding(name, pretty=pretty, export=export, exact=exact)

read the specified ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ClusterPolicyBinding
    api_response = api_instance.read_namespaced_cluster_policy_binding(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_cluster_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterPolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ClusterPolicyBinding**](V1ClusterPolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cluster_role**
> V1ClusterRole read_namespaced_cluster_role(name, pretty=pretty)

read the specified ClusterRole

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ClusterRole
    api_response = api_instance.read_namespaced_cluster_role(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_cluster_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRole | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRole**](V1ClusterRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cluster_role_binding**
> V1ClusterRoleBinding read_namespaced_cluster_role_binding(name, pretty=pretty)

read the specified ClusterRoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ClusterRoleBinding
    api_response = api_instance.read_namespaced_cluster_role_binding(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_cluster_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRoleBinding**](V1ClusterRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment_config**
> V1DeploymentConfig read_namespaced_deployment_config(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified DeploymentConfig
    api_response = api_instance.read_namespaced_deployment_config(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_deployment_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment_config_0**
> V1DeploymentConfig read_namespaced_deployment_config_0(namespace, name, pretty=pretty)

read the specified DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified DeploymentConfig
    api_response = api_instance.read_namespaced_deployment_config_0(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_deployment_config_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment_log_log**
> V1DeploymentLog read_namespaced_deployment_log_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)

read log of the specified DeploymentLog

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentLog
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
container = 'container_example' # str | The container for which to stream logs. Defaults to only container if there is one container in the pod. (optional)
follow = true # bool | Follow if true indicates that the build log should be streamed until the build terminates. (optional)
previous = true # bool | Return previous deployment logs. Defaults to false. (optional)
since_seconds = 56 # int | A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
since_time = 'since_time_example' # str | An RFC3339 timestamp from which to show logs. If this value preceeds the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
timestamps = true # bool | If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. (optional)
tail_lines = 56 # int | If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime (optional)
limit_bytes = 56 # int | If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. (optional)
nowait = true # bool | NoWait if true causes the call to return immediately even if the deployment is not available yet. Otherwise the server will wait until the deployment has started. (optional)
version = 56 # int | Version of the deployment for which to view logs. (optional)

try: 
    # read log of the specified DeploymentLog
    api_response = api_instance.read_namespaced_deployment_log_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_deployment_log_log: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentLog | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **container** | **str**| The container for which to stream logs. Defaults to only container if there is one container in the pod. | [optional] 
 **follow** | **bool**| Follow if true indicates that the build log should be streamed until the build terminates. | [optional] 
 **previous** | **bool**| Return previous deployment logs. Defaults to false. | [optional] 
 **since_seconds** | **int**| A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **since_time** | **str**| An RFC3339 timestamp from which to show logs. If this value preceeds the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **timestamps** | **bool**| If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. | [optional] 
 **tail_lines** | **int**| If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime | [optional] 
 **limit_bytes** | **int**| If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. | [optional] 
 **nowait** | **bool**| NoWait if true causes the call to return immediately even if the deployment is not available yet. Otherwise the server will wait until the deployment has started. | [optional] 
 **version** | **int**| Version of the deployment for which to view logs. | [optional] 

### Return type

[**V1DeploymentLog**](V1DeploymentLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_group**
> V1Group read_namespaced_group(name, pretty=pretty, export=export, exact=exact)

read the specified Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Group
    api_response = api_instance.read_namespaced_group(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Group | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Group**](V1Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_host_subnet**
> V1HostSubnet read_namespaced_host_subnet(name, pretty=pretty, export=export, exact=exact)

read the specified HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified HostSubnet
    api_response = api_instance.read_namespaced_host_subnet(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_host_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HostSubnet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_identity**
> V1Identity read_namespaced_identity(name, pretty=pretty, export=export, exact=exact)

read the specified Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Identity
    api_response = api_instance.read_namespaced_identity(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_identity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Identity | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Identity**](V1Identity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_image**
> V1Image read_namespaced_image(name, pretty=pretty, export=export, exact=exact)

read the specified Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Image
    api_response = api_instance.read_namespaced_image(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Image | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_image_stream**
> V1ImageStream read_namespaced_image_stream(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ImageStream
    api_response = api_instance.read_namespaced_image_stream(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_image_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStream | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_image_stream_image**
> V1ImageStreamImage read_namespaced_image_stream_image(namespace, name, pretty=pretty)

read the specified ImageStreamImage

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamImage
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ImageStreamImage
    api_response = api_instance.read_namespaced_image_stream_image(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_image_stream_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStreamImage | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamImage**](V1ImageStreamImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_image_stream_tag**
> V1ImageStreamTag read_namespaced_image_stream_tag(namespace, name, pretty=pretty)

read the specified ImageStreamTag

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ImageStreamTag
    api_response = api_instance.read_namespaced_image_stream_tag(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_image_stream_tag: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStreamTag | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_net_namespace**
> V1NetNamespace read_namespaced_net_namespace(name, pretty=pretty, export=export, exact=exact)

read the specified NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified NetNamespace
    api_response = api_instance.read_namespaced_net_namespace(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_net_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetNamespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_o_auth_access_token**
> V1OAuthAccessToken read_namespaced_o_auth_access_token(name, pretty=pretty)

read the specified OAuthAccessToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the OAuthAccessToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified OAuthAccessToken
    api_response = api_instance.read_namespaced_o_auth_access_token(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_o_auth_access_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the OAuthAccessToken | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthAccessToken**](V1OAuthAccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_o_auth_authorize_token**
> V1OAuthAuthorizeToken read_namespaced_o_auth_authorize_token(name, pretty=pretty)

read the specified OAuthAuthorizeToken

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the OAuthAuthorizeToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified OAuthAuthorizeToken
    api_response = api_instance.read_namespaced_o_auth_authorize_token(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_o_auth_authorize_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the OAuthAuthorizeToken | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthAuthorizeToken**](V1OAuthAuthorizeToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_o_auth_client**
> V1OAuthClient read_namespaced_o_auth_client(name, pretty=pretty, export=export, exact=exact)

read the specified OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified OAuthClient
    api_response = api_instance.read_namespaced_o_auth_client(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_o_auth_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the OAuthClient | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1OAuthClient**](V1OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_o_auth_client_authorization**
> V1OAuthClientAuthorization read_namespaced_o_auth_client_authorization(name, pretty=pretty, export=export, exact=exact)

read the specified OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified OAuthClientAuthorization
    api_response = api_instance.read_namespaced_o_auth_client_authorization(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_o_auth_client_authorization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the OAuthClientAuthorization | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1OAuthClientAuthorization**](V1OAuthClientAuthorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_policy**
> V1Policy read_namespaced_policy(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Policy
    api_response = api_instance.read_namespaced_policy(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Policy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Policy**](V1Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_policy_binding**
> V1PolicyBinding read_namespaced_policy_binding(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified PolicyBinding
    api_response = api_instance.read_namespaced_policy_binding(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1PolicyBinding**](V1PolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_project**
> V1Project read_namespaced_project(name, pretty=pretty)

read the specified Project

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified Project
    api_response = api_instance.read_namespaced_project(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_project: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Project | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_role**
> V1Role read_namespaced_role(namespace, name, pretty=pretty)

read the specified Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified Role
    api_response = api_instance.read_namespaced_role(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Role | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Role**](V1Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_role_binding**
> V1RoleBinding read_namespaced_role_binding(namespace, name, pretty=pretty)

read the specified RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified RoleBinding
    api_response = api_instance.read_namespaced_role_binding(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the RoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1RoleBinding**](V1RoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_route**
> V1Route read_namespaced_route(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Route
    api_response = api_instance.read_namespaced_route(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Route | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Route**](V1Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_scale_scale**
> V1beta1Scale read_namespaced_scale_scale(namespace, name, pretty=pretty)

read scale of the specified Scale

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read scale of the specified Scale
    api_response = api_instance.read_namespaced_scale_scale(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_secret_list_secrets**
> V1SecretList read_namespaced_secret_list_secrets(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

read secrets of the specified SecretList

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the SecretList
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # read secrets of the specified SecretList
    api_response = api_instance.read_namespaced_secret_list_secrets(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_secret_list_secrets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the SecretList | 
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

# **read_namespaced_template**
> V1Template read_namespaced_template(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Template
    api_response = api_instance.read_namespaced_template(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Template | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_user**
> V1User read_namespaced_user(name, pretty=pretty, export=export, exact=exact)

read the specified User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified User
    api_response = api_instance.read_namespaced_user(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the User | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_user_identity_mapping**
> V1UserIdentityMapping read_namespaced_user_identity_mapping(name, pretty=pretty)

read the specified UserIdentityMapping

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified UserIdentityMapping
    api_response = api_instance.read_namespaced_user_identity_mapping(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->read_namespaced_user_identity_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the UserIdentityMapping | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1UserIdentityMapping**](V1UserIdentityMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_build**
> V1Build replace_namespaced_build(body, namespace, name, pretty=pretty)

replace the specified Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Build() # V1Build | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Build
    api_response = api_instance.replace_namespaced_build(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_build: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Build**](V1Build.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Build | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_build_config**
> V1BuildConfig replace_namespaced_build_config(body, namespace, name, pretty=pretty)

replace the specified BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1BuildConfig() # V1BuildConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified BuildConfig
    api_response = api_instance.replace_namespaced_build_config(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_build_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildConfig**](V1BuildConfig.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_build_details**
> V1Build replace_namespaced_build_details(body, namespace, name, pretty=pretty)

replace details of the specified Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Build() # V1Build | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace details of the specified Build
    api_response = api_instance.replace_namespaced_build_details(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_build_details: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Build**](V1Build.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Build | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cluster_network**
> V1ClusterNetwork replace_namespaced_cluster_network(body, name, pretty=pretty)

replace the specified ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterNetwork() # V1ClusterNetwork | 
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterNetwork
    api_response = api_instance.replace_namespaced_cluster_network(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_cluster_network: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterNetwork**](V1ClusterNetwork.md)|  | 
 **name** | **str**| name of the ClusterNetwork | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cluster_policy**
> V1ClusterPolicy replace_namespaced_cluster_policy(body, name, pretty=pretty)

replace the specified ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterPolicy() # V1ClusterPolicy | 
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterPolicy
    api_response = api_instance.replace_namespaced_cluster_policy(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_cluster_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterPolicy**](V1ClusterPolicy.md)|  | 
 **name** | **str**| name of the ClusterPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterPolicy**](V1ClusterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cluster_policy_binding**
> V1ClusterPolicyBinding replace_namespaced_cluster_policy_binding(body, name, pretty=pretty)

replace the specified ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterPolicyBinding() # V1ClusterPolicyBinding | 
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterPolicyBinding
    api_response = api_instance.replace_namespaced_cluster_policy_binding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_cluster_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterPolicyBinding**](V1ClusterPolicyBinding.md)|  | 
 **name** | **str**| name of the ClusterPolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterPolicyBinding**](V1ClusterPolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cluster_role**
> V1ClusterRole replace_namespaced_cluster_role(body, name, pretty=pretty)

replace the specified ClusterRole

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterRole() # V1ClusterRole | 
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterRole
    api_response = api_instance.replace_namespaced_cluster_role(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_cluster_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterRole**](V1ClusterRole.md)|  | 
 **name** | **str**| name of the ClusterRole | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRole**](V1ClusterRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cluster_role_binding**
> V1ClusterRoleBinding replace_namespaced_cluster_role_binding(body, name, pretty=pretty)

replace the specified ClusterRoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ClusterRoleBinding() # V1ClusterRoleBinding | 
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterRoleBinding
    api_response = api_instance.replace_namespaced_cluster_role_binding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_cluster_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterRoleBinding**](V1ClusterRoleBinding.md)|  | 
 **name** | **str**| name of the ClusterRoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterRoleBinding**](V1ClusterRoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployment_config**
> V1DeploymentConfig replace_namespaced_deployment_config(body, namespace, name, pretty=pretty)

replace the specified DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1DeploymentConfig() # V1DeploymentConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified DeploymentConfig
    api_response = api_instance.replace_namespaced_deployment_config(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_deployment_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentConfig**](V1DeploymentConfig.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentConfig | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_group**
> V1Group replace_namespaced_group(body, name, pretty=pretty)

replace the specified Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Group() # V1Group | 
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Group
    api_response = api_instance.replace_namespaced_group(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Group**](V1Group.md)|  | 
 **name** | **str**| name of the Group | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Group**](V1Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_host_subnet**
> V1HostSubnet replace_namespaced_host_subnet(body, name, pretty=pretty)

replace the specified HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1HostSubnet() # V1HostSubnet | 
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified HostSubnet
    api_response = api_instance.replace_namespaced_host_subnet(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_host_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HostSubnet**](V1HostSubnet.md)|  | 
 **name** | **str**| name of the HostSubnet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_identity**
> V1Identity replace_namespaced_identity(body, name, pretty=pretty)

replace the specified Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Identity() # V1Identity | 
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Identity
    api_response = api_instance.replace_namespaced_identity(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_identity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Identity**](V1Identity.md)|  | 
 **name** | **str**| name of the Identity | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Identity**](V1Identity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_image**
> V1Image replace_namespaced_image(body, name, pretty=pretty)

replace the specified Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Image() # V1Image | 
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Image
    api_response = api_instance.replace_namespaced_image(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Image**](V1Image.md)|  | 
 **name** | **str**| name of the Image | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_image_stream**
> V1ImageStream replace_namespaced_image_stream(body, namespace, name, pretty=pretty)

replace the specified ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStream() # V1ImageStream | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ImageStream
    api_response = api_instance.replace_namespaced_image_stream(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_image_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStream | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_image_stream_status**
> V1ImageStream replace_namespaced_image_stream_status(body, namespace, name, pretty=pretty)

replace status of the specified ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStream() # V1ImageStream | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified ImageStream
    api_response = api_instance.replace_namespaced_image_stream_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_image_stream_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStream | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_image_stream_tag**
> V1ImageStreamTag replace_namespaced_image_stream_tag(body, namespace, name, pretty=pretty)

replace the specified ImageStreamTag

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1ImageStreamTag() # V1ImageStreamTag | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ImageStreamTag
    api_response = api_instance.replace_namespaced_image_stream_tag(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_image_stream_tag: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamTag**](V1ImageStreamTag.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStreamTag | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_net_namespace**
> V1NetNamespace replace_namespaced_net_namespace(body, name, pretty=pretty)

replace the specified NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1NetNamespace() # V1NetNamespace | 
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified NetNamespace
    api_response = api_instance.replace_namespaced_net_namespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_net_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetNamespace**](V1NetNamespace.md)|  | 
 **name** | **str**| name of the NetNamespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_o_auth_client**
> V1OAuthClient replace_namespaced_o_auth_client(body, name, pretty=pretty)

replace the specified OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1OAuthClient() # V1OAuthClient | 
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified OAuthClient
    api_response = api_instance.replace_namespaced_o_auth_client(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_o_auth_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1OAuthClient**](V1OAuthClient.md)|  | 
 **name** | **str**| name of the OAuthClient | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthClient**](V1OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_o_auth_client_authorization**
> V1OAuthClientAuthorization replace_namespaced_o_auth_client_authorization(body, name, pretty=pretty)

replace the specified OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1OAuthClientAuthorization() # V1OAuthClientAuthorization | 
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified OAuthClientAuthorization
    api_response = api_instance.replace_namespaced_o_auth_client_authorization(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_o_auth_client_authorization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1OAuthClientAuthorization**](V1OAuthClientAuthorization.md)|  | 
 **name** | **str**| name of the OAuthClientAuthorization | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1OAuthClientAuthorization**](V1OAuthClientAuthorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_policy**
> V1Policy replace_namespaced_policy(body, namespace, name, pretty=pretty)

replace the specified Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Policy() # V1Policy | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Policy
    api_response = api_instance.replace_namespaced_policy(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Policy**](V1Policy.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Policy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Policy**](V1Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_policy_binding**
> V1PolicyBinding replace_namespaced_policy_binding(body, namespace, name, pretty=pretty)

replace the specified PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1PolicyBinding() # V1PolicyBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified PolicyBinding
    api_response = api_instance.replace_namespaced_policy_binding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PolicyBinding**](V1PolicyBinding.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PolicyBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PolicyBinding**](V1PolicyBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_project**
> V1Project replace_namespaced_project(body, name, pretty=pretty)

replace the specified Project

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Project() # V1Project | 
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Project
    api_response = api_instance.replace_namespaced_project(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_project: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Project**](V1Project.md)|  | 
 **name** | **str**| name of the Project | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_role**
> V1Role replace_namespaced_role(body, namespace, name, pretty=pretty)

replace the specified Role

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Role() # V1Role | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Role
    api_response = api_instance.replace_namespaced_role(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Role**](V1Role.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Role | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Role**](V1Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_role_binding**
> V1RoleBinding replace_namespaced_role_binding(body, namespace, name, pretty=pretty)

replace the specified RoleBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1RoleBinding() # V1RoleBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified RoleBinding
    api_response = api_instance.replace_namespaced_role_binding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_role_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1RoleBinding**](V1RoleBinding.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the RoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1RoleBinding**](V1RoleBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_route**
> V1Route replace_namespaced_route(body, namespace, name, pretty=pretty)

replace the specified Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Route() # V1Route | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Route
    api_response = api_instance.replace_namespaced_route(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Route**](V1Route.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Route | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Route**](V1Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_route_status**
> V1Route replace_namespaced_route_status(body, namespace, name, pretty=pretty)

replace status of the specified Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Route() # V1Route | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Route
    api_response = api_instance.replace_namespaced_route_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_route_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Route**](V1Route.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Route | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Route**](V1Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_scale_scale**
> V1beta1Scale replace_namespaced_scale_scale(body, namespace, name, pretty=pretty)

replace scale of the specified Scale

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1beta1Scale() # V1beta1Scale | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace scale of the specified Scale
    api_response = api_instance.replace_namespaced_scale_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_template**
> V1Template replace_namespaced_template(body, namespace, name, pretty=pretty)

replace the specified Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1Template() # V1Template | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Template
    api_response = api_instance.replace_namespaced_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Template**](V1Template.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Template | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_user**
> V1User replace_namespaced_user(body, name, pretty=pretty)

replace the specified User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1User() # V1User | 
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified User
    api_response = api_instance.replace_namespaced_user(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1User**](V1User.md)|  | 
 **name** | **str**| name of the User | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_user_identity_mapping**
> V1UserIdentityMapping replace_namespaced_user_identity_mapping(body, name, pretty=pretty)

replace the specified UserIdentityMapping

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
body = oapi_v1.V1UserIdentityMapping() # V1UserIdentityMapping | 
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified UserIdentityMapping
    api_response = api_instance.replace_namespaced_user_identity_mapping(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->replace_namespaced_user_identity_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UserIdentityMapping**](V1UserIdentityMapping.md)|  | 
 **name** | **str**| name of the UserIdentityMapping | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1UserIdentityMapping**](V1UserIdentityMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_build_config_list**
> JsonWatchEvent watch_build_config_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of BuildConfig
    api_response = api_instance.watch_build_config_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_build_config_list: %s\n" % e
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

# **watch_build_list**
> JsonWatchEvent watch_build_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Build
    api_response = api_instance.watch_build_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_build_list: %s\n" % e
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

# **watch_deployment_config_list**
> JsonWatchEvent watch_deployment_config_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of DeploymentConfig
    api_response = api_instance.watch_deployment_config_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_deployment_config_list: %s\n" % e
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

# **watch_image_stream_list**
> JsonWatchEvent watch_image_stream_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ImageStream
    api_response = api_instance.watch_image_stream_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_image_stream_list: %s\n" % e
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

# **watch_namespaced_build**
> JsonWatchEvent watch_namespaced_build(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Build
    api_response = api_instance.watch_namespaced_build(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_build: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Build | 
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

# **watch_namespaced_build_config**
> JsonWatchEvent watch_namespaced_build_config(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind BuildConfig
    api_response = api_instance.watch_namespaced_build_config(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_build_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the BuildConfig | 
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

# **watch_namespaced_build_config_list**
> JsonWatchEvent watch_namespaced_build_config_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of BuildConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of BuildConfig
    api_response = api_instance.watch_namespaced_build_config_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_build_config_list: %s\n" % e
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

# **watch_namespaced_build_list**
> JsonWatchEvent watch_namespaced_build_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Build

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Build
    api_response = api_instance.watch_namespaced_build_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_build_list: %s\n" % e
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

# **watch_namespaced_cluster_network**
> JsonWatchEvent watch_namespaced_cluster_network(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ClusterNetwork
    api_response = api_instance.watch_namespaced_cluster_network(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_cluster_network: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterNetwork | 
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

# **watch_namespaced_cluster_network_list**
> JsonWatchEvent watch_namespaced_cluster_network_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ClusterNetwork

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ClusterNetwork
    api_response = api_instance.watch_namespaced_cluster_network_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_cluster_network_list: %s\n" % e
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

# **watch_namespaced_cluster_policy**
> JsonWatchEvent watch_namespaced_cluster_policy(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ClusterPolicy
    api_response = api_instance.watch_namespaced_cluster_policy(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_cluster_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterPolicy | 
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

# **watch_namespaced_cluster_policy_binding**
> JsonWatchEvent watch_namespaced_cluster_policy_binding(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ClusterPolicyBinding
    api_response = api_instance.watch_namespaced_cluster_policy_binding(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_cluster_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterPolicyBinding | 
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

# **watch_namespaced_cluster_policy_binding_list**
> JsonWatchEvent watch_namespaced_cluster_policy_binding_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ClusterPolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ClusterPolicyBinding
    api_response = api_instance.watch_namespaced_cluster_policy_binding_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_cluster_policy_binding_list: %s\n" % e
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

# **watch_namespaced_cluster_policy_list**
> JsonWatchEvent watch_namespaced_cluster_policy_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ClusterPolicy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ClusterPolicy
    api_response = api_instance.watch_namespaced_cluster_policy_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_cluster_policy_list: %s\n" % e
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

# **watch_namespaced_deployment_config**
> JsonWatchEvent watch_namespaced_deployment_config(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind DeploymentConfig
    api_response = api_instance.watch_namespaced_deployment_config(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_deployment_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentConfig | 
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

# **watch_namespaced_deployment_config_list**
> JsonWatchEvent watch_namespaced_deployment_config_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of DeploymentConfig

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of DeploymentConfig
    api_response = api_instance.watch_namespaced_deployment_config_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_deployment_config_list: %s\n" % e
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

# **watch_namespaced_group**
> JsonWatchEvent watch_namespaced_group(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Group
    api_response = api_instance.watch_namespaced_group(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Group | 
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

# **watch_namespaced_group_list**
> JsonWatchEvent watch_namespaced_group_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Group

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Group
    api_response = api_instance.watch_namespaced_group_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_group_list: %s\n" % e
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

# **watch_namespaced_host_subnet**
> JsonWatchEvent watch_namespaced_host_subnet(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind HostSubnet
    api_response = api_instance.watch_namespaced_host_subnet(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_host_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HostSubnet | 
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

# **watch_namespaced_host_subnet_list**
> JsonWatchEvent watch_namespaced_host_subnet_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of HostSubnet

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of HostSubnet
    api_response = api_instance.watch_namespaced_host_subnet_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_host_subnet_list: %s\n" % e
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

# **watch_namespaced_identity**
> JsonWatchEvent watch_namespaced_identity(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Identity
    api_response = api_instance.watch_namespaced_identity(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_identity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Identity | 
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

# **watch_namespaced_identity_list**
> JsonWatchEvent watch_namespaced_identity_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Identity

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Identity
    api_response = api_instance.watch_namespaced_identity_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_identity_list: %s\n" % e
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

# **watch_namespaced_image**
> JsonWatchEvent watch_namespaced_image(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Image
    api_response = api_instance.watch_namespaced_image(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Image | 
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

# **watch_namespaced_image_list**
> JsonWatchEvent watch_namespaced_image_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Image

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Image
    api_response = api_instance.watch_namespaced_image_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_image_list: %s\n" % e
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

# **watch_namespaced_image_stream**
> JsonWatchEvent watch_namespaced_image_stream(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ImageStream
    api_response = api_instance.watch_namespaced_image_stream(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_image_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ImageStream | 
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

# **watch_namespaced_image_stream_list**
> JsonWatchEvent watch_namespaced_image_stream_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ImageStream

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ImageStream
    api_response = api_instance.watch_namespaced_image_stream_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_image_stream_list: %s\n" % e
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

# **watch_namespaced_net_namespace**
> JsonWatchEvent watch_namespaced_net_namespace(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind NetNamespace
    api_response = api_instance.watch_namespaced_net_namespace(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_net_namespace: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetNamespace | 
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

# **watch_namespaced_net_namespace_list**
> JsonWatchEvent watch_namespaced_net_namespace_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of NetNamespace

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of NetNamespace
    api_response = api_instance.watch_namespaced_net_namespace_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_net_namespace_list: %s\n" % e
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

# **watch_namespaced_o_auth_client**
> JsonWatchEvent watch_namespaced_o_auth_client(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind OAuthClient
    api_response = api_instance.watch_namespaced_o_auth_client(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_o_auth_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the OAuthClient | 
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

# **watch_namespaced_o_auth_client_authorization**
> JsonWatchEvent watch_namespaced_o_auth_client_authorization(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind OAuthClientAuthorization
    api_response = api_instance.watch_namespaced_o_auth_client_authorization(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_o_auth_client_authorization: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the OAuthClientAuthorization | 
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

# **watch_namespaced_o_auth_client_authorization_list**
> JsonWatchEvent watch_namespaced_o_auth_client_authorization_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of OAuthClientAuthorization

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of OAuthClientAuthorization
    api_response = api_instance.watch_namespaced_o_auth_client_authorization_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_o_auth_client_authorization_list: %s\n" % e
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

# **watch_namespaced_o_auth_client_list**
> JsonWatchEvent watch_namespaced_o_auth_client_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of OAuthClient

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of OAuthClient
    api_response = api_instance.watch_namespaced_o_auth_client_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_o_auth_client_list: %s\n" % e
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

# **watch_namespaced_policy**
> JsonWatchEvent watch_namespaced_policy(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Policy
    api_response = api_instance.watch_namespaced_policy(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Policy | 
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

# **watch_namespaced_policy_binding**
> JsonWatchEvent watch_namespaced_policy_binding(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind PolicyBinding
    api_response = api_instance.watch_namespaced_policy_binding(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_policy_binding: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the PolicyBinding | 
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

# **watch_namespaced_policy_binding_list**
> JsonWatchEvent watch_namespaced_policy_binding_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PolicyBinding
    api_response = api_instance.watch_namespaced_policy_binding_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_policy_binding_list: %s\n" % e
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

# **watch_namespaced_policy_list**
> JsonWatchEvent watch_namespaced_policy_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Policy
    api_response = api_instance.watch_namespaced_policy_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_policy_list: %s\n" % e
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

# **watch_namespaced_route**
> JsonWatchEvent watch_namespaced_route(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Route
    api_response = api_instance.watch_namespaced_route(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Route | 
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

# **watch_namespaced_route_list**
> JsonWatchEvent watch_namespaced_route_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Route
    api_response = api_instance.watch_namespaced_route_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_route_list: %s\n" % e
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

# **watch_namespaced_template**
> JsonWatchEvent watch_namespaced_template(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Template
    api_response = api_instance.watch_namespaced_template(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Template | 
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

# **watch_namespaced_template_list**
> JsonWatchEvent watch_namespaced_template_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Template
    api_response = api_instance.watch_namespaced_template_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_template_list: %s\n" % e
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

# **watch_namespaced_user**
> JsonWatchEvent watch_namespaced_user(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind User
    api_response = api_instance.watch_namespaced_user(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the User | 
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

# **watch_namespaced_user_list**
> JsonWatchEvent watch_namespaced_user_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of User

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of User
    api_response = api_instance.watch_namespaced_user_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_namespaced_user_list: %s\n" % e
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

# **watch_policy_binding_list**
> JsonWatchEvent watch_policy_binding_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PolicyBinding

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PolicyBinding
    api_response = api_instance.watch_policy_binding_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_policy_binding_list: %s\n" % e
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

# **watch_policy_list**
> JsonWatchEvent watch_policy_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Policy

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Policy
    api_response = api_instance.watch_policy_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_policy_list: %s\n" % e
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

# **watch_route_list**
> JsonWatchEvent watch_route_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Route

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Route
    api_response = api_instance.watch_route_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_route_list: %s\n" % e
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

# **watch_template_list**
> JsonWatchEvent watch_template_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Template

### Example 
```python
import time
import oapi_v1
from oapi_v1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oapi_v1.Oapiv1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Template
    api_response = api_instance.watch_template_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling Oapiv1Api->watch_template_list: %s\n" % e
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

