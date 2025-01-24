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

from aind_slurm_rest.models.v0040_shares_float128_tres import V0040SharesFloat128Tres

class TestV0040SharesFloat128Tres(unittest.TestCase):
    """V0040SharesFloat128Tres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040SharesFloat128Tres:
        """Test V0040SharesFloat128Tres
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040SharesFloat128Tres`
        """
        model = V0040SharesFloat128Tres()
        if include_optional:
            return V0040SharesFloat128Tres(
                name = '',
                value = 1.337
            )
        else:
            return V0040SharesFloat128Tres(
        )
        """

    def testV0040SharesFloat128Tres(self):
        """Test V0040SharesFloat128Tres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
