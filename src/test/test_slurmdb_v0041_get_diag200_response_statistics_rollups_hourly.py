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

from aind_slurm_rest.models.slurmdb_v0041_get_diag200_response_statistics_rollups_hourly import SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly

class TestSlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly(unittest.TestCase):
    """SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly:
        """Test SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly`
        """
        model = SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly()
        if include_optional:
            return SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly(
                count = 56,
                last_run = 56,
                duration = aind_slurm_rest.models.slurmdb_v0041_get_diag_200_response_statistics_rollups_hourly_duration.slurmdb_v0041_get_diag_200_response_statistics_rollups_hourly_duration(
                    last = 56, 
                    max = 56, 
                    time = 56, )
            )
        else:
            return SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly(
        )
        """

    def testSlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly(self):
        """Test SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
