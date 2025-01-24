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

from aind_slurm_rest.models.slurmdb_v0041_get_diag200_response_statistics_rpcs_inner import SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner

class TestSlurmdbV0041GetDiag200ResponseStatisticsRPCsInner(unittest.TestCase):
    """SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner:
        """Test SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner`
        """
        model = SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner()
        if include_optional:
            return SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner(
                rpc = '',
                count = 56,
                time = aind_slurm_rest.models.slurmdb_v0041_get_diag_200_response_statistics_rpcs_inner_time.slurmdb_v0041_get_diag_200_response_statistics_RPCs_inner_time(
                    average = 56, 
                    total = 56, )
            )
        else:
            return SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner(
        )
        """

    def testSlurmdbV0041GetDiag200ResponseStatisticsRPCsInner(self):
        """Test SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
