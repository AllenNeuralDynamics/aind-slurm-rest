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

from aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_minpriothresh import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh

class TestSlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh(unittest.TestCase):
    """SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh:
        """Test SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh`
        """
        model = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh()
        if include_optional:
            return SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh(
        )
        """

    def testSlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh(self):
        """Test SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
