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

from aind_slurm_rest.models.v0039_qos_limits_max import V0039QosLimitsMax

class TestV0039QosLimitsMax(unittest.TestCase):
    """V0039QosLimitsMax unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosLimitsMax:
        """Test V0039QosLimitsMax
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosLimitsMax`
        """
        model = V0039QosLimitsMax()
        if include_optional:
            return V0039QosLimitsMax(
                active_jobs = aind_slurm_rest.models.v0_0_39_qos_limits_max_active_jobs.v0_0_39_qos_limits_max_active_jobs(
                    accruing = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    count = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                tres = aind_slurm_rest.models.v0_0_39_qos_limits_max_tres.v0_0_39_qos_limits_max_tres(
                    total = [
                        aind_slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    minutes = aind_slurm_rest.models.v0_0_39_qos_limits_max_tres_minutes.v0_0_39_qos_limits_max_tres_minutes(
                        per = aind_slurm_rest.models.v0_0_39_qos_limits_max_tres_minutes_per.v0_0_39_qos_limits_max_tres_minutes_per(
                            qos = [
                                aind_slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                                    type = '', 
                                    name = '', 
                                    id = 56, 
                                    count = 56, )
                                ], 
                            job = , 
                            account = , 
                            user = , ), ), 
                    per = aind_slurm_rest.models.v0_0_39_qos_limits_max_tres_per.v0_0_39_qos_limits_max_tres_per(
                        account = , 
                        job = , 
                        node = , 
                        user = , ), ),
                wall_clock = aind_slurm_rest.models.v0_0_39_qos_limits_max_wall_clock.v0_0_39_qos_limits_max_wall_clock(
                    per = aind_slurm_rest.models.v0_0_39_qos_limits_max_wall_clock_per.v0_0_39_qos_limits_max_wall_clock_per(
                        qos = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        job = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), ), ),
                jobs = aind_slurm_rest.models.v0_0_39_qos_limits_max_jobs.v0_0_39_qos_limits_max_jobs(
                    active_jobs = aind_slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs.v0_0_39_qos_limits_max_jobs_active_jobs(
                        per = aind_slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs_per.v0_0_39_qos_limits_max_jobs_active_jobs_per(
                            account = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            user = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), ), 
                    per = aind_slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs_per.v0_0_39_qos_limits_max_jobs_active_jobs_per(), ),
                accruing = aind_slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs.v0_0_39_qos_limits_max_jobs_active_jobs(
                    per = aind_slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs_per.v0_0_39_qos_limits_max_jobs_active_jobs_per(
                        account = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        user = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), ), )
            )
        else:
            return V0039QosLimitsMax(
        )
        """

    def testV0039QosLimitsMax(self):
        """Test V0039QosLimitsMax"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
