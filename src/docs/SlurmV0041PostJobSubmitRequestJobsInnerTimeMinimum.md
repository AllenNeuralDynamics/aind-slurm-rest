# SlurmV0041PostJobSubmitRequestJobsInnerTimeMinimum

Minimum run time in minutes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from aind_slurm_rest.models.slurm_v0041_post_job_submit_request_jobs_inner_time_minimum import SlurmV0041PostJobSubmitRequestJobsInnerTimeMinimum

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerTimeMinimum from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_time_minimum_instance = SlurmV0041PostJobSubmitRequestJobsInnerTimeMinimum.from_json(json)
# print the JSON string representation of the object
print SlurmV0041PostJobSubmitRequestJobsInnerTimeMinimum.to_json()

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_time_minimum_dict = slurm_v0041_post_job_submit_request_jobs_inner_time_minimum_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerTimeMinimum from a dict
slurm_v0041_post_job_submit_request_jobs_inner_time_minimum_form_dict = slurm_v0041_post_job_submit_request_jobs_inner_time_minimum.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_time_minimum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


