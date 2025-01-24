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

from aind_slurm_rest.models.v0040_step_tres_consumed import V0040StepTresConsumed

class TestV0040StepTresConsumed(unittest.TestCase):
    """V0040StepTresConsumed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040StepTresConsumed:
        """Test V0040StepTresConsumed
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040StepTresConsumed`
        """
        model = V0040StepTresConsumed()
        if include_optional:
            return V0040StepTresConsumed(
                max = [
                    aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                min = [
                    aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                average = [
                    aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                total = [
                    aind_slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0040StepTresConsumed(
        )
        """

    def testV0040StepTresConsumed(self):
        """Test V0040StepTresConsumed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
