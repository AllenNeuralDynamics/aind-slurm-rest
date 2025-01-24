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

from aind_slurm_rest.models.v0039_qos_limits_max_jobs import V0039QosLimitsMaxJobs

class TestV0039QosLimitsMaxJobs(unittest.TestCase):
    """V0039QosLimitsMaxJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosLimitsMaxJobs:
        """Test V0039QosLimitsMaxJobs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosLimitsMaxJobs`
        """
        model = V0039QosLimitsMaxJobs()
        if include_optional:
            return V0039QosLimitsMaxJobs(
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
                per = aind_slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs_per.v0_0_39_qos_limits_max_jobs_active_jobs_per(
                    account = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    user = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), )
            )
        else:
            return V0039QosLimitsMaxJobs(
        )
        """

    def testV0039QosLimitsMaxJobs(self):
        """Test V0039QosLimitsMaxJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
