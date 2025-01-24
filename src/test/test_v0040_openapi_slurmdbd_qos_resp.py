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

from aind_slurm_rest.models.v0040_openapi_slurmdbd_qos_resp import V0040OpenapiSlurmdbdQosResp

class TestV0040OpenapiSlurmdbdQosResp(unittest.TestCase):
    """V0040OpenapiSlurmdbdQosResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiSlurmdbdQosResp:
        """Test V0040OpenapiSlurmdbdQosResp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiSlurmdbdQosResp`
        """
        model = V0040OpenapiSlurmdbdQosResp()
        if include_optional:
            return V0040OpenapiSlurmdbdQosResp(
                qos = [
                    aind_slurm_rest.models.v0/0/40_qos.v0.0.40_qos(
                        description = '', 
                        flags = [
                            'NOT_SET'
                            ], 
                        id = 56, 
                        limits = aind_slurm_rest.models.v0_0_40_qos_limits.v0_0_40_qos_limits(
                            grace_time = 56, 
                            max = aind_slurm_rest.models.v0_0_40_qos_limits_max.v0_0_40_qos_limits_max(
                                active_jobs = aind_slurm_rest.models.v0_0_40_qos_limits_max_active_jobs.v0_0_40_qos_limits_max_active_jobs(
                                    accruing = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    count = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), ), 
                                tres = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres.v0_0_40_qos_limits_max_tres(
                                    total = [
                                        aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], 
                                    minutes = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres_minutes.v0_0_40_qos_limits_max_tres_minutes(
                                        per = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres_minutes_per.v0_0_40_qos_limits_max_tres_minutes_per(
                                            qos = [
                                                aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                                                    type = '', 
                                                    name = '', 
                                                    id = 56, )
                                                ], 
                                            job = , 
                                            account = , 
                                            user = , ), ), 
                                    per = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres_per.v0_0_40_qos_limits_max_tres_per(
                                        node = , ), ), 
                                wall_clock = aind_slurm_rest.models.v0_0_40_qos_limits_max_wall_clock.v0_0_40_qos_limits_max_wall_clock(), 
                                jobs = aind_slurm_rest.models.v0_0_40_qos_limits_max_jobs.v0_0_40_qos_limits_max_jobs(), 
                                accruing = aind_slurm_rest.models.v0_0_40_qos_limits_max_jobs_active_jobs.v0_0_40_qos_limits_max_jobs_active_jobs(), ), 
                            factor = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            min = aind_slurm_rest.models.v0_0_40_qos_limits_min.v0_0_40_qos_limits_min(
                                priority_threshold = , ), ), 
                        name = '', 
                        preempt = aind_slurm_rest.models.v0_0_40_qos_preempt.v0_0_40_qos_preempt(
                            list = [
                                ''
                                ], 
                            mode = [
                                'DISABLED'
                                ], 
                            exempt_time = , ), 
                        priority = , 
                        usage_factor = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        usage_threshold = , )
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
            return V0040OpenapiSlurmdbdQosResp(
                qos = [
                    aind_slurm_rest.models.v0/0/40_qos.v0.0.40_qos(
                        description = '', 
                        flags = [
                            'NOT_SET'
                            ], 
                        id = 56, 
                        limits = aind_slurm_rest.models.v0_0_40_qos_limits.v0_0_40_qos_limits(
                            grace_time = 56, 
                            max = aind_slurm_rest.models.v0_0_40_qos_limits_max.v0_0_40_qos_limits_max(
                                active_jobs = aind_slurm_rest.models.v0_0_40_qos_limits_max_active_jobs.v0_0_40_qos_limits_max_active_jobs(
                                    accruing = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    count = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), ), 
                                tres = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres.v0_0_40_qos_limits_max_tres(
                                    total = [
                                        aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], 
                                    minutes = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres_minutes.v0_0_40_qos_limits_max_tres_minutes(
                                        per = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres_minutes_per.v0_0_40_qos_limits_max_tres_minutes_per(
                                            qos = [
                                                aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                                                    type = '', 
                                                    name = '', 
                                                    id = 56, )
                                                ], 
                                            job = , 
                                            account = , 
                                            user = , ), ), 
                                    per = aind_slurm_rest.models.v0_0_40_qos_limits_max_tres_per.v0_0_40_qos_limits_max_tres_per(
                                        node = , ), ), 
                                wall_clock = aind_slurm_rest.models.v0_0_40_qos_limits_max_wall_clock.v0_0_40_qos_limits_max_wall_clock(), 
                                jobs = aind_slurm_rest.models.v0_0_40_qos_limits_max_jobs.v0_0_40_qos_limits_max_jobs(), 
                                accruing = aind_slurm_rest.models.v0_0_40_qos_limits_max_jobs_active_jobs.v0_0_40_qos_limits_max_jobs_active_jobs(), ), 
                            factor = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            min = aind_slurm_rest.models.v0_0_40_qos_limits_min.v0_0_40_qos_limits_min(
                                priority_threshold = , ), ), 
                        name = '', 
                        preempt = aind_slurm_rest.models.v0_0_40_qos_preempt.v0_0_40_qos_preempt(
                            list = [
                                ''
                                ], 
                            mode = [
                                'DISABLED'
                                ], 
                            exempt_time = , ), 
                        priority = , 
                        usage_factor = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        usage_threshold = , )
                    ],
        )
        """

    def testV0040OpenapiSlurmdbdQosResp(self):
        """Test V0040OpenapiSlurmdbdQosResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
