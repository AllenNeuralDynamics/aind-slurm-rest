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

from aind_slurm_rest.models.slurm_v0041_get_shares200_response_warnings_inner import SlurmV0041GetShares200ResponseWarningsInner

class TestSlurmV0041GetShares200ResponseWarningsInner(unittest.TestCase):
    """SlurmV0041GetShares200ResponseWarningsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmV0041GetShares200ResponseWarningsInner:
        """Test SlurmV0041GetShares200ResponseWarningsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmV0041GetShares200ResponseWarningsInner`
        """
        model = SlurmV0041GetShares200ResponseWarningsInner()
        if include_optional:
            return SlurmV0041GetShares200ResponseWarningsInner(
                description = '',
                source = ''
            )
        else:
            return SlurmV0041GetShares200ResponseWarningsInner(
        )
        """

    def testSlurmV0041GetShares200ResponseWarningsInner(self):
        """Test SlurmV0041GetShares200ResponseWarningsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
