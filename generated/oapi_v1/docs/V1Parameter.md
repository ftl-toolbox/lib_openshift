# V1Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name must be set and it can be referenced in Template Items using ${PARAMETER_NAME}. Required. | 
**display_name** | **str** | Optional: The name that will show in UI instead of parameter &#39;Name&#39; | [optional] 
**description** | **str** | Description of a parameter. Optional. | [optional] 
**value** | **str** | Value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional. | [optional] 
**generate** | **str** | Generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional. | [optional] 
**_from** | **str** | From is an input value for the generator. Optional. | [optional] 
**required** | **bool** | Optional: Indicates the parameter must have a value.  Defaults to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


