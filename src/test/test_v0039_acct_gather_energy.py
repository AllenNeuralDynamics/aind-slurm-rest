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

from aind_slurm_rest.models.v0039_acct_gather_energy import V0039AcctGatherEnergy

class TestV0039AcctGatherEnergy(unittest.TestCase):
    """V0039AcctGatherEnergy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039AcctGatherEnergy:
        """Test V0039AcctGatherEnergy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039AcctGatherEnergy`
        """
        model = V0039AcctGatherEnergy()
        if include_optional:
            return V0039AcctGatherEnergy(
                average_watts = 56,
                base_consumed_energy = 56,
                consumed_energy = 56,
                current_watts = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                previous_consumed_energy = 56,
                last_collected = 56
            )
        else:
            return V0039AcctGatherEnergy(
        )
        """

    def testV0039AcctGatherEnergy(self):
        """Test V0039AcctGatherEnergy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
