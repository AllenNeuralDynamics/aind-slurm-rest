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

from aind_slurm_rest.models.v0041_openapi_slurmdbd_qos_resp import V0041OpenapiSlurmdbdQosResp

class TestV0041OpenapiSlurmdbdQosResp(unittest.TestCase):
    """V0041OpenapiSlurmdbdQosResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdQosResp:
        """Test V0041OpenapiSlurmdbdQosResp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdQosResp`
        """
        model = V0041OpenapiSlurmdbdQosResp()
        if include_optional:
            return V0041OpenapiSlurmdbdQosResp(
                qos = [
                    aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner.v0_0_41_openapi_slurmdbd_config_resp_qos_inner(
                        description = '', 
                        flags = [
                            'NOT_SET'
                            ], 
                        id = 56, 
                        limits = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits(
                            grace_time = 56, 
                            max = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max(
                                active_jobs = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs(
                                    accruing = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    count = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), ), 
                                tres = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres(
                                    total = [
                                        aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], 
                                    minutes = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes(
                                        per = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per(
                                            qos = [
                                                aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner(
                                                    type = '', 
                                                    name = '', 
                                                    id = 56, )
                                                ], 
                                            job = [
                                                
                                                ], 
                                            account = [
                                                
                                                ], 
                                            user = [
                                                
                                                ], ), ), 
                                    per = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per(
                                        node = [
                                            
                                            ], ), ), 
                                wall_clock = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock(), 
                                jobs = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs(), 
                                accruing = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing(), ), 
                            factor = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            min = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min(
                                priority_threshold = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), ), ), 
                        name = '', 
                        preempt = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt(
                            list = [
                                ''
                                ], 
                            mode = [
                                'DISABLED'
                                ], 
                            exempt_time = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        priority = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        usage_factor = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        usage_threshold = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), )
                    ],
                meta = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta.slurm_v0041_get_shares_200_response_meta(
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
                    aind_slurm_rest.models.slurm_v0041_get_shares_200_response_errors_inner.slurm_v0041_get_shares_200_response_errors_inner(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.slurm_v0041_get_shares_200_response_warnings_inner.slurm_v0041_get_shares_200_response_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiSlurmdbdQosResp(
                qos = [
                    aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner.v0_0_41_openapi_slurmdbd_config_resp_qos_inner(
                        description = '', 
                        flags = [
                            'NOT_SET'
                            ], 
                        id = 56, 
                        limits = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits(
                            grace_time = 56, 
                            max = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max(
                                active_jobs = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs(
                                    accruing = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    count = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), ), 
                                tres = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres(
                                    total = [
                                        aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], 
                                    minutes = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes(
                                        per = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per(
                                            qos = [
                                                aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner(
                                                    type = '', 
                                                    name = '', 
                                                    id = 56, )
                                                ], 
                                            job = [
                                                
                                                ], 
                                            account = [
                                                
                                                ], 
                                            user = [
                                                
                                                ], ), ), 
                                    per = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per(
                                        node = [
                                            
                                            ], ), ), 
                                wall_clock = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock(), 
                                jobs = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs(), 
                                accruing = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing(), ), 
                            factor = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            min = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min(
                                priority_threshold = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_priority_threshold(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), ), ), 
                        name = '', 
                        preempt = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt(
                            list = [
                                ''
                                ], 
                            mode = [
                                'DISABLED'
                                ], 
                            exempt_time = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        priority = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        usage_factor = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        usage_threshold = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), )
                    ],
        )
        """

    def testV0041OpenapiSlurmdbdQosResp(self):
        """Test V0041OpenapiSlurmdbdQosResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
