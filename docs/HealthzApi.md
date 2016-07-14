# lib_openshift.HealthzApi

All URIs are relative to *https://10.0.0.51:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**func1**](HealthzApi.md#func1) | **GET** /healthz | return the health state of the master


# **func1**
> func1()

return the health state of the master

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.HealthzApi()

try: 
    # return the health state of the master
    api_instance.func1()
except ApiException as e:
    print "Exception when calling HealthzApi->func1: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

