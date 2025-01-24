# SlurmV0041GetDiag200ResponseStatisticsScheduleExit

Reasons for which the scheduling cycle exited since last reset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** | Reached end of queue | [optional] 
**default_queue_depth** | **int** | Reached number of jobs allowed to be tested | [optional] 
**max_job_start** | **int** | Reached number of jobs allowed to start | [optional] 
**max_rpc_cnt** | **int** | Reached RPC limit | [optional] 
**max_sched_time** | **int** | Reached maximum allowed scheduler time | [optional] 
**licenses** | **int** | Blocked on licenses | [optional] 

## Example

```python
from aind_slurm_rest.models.slurm_v0041_get_diag200_response_statistics_schedule_exit import SlurmV0041GetDiag200ResponseStatisticsScheduleExit

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetDiag200ResponseStatisticsScheduleExit from a JSON string
slurm_v0041_get_diag200_response_statistics_schedule_exit_instance = SlurmV0041GetDiag200ResponseStatisticsScheduleExit.from_json(json)
# print the JSON string representation of the object
print SlurmV0041GetDiag200ResponseStatisticsScheduleExit.to_json()

# convert the object into a dict
slurm_v0041_get_diag200_response_statistics_schedule_exit_dict = slurm_v0041_get_diag200_response_statistics_schedule_exit_instance.to_dict()
# create an instance of SlurmV0041GetDiag200ResponseStatisticsScheduleExit from a dict
slurm_v0041_get_diag200_response_statistics_schedule_exit_form_dict = slurm_v0041_get_diag200_response_statistics_schedule_exit.from_dict(slurm_v0041_get_diag200_response_statistics_schedule_exit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


