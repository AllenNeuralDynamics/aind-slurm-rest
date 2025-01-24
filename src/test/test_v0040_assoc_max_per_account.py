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

from aind_slurm_rest.models.v0040_assoc_max_per_account import V0040AssocMaxPerAccount

class TestV0040AssocMaxPerAccount(unittest.TestCase):
    """V0040AssocMaxPerAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040AssocMaxPerAccount:
        """Test V0040AssocMaxPerAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040AssocMaxPerAccount`
        """
        model = V0040AssocMaxPerAccount()
        if include_optional:
            return V0040AssocMaxPerAccount(
                wall_clock = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0040AssocMaxPerAccount(
        )
        """

    def testV0040AssocMaxPerAccount(self):
        """Test V0040AssocMaxPerAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
