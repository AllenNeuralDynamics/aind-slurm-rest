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

from aind_slurm_rest.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_per import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer

class TestV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer:
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer`
        """
        model = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer(
                job = [
                    aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer(self):
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
