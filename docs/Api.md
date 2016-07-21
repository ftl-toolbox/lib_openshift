# lib_openshift.Api

All URIs are relative to *https://localhost:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_versions**](Api.md#get_api_versions) | **GET** /api | get available API versions


# **get_api_versions**
> get_api_versions()

get available API versions

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.Api()

try: 
    # get available API versions
    api_instance.get_api_versions()
except ApiException as e:
    print "Exception when calling Api->get_api_versions: %s\n" % e
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

