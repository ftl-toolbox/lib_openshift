# lib_openshift.VersionApi

All URIs are relative to *https://10.0.0.51:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code_version**](VersionApi.md#get_code_version) | **GET** /version | get the code version


# **get_code_version**
> get_code_version()

get the code version

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.VersionApi()

try: 
    # get the code version
    api_instance.get_code_version()
except ApiException as e:
    print "Exception when calling VersionApi->get_code_version: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

