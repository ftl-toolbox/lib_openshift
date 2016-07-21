# lib_openshift.ApisAutoscaling

All URIs are relative to *https://localhost:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_group**](ApisAutoscaling.md#get_api_group) | **GET** /apis/autoscaling | get information of a group


# **get_api_group**
> get_api_group()

get information of a group

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.ApisAutoscaling()

try: 
    # get information of a group
    api_instance.get_api_group()
except ApiException as e:
    print "Exception when calling ApisAutoscaling->get_api_group: %s\n" % e
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

