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

from aind_slurm_rest.models.slurmdb_v0041_delete_single_qos200_response import SlurmdbV0041DeleteSingleQos200Response

class TestSlurmdbV0041DeleteSingleQos200Response(unittest.TestCase):
    """SlurmdbV0041DeleteSingleQos200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmdbV0041DeleteSingleQos200Response:
        """Test SlurmdbV0041DeleteSingleQos200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmdbV0041DeleteSingleQos200Response`
        """
        model = SlurmdbV0041DeleteSingleQos200Response()
        if include_optional:
            return SlurmdbV0041DeleteSingleQos200Response(
                removed_qos = [
                    ''
                    ],
                meta = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta.slurm_v0041_get_shares_200_response_meta(
                    plugin = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_plugin.slurm_v0041_get_shares_200_response_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_client.slurm_v0041_get_shares_200_response_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_slurm.slurm_v0041_get_shares_200_response_meta_slurm(
                        version = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_slurm_version.slurm_v0041_get_shares_200_response_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    aind_slurm_rest.models.slurm_v0041_get_shares_200_response_errors_inner.slurm_v0041_get_shares_200_response_errors_inner(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.slurm_v0041_get_shares_200_response_warnings_inner.slurm_v0041_get_shares_200_response_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return SlurmdbV0041DeleteSingleQos200Response(
                removed_qos = [
                    ''
                    ],
        )
        """

    def testSlurmdbV0041DeleteSingleQos200Response(self):
        """Test SlurmdbV0041DeleteSingleQos200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
