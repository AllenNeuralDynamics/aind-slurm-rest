# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.4&openapi/dbv0.0.39&openapi/slurmctld&openapi/slurmdbd&openapi/v0.0.39
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from aind_slurm_rest.models.v0040_openapi_kill_jobs_resp import V0040OpenapiKillJobsResp

class TestV0040OpenapiKillJobsResp(unittest.TestCase):
    """V0040OpenapiKillJobsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiKillJobsResp:
        """Test V0040OpenapiKillJobsResp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiKillJobsResp`
        """
        model = V0040OpenapiKillJobsResp()
        if include_optional:
            return V0040OpenapiKillJobsResp(
                status = [
                    aind_slurm_rest.models.v0/0/40_kill_jobs_resp_job.v0.0.40_kill_jobs_resp_job(
                        error = aind_slurm_rest.models.slurm_v0041_delete_jobs_200_response_status_inner_error.slurm_v0041_delete_jobs_200_response_status_inner_error(
                            string = '', 
                            code = 56, 
                            message = '', ), 
                        step_id = '', 
                        job_id = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        federation = aind_slurm_rest.models.slurm_v0041_delete_jobs_200_response_status_inner_federation.slurm_v0041_delete_jobs_200_response_status_inner_federation(
                            sibling = '', ), )
                    ],
                meta = aind_slurm_rest.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_plugin.slurm_v0041_get_shares_200_response_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_client.slurm_v0041_get_shares_200_response_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_slurm.slurm_v0041_get_shares_200_response_meta_slurm(
                        version = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_slurm_version.slurm_v0041_get_shares_200_response_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    aind_slurm_rest.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiKillJobsResp(
                status = [
                    aind_slurm_rest.models.v0/0/40_kill_jobs_resp_job.v0.0.40_kill_jobs_resp_job(
                        error = aind_slurm_rest.models.slurm_v0041_delete_jobs_200_response_status_inner_error.slurm_v0041_delete_jobs_200_response_status_inner_error(
                            string = '', 
                            code = 56, 
                            message = '', ), 
                        step_id = '', 
                        job_id = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        federation = aind_slurm_rest.models.slurm_v0041_delete_jobs_200_response_status_inner_federation.slurm_v0041_delete_jobs_200_response_status_inner_federation(
                            sibling = '', ), )
                    ],
        )
        """

    def testV0040OpenapiKillJobsResp(self):
        """Test V0040OpenapiKillJobsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
