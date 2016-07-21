# lib_openshift.Controllers

All URIs are relative to *https://localhost:8443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**func1**](Controllers.md#func1) | **GET** /controllers | Check whether the controllers are running on this master
[**func2**](Controllers.md#func2) | **PUT** /controllers | Start controllers on this master
[**func3**](Controllers.md#func3) | **DELETE** /controllers | Stop the master


# **func1**
> func1()

Check whether the controllers are running on this master

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.Controllers()

try: 
    # Check whether the controllers are running on this master
    api_instance.func1()
except ApiException as e:
    print "Exception when calling Controllers->func1: %s\n" % e
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

# **func2**
> func2()

Start controllers on this master

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.Controllers()

try: 
    # Start controllers on this master
    api_instance.func2()
except ApiException as e:
    print "Exception when calling Controllers->func2: %s\n" % e
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

# **func3**
> func3()

Stop the master

### Example 
```python
import time
import lib_openshift
from lib_openshift.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lib_openshift.Controllers()

try: 
    # Stop the master
    api_instance.func3()
except ApiException as e:
    print "Exception when calling Controllers->func3: %s\n" % e
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

