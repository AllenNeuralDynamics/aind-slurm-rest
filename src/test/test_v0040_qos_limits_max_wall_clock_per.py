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

from aind_slurm_rest.models.v0040_qos_limits_max_wall_clock_per import V0040QosLimitsMaxWallClockPer

class TestV0040QosLimitsMaxWallClockPer(unittest.TestCase):
    """V0040QosLimitsMaxWallClockPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040QosLimitsMaxWallClockPer:
        """Test V0040QosLimitsMaxWallClockPer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040QosLimitsMaxWallClockPer`
        """
        model = V0040QosLimitsMaxWallClockPer()
        if include_optional:
            return V0040QosLimitsMaxWallClockPer(
                qos = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                job = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0040QosLimitsMaxWallClockPer(
        )
        """

    def testV0040QosLimitsMaxWallClockPer(self):
        """Test V0040QosLimitsMaxWallClockPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
