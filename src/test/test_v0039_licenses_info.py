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

from aind_slurm_rest.models.v0039_licenses_info import V0039LicensesInfo

class TestV0039LicensesInfo(unittest.TestCase):
    """V0039LicensesInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039LicensesInfo:
        """Test V0039LicensesInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039LicensesInfo`
        """
        model = V0039LicensesInfo()
        if include_optional:
            return V0039LicensesInfo(
                meta = aind_slurm_rest.models.v0/0/39_meta.v0.0.39_meta(
                    plugin = aind_slurm_rest.models.dbv0_0_39_meta_plugin.dbv0_0_39_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = aind_slurm_rest.models.dbv0_0_39_meta_slurm.dbv0_0_39_meta_Slurm(
                        version = aind_slurm_rest.models.dbv0_0_39_meta_slurm_version.dbv0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                errors = [
                    aind_slurm_rest.models.v0/0/39_error.v0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.v0/0/39_warning.v0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                licenses = [
                    aind_slurm_rest.models.v0/0/39_license.v0.0.39_license(
                        license_name = '', 
                        total = 56, 
                        used = 56, 
                        free = 56, 
                        remote = True, 
                        reserved = 56, 
                        last_consumed = 56, 
                        last_deficit = 56, 
                        last_update = 56, )
                    ]
            )
        else:
            return V0039LicensesInfo(
        )
        """

    def testV0039LicensesInfo(self):
        """Test V0039LicensesInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
