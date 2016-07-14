# lib_openshift.ApisautoscalingvApi

All URIs are relative to *https://localhost:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#create_horizontal_pod_autoscaler) | **POST** /apis/autoscaling/v1/horizontalpodautoscalers | create a HorizontalPodAutoscaler
[**create_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#create_namespaced_horizontal_pod_autoscaler) | **POST** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers | create a HorizontalPodAutoscaler
[**delete_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#delete_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | delete a HorizontalPodAutoscaler
[**deletecollection_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#deletecollection_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers | delete collection of HorizontalPodAutoscaler
[**get_api_resources**](ApisautoscalingvApi.md#get_api_resources) | **GET** /apis/autoscaling/v1 | get available resources
[**list_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#list_horizontal_pod_autoscaler) | **GET** /apis/autoscaling/v1/horizontalpodautoscalers | list or watch objects of kind HorizontalPodAutoscaler
[**list_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#list_namespaced_horizontal_pod_autoscaler) | **GET** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers | list or watch objects of kind HorizontalPodAutoscaler
[**patch_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#patch_namespaced_horizontal_pod_autoscaler) | **PATCH** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | partially update the specified HorizontalPodAutoscaler
[**read_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#read_namespaced_horizontal_pod_autoscaler) | **GET** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | read the specified HorizontalPodAutoscaler
[**replace_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#replace_namespaced_horizontal_pod_autoscaler) | **PUT** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | replace the specified HorizontalPodAutoscaler
[**replace_namespaced_horizontal_pod_autoscaler_status**](ApisautoscalingvApi.md#replace_namespaced_horizontal_pod_autoscaler_status) | **PUT** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | replace status of the specified HorizontalPodAutoscaler
[**watch_horizontal_pod_autoscaler_list**](ApisautoscalingvApi.md#watch_horizontal_pod_autoscaler_list) | **GET** /apis/autoscaling/v1/watch/horizontalpodautoscalers | watch individual changes to a list of HorizontalPodAutoscaler
[**watch_namespaced_horizontal_pod_autoscaler**](ApisautoscalingvApi.md#watch_namespaced_horizontal_pod_autoscaler) | **GET** /apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers/{name} | watch changes to an object of kind HorizontalPodAutoscaler
[**watch_namespaced_horizontal_pod_autoscaler_list**](ApisautoscalingvApi.md#watch_namespaced_horizontal_pod_autoscaler_list) | **GET** /apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers | watch individual changes to a list of HorizontalPodAutoscaler


# **create_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler create_horizontal_pod_autoscaler(body, pretty=pretty)

create a HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
body = lib_openshift.V1HorizontalPodAutoscaler() # V1HorizontalPodAutoscaler | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a HorizontalPodAutoscaler
    api_response = api_instance.create_horizontal_pod_autoscaler(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->create_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler create_namespaced_horizontal_pod_autoscaler(body, namespace, pretty=pretty)

create a HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
body = lib_openshift.V1HorizontalPodAutoscaler() # V1HorizontalPodAutoscaler | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a HorizontalPodAutoscaler
    api_response = api_instance.create_namespaced_horizontal_pod_autoscaler(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->create_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus delete_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)

delete a HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
body = lib_openshift.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a HorizontalPodAutoscaler
    api_response = api_instance.delete_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->delete_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus deletecollection_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

delete collection of HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of HorizontalPodAutoscaler
    api_response = api_instance.deletecollection_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->deletecollection_namespaced_horizontal_pod_autoscaler: %s\n" % e
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
api_instance = lib_openshift.ApisautoscalingvApi()

try: 
    # get available resources
    api_instance.get_api_resources()
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->get_api_resources: %s\n" % e
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

# **list_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscalerList list_horizontal_pod_autoscaler(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind HorizontalPodAutoscaler
    api_response = api_instance.list_horizontal_pod_autoscaler(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->list_horizontal_pod_autoscaler: %s\n" % e
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

[**V1HorizontalPodAutoscalerList**](V1HorizontalPodAutoscalerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscalerList list_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind HorizontalPodAutoscaler
    api_response = api_instance.list_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->list_namespaced_horizontal_pod_autoscaler: %s\n" % e
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

[**V1HorizontalPodAutoscalerList**](V1HorizontalPodAutoscalerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler patch_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)

partially update the specified HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
body = lib_openshift.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified HorizontalPodAutoscaler
    api_response = api_instance.patch_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->patch_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler read_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified HorizontalPodAutoscaler
    api_response = api_instance.read_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->read_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)

replace the specified HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
body = lib_openshift.V1HorizontalPodAutoscaler() # V1HorizontalPodAutoscaler | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified HorizontalPodAutoscaler
    api_response = api_instance.replace_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->replace_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler_status**
> V1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler_status(body, namespace, name, pretty=pretty)

replace status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
body = lib_openshift.V1HorizontalPodAutoscaler() # V1HorizontalPodAutoscaler | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified HorizontalPodAutoscaler
    api_response = api_instance.replace_namespaced_horizontal_pod_autoscaler_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->replace_namespaced_horizontal_pod_autoscaler_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_horizontal_pod_autoscaler_list**
> JsonWatchEvent watch_horizontal_pod_autoscaler_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of HorizontalPodAutoscaler
    api_response = api_instance.watch_horizontal_pod_autoscaler_list(pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->watch_horizontal_pod_autoscaler_list: %s\n" % e
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

# **watch_namespaced_horizontal_pod_autoscaler**
> JsonWatchEvent watch_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch changes to an object of kind HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind HorizontalPodAutoscaler
    api_response = api_instance.watch_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->watch_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
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

# **watch_namespaced_horizontal_pod_autoscaler_list**
> JsonWatchEvent watch_namespaced_horizontal_pod_autoscaler_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)

watch individual changes to a list of HorizontalPodAutoscaler

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisautoscalingvApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of HorizontalPodAutoscaler
    api_response = api_instance.watch_namespaced_horizontal_pod_autoscaler_list(namespace, pretty=pretty, label_selector=label_selector, field_selector=field_selector, watch=watch, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisautoscalingvApi->watch_namespaced_horizontal_pod_autoscaler_list: %s\n" % e
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

