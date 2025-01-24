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

from aind_slurm_rest.models.v0040_job_time import V0040JobTime

class TestV0040JobTime(unittest.TestCase):
    """V0040JobTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040JobTime:
        """Test V0040JobTime
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040JobTime`
        """
        model = V0040JobTime()
        if include_optional:
            return V0040JobTime(
                elapsed = 56,
                eligible = 56,
                end = 56,
                start = 56,
                submission = 56,
                suspended = 56,
                system = aind_slurm_rest.models.v0_0_40_job_time_system.v0_0_40_job_time_system(
                    seconds = 56, 
                    microseconds = 56, ),
                limit = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                total = aind_slurm_rest.models.v0_0_40_job_time_total.v0_0_40_job_time_total(
                    seconds = 56, 
                    microseconds = 56, ),
                user = aind_slurm_rest.models.v0_0_40_job_time_user.v0_0_40_job_time_user(
                    seconds = 56, 
                    microseconds = 56, )
            )
        else:
            return V0040JobTime(
        )
        """

    def testV0040JobTime(self):
        """Test V0040JobTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
