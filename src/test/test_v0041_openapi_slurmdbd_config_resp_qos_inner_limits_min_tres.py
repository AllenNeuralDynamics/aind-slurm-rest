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

from aind_slurm_rest.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres

class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres(
                per = aind_slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres_per(
                    job = [
                        aind_slurm_rest.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
