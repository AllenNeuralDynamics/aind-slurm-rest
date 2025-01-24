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

from aind_slurm_rest.models.v0039_step_time_system import V0039StepTimeSystem

class TestV0039StepTimeSystem(unittest.TestCase):
    """V0039StepTimeSystem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039StepTimeSystem:
        """Test V0039StepTimeSystem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039StepTimeSystem`
        """
        model = V0039StepTimeSystem()
        if include_optional:
            return V0039StepTimeSystem(
                seconds = 56,
                microseconds = 56
            )
        else:
            return V0039StepTimeSystem(
        )
        """

    def testV0039StepTimeSystem(self):
        """Test V0039StepTimeSystem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
