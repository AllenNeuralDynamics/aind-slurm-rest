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

from aind_slurm_rest.models.v0040_openapi_shares_resp import V0040OpenapiSharesResp

class TestV0040OpenapiSharesResp(unittest.TestCase):
    """V0040OpenapiSharesResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiSharesResp:
        """Test V0040OpenapiSharesResp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiSharesResp`
        """
        model = V0040OpenapiSharesResp()
        if include_optional:
            return V0040OpenapiSharesResp(
                shares = aind_slurm_rest.models.v0/0/40_shares_resp_msg.v0.0.40_shares_resp_msg(
                    shares = [
                        aind_slurm_rest.models.v0/0/40_assoc_shares_obj_wrap.v0.0.40_assoc_shares_obj_wrap(
                            id = 56, 
                            cluster = '', 
                            name = '', 
                            parent = '', 
                            partition = '', 
                            shares_normalized = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            tres = aind_slurm_rest.models.v0_0_40_assoc_shares_obj_wrap_tres.v0_0_40_assoc_shares_obj_wrap_tres(
                                run_seconds = [
                                    aind_slurm_rest.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                        name = '', 
                                        value = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                            set = True, 
                                            infinite = True, 
                                            number = 56, ), )
                                    ], 
                                group_minutes = [
                                    aind_slurm_rest.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                        name = '', )
                                    ], 
                                usage = [
                                    aind_slurm_rest.models.v0/0/40_shares_float128_tres.v0.0.40_shares_float128_tres(
                                        name = '', )
                                    ], ), 
                            effective_usage = 1.337, 
                            usage_normalized = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            usage = 56, 
                            fairshare = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_fairshare.slurm_v0041_get_shares_200_response_shares_shares_inner_fairshare(
                                factor = 1.337, 
                                level = 1.337, ), 
                            type = [
                                'USER'
                                ], )
                        ], 
                    total_shares = 56, ),
                meta = aind_slurm_rest.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
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
                    aind_slurm_rest.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiSharesResp(
                shares = aind_slurm_rest.models.v0/0/40_shares_resp_msg.v0.0.40_shares_resp_msg(
                    shares = [
                        aind_slurm_rest.models.v0/0/40_assoc_shares_obj_wrap.v0.0.40_assoc_shares_obj_wrap(
                            id = 56, 
                            cluster = '', 
                            name = '', 
                            parent = '', 
                            partition = '', 
                            shares_normalized = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            tres = aind_slurm_rest.models.v0_0_40_assoc_shares_obj_wrap_tres.v0_0_40_assoc_shares_obj_wrap_tres(
                                run_seconds = [
                                    aind_slurm_rest.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                        name = '', 
                                        value = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                            set = True, 
                                            infinite = True, 
                                            number = 56, ), )
                                    ], 
                                group_minutes = [
                                    aind_slurm_rest.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                        name = '', )
                                    ], 
                                usage = [
                                    aind_slurm_rest.models.v0/0/40_shares_float128_tres.v0.0.40_shares_float128_tres(
                                        name = '', )
                                    ], ), 
                            effective_usage = 1.337, 
                            usage_normalized = aind_slurm_rest.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            usage = 56, 
                            fairshare = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_shares_shares_inner_fairshare.slurm_v0041_get_shares_200_response_shares_shares_inner_fairshare(
                                factor = 1.337, 
                                level = 1.337, ), 
                            type = [
                                'USER'
                                ], )
                        ], 
                    total_shares = 56, ),
        )
        """

    def testV0040OpenapiSharesResp(self):
        """Test V0040OpenapiSharesResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
