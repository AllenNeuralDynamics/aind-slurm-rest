# V0041OpenapiSlurmdbdJobsResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInner]**](V0041OpenapiSlurmdbdJobsRespJobsInner.md) | jobs | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from aind_slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp import V0041OpenapiSlurmdbdJobsResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsResp from a JSON string
v0041_openapi_slurmdbd_jobs_resp_instance = V0041OpenapiSlurmdbdJobsResp.from_json(json)
# print the JSON string representation of the object
print V0041OpenapiSlurmdbdJobsResp.to_json()

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_dict = v0041_openapi_slurmdbd_jobs_resp_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsResp from a dict
v0041_openapi_slurmdbd_jobs_resp_form_dict = v0041_openapi_slurmdbd_jobs_resp.from_dict(v0041_openapi_slurmdbd_jobs_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


