# lib_openshift.OapiV1

All URIs are relative to *https://localhost:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_build**](OapiV1.md#create_build) | **POST** /oapi/v1/builds | create a Build
[**create_buildconfig**](OapiV1.md#create_buildconfig) | **POST** /oapi/v1/buildconfigs | create a BuildConfig
[**create_clusternetwork**](OapiV1.md#create_clusternetwork) | **POST** /oapi/v1/clusternetworks | create a ClusterNetwork
[**create_clusterpolicie**](OapiV1.md#create_clusterpolicie) | **POST** /oapi/v1/clusterpolicies | create a ClusterPolicy
[**create_clusterpolicybinding**](OapiV1.md#create_clusterpolicybinding) | **POST** /oapi/v1/clusterpolicybindings | create a ClusterPolicyBinding
[**create_clusterrole**](OapiV1.md#create_clusterrole) | **POST** /oapi/v1/clusterroles | create a ClusterRole
[**create_clusterrolebinding**](OapiV1.md#create_clusterrolebinding) | **POST** /oapi/v1/clusterrolebindings | create a ClusterRoleBinding
[**create_deploymentconfig**](OapiV1.md#create_deploymentconfig) | **POST** /oapi/v1/deploymentconfigs | create a DeploymentConfig
[**create_deploymentconfigrollback**](OapiV1.md#create_deploymentconfigrollback) | **POST** /oapi/v1/deploymentconfigrollbacks | create a DeploymentConfigRollback
[**create_group**](OapiV1.md#create_group) | **POST** /oapi/v1/groups | create a Group
[**create_hostsubnet**](OapiV1.md#create_hostsubnet) | **POST** /oapi/v1/hostsubnets | create a HostSubnet
[**create_identitie**](OapiV1.md#create_identitie) | **POST** /oapi/v1/identities | create a Identity
[**create_image**](OapiV1.md#create_image) | **POST** /oapi/v1/images | create a Image
[**create_imagestream**](OapiV1.md#create_imagestream) | **POST** /oapi/v1/imagestreams | create a ImageStream
[**create_imagestreamimport**](OapiV1.md#create_imagestreamimport) | **POST** /oapi/v1/imagestreamimports | create a ImageStreamImport
[**create_imagestreammapping**](OapiV1.md#create_imagestreammapping) | **POST** /oapi/v1/imagestreammappings | create a ImageStreamMapping
[**create_localresourceaccessreview**](OapiV1.md#create_localresourceaccessreview) | **POST** /oapi/v1/localresourceaccessreviews | create a LocalResourceAccessReview
[**create_localsubjectaccessreview**](OapiV1.md#create_localsubjectaccessreview) | **POST** /oapi/v1/localsubjectaccessreviews | create a LocalSubjectAccessReview
[**create_namespaced_build**](OapiV1.md#create_namespaced_build) | **POST** /oapi/v1/namespaces/{namespace}/builds | create a Build
[**create_namespaced_build_clone**](OapiV1.md#create_namespaced_build_clone) | **POST** /oapi/v1/namespaces/{namespace}/builds/{name}/clone | create clone of a BuildRequest
[**create_namespaced_buildconfig**](OapiV1.md#create_namespaced_buildconfig) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs | create a BuildConfig
[**create_namespaced_buildconfig_instantiate**](OapiV1.md#create_namespaced_buildconfig_instantiate) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/instantiate | create instantiate of a BuildRequest
[**create_namespaced_buildconfig_instantiatebinary**](OapiV1.md#create_namespaced_buildconfig_instantiatebinary) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/instantiatebinary | connect POST requests to instantiatebinary of BinaryBuildRequestOptions
[**create_namespaced_buildconfig_webhook**](OapiV1.md#create_namespaced_buildconfig_webhook) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks | connect POST requests to webhooks of Status
[**create_namespaced_buildconfig_webhookspath**](OapiV1.md#create_namespaced_buildconfig_webhookspath) | **POST** /oapi/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks/{path} | connect POST requests to webhooks of Status
[**create_namespaced_deploymentconfig**](OapiV1.md#create_namespaced_deploymentconfig) | **POST** /oapi/v1/namespaces/{namespace}/deploymentconfigs | create a DeploymentConfig
[**create_namespaced_deploymentconfigrollback**](OapiV1.md#create_namespaced_deploymentconfigrollback) | **POST** /oapi/v1/namespaces/{namespace}/deploymentconfigrollbacks | create a DeploymentConfigRollback
[**create_namespaced_imagestream**](OapiV1.md#create_namespaced_imagestream) | **POST** /oapi/v1/namespaces/{namespace}/imagestreams | create a ImageStream
[**create_namespaced_imagestreamimport**](OapiV1.md#create_namespaced_imagestreamimport) | **POST** /oapi/v1/namespaces/{namespace}/imagestreamimports | create a ImageStreamImport
[**create_namespaced_imagestreammapping**](OapiV1.md#create_namespaced_imagestreammapping) | **POST** /oapi/v1/namespaces/{namespace}/imagestreammappings | create a ImageStreamMapping
[**create_namespaced_localresourceaccessreview**](OapiV1.md#create_namespaced_localresourceaccessreview) | **POST** /oapi/v1/namespaces/{namespace}/localresourceaccessreviews | create a LocalResourceAccessReview
[**create_namespaced_localsubjectaccessreview**](OapiV1.md#create_namespaced_localsubjectaccessreview) | **POST** /oapi/v1/namespaces/{namespace}/localsubjectaccessreviews | create a LocalSubjectAccessReview
[**create_namespaced_policie**](OapiV1.md#create_namespaced_policie) | **POST** /oapi/v1/namespaces/{namespace}/policies | create a Policy
[**create_namespaced_policybinding**](OapiV1.md#create_namespaced_policybinding) | **POST** /oapi/v1/namespaces/{namespace}/policybindings | create a PolicyBinding
[**create_namespaced_processedtemplate**](OapiV1.md#create_namespaced_processedtemplate) | **POST** /oapi/v1/namespaces/{namespace}/processedtemplates | create a Template
[**create_namespaced_resourceaccessreview**](OapiV1.md#create_namespaced_resourceaccessreview) | **POST** /oapi/v1/namespaces/{namespace}/resourceaccessreviews | create a ResourceAccessReview
[**create_namespaced_role**](OapiV1.md#create_namespaced_role) | **POST** /oapi/v1/namespaces/{namespace}/roles | create a Role
[**create_namespaced_rolebinding**](OapiV1.md#create_namespaced_rolebinding) | **POST** /oapi/v1/namespaces/{namespace}/rolebindings | create a RoleBinding
[**create_namespaced_route**](OapiV1.md#create_namespaced_route) | **POST** /oapi/v1/namespaces/{namespace}/routes | create a Route
[**create_namespaced_subjectaccessreview**](OapiV1.md#create_namespaced_subjectaccessreview) | **POST** /oapi/v1/namespaces/{namespace}/subjectaccessreviews | create a SubjectAccessReview
[**create_namespaced_template**](OapiV1.md#create_namespaced_template) | **POST** /oapi/v1/namespaces/{namespace}/templates | create a Template
[**create_netnamespace**](OapiV1.md#create_netnamespace) | **POST** /oapi/v1/netnamespaces | create a NetNamespace
[**create_oauthaccesstoken**](OapiV1.md#create_oauthaccesstoken) | **POST** /oapi/v1/oauthaccesstokens | create a OAuthAccessToken
[**create_oauthauthorizetoken**](OapiV1.md#create_oauthauthorizetoken) | **POST** /oapi/v1/oauthauthorizetokens | create a OAuthAuthorizeToken
[**create_oauthclient**](OapiV1.md#create_oauthclient) | **POST** /oapi/v1/oauthclients | create a OAuthClient
[**create_oauthclientauthorization**](OapiV1.md#create_oauthclientauthorization) | **POST** /oapi/v1/oauthclientauthorizations | create a OAuthClientAuthorization
[**create_policie**](OapiV1.md#create_policie) | **POST** /oapi/v1/policies | create a Policy
[**create_policybinding**](OapiV1.md#create_policybinding) | **POST** /oapi/v1/policybindings | create a PolicyBinding
[**create_processedtemplate**](OapiV1.md#create_processedtemplate) | **POST** /oapi/v1/processedtemplates | create a Template
[**create_project**](OapiV1.md#create_project) | **POST** /oapi/v1/projects | create a Project
[**create_projectrequest**](OapiV1.md#create_projectrequest) | **POST** /oapi/v1/projectrequests | create a ProjectRequest
[**create_resourceaccessreview**](OapiV1.md#create_resourceaccessreview) | **POST** /oapi/v1/resourceaccessreviews | create a ResourceAccessReview
[**create_role**](OapiV1.md#create_role) | **POST** /oapi/v1/roles | create a Role
[**create_rolebinding**](OapiV1.md#create_rolebinding) | **POST** /oapi/v1/rolebindings | create a RoleBinding
[**create_route**](OapiV1.md#create_route) | **POST** /oapi/v1/routes | create a Route
[**create_subjectaccessreview**](OapiV1.md#create_subjectaccessreview) | **POST** /oapi/v1/subjectaccessreviews | create a SubjectAccessReview
[**create_template**](OapiV1.md#create_template) | **POST** /oapi/v1/templates | create a Template
[**create_user**](OapiV1.md#create_user) | **POST** /oapi/v1/users | create a User
[**create_useridentitymapping**](OapiV1.md#create_useridentitymapping) | **POST** /oapi/v1/useridentitymappings | create a UserIdentityMapping
[**delete_clusternetwork**](OapiV1.md#delete_clusternetwork) | **DELETE** /oapi/v1/clusternetworks/{name} | delete a ClusterNetwork
[**delete_clusternetworks**](OapiV1.md#delete_clusternetworks) | **DELETE** /oapi/v1/clusternetworks | delete collection of ClusterNetwork
[**delete_clusterpolicie**](OapiV1.md#delete_clusterpolicie) | **DELETE** /oapi/v1/clusterpolicies/{name} | delete a ClusterPolicy
[**delete_clusterpolicies**](OapiV1.md#delete_clusterpolicies) | **DELETE** /oapi/v1/clusterpolicies | delete collection of ClusterPolicy
[**delete_clusterpolicybinding**](OapiV1.md#delete_clusterpolicybinding) | **DELETE** /oapi/v1/clusterpolicybindings/{name} | delete a ClusterPolicyBinding
[**delete_clusterpolicybindings**](OapiV1.md#delete_clusterpolicybindings) | **DELETE** /oapi/v1/clusterpolicybindings | delete collection of ClusterPolicyBinding
[**delete_clusterrole**](OapiV1.md#delete_clusterrole) | **DELETE** /oapi/v1/clusterroles/{name} | delete a ClusterRole
[**delete_clusterrolebinding**](OapiV1.md#delete_clusterrolebinding) | **DELETE** /oapi/v1/clusterrolebindings/{name} | delete a ClusterRoleBinding
[**delete_group**](OapiV1.md#delete_group) | **DELETE** /oapi/v1/groups/{name} | delete a Group
[**delete_groups**](OapiV1.md#delete_groups) | **DELETE** /oapi/v1/groups | delete collection of Group
[**delete_hostsubnet**](OapiV1.md#delete_hostsubnet) | **DELETE** /oapi/v1/hostsubnets/{name} | delete a HostSubnet
[**delete_hostsubnets**](OapiV1.md#delete_hostsubnets) | **DELETE** /oapi/v1/hostsubnets | delete collection of HostSubnet
[**delete_identitie**](OapiV1.md#delete_identitie) | **DELETE** /oapi/v1/identities/{name} | delete a Identity
[**delete_identities**](OapiV1.md#delete_identities) | **DELETE** /oapi/v1/identities | delete collection of Identity
[**delete_image**](OapiV1.md#delete_image) | **DELETE** /oapi/v1/images/{name} | delete a Image
[**delete_images**](OapiV1.md#delete_images) | **DELETE** /oapi/v1/images | delete collection of Image
[**delete_namespaced_build**](OapiV1.md#delete_namespaced_build) | **DELETE** /oapi/v1/namespaces/{namespace}/builds/{name} | delete a Build
[**delete_namespaced_buildconfig**](OapiV1.md#delete_namespaced_buildconfig) | **DELETE** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | delete a BuildConfig
[**delete_namespaced_buildconfigs**](OapiV1.md#delete_namespaced_buildconfigs) | **DELETE** /oapi/v1/namespaces/{namespace}/buildconfigs | delete collection of BuildConfig
[**delete_namespaced_builds**](OapiV1.md#delete_namespaced_builds) | **DELETE** /oapi/v1/namespaces/{namespace}/builds | delete collection of Build
[**delete_namespaced_deploymentconfig**](OapiV1.md#delete_namespaced_deploymentconfig) | **DELETE** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | delete a DeploymentConfig
[**delete_namespaced_deploymentconfigs**](OapiV1.md#delete_namespaced_deploymentconfigs) | **DELETE** /oapi/v1/namespaces/{namespace}/deploymentconfigs | delete collection of DeploymentConfig
[**delete_namespaced_imagestream**](OapiV1.md#delete_namespaced_imagestream) | **DELETE** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | delete a ImageStream
[**delete_namespaced_imagestreams**](OapiV1.md#delete_namespaced_imagestreams) | **DELETE** /oapi/v1/namespaces/{namespace}/imagestreams | delete collection of ImageStream
[**delete_namespaced_imagestreamtag**](OapiV1.md#delete_namespaced_imagestreamtag) | **DELETE** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | delete a ImageStreamTag
[**delete_namespaced_policie**](OapiV1.md#delete_namespaced_policie) | **DELETE** /oapi/v1/namespaces/{namespace}/policies/{name} | delete a Policy
[**delete_namespaced_policies**](OapiV1.md#delete_namespaced_policies) | **DELETE** /oapi/v1/namespaces/{namespace}/policies | delete collection of Policy
[**delete_namespaced_policybinding**](OapiV1.md#delete_namespaced_policybinding) | **DELETE** /oapi/v1/namespaces/{namespace}/policybindings/{name} | delete a PolicyBinding
[**delete_namespaced_policybindings**](OapiV1.md#delete_namespaced_policybindings) | **DELETE** /oapi/v1/namespaces/{namespace}/policybindings | delete collection of PolicyBinding
[**delete_namespaced_role**](OapiV1.md#delete_namespaced_role) | **DELETE** /oapi/v1/namespaces/{namespace}/roles/{name} | delete a Role
[**delete_namespaced_rolebinding**](OapiV1.md#delete_namespaced_rolebinding) | **DELETE** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | delete a RoleBinding
[**delete_namespaced_route**](OapiV1.md#delete_namespaced_route) | **DELETE** /oapi/v1/namespaces/{namespace}/routes/{name} | delete a Route
[**delete_namespaced_routes**](OapiV1.md#delete_namespaced_routes) | **DELETE** /oapi/v1/namespaces/{namespace}/routes | delete collection of Route
[**delete_namespaced_template**](OapiV1.md#delete_namespaced_template) | **DELETE** /oapi/v1/namespaces/{namespace}/templates/{name} | delete a Template
[**delete_namespaced_templates**](OapiV1.md#delete_namespaced_templates) | **DELETE** /oapi/v1/namespaces/{namespace}/templates | delete collection of Template
[**delete_netnamespace**](OapiV1.md#delete_netnamespace) | **DELETE** /oapi/v1/netnamespaces/{name} | delete a NetNamespace
[**delete_netnamespaces**](OapiV1.md#delete_netnamespaces) | **DELETE** /oapi/v1/netnamespaces | delete collection of NetNamespace
[**delete_oauthaccesstoken**](OapiV1.md#delete_oauthaccesstoken) | **DELETE** /oapi/v1/oauthaccesstokens/{name} | delete a OAuthAccessToken
[**delete_oauthauthorizetoken**](OapiV1.md#delete_oauthauthorizetoken) | **DELETE** /oapi/v1/oauthauthorizetokens/{name} | delete a OAuthAuthorizeToken
[**delete_oauthclient**](OapiV1.md#delete_oauthclient) | **DELETE** /oapi/v1/oauthclients/{name} | delete a OAuthClient
[**delete_oauthclientauthorization**](OapiV1.md#delete_oauthclientauthorization) | **DELETE** /oapi/v1/oauthclientauthorizations/{name} | delete a OAuthClientAuthorization
[**delete_oauthclientauthorizations**](OapiV1.md#delete_oauthclientauthorizations) | **DELETE** /oapi/v1/oauthclientauthorizations | delete collection of OAuthClientAuthorization
[**delete_oauthclients**](OapiV1.md#delete_oauthclients) | **DELETE** /oapi/v1/oauthclients | delete collection of OAuthClient
[**delete_project**](OapiV1.md#delete_project) | **DELETE** /oapi/v1/projects/{name} | delete a Project
[**delete_user**](OapiV1.md#delete_user) | **DELETE** /oapi/v1/users/{name} | delete a User
[**delete_useridentitymapping**](OapiV1.md#delete_useridentitymapping) | **DELETE** /oapi/v1/useridentitymappings/{name} | delete a UserIdentityMapping
[**delete_users**](OapiV1.md#delete_users) | **DELETE** /oapi/v1/users | delete collection of User
[**get_clusternetwork**](OapiV1.md#get_clusternetwork) | **GET** /oapi/v1/clusternetworks/{name} | read the specified ClusterNetwork
[**get_clusterpolicie**](OapiV1.md#get_clusterpolicie) | **GET** /oapi/v1/clusterpolicies/{name} | read the specified ClusterPolicy
[**get_clusterpolicybinding**](OapiV1.md#get_clusterpolicybinding) | **GET** /oapi/v1/clusterpolicybindings/{name} | read the specified ClusterPolicyBinding
[**get_clusterrole**](OapiV1.md#get_clusterrole) | **GET** /oapi/v1/clusterroles/{name} | read the specified ClusterRole
[**get_clusterrolebinding**](OapiV1.md#get_clusterrolebinding) | **GET** /oapi/v1/clusterrolebindings/{name} | read the specified ClusterRoleBinding
[**get_group**](OapiV1.md#get_group) | **GET** /oapi/v1/groups/{name} | read the specified Group
[**get_hostsubnet**](OapiV1.md#get_hostsubnet) | **GET** /oapi/v1/hostsubnets/{name} | read the specified HostSubnet
[**get_identitie**](OapiV1.md#get_identitie) | **GET** /oapi/v1/identities/{name} | read the specified Identity
[**get_image**](OapiV1.md#get_image) | **GET** /oapi/v1/images/{name} | read the specified Image
[**get_namespaced_build**](OapiV1.md#get_namespaced_build) | **GET** /oapi/v1/namespaces/{namespace}/builds/{name} | read the specified Build
[**get_namespaced_build_log**](OapiV1.md#get_namespaced_build_log) | **GET** /oapi/v1/namespaces/{namespace}/builds/{name}/log | read log of the specified BuildLog
[**get_namespaced_buildconfig**](OapiV1.md#get_namespaced_buildconfig) | **GET** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | read the specified BuildConfig
[**get_namespaced_deploymentconfig**](OapiV1.md#get_namespaced_deploymentconfig) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | read the specified DeploymentConfig
[**get_namespaced_deploymentconfig_log**](OapiV1.md#get_namespaced_deploymentconfig_log) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/log | read log of the specified DeploymentLog
[**get_namespaced_deploymentconfig_scale**](OapiV1.md#get_namespaced_deploymentconfig_scale) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | read scale of the specified Scale
[**get_namespaced_generatedeploymentconfig**](OapiV1.md#get_namespaced_generatedeploymentconfig) | **GET** /oapi/v1/namespaces/{namespace}/generatedeploymentconfigs/{name} | read the specified DeploymentConfig
[**get_namespaced_imagestream**](OapiV1.md#get_namespaced_imagestream) | **GET** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | read the specified ImageStream
[**get_namespaced_imagestream_secrets**](OapiV1.md#get_namespaced_imagestream_secrets) | **GET** /oapi/v1/namespaces/{namespace}/imagestreams/{name}/secrets | read secrets of the specified SecretList
[**get_namespaced_imagestreamimage**](OapiV1.md#get_namespaced_imagestreamimage) | **GET** /oapi/v1/namespaces/{namespace}/imagestreamimages/{name} | read the specified ImageStreamImage
[**get_namespaced_imagestreamtag**](OapiV1.md#get_namespaced_imagestreamtag) | **GET** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | read the specified ImageStreamTag
[**get_namespaced_policie**](OapiV1.md#get_namespaced_policie) | **GET** /oapi/v1/namespaces/{namespace}/policies/{name} | read the specified Policy
[**get_namespaced_policybinding**](OapiV1.md#get_namespaced_policybinding) | **GET** /oapi/v1/namespaces/{namespace}/policybindings/{name} | read the specified PolicyBinding
[**get_namespaced_role**](OapiV1.md#get_namespaced_role) | **GET** /oapi/v1/namespaces/{namespace}/roles/{name} | read the specified Role
[**get_namespaced_rolebinding**](OapiV1.md#get_namespaced_rolebinding) | **GET** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | read the specified RoleBinding
[**get_namespaced_route**](OapiV1.md#get_namespaced_route) | **GET** /oapi/v1/namespaces/{namespace}/routes/{name} | read the specified Route
[**get_namespaced_template**](OapiV1.md#get_namespaced_template) | **GET** /oapi/v1/namespaces/{namespace}/templates/{name} | read the specified Template
[**get_netnamespace**](OapiV1.md#get_netnamespace) | **GET** /oapi/v1/netnamespaces/{name} | read the specified NetNamespace
[**get_oauthaccesstoken**](OapiV1.md#get_oauthaccesstoken) | **GET** /oapi/v1/oauthaccesstokens/{name} | read the specified OAuthAccessToken
[**get_oauthauthorizetoken**](OapiV1.md#get_oauthauthorizetoken) | **GET** /oapi/v1/oauthauthorizetokens/{name} | read the specified OAuthAuthorizeToken
[**get_oauthclient**](OapiV1.md#get_oauthclient) | **GET** /oapi/v1/oauthclients/{name} | read the specified OAuthClient
[**get_oauthclientauthorization**](OapiV1.md#get_oauthclientauthorization) | **GET** /oapi/v1/oauthclientauthorizations/{name} | read the specified OAuthClientAuthorization
[**get_project**](OapiV1.md#get_project) | **GET** /oapi/v1/projects/{name} | read the specified Project
[**get_user**](OapiV1.md#get_user) | **GET** /oapi/v1/users/{name} | read the specified User
[**get_useridentitymapping**](OapiV1.md#get_useridentitymapping) | **GET** /oapi/v1/useridentitymappings/{name} | read the specified UserIdentityMapping
[**list**](OapiV1.md#list) | **GET** /oapi/v1 | get available resources
[**list_buildconfigs**](OapiV1.md#list_buildconfigs) | **GET** /oapi/v1/buildconfigs | list or watch objects of kind BuildConfig
[**list_builds**](OapiV1.md#list_builds) | **GET** /oapi/v1/builds | list or watch objects of kind Build
[**list_clusternetworks**](OapiV1.md#list_clusternetworks) | **GET** /oapi/v1/clusternetworks | list or watch objects of kind ClusterNetwork
[**list_clusterpolicies**](OapiV1.md#list_clusterpolicies) | **GET** /oapi/v1/clusterpolicies | list or watch objects of kind ClusterPolicy
[**list_clusterpolicybindings**](OapiV1.md#list_clusterpolicybindings) | **GET** /oapi/v1/clusterpolicybindings | list or watch objects of kind ClusterPolicyBinding
[**list_clusterrolebindings**](OapiV1.md#list_clusterrolebindings) | **GET** /oapi/v1/clusterrolebindings | list objects of kind ClusterRoleBinding
[**list_clusterroles**](OapiV1.md#list_clusterroles) | **GET** /oapi/v1/clusterroles | list objects of kind ClusterRole
[**list_deploymentconfigs**](OapiV1.md#list_deploymentconfigs) | **GET** /oapi/v1/deploymentconfigs | list or watch objects of kind DeploymentConfig
[**list_groups**](OapiV1.md#list_groups) | **GET** /oapi/v1/groups | list or watch objects of kind Group
[**list_hostsubnets**](OapiV1.md#list_hostsubnets) | **GET** /oapi/v1/hostsubnets | list or watch objects of kind HostSubnet
[**list_identities**](OapiV1.md#list_identities) | **GET** /oapi/v1/identities | list or watch objects of kind Identity
[**list_images**](OapiV1.md#list_images) | **GET** /oapi/v1/images | list or watch objects of kind Image
[**list_imagestreams**](OapiV1.md#list_imagestreams) | **GET** /oapi/v1/imagestreams | list or watch objects of kind ImageStream
[**list_imagestreamtags**](OapiV1.md#list_imagestreamtags) | **GET** /oapi/v1/imagestreamtags | list objects of kind ImageStreamTag
[**list_namespaced_buildconfigs**](OapiV1.md#list_namespaced_buildconfigs) | **GET** /oapi/v1/namespaces/{namespace}/buildconfigs | list or watch objects of kind BuildConfig
[**list_namespaced_builds**](OapiV1.md#list_namespaced_builds) | **GET** /oapi/v1/namespaces/{namespace}/builds | list or watch objects of kind Build
[**list_namespaced_deploymentconfigs**](OapiV1.md#list_namespaced_deploymentconfigs) | **GET** /oapi/v1/namespaces/{namespace}/deploymentconfigs | list or watch objects of kind DeploymentConfig
[**list_namespaced_imagestreams**](OapiV1.md#list_namespaced_imagestreams) | **GET** /oapi/v1/namespaces/{namespace}/imagestreams | list or watch objects of kind ImageStream
[**list_namespaced_imagestreamtags**](OapiV1.md#list_namespaced_imagestreamtags) | **GET** /oapi/v1/namespaces/{namespace}/imagestreamtags | list objects of kind ImageStreamTag
[**list_namespaced_policies**](OapiV1.md#list_namespaced_policies) | **GET** /oapi/v1/namespaces/{namespace}/policies | list or watch objects of kind Policy
[**list_namespaced_policybindings**](OapiV1.md#list_namespaced_policybindings) | **GET** /oapi/v1/namespaces/{namespace}/policybindings | list or watch objects of kind PolicyBinding
[**list_namespaced_rolebindings**](OapiV1.md#list_namespaced_rolebindings) | **GET** /oapi/v1/namespaces/{namespace}/rolebindings | list objects of kind RoleBinding
[**list_namespaced_roles**](OapiV1.md#list_namespaced_roles) | **GET** /oapi/v1/namespaces/{namespace}/roles | list objects of kind Role
[**list_namespaced_routes**](OapiV1.md#list_namespaced_routes) | **GET** /oapi/v1/namespaces/{namespace}/routes | list or watch objects of kind Route
[**list_namespaced_templates**](OapiV1.md#list_namespaced_templates) | **GET** /oapi/v1/namespaces/{namespace}/templates | list or watch objects of kind Template
[**list_netnamespaces**](OapiV1.md#list_netnamespaces) | **GET** /oapi/v1/netnamespaces | list or watch objects of kind NetNamespace
[**list_oauthaccesstokens**](OapiV1.md#list_oauthaccesstokens) | **GET** /oapi/v1/oauthaccesstokens | list objects of kind OAuthAccessToken
[**list_oauthauthorizetokens**](OapiV1.md#list_oauthauthorizetokens) | **GET** /oapi/v1/oauthauthorizetokens | list objects of kind OAuthAuthorizeToken
[**list_oauthclientauthorizations**](OapiV1.md#list_oauthclientauthorizations) | **GET** /oapi/v1/oauthclientauthorizations | list or watch objects of kind OAuthClientAuthorization
[**list_oauthclients**](OapiV1.md#list_oauthclients) | **GET** /oapi/v1/oauthclients | list or watch objects of kind OAuthClient
[**list_policies**](OapiV1.md#list_policies) | **GET** /oapi/v1/policies | list or watch objects of kind Policy
[**list_policybindings**](OapiV1.md#list_policybindings) | **GET** /oapi/v1/policybindings | list or watch objects of kind PolicyBinding
[**list_projectrequests**](OapiV1.md#list_projectrequests) | **GET** /oapi/v1/projectrequests | list objects of kind ProjectRequest
[**list_projects**](OapiV1.md#list_projects) | **GET** /oapi/v1/projects | list objects of kind Project
[**list_rolebindings**](OapiV1.md#list_rolebindings) | **GET** /oapi/v1/rolebindings | list objects of kind RoleBinding
[**list_roles**](OapiV1.md#list_roles) | **GET** /oapi/v1/roles | list objects of kind Role
[**list_routes**](OapiV1.md#list_routes) | **GET** /oapi/v1/routes | list or watch objects of kind Route
[**list_templates**](OapiV1.md#list_templates) | **GET** /oapi/v1/templates | list or watch objects of kind Template
[**list_users**](OapiV1.md#list_users) | **GET** /oapi/v1/users | list or watch objects of kind User
[**patch_clusternetwork**](OapiV1.md#patch_clusternetwork) | **PATCH** /oapi/v1/clusternetworks/{name} | partially update the specified ClusterNetwork
[**patch_clusterpolicie**](OapiV1.md#patch_clusterpolicie) | **PATCH** /oapi/v1/clusterpolicies/{name} | partially update the specified ClusterPolicy
[**patch_clusterpolicybinding**](OapiV1.md#patch_clusterpolicybinding) | **PATCH** /oapi/v1/clusterpolicybindings/{name} | partially update the specified ClusterPolicyBinding
[**patch_clusterrole**](OapiV1.md#patch_clusterrole) | **PATCH** /oapi/v1/clusterroles/{name} | partially update the specified ClusterRole
[**patch_clusterrolebinding**](OapiV1.md#patch_clusterrolebinding) | **PATCH** /oapi/v1/clusterrolebindings/{name} | partially update the specified ClusterRoleBinding
[**patch_group**](OapiV1.md#patch_group) | **PATCH** /oapi/v1/groups/{name} | partially update the specified Group
[**patch_hostsubnet**](OapiV1.md#patch_hostsubnet) | **PATCH** /oapi/v1/hostsubnets/{name} | partially update the specified HostSubnet
[**patch_identitie**](OapiV1.md#patch_identitie) | **PATCH** /oapi/v1/identities/{name} | partially update the specified Identity
[**patch_image**](OapiV1.md#patch_image) | **PATCH** /oapi/v1/images/{name} | partially update the specified Image
[**patch_namespaced_build**](OapiV1.md#patch_namespaced_build) | **PATCH** /oapi/v1/namespaces/{namespace}/builds/{name} | partially update the specified Build
[**patch_namespaced_buildconfig**](OapiV1.md#patch_namespaced_buildconfig) | **PATCH** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | partially update the specified BuildConfig
[**patch_namespaced_deploymentconfig**](OapiV1.md#patch_namespaced_deploymentconfig) | **PATCH** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | partially update the specified DeploymentConfig
[**patch_namespaced_deploymentconfig_scale**](OapiV1.md#patch_namespaced_deploymentconfig_scale) | **PATCH** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | partially update scale of the specified Scale
[**patch_namespaced_imagestream**](OapiV1.md#patch_namespaced_imagestream) | **PATCH** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | partially update the specified ImageStream
[**patch_namespaced_imagestreamtag**](OapiV1.md#patch_namespaced_imagestreamtag) | **PATCH** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | partially update the specified ImageStreamTag
[**patch_namespaced_policie**](OapiV1.md#patch_namespaced_policie) | **PATCH** /oapi/v1/namespaces/{namespace}/policies/{name} | partially update the specified Policy
[**patch_namespaced_policybinding**](OapiV1.md#patch_namespaced_policybinding) | **PATCH** /oapi/v1/namespaces/{namespace}/policybindings/{name} | partially update the specified PolicyBinding
[**patch_namespaced_role**](OapiV1.md#patch_namespaced_role) | **PATCH** /oapi/v1/namespaces/{namespace}/roles/{name} | partially update the specified Role
[**patch_namespaced_rolebinding**](OapiV1.md#patch_namespaced_rolebinding) | **PATCH** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | partially update the specified RoleBinding
[**patch_namespaced_route**](OapiV1.md#patch_namespaced_route) | **PATCH** /oapi/v1/namespaces/{namespace}/routes/{name} | partially update the specified Route
[**patch_namespaced_template**](OapiV1.md#patch_namespaced_template) | **PATCH** /oapi/v1/namespaces/{namespace}/templates/{name} | partially update the specified Template
[**patch_netnamespace**](OapiV1.md#patch_netnamespace) | **PATCH** /oapi/v1/netnamespaces/{name} | partially update the specified NetNamespace
[**patch_oauthclient**](OapiV1.md#patch_oauthclient) | **PATCH** /oapi/v1/oauthclients/{name} | partially update the specified OAuthClient
[**patch_oauthclientauthorization**](OapiV1.md#patch_oauthclientauthorization) | **PATCH** /oapi/v1/oauthclientauthorizations/{name} | partially update the specified OAuthClientAuthorization
[**patch_project**](OapiV1.md#patch_project) | **PATCH** /oapi/v1/projects/{name} | partially update the specified Project
[**patch_user**](OapiV1.md#patch_user) | **PATCH** /oapi/v1/users/{name} | partially update the specified User
[**patch_useridentitymapping**](OapiV1.md#patch_useridentitymapping) | **PATCH** /oapi/v1/useridentitymappings/{name} | partially update the specified UserIdentityMapping
[**replace_clusternetwork**](OapiV1.md#replace_clusternetwork) | **PUT** /oapi/v1/clusternetworks/{name} | replace the specified ClusterNetwork
[**replace_clusterpolicie**](OapiV1.md#replace_clusterpolicie) | **PUT** /oapi/v1/clusterpolicies/{name} | replace the specified ClusterPolicy
[**replace_clusterpolicybinding**](OapiV1.md#replace_clusterpolicybinding) | **PUT** /oapi/v1/clusterpolicybindings/{name} | replace the specified ClusterPolicyBinding
[**replace_clusterrole**](OapiV1.md#replace_clusterrole) | **PUT** /oapi/v1/clusterroles/{name} | replace the specified ClusterRole
[**replace_clusterrolebinding**](OapiV1.md#replace_clusterrolebinding) | **PUT** /oapi/v1/clusterrolebindings/{name} | replace the specified ClusterRoleBinding
[**replace_group**](OapiV1.md#replace_group) | **PUT** /oapi/v1/groups/{name} | replace the specified Group
[**replace_hostsubnet**](OapiV1.md#replace_hostsubnet) | **PUT** /oapi/v1/hostsubnets/{name} | replace the specified HostSubnet
[**replace_identitie**](OapiV1.md#replace_identitie) | **PUT** /oapi/v1/identities/{name} | replace the specified Identity
[**replace_image**](OapiV1.md#replace_image) | **PUT** /oapi/v1/images/{name} | replace the specified Image
[**replace_namespaced_build**](OapiV1.md#replace_namespaced_build) | **PUT** /oapi/v1/namespaces/{namespace}/builds/{name} | replace the specified Build
[**replace_namespaced_build_details**](OapiV1.md#replace_namespaced_build_details) | **PUT** /oapi/v1/namespaces/{namespace}/builds/{name}/details | replace details of the specified Build
[**replace_namespaced_buildconfig**](OapiV1.md#replace_namespaced_buildconfig) | **PUT** /oapi/v1/namespaces/{namespace}/buildconfigs/{name} | replace the specified BuildConfig
[**replace_namespaced_deploymentconfig**](OapiV1.md#replace_namespaced_deploymentconfig) | **PUT** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name} | replace the specified DeploymentConfig
[**replace_namespaced_deploymentconfig_scale**](OapiV1.md#replace_namespaced_deploymentconfig_scale) | **PUT** /oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | replace scale of the specified Scale
[**replace_namespaced_imagestream**](OapiV1.md#replace_namespaced_imagestream) | **PUT** /oapi/v1/namespaces/{namespace}/imagestreams/{name} | replace the specified ImageStream
[**replace_namespaced_imagestreamtag**](OapiV1.md#replace_namespaced_imagestreamtag) | **PUT** /oapi/v1/namespaces/{namespace}/imagestreamtags/{name} | replace the specified ImageStreamTag
[**replace_namespaced_policie**](OapiV1.md#replace_namespaced_policie) | **PUT** /oapi/v1/namespaces/{namespace}/policies/{name} | replace the specified Policy
[**replace_namespaced_policybinding**](OapiV1.md#replace_namespaced_policybinding) | **PUT** /oapi/v1/namespaces/{namespace}/policybindings/{name} | replace the specified PolicyBinding
[**replace_namespaced_role**](OapiV1.md#replace_namespaced_role) | **PUT** /oapi/v1/namespaces/{namespace}/roles/{name} | replace the specified Role
[**replace_namespaced_rolebinding**](OapiV1.md#replace_namespaced_rolebinding) | **PUT** /oapi/v1/namespaces/{namespace}/rolebindings/{name} | replace the specified RoleBinding
[**replace_namespaced_route**](OapiV1.md#replace_namespaced_route) | **PUT** /oapi/v1/namespaces/{namespace}/routes/{name} | replace the specified Route
[**replace_namespaced_template**](OapiV1.md#replace_namespaced_template) | **PUT** /oapi/v1/namespaces/{namespace}/templates/{name} | replace the specified Template
[**replace_netnamespace**](OapiV1.md#replace_netnamespace) | **PUT** /oapi/v1/netnamespaces/{name} | replace the specified NetNamespace
[**replace_oauthclient**](OapiV1.md#replace_oauthclient) | **PUT** /oapi/v1/oauthclients/{name} | replace the specified OAuthClient
[**replace_oauthclientauthorization**](OapiV1.md#replace_oauthclientauthorization) | **PUT** /oapi/v1/oauthclientauthorizations/{name} | replace the specified OAuthClientAuthorization
[**replace_project**](OapiV1.md#replace_project) | **PUT** /oapi/v1/projects/{name} | replace the specified Project
[**replace_user**](OapiV1.md#replace_user) | **PUT** /oapi/v1/users/{name} | replace the specified User
[**replace_useridentitymapping**](OapiV1.md#replace_useridentitymapping) | **PUT** /oapi/v1/useridentitymappings/{name} | replace the specified UserIdentityMapping
[**watch_namespaced_watch_build**](OapiV1.md#watch_namespaced_watch_build) | **GET** /oapi/v1/watch/namespaces/{namespace}/builds/{name} | watch changes to an object of kind Build
[**watch_namespaced_watch_buildconfig**](OapiV1.md#watch_namespaced_watch_buildconfig) | **GET** /oapi/v1/watch/namespaces/{namespace}/buildconfigs/{name} | watch changes to an object of kind BuildConfig
[**watch_namespaced_watch_buildconfigs**](OapiV1.md#watch_namespaced_watch_buildconfigs) | **GET** /oapi/v1/watch/namespaces/{namespace}/buildconfigs | watch individual changes to a list of BuildConfig
[**watch_namespaced_watch_builds**](OapiV1.md#watch_namespaced_watch_builds) | **GET** /oapi/v1/watch/namespaces/{namespace}/builds | watch individual changes to a list of Build
[**watch_namespaced_watch_deploymentconfig**](OapiV1.md#watch_namespaced_watch_deploymentconfig) | **GET** /oapi/v1/watch/namespaces/{namespace}/deploymentconfigs/{name} | watch changes to an object of kind DeploymentConfig
[**watch_namespaced_watch_deploymentconfigs**](OapiV1.md#watch_namespaced_watch_deploymentconfigs) | **GET** /oapi/v1/watch/namespaces/{namespace}/deploymentconfigs | watch individual changes to a list of DeploymentConfig
[**watch_namespaced_watch_imagestream**](OapiV1.md#watch_namespaced_watch_imagestream) | **GET** /oapi/v1/watch/namespaces/{namespace}/imagestreams/{name} | watch changes to an object of kind ImageStream
[**watch_namespaced_watch_imagestreams**](OapiV1.md#watch_namespaced_watch_imagestreams) | **GET** /oapi/v1/watch/namespaces/{namespace}/imagestreams | watch individual changes to a list of ImageStream
[**watch_namespaced_watch_policie**](OapiV1.md#watch_namespaced_watch_policie) | **GET** /oapi/v1/watch/namespaces/{namespace}/policies/{name} | watch changes to an object of kind Policy
[**watch_namespaced_watch_policies**](OapiV1.md#watch_namespaced_watch_policies) | **GET** /oapi/v1/watch/namespaces/{namespace}/policies | watch individual changes to a list of Policy
[**watch_namespaced_watch_policybinding**](OapiV1.md#watch_namespaced_watch_policybinding) | **GET** /oapi/v1/watch/namespaces/{namespace}/policybindings/{name} | watch changes to an object of kind PolicyBinding
[**watch_namespaced_watch_policybindings**](OapiV1.md#watch_namespaced_watch_policybindings) | **GET** /oapi/v1/watch/namespaces/{namespace}/policybindings | watch individual changes to a list of PolicyBinding
[**watch_namespaced_watch_route**](OapiV1.md#watch_namespaced_watch_route) | **GET** /oapi/v1/watch/namespaces/{namespace}/routes/{name} | watch changes to an object of kind Route
[**watch_namespaced_watch_routes**](OapiV1.md#watch_namespaced_watch_routes) | **GET** /oapi/v1/watch/namespaces/{namespace}/routes | watch individual changes to a list of Route
[**watch_namespaced_watch_template**](OapiV1.md#watch_namespaced_watch_template) | **GET** /oapi/v1/watch/namespaces/{namespace}/templates/{name} | watch changes to an object of kind Template
[**watch_namespaced_watch_templates**](OapiV1.md#watch_namespaced_watch_templates) | **GET** /oapi/v1/watch/namespaces/{namespace}/templates | watch individual changes to a list of Template
[**watch_watch_buildconfigs**](OapiV1.md#watch_watch_buildconfigs) | **GET** /oapi/v1/watch/buildconfigs | watch individual changes to a list of BuildConfig
[**watch_watch_builds**](OapiV1.md#watch_watch_builds) | **GET** /oapi/v1/watch/builds | watch individual changes to a list of Build
[**watch_watch_clusternetwork**](OapiV1.md#watch_watch_clusternetwork) | **GET** /oapi/v1/watch/clusternetworks/{name} | watch changes to an object of kind ClusterNetwork
[**watch_watch_clusternetworks**](OapiV1.md#watch_watch_clusternetworks) | **GET** /oapi/v1/watch/clusternetworks | watch individual changes to a list of ClusterNetwork
[**watch_watch_clusterpolicie**](OapiV1.md#watch_watch_clusterpolicie) | **GET** /oapi/v1/watch/clusterpolicies/{name} | watch changes to an object of kind ClusterPolicy
[**watch_watch_clusterpolicies**](OapiV1.md#watch_watch_clusterpolicies) | **GET** /oapi/v1/watch/clusterpolicies | watch individual changes to a list of ClusterPolicy
[**watch_watch_clusterpolicybinding**](OapiV1.md#watch_watch_clusterpolicybinding) | **GET** /oapi/v1/watch/clusterpolicybindings/{name} | watch changes to an object of kind ClusterPolicyBinding
[**watch_watch_clusterpolicybindings**](OapiV1.md#watch_watch_clusterpolicybindings) | **GET** /oapi/v1/watch/clusterpolicybindings | watch individual changes to a list of ClusterPolicyBinding
[**watch_watch_deploymentconfigs**](OapiV1.md#watch_watch_deploymentconfigs) | **GET** /oapi/v1/watch/deploymentconfigs | watch individual changes to a list of DeploymentConfig
[**watch_watch_group**](OapiV1.md#watch_watch_group) | **GET** /oapi/v1/watch/groups/{name} | watch changes to an object of kind Group
[**watch_watch_groups**](OapiV1.md#watch_watch_groups) | **GET** /oapi/v1/watch/groups | watch individual changes to a list of Group
[**watch_watch_hostsubnet**](OapiV1.md#watch_watch_hostsubnet) | **GET** /oapi/v1/watch/hostsubnets/{name} | watch changes to an object of kind HostSubnet
[**watch_watch_hostsubnets**](OapiV1.md#watch_watch_hostsubnets) | **GET** /oapi/v1/watch/hostsubnets | watch individual changes to a list of HostSubnet
[**watch_watch_identitie**](OapiV1.md#watch_watch_identitie) | **GET** /oapi/v1/watch/identities/{name} | watch changes to an object of kind Identity
[**watch_watch_identities**](OapiV1.md#watch_watch_identities) | **GET** /oapi/v1/watch/identities | watch individual changes to a list of Identity
[**watch_watch_image**](OapiV1.md#watch_watch_image) | **GET** /oapi/v1/watch/images/{name} | watch changes to an object of kind Image
[**watch_watch_images**](OapiV1.md#watch_watch_images) | **GET** /oapi/v1/watch/images | watch individual changes to a list of Image
[**watch_watch_imagestreams**](OapiV1.md#watch_watch_imagestreams) | **GET** /oapi/v1/watch/imagestreams | watch individual changes to a list of ImageStream
[**watch_watch_netnamespace**](OapiV1.md#watch_watch_netnamespace) | **GET** /oapi/v1/watch/netnamespaces/{name} | watch changes to an object of kind NetNamespace
[**watch_watch_netnamespaces**](OapiV1.md#watch_watch_netnamespaces) | **GET** /oapi/v1/watch/netnamespaces | watch individual changes to a list of NetNamespace
[**watch_watch_oauthclient**](OapiV1.md#watch_watch_oauthclient) | **GET** /oapi/v1/watch/oauthclients/{name} | watch changes to an object of kind OAuthClient
[**watch_watch_oauthclientauthorization**](OapiV1.md#watch_watch_oauthclientauthorization) | **GET** /oapi/v1/watch/oauthclientauthorizations/{name} | watch changes to an object of kind OAuthClientAuthorization
[**watch_watch_oauthclientauthorizations**](OapiV1.md#watch_watch_oauthclientauthorizations) | **GET** /oapi/v1/watch/oauthclientauthorizations | watch individual changes to a list of OAuthClientAuthorization
[**watch_watch_oauthclients**](OapiV1.md#watch_watch_oauthclients) | **GET** /oapi/v1/watch/oauthclients | watch individual changes to a list of OAuthClient
[**watch_watch_policies**](OapiV1.md#watch_watch_policies) | **GET** /oapi/v1/watch/policies | watch individual changes to a list of Policy
[**watch_watch_policybindings**](OapiV1.md#watch_watch_policybindings) | **GET** /oapi/v1/watch/policybindings | watch individual changes to a list of PolicyBinding
[**watch_watch_routes**](OapiV1.md#watch_watch_routes) | **GET** /oapi/v1/watch/routes | watch individual changes to a list of Route
[**watch_watch_templates**](OapiV1.md#watch_watch_templates) | **GET** /oapi/v1/watch/templates | watch individual changes to a list of Template
[**watch_watch_user**](OapiV1.md#watch_watch_user) | **GET** /oapi/v1/watch/users/{name} | watch changes to an object of kind User
[**watch_watch_users**](OapiV1.md#watch_watch_users) | **GET** /oapi/v1/watch/users | watch individual changes to a list of User


# **create_build**
> V1Build create_build(body, pretty=pretty)

create a Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Build() # V1Build | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Build
    api_response = api_instance.create_build(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_build: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buildconfig**
> V1BuildConfig create_buildconfig(body, pretty=pretty)

create a BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1BuildConfig() # V1BuildConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a BuildConfig
    api_response = api_instance.create_buildconfig(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_buildconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clusternetwork**
> V1ClusterNetwork create_clusternetwork(body, pretty=pretty)

create a ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterNetwork() # V1ClusterNetwork | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterNetwork
    api_response = api_instance.create_clusternetwork(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_clusternetwork: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clusterpolicie**
> V1ClusterPolicy create_clusterpolicie(body, pretty=pretty)

create a ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterPolicy() # V1ClusterPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterPolicy
    api_response = api_instance.create_clusterpolicie(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_clusterpolicie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clusterpolicybinding**
> V1ClusterPolicyBinding create_clusterpolicybinding(body, pretty=pretty)

create a ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterPolicyBinding() # V1ClusterPolicyBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterPolicyBinding
    api_response = api_instance.create_clusterpolicybinding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_clusterpolicybinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clusterrole**
> V1ClusterRole create_clusterrole(body, pretty=pretty)

create a ClusterRole

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterRole() # V1ClusterRole | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterRole
    api_response = api_instance.create_clusterrole(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_clusterrole: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clusterrolebinding**
> V1ClusterRoleBinding create_clusterrolebinding(body, pretty=pretty)

create a ClusterRoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterRoleBinding() # V1ClusterRoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ClusterRoleBinding
    api_response = api_instance.create_clusterrolebinding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_clusterrolebinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deploymentconfig**
> V1DeploymentConfig create_deploymentconfig(body, pretty=pretty)

create a DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeploymentConfig() # V1DeploymentConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfig
    api_response = api_instance.create_deploymentconfig(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_deploymentconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deploymentconfigrollback**
> V1DeploymentConfigRollback create_deploymentconfigrollback(body, pretty=pretty)

create a DeploymentConfigRollback

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeploymentConfigRollback() # V1DeploymentConfigRollback | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfigRollback
    api_response = api_instance.create_deploymentconfigrollback(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_deploymentconfigrollback: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> V1Group create_group(body, pretty=pretty)

create a Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Group() # V1Group | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Group
    api_response = api_instance.create_group(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_group: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hostsubnet**
> V1HostSubnet create_hostsubnet(body, pretty=pretty)

create a HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1HostSubnet() # V1HostSubnet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a HostSubnet
    api_response = api_instance.create_hostsubnet(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_hostsubnet: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_identitie**
> V1Identity create_identitie(body, pretty=pretty)

create a Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Identity() # V1Identity | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Identity
    api_response = api_instance.create_identitie(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_identitie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image**
> V1Image create_image(body, pretty=pretty)

create a Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Image() # V1Image | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Image
    api_response = api_instance.create_image(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_image: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_imagestream**
> V1ImageStream create_imagestream(body, pretty=pretty)

create a ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStream() # V1ImageStream | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStream
    api_response = api_instance.create_imagestream(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_imagestream: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_imagestreamimport**
> V1ImageStreamImport create_imagestreamimport(body, pretty=pretty)

create a ImageStreamImport

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStreamImport() # V1ImageStreamImport | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamImport
    api_response = api_instance.create_imagestreamimport(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_imagestreamimport: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_imagestreammapping**
> V1ImageStreamMapping create_imagestreammapping(body, pretty=pretty)

create a ImageStreamMapping

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStreamMapping() # V1ImageStreamMapping | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamMapping
    api_response = api_instance.create_imagestreammapping(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_imagestreammapping: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localresourceaccessreview**
> V1LocalResourceAccessReview create_localresourceaccessreview(body, pretty=pretty)

create a LocalResourceAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1LocalResourceAccessReview() # V1LocalResourceAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalResourceAccessReview
    api_response = api_instance.create_localresourceaccessreview(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_localresourceaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_localsubjectaccessreview**
> V1LocalSubjectAccessReview create_localsubjectaccessreview(body, pretty=pretty)

create a LocalSubjectAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1LocalSubjectAccessReview() # V1LocalSubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalSubjectAccessReview
    api_response = api_instance.create_localsubjectaccessreview(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_localsubjectaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_build**
> V1Build create_namespaced_build(body, namespace, pretty=pretty)

create a Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Build() # V1Build | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Build
    api_response = api_instance.create_namespaced_build(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_build: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_build_clone**
> V1BuildRequest create_namespaced_build_clone(body, namespace, name, pretty=pretty)

create clone of a BuildRequest

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1BuildRequest() # V1BuildRequest | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildRequest
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create clone of a BuildRequest
    api_response = api_instance.create_namespaced_build_clone(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_build_clone: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_buildconfig**
> V1BuildConfig create_namespaced_buildconfig(body, namespace, pretty=pretty)

create a BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1BuildConfig() # V1BuildConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a BuildConfig
    api_response = api_instance.create_namespaced_buildconfig(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_buildconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_buildconfig_instantiate**
> V1BuildRequest create_namespaced_buildconfig_instantiate(body, namespace, name, pretty=pretty)

create instantiate of a BuildRequest

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1BuildRequest() # V1BuildRequest | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildRequest
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create instantiate of a BuildRequest
    api_response = api_instance.create_namespaced_buildconfig_instantiate(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_buildconfig_instantiate: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_buildconfig_instantiatebinary**
> str create_namespaced_buildconfig_instantiatebinary(namespace, name, as_file=as_file, revision_commit=revision_commit, revision_message=revision_message, revision_author_name=revision_author_name, revision_author_email=revision_author_email, revision_committer_name=revision_committer_name, revision_committer_email=revision_committer_email)

connect POST requests to instantiatebinary of BinaryBuildRequestOptions

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.create_namespaced_buildconfig_instantiatebinary(namespace, name, as_file=as_file, revision_commit=revision_commit, revision_message=revision_message, revision_author_name=revision_author_name, revision_author_email=revision_author_email, revision_committer_name=revision_committer_name, revision_committer_email=revision_committer_email)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_buildconfig_instantiatebinary: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_buildconfig_webhook**
> str create_namespaced_buildconfig_webhook(namespace, name, path=path)

connect POST requests to webhooks of Status

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Status
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect POST requests to webhooks of Status
    api_response = api_instance.create_namespaced_buildconfig_webhook(namespace, name, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_buildconfig_webhook: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_buildconfig_webhookspath**
> str create_namespaced_buildconfig_webhookspath(namespace, name, path2, path=path)

connect POST requests to webhooks of Status

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Status
path2 = 'path_example' # str | path to the resource
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    # connect POST requests to webhooks of Status
    api_response = api_instance.create_namespaced_buildconfig_webhookspath(namespace, name, path2, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_buildconfig_webhookspath: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deploymentconfig**
> V1DeploymentConfig create_namespaced_deploymentconfig(body, namespace, pretty=pretty)

create a DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeploymentConfig() # V1DeploymentConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfig
    api_response = api_instance.create_namespaced_deploymentconfig(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_deploymentconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deploymentconfigrollback**
> V1DeploymentConfigRollback create_namespaced_deploymentconfigrollback(body, namespace, pretty=pretty)

create a DeploymentConfigRollback

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeploymentConfigRollback() # V1DeploymentConfigRollback | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DeploymentConfigRollback
    api_response = api_instance.create_namespaced_deploymentconfigrollback(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_deploymentconfigrollback: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_imagestream**
> V1ImageStream create_namespaced_imagestream(body, namespace, pretty=pretty)

create a ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStream() # V1ImageStream | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStream
    api_response = api_instance.create_namespaced_imagestream(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_imagestream: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_imagestreamimport**
> V1ImageStreamImport create_namespaced_imagestreamimport(body, namespace, pretty=pretty)

create a ImageStreamImport

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStreamImport() # V1ImageStreamImport | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamImport
    api_response = api_instance.create_namespaced_imagestreamimport(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_imagestreamimport: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_imagestreammapping**
> V1ImageStreamMapping create_namespaced_imagestreammapping(body, namespace, pretty=pretty)

create a ImageStreamMapping

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStreamMapping() # V1ImageStreamMapping | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ImageStreamMapping
    api_response = api_instance.create_namespaced_imagestreammapping(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_imagestreammapping: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_localresourceaccessreview**
> V1LocalResourceAccessReview create_namespaced_localresourceaccessreview(body, namespace, pretty=pretty)

create a LocalResourceAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1LocalResourceAccessReview() # V1LocalResourceAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalResourceAccessReview
    api_response = api_instance.create_namespaced_localresourceaccessreview(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_localresourceaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_localsubjectaccessreview**
> V1LocalSubjectAccessReview create_namespaced_localsubjectaccessreview(body, namespace, pretty=pretty)

create a LocalSubjectAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1LocalSubjectAccessReview() # V1LocalSubjectAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a LocalSubjectAccessReview
    api_response = api_instance.create_namespaced_localsubjectaccessreview(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_localsubjectaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_policie**
> V1Policy create_namespaced_policie(body, namespace, pretty=pretty)

create a Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Policy() # V1Policy | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Policy
    api_response = api_instance.create_namespaced_policie(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_policie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_policybinding**
> V1PolicyBinding create_namespaced_policybinding(body, namespace, pretty=pretty)

create a PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1PolicyBinding() # V1PolicyBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PolicyBinding
    api_response = api_instance.create_namespaced_policybinding(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_policybinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_processedtemplate**
> V1Template create_namespaced_processedtemplate(body, namespace, pretty=pretty)

create a Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Template() # V1Template | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_namespaced_processedtemplate(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_processedtemplate: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_resourceaccessreview**
> V1ResourceAccessReview create_namespaced_resourceaccessreview(body, namespace, pretty=pretty)

create a ResourceAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ResourceAccessReview() # V1ResourceAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ResourceAccessReview
    api_response = api_instance.create_namespaced_resourceaccessreview(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_resourceaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_role**
> V1Role create_namespaced_role(body, namespace, pretty=pretty)

create a Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Role() # V1Role | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Role
    api_response = api_instance.create_namespaced_role(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_role: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_rolebinding**
> V1RoleBinding create_namespaced_rolebinding(body, namespace, pretty=pretty)

create a RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1RoleBinding() # V1RoleBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a RoleBinding
    api_response = api_instance.create_namespaced_rolebinding(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_rolebinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_route**
> V1Route create_namespaced_route(body, namespace, pretty=pretty)

create a Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Route() # V1Route | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Route
    api_response = api_instance.create_namespaced_route(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_route: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_subjectaccessreview**
> V1SubjectAccessReview create_namespaced_subjectaccessreview(body, namespace, pretty=pretty)

create a SubjectAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1SubjectAccessReview() # V1SubjectAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a SubjectAccessReview
    api_response = api_instance.create_namespaced_subjectaccessreview(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_subjectaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_template**
> V1Template create_namespaced_template(body, namespace, pretty=pretty)

create a Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Template() # V1Template | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_namespaced_template(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_namespaced_template: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_netnamespace**
> V1NetNamespace create_netnamespace(body, pretty=pretty)

create a NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1NetNamespace() # V1NetNamespace | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a NetNamespace
    api_response = api_instance.create_netnamespace(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_netnamespace: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_oauthaccesstoken**
> V1OAuthAccessToken create_oauthaccesstoken(body, pretty=pretty)

create a OAuthAccessToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1OAuthAccessToken() # V1OAuthAccessToken | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthAccessToken
    api_response = api_instance.create_oauthaccesstoken(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_oauthaccesstoken: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_oauthauthorizetoken**
> V1OAuthAuthorizeToken create_oauthauthorizetoken(body, pretty=pretty)

create a OAuthAuthorizeToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1OAuthAuthorizeToken() # V1OAuthAuthorizeToken | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthAuthorizeToken
    api_response = api_instance.create_oauthauthorizetoken(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_oauthauthorizetoken: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_oauthclient**
> V1OAuthClient create_oauthclient(body, pretty=pretty)

create a OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1OAuthClient() # V1OAuthClient | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthClient
    api_response = api_instance.create_oauthclient(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_oauthclient: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_oauthclientauthorization**
> V1OAuthClientAuthorization create_oauthclientauthorization(body, pretty=pretty)

create a OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1OAuthClientAuthorization() # V1OAuthClientAuthorization | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a OAuthClientAuthorization
    api_response = api_instance.create_oauthclientauthorization(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_oauthclientauthorization: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policie**
> V1Policy create_policie(body, pretty=pretty)

create a Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Policy() # V1Policy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Policy
    api_response = api_instance.create_policie(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_policie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policybinding**
> V1PolicyBinding create_policybinding(body, pretty=pretty)

create a PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1PolicyBinding() # V1PolicyBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a PolicyBinding
    api_response = api_instance.create_policybinding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_policybinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_processedtemplate**
> V1Template create_processedtemplate(body, pretty=pretty)

create a Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Template() # V1Template | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_processedtemplate(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_processedtemplate: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> V1Project create_project(body, pretty=pretty)

create a Project

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Project() # V1Project | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Project
    api_response = api_instance.create_project(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_project: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_projectrequest**
> V1ProjectRequest create_projectrequest(body, pretty=pretty)

create a ProjectRequest

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ProjectRequest() # V1ProjectRequest | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ProjectRequest
    api_response = api_instance.create_projectrequest(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_projectrequest: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resourceaccessreview**
> V1ResourceAccessReview create_resourceaccessreview(body, pretty=pretty)

create a ResourceAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ResourceAccessReview() # V1ResourceAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ResourceAccessReview
    api_response = api_instance.create_resourceaccessreview(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_resourceaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> V1Role create_role(body, pretty=pretty)

create a Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Role() # V1Role | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Role
    api_response = api_instance.create_role(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_role: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rolebinding**
> V1RoleBinding create_rolebinding(body, pretty=pretty)

create a RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1RoleBinding() # V1RoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a RoleBinding
    api_response = api_instance.create_rolebinding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_rolebinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route**
> V1Route create_route(body, pretty=pretty)

create a Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Route() # V1Route | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Route
    api_response = api_instance.create_route(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_route: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subjectaccessreview**
> V1SubjectAccessReview create_subjectaccessreview(body, pretty=pretty)

create a SubjectAccessReview

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1SubjectAccessReview() # V1SubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a SubjectAccessReview
    api_response = api_instance.create_subjectaccessreview(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_subjectaccessreview: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> V1Template create_template(body, pretty=pretty)

create a Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Template() # V1Template | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Template
    api_response = api_instance.create_template(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_template: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> V1User create_user(body, pretty=pretty)

create a User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1User() # V1User | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a User
    api_response = api_instance.create_user(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_user: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_useridentitymapping**
> V1UserIdentityMapping create_useridentitymapping(body, pretty=pretty)

create a UserIdentityMapping

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1UserIdentityMapping() # V1UserIdentityMapping | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a UserIdentityMapping
    api_response = api_instance.create_useridentitymapping(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->create_useridentitymapping: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusternetwork**
> UnversionedStatus delete_clusternetwork(body, name, pretty=pretty)

delete a ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterNetwork
    api_response = api_instance.delete_clusternetwork(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusternetwork: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusternetworks**
> UnversionedStatus delete_clusternetworks(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ClusterNetwork
    api_response = api_instance.delete_clusternetworks(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusternetworks: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusterpolicie**
> UnversionedStatus delete_clusterpolicie(body, name, pretty=pretty)

delete a ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterPolicy
    api_response = api_instance.delete_clusterpolicie(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusterpolicie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusterpolicies**
> UnversionedStatus delete_clusterpolicies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ClusterPolicy
    api_response = api_instance.delete_clusterpolicies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusterpolicies: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusterpolicybinding**
> UnversionedStatus delete_clusterpolicybinding(body, name, pretty=pretty)

delete a ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterPolicyBinding
    api_response = api_instance.delete_clusterpolicybinding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusterpolicybinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusterpolicybindings**
> UnversionedStatus delete_clusterpolicybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ClusterPolicyBinding
    api_response = api_instance.delete_clusterpolicybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusterpolicybindings: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusterrole**
> UnversionedStatus delete_clusterrole(body, name, pretty=pretty)

delete a ClusterRole

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterRole
    api_response = api_instance.delete_clusterrole(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusterrole: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clusterrolebinding**
> UnversionedStatus delete_clusterrolebinding(body, name, pretty=pretty)

delete a ClusterRoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ClusterRoleBinding
    api_response = api_instance.delete_clusterrolebinding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_clusterrolebinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> UnversionedStatus delete_group(body, name, pretty=pretty)

delete a Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Group
    api_response = api_instance.delete_group(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_group: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groups**
> UnversionedStatus delete_groups(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Group
    api_response = api_instance.delete_groups(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_groups: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hostsubnet**
> UnversionedStatus delete_hostsubnet(body, name, pretty=pretty)

delete a HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a HostSubnet
    api_response = api_instance.delete_hostsubnet(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_hostsubnet: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hostsubnets**
> UnversionedStatus delete_hostsubnets(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of HostSubnet
    api_response = api_instance.delete_hostsubnets(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_hostsubnets: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identitie**
> UnversionedStatus delete_identitie(body, name, pretty=pretty)

delete a Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Identity
    api_response = api_instance.delete_identitie(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_identitie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identities**
> UnversionedStatus delete_identities(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Identity
    api_response = api_instance.delete_identities(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_identities: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> UnversionedStatus delete_image(body, name, pretty=pretty)

delete a Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Image
    api_response = api_instance.delete_image(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_image: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_images**
> UnversionedStatus delete_images(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Image
    api_response = api_instance.delete_images(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_images: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_build**
> UnversionedStatus delete_namespaced_build(body, namespace, name, pretty=pretty)

delete a Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Build
    api_response = api_instance.delete_namespaced_build(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_build: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_buildconfig**
> UnversionedStatus delete_namespaced_buildconfig(body, namespace, name, pretty=pretty)

delete a BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a BuildConfig
    api_response = api_instance.delete_namespaced_buildconfig(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_buildconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_buildconfigs**
> UnversionedStatus delete_namespaced_buildconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of BuildConfig
    api_response = api_instance.delete_namespaced_buildconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_buildconfigs: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_builds**
> UnversionedStatus delete_namespaced_builds(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Build
    api_response = api_instance.delete_namespaced_builds(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_builds: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_deploymentconfig**
> UnversionedStatus delete_namespaced_deploymentconfig(body, namespace, name, pretty=pretty)

delete a DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a DeploymentConfig
    api_response = api_instance.delete_namespaced_deploymentconfig(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_deploymentconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_deploymentconfigs**
> UnversionedStatus delete_namespaced_deploymentconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of DeploymentConfig
    api_response = api_instance.delete_namespaced_deploymentconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_deploymentconfigs: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_imagestream**
> UnversionedStatus delete_namespaced_imagestream(body, namespace, name, pretty=pretty)

delete a ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ImageStream
    api_response = api_instance.delete_namespaced_imagestream(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_imagestream: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_imagestreams**
> UnversionedStatus delete_namespaced_imagestreams(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ImageStream
    api_response = api_instance.delete_namespaced_imagestreams(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_imagestreams: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_imagestreamtag**
> UnversionedStatus delete_namespaced_imagestreamtag(namespace, name, pretty=pretty)

delete a ImageStreamTag

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ImageStreamTag
    api_response = api_instance.delete_namespaced_imagestreamtag(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_imagestreamtag: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_policie**
> UnversionedStatus delete_namespaced_policie(body, namespace, name, pretty=pretty)

delete a Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Policy
    api_response = api_instance.delete_namespaced_policie(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_policie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_policies**
> UnversionedStatus delete_namespaced_policies(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Policy
    api_response = api_instance.delete_namespaced_policies(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_policies: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_policybinding**
> UnversionedStatus delete_namespaced_policybinding(body, namespace, name, pretty=pretty)

delete a PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a PolicyBinding
    api_response = api_instance.delete_namespaced_policybinding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_policybinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_policybindings**
> UnversionedStatus delete_namespaced_policybindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of PolicyBinding
    api_response = api_instance.delete_namespaced_policybindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_policybindings: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_role**
> UnversionedStatus delete_namespaced_role(body, namespace, name, pretty=pretty)

delete a Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Role
    api_response = api_instance.delete_namespaced_role(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_role: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_rolebinding**
> UnversionedStatus delete_namespaced_rolebinding(body, namespace, name, pretty=pretty)

delete a RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a RoleBinding
    api_response = api_instance.delete_namespaced_rolebinding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_rolebinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_route**
> UnversionedStatus delete_namespaced_route(body, namespace, name, pretty=pretty)

delete a Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Route
    api_response = api_instance.delete_namespaced_route(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_route: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_routes**
> UnversionedStatus delete_namespaced_routes(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Route
    api_response = api_instance.delete_namespaced_routes(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_routes: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_template**
> UnversionedStatus delete_namespaced_template(body, namespace, name, pretty=pretty)

delete a Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Template
    api_response = api_instance.delete_namespaced_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_template: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_templates**
> UnversionedStatus delete_namespaced_templates(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Template
    api_response = api_instance.delete_namespaced_templates(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_namespaced_templates: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_netnamespace**
> UnversionedStatus delete_netnamespace(body, name, pretty=pretty)

delete a NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a NetNamespace
    api_response = api_instance.delete_netnamespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_netnamespace: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_netnamespaces**
> UnversionedStatus delete_netnamespaces(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of NetNamespace
    api_response = api_instance.delete_netnamespaces(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_netnamespaces: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oauthaccesstoken**
> UnversionedStatus delete_oauthaccesstoken(body, name, pretty=pretty)

delete a OAuthAccessToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthAccessToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthAccessToken
    api_response = api_instance.delete_oauthaccesstoken(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_oauthaccesstoken: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oauthauthorizetoken**
> UnversionedStatus delete_oauthauthorizetoken(body, name, pretty=pretty)

delete a OAuthAuthorizeToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthAuthorizeToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthAuthorizeToken
    api_response = api_instance.delete_oauthauthorizetoken(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_oauthauthorizetoken: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oauthclient**
> UnversionedStatus delete_oauthclient(body, name, pretty=pretty)

delete a OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthClient
    api_response = api_instance.delete_oauthclient(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_oauthclient: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oauthclientauthorization**
> UnversionedStatus delete_oauthclientauthorization(body, name, pretty=pretty)

delete a OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a OAuthClientAuthorization
    api_response = api_instance.delete_oauthclientauthorization(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_oauthclientauthorization: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oauthclientauthorizations**
> UnversionedStatus delete_oauthclientauthorizations(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of OAuthClientAuthorization
    api_response = api_instance.delete_oauthclientauthorizations(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_oauthclientauthorizations: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oauthclients**
> UnversionedStatus delete_oauthclients(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of OAuthClient
    api_response = api_instance.delete_oauthclients(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_oauthclients: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> UnversionedStatus delete_project(name, pretty=pretty)

delete a Project

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Project
    api_response = api_instance.delete_project(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_project: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> UnversionedStatus delete_user(body, name, pretty=pretty)

delete a User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a User
    api_response = api_instance.delete_user(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_user: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_useridentitymapping**
> UnversionedStatus delete_useridentitymapping(name, pretty=pretty)

delete a UserIdentityMapping

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a UserIdentityMapping
    api_response = api_instance.delete_useridentitymapping(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_useridentitymapping: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users**
> UnversionedStatus delete_users(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of User
    api_response = api_instance.delete_users(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->delete_users: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusternetwork**
> V1ClusterNetwork get_clusternetwork(name, pretty=pretty, export=export, exact=exact)

read the specified ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ClusterNetwork
    api_response = api_instance.get_clusternetwork(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_clusternetwork: %s\n" % e
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

# **get_clusterpolicie**
> V1ClusterPolicy get_clusterpolicie(name, pretty=pretty, export=export, exact=exact)

read the specified ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ClusterPolicy
    api_response = api_instance.get_clusterpolicie(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_clusterpolicie: %s\n" % e
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

# **get_clusterpolicybinding**
> V1ClusterPolicyBinding get_clusterpolicybinding(name, pretty=pretty, export=export, exact=exact)

read the specified ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ClusterPolicyBinding
    api_response = api_instance.get_clusterpolicybinding(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_clusterpolicybinding: %s\n" % e
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

# **get_clusterrole**
> V1ClusterRole get_clusterrole(name, pretty=pretty)

read the specified ClusterRole

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ClusterRole
    api_response = api_instance.get_clusterrole(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_clusterrole: %s\n" % e
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

# **get_clusterrolebinding**
> V1ClusterRoleBinding get_clusterrolebinding(name, pretty=pretty)

read the specified ClusterRoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ClusterRoleBinding
    api_response = api_instance.get_clusterrolebinding(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_clusterrolebinding: %s\n" % e
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

# **get_group**
> V1Group get_group(name, pretty=pretty, export=export, exact=exact)

read the specified Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Group
    api_response = api_instance.get_group(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_group: %s\n" % e
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

# **get_hostsubnet**
> V1HostSubnet get_hostsubnet(name, pretty=pretty, export=export, exact=exact)

read the specified HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified HostSubnet
    api_response = api_instance.get_hostsubnet(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_hostsubnet: %s\n" % e
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

# **get_identitie**
> V1Identity get_identitie(name, pretty=pretty, export=export, exact=exact)

read the specified Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Identity
    api_response = api_instance.get_identitie(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_identitie: %s\n" % e
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

# **get_image**
> V1Image get_image(name, pretty=pretty, export=export, exact=exact)

read the specified Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Image
    api_response = api_instance.get_image(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_image: %s\n" % e
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

# **get_namespaced_build**
> V1Build get_namespaced_build(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Build
    api_response = api_instance.get_namespaced_build(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_build: %s\n" % e
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

# **get_namespaced_build_log**
> V1BuildLog get_namespaced_build_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)

read log of the specified BuildLog

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.get_namespaced_build_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_build_log: %s\n" % e
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

# **get_namespaced_buildconfig**
> V1BuildConfig get_namespaced_buildconfig(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified BuildConfig
    api_response = api_instance.get_namespaced_buildconfig(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_buildconfig: %s\n" % e
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

# **get_namespaced_deploymentconfig**
> V1DeploymentConfig get_namespaced_deploymentconfig(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified DeploymentConfig
    api_response = api_instance.get_namespaced_deploymentconfig(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_deploymentconfig: %s\n" % e
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

# **get_namespaced_deploymentconfig_log**
> V1DeploymentLog get_namespaced_deploymentconfig_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)

read log of the specified DeploymentLog

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.get_namespaced_deploymentconfig_log(namespace, name, pretty=pretty, container=container, follow=follow, previous=previous, since_seconds=since_seconds, since_time=since_time, timestamps=timestamps, tail_lines=tail_lines, limit_bytes=limit_bytes, nowait=nowait, version=version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_deploymentconfig_log: %s\n" % e
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

# **get_namespaced_deploymentconfig_scale**
> V1beta1Scale get_namespaced_deploymentconfig_scale(namespace, name, pretty=pretty)

read scale of the specified Scale

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read scale of the specified Scale
    api_response = api_instance.get_namespaced_deploymentconfig_scale(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_deploymentconfig_scale: %s\n" % e
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

# **get_namespaced_generatedeploymentconfig**
> V1DeploymentConfig get_namespaced_generatedeploymentconfig(namespace, name, pretty=pretty)

read the specified DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified DeploymentConfig
    api_response = api_instance.get_namespaced_generatedeploymentconfig(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_generatedeploymentconfig: %s\n" % e
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

# **get_namespaced_imagestream**
> V1ImageStream get_namespaced_imagestream(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ImageStream
    api_response = api_instance.get_namespaced_imagestream(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_imagestream: %s\n" % e
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

# **get_namespaced_imagestream_secrets**
> V1SecretList get_namespaced_imagestream_secrets(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

read secrets of the specified SecretList

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.get_namespaced_imagestream_secrets(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_imagestream_secrets: %s\n" % e
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

# **get_namespaced_imagestreamimage**
> V1ImageStreamImage get_namespaced_imagestreamimage(namespace, name, pretty=pretty)

read the specified ImageStreamImage

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamImage
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ImageStreamImage
    api_response = api_instance.get_namespaced_imagestreamimage(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_imagestreamimage: %s\n" % e
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

# **get_namespaced_imagestreamtag**
> V1ImageStreamTag get_namespaced_imagestreamtag(namespace, name, pretty=pretty)

read the specified ImageStreamTag

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified ImageStreamTag
    api_response = api_instance.get_namespaced_imagestreamtag(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_imagestreamtag: %s\n" % e
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

# **get_namespaced_policie**
> V1Policy get_namespaced_policie(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Policy
    api_response = api_instance.get_namespaced_policie(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_policie: %s\n" % e
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

# **get_namespaced_policybinding**
> V1PolicyBinding get_namespaced_policybinding(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified PolicyBinding
    api_response = api_instance.get_namespaced_policybinding(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_policybinding: %s\n" % e
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

# **get_namespaced_role**
> V1Role get_namespaced_role(namespace, name, pretty=pretty)

read the specified Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified Role
    api_response = api_instance.get_namespaced_role(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_role: %s\n" % e
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

# **get_namespaced_rolebinding**
> V1RoleBinding get_namespaced_rolebinding(namespace, name, pretty=pretty)

read the specified RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified RoleBinding
    api_response = api_instance.get_namespaced_rolebinding(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_rolebinding: %s\n" % e
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

# **get_namespaced_route**
> V1Route get_namespaced_route(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Route
    api_response = api_instance.get_namespaced_route(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_route: %s\n" % e
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

# **get_namespaced_template**
> V1Template get_namespaced_template(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Template
    api_response = api_instance.get_namespaced_template(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_namespaced_template: %s\n" % e
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

# **get_netnamespace**
> V1NetNamespace get_netnamespace(name, pretty=pretty, export=export, exact=exact)

read the specified NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified NetNamespace
    api_response = api_instance.get_netnamespace(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_netnamespace: %s\n" % e
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

# **get_oauthaccesstoken**
> V1OAuthAccessToken get_oauthaccesstoken(name, pretty=pretty)

read the specified OAuthAccessToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the OAuthAccessToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified OAuthAccessToken
    api_response = api_instance.get_oauthaccesstoken(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_oauthaccesstoken: %s\n" % e
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

# **get_oauthauthorizetoken**
> V1OAuthAuthorizeToken get_oauthauthorizetoken(name, pretty=pretty)

read the specified OAuthAuthorizeToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the OAuthAuthorizeToken
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified OAuthAuthorizeToken
    api_response = api_instance.get_oauthauthorizetoken(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_oauthauthorizetoken: %s\n" % e
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

# **get_oauthclient**
> V1OAuthClient get_oauthclient(name, pretty=pretty, export=export, exact=exact)

read the specified OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified OAuthClient
    api_response = api_instance.get_oauthclient(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_oauthclient: %s\n" % e
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

# **get_oauthclientauthorization**
> V1OAuthClientAuthorization get_oauthclientauthorization(name, pretty=pretty, export=export, exact=exact)

read the specified OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified OAuthClientAuthorization
    api_response = api_instance.get_oauthclientauthorization(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_oauthclientauthorization: %s\n" % e
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

# **get_project**
> V1Project get_project(name, pretty=pretty)

read the specified Project

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified Project
    api_response = api_instance.get_project(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_project: %s\n" % e
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

# **get_user**
> V1User get_user(name, pretty=pretty, export=export, exact=exact)

read the specified User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified User
    api_response = api_instance.get_user(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_user: %s\n" % e
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

# **get_useridentitymapping**
> V1UserIdentityMapping get_useridentitymapping(name, pretty=pretty)

read the specified UserIdentityMapping

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read the specified UserIdentityMapping
    api_response = api_instance.get_useridentitymapping(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->get_useridentitymapping: %s\n" % e
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

# **list**
> list()

get available resources

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()

try: 
    # get available resources
    api_instance.list()
except ApiException as e:
    print "Exception when calling OapiV1->list: %s\n" % e
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

# **list_buildconfigs**
> V1BuildConfigList list_buildconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind BuildConfig
    api_response = api_instance.list_buildconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_buildconfigs: %s\n" % e
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

# **list_builds**
> V1BuildList list_builds(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Build
    api_response = api_instance.list_builds(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_builds: %s\n" % e
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

# **list_clusternetworks**
> V1ClusterNetworkList list_clusternetworks(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ClusterNetwork
    api_response = api_instance.list_clusternetworks(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_clusternetworks: %s\n" % e
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

# **list_clusterpolicies**
> V1ClusterPolicyList list_clusterpolicies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ClusterPolicy
    api_response = api_instance.list_clusterpolicies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_clusterpolicies: %s\n" % e
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

# **list_clusterpolicybindings**
> V1ClusterPolicyBindingList list_clusterpolicybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ClusterPolicyBinding
    api_response = api_instance.list_clusterpolicybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_clusterpolicybindings: %s\n" % e
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

# **list_clusterrolebindings**
> V1ClusterRoleBindingList list_clusterrolebindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ClusterRoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ClusterRoleBinding
    api_response = api_instance.list_clusterrolebindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_clusterrolebindings: %s\n" % e
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

# **list_clusterroles**
> V1ClusterRoleList list_clusterroles(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ClusterRole

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ClusterRole
    api_response = api_instance.list_clusterroles(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_clusterroles: %s\n" % e
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

# **list_deploymentconfigs**
> V1DeploymentConfigList list_deploymentconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind DeploymentConfig
    api_response = api_instance.list_deploymentconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_deploymentconfigs: %s\n" % e
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

# **list_groups**
> V1GroupList list_groups(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Group
    api_response = api_instance.list_groups(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_groups: %s\n" % e
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

# **list_hostsubnets**
> V1HostSubnetList list_hostsubnets(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind HostSubnet
    api_response = api_instance.list_hostsubnets(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_hostsubnets: %s\n" % e
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

# **list_identities**
> V1IdentityList list_identities(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Identity
    api_response = api_instance.list_identities(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_identities: %s\n" % e
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

# **list_images**
> V1ImageList list_images(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Image
    api_response = api_instance.list_images(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_images: %s\n" % e
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

# **list_imagestreams**
> V1ImageStreamList list_imagestreams(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ImageStream
    api_response = api_instance.list_imagestreams(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_imagestreams: %s\n" % e
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

# **list_imagestreamtags**
> V1ImageStreamTagList list_imagestreamtags(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ImageStreamTag

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ImageStreamTag
    api_response = api_instance.list_imagestreamtags(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_imagestreamtags: %s\n" % e
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

# **list_namespaced_buildconfigs**
> V1BuildConfigList list_namespaced_buildconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind BuildConfig
    api_response = api_instance.list_namespaced_buildconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_buildconfigs: %s\n" % e
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

# **list_namespaced_builds**
> V1BuildList list_namespaced_builds(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Build
    api_response = api_instance.list_namespaced_builds(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_builds: %s\n" % e
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

# **list_namespaced_deploymentconfigs**
> V1DeploymentConfigList list_namespaced_deploymentconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind DeploymentConfig
    api_response = api_instance.list_namespaced_deploymentconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_deploymentconfigs: %s\n" % e
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

# **list_namespaced_imagestreams**
> V1ImageStreamList list_namespaced_imagestreams(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ImageStream
    api_response = api_instance.list_namespaced_imagestreams(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_imagestreams: %s\n" % e
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

# **list_namespaced_imagestreamtags**
> V1ImageStreamTagList list_namespaced_imagestreamtags(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ImageStreamTag

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ImageStreamTag
    api_response = api_instance.list_namespaced_imagestreamtags(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_imagestreamtags: %s\n" % e
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

# **list_namespaced_policies**
> V1PolicyList list_namespaced_policies(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Policy
    api_response = api_instance.list_namespaced_policies(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_policies: %s\n" % e
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

# **list_namespaced_policybindings**
> V1PolicyBindingList list_namespaced_policybindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PolicyBinding
    api_response = api_instance.list_namespaced_policybindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_policybindings: %s\n" % e
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

# **list_namespaced_rolebindings**
> V1RoleBindingList list_namespaced_rolebindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind RoleBinding
    api_response = api_instance.list_namespaced_rolebindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_rolebindings: %s\n" % e
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

# **list_namespaced_roles**
> V1RoleList list_namespaced_roles(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind Role
    api_response = api_instance.list_namespaced_roles(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_roles: %s\n" % e
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

# **list_namespaced_routes**
> V1RouteList list_namespaced_routes(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Route
    api_response = api_instance.list_namespaced_routes(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_routes: %s\n" % e
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

# **list_namespaced_templates**
> V1TemplateList list_namespaced_templates(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Template
    api_response = api_instance.list_namespaced_templates(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_namespaced_templates: %s\n" % e
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

# **list_netnamespaces**
> V1NetNamespaceList list_netnamespaces(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind NetNamespace
    api_response = api_instance.list_netnamespaces(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_netnamespaces: %s\n" % e
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

# **list_oauthaccesstokens**
> V1OAuthAccessTokenList list_oauthaccesstokens(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind OAuthAccessToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind OAuthAccessToken
    api_response = api_instance.list_oauthaccesstokens(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_oauthaccesstokens: %s\n" % e
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

# **list_oauthauthorizetokens**
> V1OAuthAuthorizeTokenList list_oauthauthorizetokens(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind OAuthAuthorizeToken

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind OAuthAuthorizeToken
    api_response = api_instance.list_oauthauthorizetokens(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_oauthauthorizetokens: %s\n" % e
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

# **list_oauthclientauthorizations**
> V1OAuthClientAuthorizationList list_oauthclientauthorizations(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind OAuthClientAuthorization
    api_response = api_instance.list_oauthclientauthorizations(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_oauthclientauthorizations: %s\n" % e
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

# **list_oauthclients**
> V1OAuthClientList list_oauthclients(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind OAuthClient
    api_response = api_instance.list_oauthclients(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_oauthclients: %s\n" % e
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

# **list_policies**
> V1PolicyList list_policies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Policy
    api_response = api_instance.list_policies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_policies: %s\n" % e
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

# **list_policybindings**
> V1PolicyBindingList list_policybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind PolicyBinding
    api_response = api_instance.list_policybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_policybindings: %s\n" % e
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

# **list_projectrequests**
> UnversionedStatus list_projectrequests(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind ProjectRequest

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind ProjectRequest
    api_response = api_instance.list_projectrequests(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_projectrequests: %s\n" % e
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

# **list_projects**
> V1ProjectList list_projects(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind Project

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind Project
    api_response = api_instance.list_projects(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_projects: %s\n" % e
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

# **list_rolebindings**
> V1RoleBindingList list_rolebindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind RoleBinding
    api_response = api_instance.list_rolebindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_rolebindings: %s\n" % e
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

# **list_roles**
> V1RoleList list_roles(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list objects of kind Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list objects of kind Role
    api_response = api_instance.list_roles(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_roles: %s\n" % e
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

# **list_routes**
> V1RouteList list_routes(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Route
    api_response = api_instance.list_routes(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_routes: %s\n" % e
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

# **list_templates**
> V1TemplateList list_templates(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Template
    api_response = api_instance.list_templates(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_templates: %s\n" % e
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

# **list_users**
> V1UserList list_users(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind User
    api_response = api_instance.list_users(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->list_users: %s\n" % e
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

# **patch_clusternetwork**
> V1ClusterNetwork patch_clusternetwork(body, name, pretty=pretty)

partially update the specified ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterNetwork
    api_response = api_instance.patch_clusternetwork(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_clusternetwork: %s\n" % e
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

# **patch_clusterpolicie**
> V1ClusterPolicy patch_clusterpolicie(body, name, pretty=pretty)

partially update the specified ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterPolicy
    api_response = api_instance.patch_clusterpolicie(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_clusterpolicie: %s\n" % e
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

# **patch_clusterpolicybinding**
> V1ClusterPolicyBinding patch_clusterpolicybinding(body, name, pretty=pretty)

partially update the specified ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterPolicyBinding
    api_response = api_instance.patch_clusterpolicybinding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_clusterpolicybinding: %s\n" % e
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

# **patch_clusterrole**
> V1ClusterRole patch_clusterrole(body, name, pretty=pretty)

partially update the specified ClusterRole

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterRole
    api_response = api_instance.patch_clusterrole(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_clusterrole: %s\n" % e
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

# **patch_clusterrolebinding**
> V1ClusterRoleBinding patch_clusterrolebinding(body, name, pretty=pretty)

partially update the specified ClusterRoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ClusterRoleBinding
    api_response = api_instance.patch_clusterrolebinding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_clusterrolebinding: %s\n" % e
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

# **patch_group**
> V1Group patch_group(body, name, pretty=pretty)

partially update the specified Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Group
    api_response = api_instance.patch_group(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_group: %s\n" % e
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

# **patch_hostsubnet**
> V1HostSubnet patch_hostsubnet(body, name, pretty=pretty)

partially update the specified HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified HostSubnet
    api_response = api_instance.patch_hostsubnet(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_hostsubnet: %s\n" % e
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

# **patch_identitie**
> V1Identity patch_identitie(body, name, pretty=pretty)

partially update the specified Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Identity
    api_response = api_instance.patch_identitie(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_identitie: %s\n" % e
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

# **patch_image**
> V1Image patch_image(body, name, pretty=pretty)

partially update the specified Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Image
    api_response = api_instance.patch_image(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_image: %s\n" % e
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

# **patch_namespaced_build**
> V1Build patch_namespaced_build(body, namespace, name, pretty=pretty)

partially update the specified Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Build
    api_response = api_instance.patch_namespaced_build(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_build: %s\n" % e
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

# **patch_namespaced_buildconfig**
> V1BuildConfig patch_namespaced_buildconfig(body, namespace, name, pretty=pretty)

partially update the specified BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified BuildConfig
    api_response = api_instance.patch_namespaced_buildconfig(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_buildconfig: %s\n" % e
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

# **patch_namespaced_deploymentconfig**
> V1DeploymentConfig patch_namespaced_deploymentconfig(body, namespace, name, pretty=pretty)

partially update the specified DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified DeploymentConfig
    api_response = api_instance.patch_namespaced_deploymentconfig(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_deploymentconfig: %s\n" % e
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

# **patch_namespaced_deploymentconfig_scale**
> V1beta1Scale patch_namespaced_deploymentconfig_scale(body, namespace, name, pretty=pretty)

partially update scale of the specified Scale

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update scale of the specified Scale
    api_response = api_instance.patch_namespaced_deploymentconfig_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_deploymentconfig_scale: %s\n" % e
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

# **patch_namespaced_imagestream**
> V1ImageStream patch_namespaced_imagestream(body, namespace, name, pretty=pretty)

partially update the specified ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ImageStream
    api_response = api_instance.patch_namespaced_imagestream(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_imagestream: %s\n" % e
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

# **patch_namespaced_imagestreamtag**
> V1ImageStreamTag patch_namespaced_imagestreamtag(body, namespace, name, pretty=pretty)

partially update the specified ImageStreamTag

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ImageStreamTag
    api_response = api_instance.patch_namespaced_imagestreamtag(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_imagestreamtag: %s\n" % e
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

# **patch_namespaced_policie**
> V1Policy patch_namespaced_policie(body, namespace, name, pretty=pretty)

partially update the specified Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Policy
    api_response = api_instance.patch_namespaced_policie(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_policie: %s\n" % e
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

# **patch_namespaced_policybinding**
> V1PolicyBinding patch_namespaced_policybinding(body, namespace, name, pretty=pretty)

partially update the specified PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified PolicyBinding
    api_response = api_instance.patch_namespaced_policybinding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_policybinding: %s\n" % e
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

# **patch_namespaced_role**
> V1Role patch_namespaced_role(body, namespace, name, pretty=pretty)

partially update the specified Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Role
    api_response = api_instance.patch_namespaced_role(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_role: %s\n" % e
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

# **patch_namespaced_rolebinding**
> V1RoleBinding patch_namespaced_rolebinding(body, namespace, name, pretty=pretty)

partially update the specified RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified RoleBinding
    api_response = api_instance.patch_namespaced_rolebinding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_rolebinding: %s\n" % e
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
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Route
    api_response = api_instance.patch_namespaced_route(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_route: %s\n" % e
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

# **patch_namespaced_template**
> V1Template patch_namespaced_template(body, namespace, name, pretty=pretty)

partially update the specified Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Template
    api_response = api_instance.patch_namespaced_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_namespaced_template: %s\n" % e
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

# **patch_netnamespace**
> V1NetNamespace patch_netnamespace(body, name, pretty=pretty)

partially update the specified NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified NetNamespace
    api_response = api_instance.patch_netnamespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_netnamespace: %s\n" % e
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

# **patch_oauthclient**
> V1OAuthClient patch_oauthclient(body, name, pretty=pretty)

partially update the specified OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified OAuthClient
    api_response = api_instance.patch_oauthclient(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_oauthclient: %s\n" % e
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

# **patch_oauthclientauthorization**
> V1OAuthClientAuthorization patch_oauthclientauthorization(body, name, pretty=pretty)

partially update the specified OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified OAuthClientAuthorization
    api_response = api_instance.patch_oauthclientauthorization(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_oauthclientauthorization: %s\n" % e
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

# **patch_project**
> V1Project patch_project(body, name, pretty=pretty)

partially update the specified Project

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Project
    api_response = api_instance.patch_project(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_project: %s\n" % e
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

# **patch_user**
> V1User patch_user(body, name, pretty=pretty)

partially update the specified User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified User
    api_response = api_instance.patch_user(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_user: %s\n" % e
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

# **patch_useridentitymapping**
> V1UserIdentityMapping patch_useridentitymapping(body, name, pretty=pretty)

partially update the specified UserIdentityMapping

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified UserIdentityMapping
    api_response = api_instance.patch_useridentitymapping(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->patch_useridentitymapping: %s\n" % e
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

# **replace_clusternetwork**
> V1ClusterNetwork replace_clusternetwork(body, name, pretty=pretty)

replace the specified ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterNetwork() # V1ClusterNetwork | 
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterNetwork
    api_response = api_instance.replace_clusternetwork(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_clusternetwork: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_clusterpolicie**
> V1ClusterPolicy replace_clusterpolicie(body, name, pretty=pretty)

replace the specified ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterPolicy() # V1ClusterPolicy | 
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterPolicy
    api_response = api_instance.replace_clusterpolicie(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_clusterpolicie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_clusterpolicybinding**
> V1ClusterPolicyBinding replace_clusterpolicybinding(body, name, pretty=pretty)

replace the specified ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterPolicyBinding() # V1ClusterPolicyBinding | 
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterPolicyBinding
    api_response = api_instance.replace_clusterpolicybinding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_clusterpolicybinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_clusterrole**
> V1ClusterRole replace_clusterrole(body, name, pretty=pretty)

replace the specified ClusterRole

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterRole() # V1ClusterRole | 
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterRole
    api_response = api_instance.replace_clusterrole(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_clusterrole: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_clusterrolebinding**
> V1ClusterRoleBinding replace_clusterrolebinding(body, name, pretty=pretty)

replace the specified ClusterRoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ClusterRoleBinding() # V1ClusterRoleBinding | 
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ClusterRoleBinding
    api_response = api_instance.replace_clusterrolebinding(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_clusterrolebinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_group**
> V1Group replace_group(body, name, pretty=pretty)

replace the specified Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Group() # V1Group | 
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Group
    api_response = api_instance.replace_group(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_group: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_hostsubnet**
> V1HostSubnet replace_hostsubnet(body, name, pretty=pretty)

replace the specified HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1HostSubnet() # V1HostSubnet | 
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified HostSubnet
    api_response = api_instance.replace_hostsubnet(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_hostsubnet: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_identitie**
> V1Identity replace_identitie(body, name, pretty=pretty)

replace the specified Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Identity() # V1Identity | 
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Identity
    api_response = api_instance.replace_identitie(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_identitie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_image**
> V1Image replace_image(body, name, pretty=pretty)

replace the specified Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Image() # V1Image | 
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Image
    api_response = api_instance.replace_image(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_image: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_build**
> V1Build replace_namespaced_build(body, namespace, name, pretty=pretty)

replace the specified Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Build() # V1Build | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Build
    api_response = api_instance.replace_namespaced_build(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_build: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_build_details**
> V1Build replace_namespaced_build_details(body, namespace, name, pretty=pretty)

replace details of the specified Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Build() # V1Build | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Build
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace details of the specified Build
    api_response = api_instance.replace_namespaced_build_details(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_build_details: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_buildconfig**
> V1BuildConfig replace_namespaced_buildconfig(body, namespace, name, pretty=pretty)

replace the specified BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1BuildConfig() # V1BuildConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the BuildConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified BuildConfig
    api_response = api_instance.replace_namespaced_buildconfig(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_buildconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deploymentconfig**
> V1DeploymentConfig replace_namespaced_deploymentconfig(body, namespace, name, pretty=pretty)

replace the specified DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1DeploymentConfig() # V1DeploymentConfig | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentConfig
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified DeploymentConfig
    api_response = api_instance.replace_namespaced_deploymentconfig(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_deploymentconfig: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deploymentconfig_scale**
> V1beta1Scale replace_namespaced_deploymentconfig_scale(body, namespace, name, pretty=pretty)

replace scale of the specified Scale

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1beta1Scale() # V1beta1Scale | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace scale of the specified Scale
    api_response = api_instance.replace_namespaced_deploymentconfig_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_deploymentconfig_scale: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_imagestream**
> V1ImageStream replace_namespaced_imagestream(body, namespace, name, pretty=pretty)

replace the specified ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStream() # V1ImageStream | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStream
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ImageStream
    api_response = api_instance.replace_namespaced_imagestream(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_imagestream: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_imagestreamtag**
> V1ImageStreamTag replace_namespaced_imagestreamtag(body, namespace, name, pretty=pretty)

replace the specified ImageStreamTag

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1ImageStreamTag() # V1ImageStreamTag | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ImageStreamTag
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ImageStreamTag
    api_response = api_instance.replace_namespaced_imagestreamtag(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_imagestreamtag: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_policie**
> V1Policy replace_namespaced_policie(body, namespace, name, pretty=pretty)

replace the specified Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Policy() # V1Policy | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Policy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Policy
    api_response = api_instance.replace_namespaced_policie(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_policie: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_policybinding**
> V1PolicyBinding replace_namespaced_policybinding(body, namespace, name, pretty=pretty)

replace the specified PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1PolicyBinding() # V1PolicyBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the PolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified PolicyBinding
    api_response = api_instance.replace_namespaced_policybinding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_policybinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_role**
> V1Role replace_namespaced_role(body, namespace, name, pretty=pretty)

replace the specified Role

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Role() # V1Role | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Role
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Role
    api_response = api_instance.replace_namespaced_role(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_role: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_rolebinding**
> V1RoleBinding replace_namespaced_rolebinding(body, namespace, name, pretty=pretty)

replace the specified RoleBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1RoleBinding() # V1RoleBinding | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the RoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified RoleBinding
    api_response = api_instance.replace_namespaced_rolebinding(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_rolebinding: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_route**
> V1Route replace_namespaced_route(body, namespace, name, pretty=pretty)

replace the specified Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Route() # V1Route | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Route
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Route
    api_response = api_instance.replace_namespaced_route(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_route: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_template**
> V1Template replace_namespaced_template(body, namespace, name, pretty=pretty)

replace the specified Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Template() # V1Template | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Template
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Template
    api_response = api_instance.replace_namespaced_template(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_namespaced_template: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_netnamespace**
> V1NetNamespace replace_netnamespace(body, name, pretty=pretty)

replace the specified NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1NetNamespace() # V1NetNamespace | 
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified NetNamespace
    api_response = api_instance.replace_netnamespace(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_netnamespace: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_oauthclient**
> V1OAuthClient replace_oauthclient(body, name, pretty=pretty)

replace the specified OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1OAuthClient() # V1OAuthClient | 
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified OAuthClient
    api_response = api_instance.replace_oauthclient(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_oauthclient: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_oauthclientauthorization**
> V1OAuthClientAuthorization replace_oauthclientauthorization(body, name, pretty=pretty)

replace the specified OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1OAuthClientAuthorization() # V1OAuthClientAuthorization | 
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified OAuthClientAuthorization
    api_response = api_instance.replace_oauthclientauthorization(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_oauthclientauthorization: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_project**
> V1Project replace_project(body, name, pretty=pretty)

replace the specified Project

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1Project() # V1Project | 
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Project
    api_response = api_instance.replace_project(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_project: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_user**
> V1User replace_user(body, name, pretty=pretty)

replace the specified User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1User() # V1User | 
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified User
    api_response = api_instance.replace_user(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_user: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_useridentitymapping**
> V1UserIdentityMapping replace_useridentitymapping(body, name, pretty=pretty)

replace the specified UserIdentityMapping

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
body = lib_openshift.V1UserIdentityMapping() # V1UserIdentityMapping | 
name = 'name_example' # str | name of the UserIdentityMapping
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified UserIdentityMapping
    api_response = api_instance.replace_useridentitymapping(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->replace_useridentitymapping: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_watch_build**
> JsonWatchEvent watch_namespaced_watch_build(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_build(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_build: %s\n" % e
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

# **watch_namespaced_watch_buildconfig**
> JsonWatchEvent watch_namespaced_watch_buildconfig(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_buildconfig(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_buildconfig: %s\n" % e
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

# **watch_namespaced_watch_buildconfigs**
> JsonWatchEvent watch_namespaced_watch_buildconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of BuildConfig
    api_response = api_instance.watch_namespaced_watch_buildconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_buildconfigs: %s\n" % e
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

# **watch_namespaced_watch_builds**
> JsonWatchEvent watch_namespaced_watch_builds(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Build
    api_response = api_instance.watch_namespaced_watch_builds(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_builds: %s\n" % e
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

# **watch_namespaced_watch_deploymentconfig**
> JsonWatchEvent watch_namespaced_watch_deploymentconfig(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_deploymentconfig(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_deploymentconfig: %s\n" % e
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

# **watch_namespaced_watch_deploymentconfigs**
> JsonWatchEvent watch_namespaced_watch_deploymentconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of DeploymentConfig
    api_response = api_instance.watch_namespaced_watch_deploymentconfigs(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_deploymentconfigs: %s\n" % e
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

# **watch_namespaced_watch_imagestream**
> JsonWatchEvent watch_namespaced_watch_imagestream(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_imagestream(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_imagestream: %s\n" % e
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

# **watch_namespaced_watch_imagestreams**
> JsonWatchEvent watch_namespaced_watch_imagestreams(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ImageStream
    api_response = api_instance.watch_namespaced_watch_imagestreams(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_imagestreams: %s\n" % e
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

# **watch_namespaced_watch_policie**
> JsonWatchEvent watch_namespaced_watch_policie(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_policie(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_policie: %s\n" % e
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

# **watch_namespaced_watch_policies**
> JsonWatchEvent watch_namespaced_watch_policies(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Policy
    api_response = api_instance.watch_namespaced_watch_policies(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_policies: %s\n" % e
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

# **watch_namespaced_watch_policybinding**
> JsonWatchEvent watch_namespaced_watch_policybinding(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_policybinding(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_policybinding: %s\n" % e
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

# **watch_namespaced_watch_policybindings**
> JsonWatchEvent watch_namespaced_watch_policybindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PolicyBinding
    api_response = api_instance.watch_namespaced_watch_policybindings(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_policybindings: %s\n" % e
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

# **watch_namespaced_watch_route**
> JsonWatchEvent watch_namespaced_watch_route(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_route(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_route: %s\n" % e
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

# **watch_namespaced_watch_routes**
> JsonWatchEvent watch_namespaced_watch_routes(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Route
    api_response = api_instance.watch_namespaced_watch_routes(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_routes: %s\n" % e
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

# **watch_namespaced_watch_template**
> JsonWatchEvent watch_namespaced_watch_template(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
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
    api_response = api_instance.watch_namespaced_watch_template(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_template: %s\n" % e
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

# **watch_namespaced_watch_templates**
> JsonWatchEvent watch_namespaced_watch_templates(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Template
    api_response = api_instance.watch_namespaced_watch_templates(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_namespaced_watch_templates: %s\n" % e
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

# **watch_watch_buildconfigs**
> JsonWatchEvent watch_watch_buildconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of BuildConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of BuildConfig
    api_response = api_instance.watch_watch_buildconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_buildconfigs: %s\n" % e
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

# **watch_watch_builds**
> JsonWatchEvent watch_watch_builds(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Build

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Build
    api_response = api_instance.watch_watch_builds(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_builds: %s\n" % e
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

# **watch_watch_clusternetwork**
> JsonWatchEvent watch_watch_clusternetwork(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ClusterNetwork
    api_response = api_instance.watch_watch_clusternetwork(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_clusternetwork: %s\n" % e
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

# **watch_watch_clusternetworks**
> JsonWatchEvent watch_watch_clusternetworks(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ClusterNetwork

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ClusterNetwork
    api_response = api_instance.watch_watch_clusternetworks(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_clusternetworks: %s\n" % e
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

# **watch_watch_clusterpolicie**
> JsonWatchEvent watch_watch_clusterpolicie(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ClusterPolicy
    api_response = api_instance.watch_watch_clusterpolicie(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_clusterpolicie: %s\n" % e
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

# **watch_watch_clusterpolicies**
> JsonWatchEvent watch_watch_clusterpolicies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ClusterPolicy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ClusterPolicy
    api_response = api_instance.watch_watch_clusterpolicies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_clusterpolicies: %s\n" % e
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

# **watch_watch_clusterpolicybinding**
> JsonWatchEvent watch_watch_clusterpolicybinding(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the ClusterPolicyBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ClusterPolicyBinding
    api_response = api_instance.watch_watch_clusterpolicybinding(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_clusterpolicybinding: %s\n" % e
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

# **watch_watch_clusterpolicybindings**
> JsonWatchEvent watch_watch_clusterpolicybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ClusterPolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ClusterPolicyBinding
    api_response = api_instance.watch_watch_clusterpolicybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_clusterpolicybindings: %s\n" % e
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

# **watch_watch_deploymentconfigs**
> JsonWatchEvent watch_watch_deploymentconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of DeploymentConfig

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of DeploymentConfig
    api_response = api_instance.watch_watch_deploymentconfigs(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_deploymentconfigs: %s\n" % e
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

# **watch_watch_group**
> JsonWatchEvent watch_watch_group(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Group
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Group
    api_response = api_instance.watch_watch_group(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_group: %s\n" % e
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

# **watch_watch_groups**
> JsonWatchEvent watch_watch_groups(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Group
    api_response = api_instance.watch_watch_groups(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_groups: %s\n" % e
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

# **watch_watch_hostsubnet**
> JsonWatchEvent watch_watch_hostsubnet(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind HostSubnet
    api_response = api_instance.watch_watch_hostsubnet(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_hostsubnet: %s\n" % e
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

# **watch_watch_hostsubnets**
> JsonWatchEvent watch_watch_hostsubnets(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of HostSubnet

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of HostSubnet
    api_response = api_instance.watch_watch_hostsubnets(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_hostsubnets: %s\n" % e
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

# **watch_watch_identitie**
> JsonWatchEvent watch_watch_identitie(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Identity
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Identity
    api_response = api_instance.watch_watch_identitie(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_identitie: %s\n" % e
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

# **watch_watch_identities**
> JsonWatchEvent watch_watch_identities(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Identity

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Identity
    api_response = api_instance.watch_watch_identities(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_identities: %s\n" % e
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

# **watch_watch_image**
> JsonWatchEvent watch_watch_image(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Image
    api_response = api_instance.watch_watch_image(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_image: %s\n" % e
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

# **watch_watch_images**
> JsonWatchEvent watch_watch_images(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Image

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Image
    api_response = api_instance.watch_watch_images(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_images: %s\n" % e
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

# **watch_watch_imagestreams**
> JsonWatchEvent watch_watch_imagestreams(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of ImageStream

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ImageStream
    api_response = api_instance.watch_watch_imagestreams(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_imagestreams: %s\n" % e
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

# **watch_watch_netnamespace**
> JsonWatchEvent watch_watch_netnamespace(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind NetNamespace
    api_response = api_instance.watch_watch_netnamespace(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_netnamespace: %s\n" % e
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

# **watch_watch_netnamespaces**
> JsonWatchEvent watch_watch_netnamespaces(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of NetNamespace

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of NetNamespace
    api_response = api_instance.watch_watch_netnamespaces(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_netnamespaces: %s\n" % e
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

# **watch_watch_oauthclient**
> JsonWatchEvent watch_watch_oauthclient(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the OAuthClient
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind OAuthClient
    api_response = api_instance.watch_watch_oauthclient(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_oauthclient: %s\n" % e
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

# **watch_watch_oauthclientauthorization**
> JsonWatchEvent watch_watch_oauthclientauthorization(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the OAuthClientAuthorization
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind OAuthClientAuthorization
    api_response = api_instance.watch_watch_oauthclientauthorization(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_oauthclientauthorization: %s\n" % e
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

# **watch_watch_oauthclientauthorizations**
> JsonWatchEvent watch_watch_oauthclientauthorizations(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of OAuthClientAuthorization

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of OAuthClientAuthorization
    api_response = api_instance.watch_watch_oauthclientauthorizations(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_oauthclientauthorizations: %s\n" % e
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

# **watch_watch_oauthclients**
> JsonWatchEvent watch_watch_oauthclients(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of OAuthClient

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of OAuthClient
    api_response = api_instance.watch_watch_oauthclients(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_oauthclients: %s\n" % e
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

# **watch_watch_policies**
> JsonWatchEvent watch_watch_policies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Policy

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Policy
    api_response = api_instance.watch_watch_policies(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_policies: %s\n" % e
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

# **watch_watch_policybindings**
> JsonWatchEvent watch_watch_policybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of PolicyBinding

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of PolicyBinding
    api_response = api_instance.watch_watch_policybindings(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_policybindings: %s\n" % e
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

# **watch_watch_routes**
> JsonWatchEvent watch_watch_routes(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Route

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Route
    api_response = api_instance.watch_watch_routes(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_routes: %s\n" % e
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

# **watch_watch_templates**
> JsonWatchEvent watch_watch_templates(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of Template

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Template
    api_response = api_instance.watch_watch_templates(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_templates: %s\n" % e
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

# **watch_watch_user**
> JsonWatchEvent watch_watch_user(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
name = 'name_example' # str | name of the User
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind User
    api_response = api_instance.watch_watch_user(name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_user: %s\n" % e
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

# **watch_watch_users**
> JsonWatchEvent watch_watch_users(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of User

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.OapiV1()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of User
    api_response = api_instance.watch_watch_users(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OapiV1->watch_watch_users: %s\n" % e
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

