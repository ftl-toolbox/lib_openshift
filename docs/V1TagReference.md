# V1TagReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the tag | 
**annotations** | **object** | Annotations associated with images using this tag | 
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From is a reference to an image stream tag or image stream this tag should track | [optional] 
**reference** | **bool** | Reference states if the tag will be imported. Default value is false, which means the tag will be imported. | [optional] 
**generation** | **int** | Generation is the image stream generation that updated this tag - setting it to 0 is an indication that the generation must be updated. Legacy clients will send this as nil, which means the client doesn&#39;t know or care. | 
**import_policy** | [**V1TagImportPolicy**](V1TagImportPolicy.md) | Import is information that controls how images may be imported by the server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


