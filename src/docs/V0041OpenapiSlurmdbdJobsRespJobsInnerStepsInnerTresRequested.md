# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Maximum TRES usage requested among all tasks | [optional] 
**min** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Minimum TRES usage requested among all tasks | [optional] 
**average** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Average TRES usage requested among all tasks | [optional] 
**total** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Total TRES usage requested among all tasks | [optional] 

## Example

```python
from aind_slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested.from_json(json)
# print the JSON string representation of the object
print V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested.to_json()

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_form_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


