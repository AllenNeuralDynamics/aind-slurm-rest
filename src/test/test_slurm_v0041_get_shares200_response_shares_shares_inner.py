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

from aind_slurm_rest.models.slurm_v0041_get_shares200_response_shares_shares_inner import SlurmV0041GetShares200ResponseSharesSharesInner

class TestSlurmV0041GetShares200ResponseSharesSharesInner(unittest.TestCase):
    """SlurmV0041GetShares200ResponseSharesSharesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmV0041GetShares200ResponseSharesSharesInner:
        """Test SlurmV0041GetShares200ResponseSharesSharesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmV0041GetShares200ResponseSharesSharesInner`
        """
        model = SlurmV0041GetShares200ResponseSharesSharesInner()
        if include_optional:
            return SlurmV0041GetShares200ResponseSharesSharesInner(
                id = 56,
                cluster = '',
                name = '',
                parent = '',
                partition = '',
                shares_normalized = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_shares_normalized.slurm_v0041_get_shares_200_response_shares_shares_inner_shares_normalized(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ),
                shares = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_shares.slurm_v0041_get_shares_200_response_shares_shares_inner_shares(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                tres = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_tres.slurm_v0041_get_shares_200_response_shares_shares_inner_tres(
                    run_seconds = [
                        aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_run_seconds_inner.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_run_seconds_inner(
                            name = '', 
                            value = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_run_seconds_inner_value.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_run_seconds_inner_value(
                                set = True, 
                                infinite = True, 
                                number = 56, ), )
                        ], 
                    group_minutes = [
                        aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_run_seconds_inner.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_run_seconds_inner(
                            name = '', )
                        ], 
                    usage = [
                        aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_usage_inner.slurm_v0041_get_shares_200_response_shares_shares_inner_tres_usage_inner(
                            name = '', )
                        ], ),
                effective_usage = 1.337,
                usage_normalized = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_usage_normalized.slurm_v0041_get_shares_200_response_shares_shares_inner_usage_normalized(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ),
                usage = 56,
                fairshare = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_fairshare.slurm_v0041_get_shares_200_response_shares_shares_inner_fairshare(
                    factor = 1.337, 
                    level = 1.337, ),
                type = [
                    'USER'
                    ]
            )
        else:
            return SlurmV0041GetShares200ResponseSharesSharesInner(
        )
        """

    def testSlurmV0041GetShares200ResponseSharesSharesInner(self):
        """Test SlurmV0041GetShares200ResponseSharesSharesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
