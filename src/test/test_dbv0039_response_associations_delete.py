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

from aind_slurm_rest.models.dbv0039_response_associations_delete import Dbv0039ResponseAssociationsDelete

class TestDbv0039ResponseAssociationsDelete(unittest.TestCase):
    """Dbv0039ResponseAssociationsDelete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039ResponseAssociationsDelete:
        """Test Dbv0039ResponseAssociationsDelete
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039ResponseAssociationsDelete`
        """
        model = Dbv0039ResponseAssociationsDelete()
        if include_optional:
            return Dbv0039ResponseAssociationsDelete(
                meta = aind_slurm_rest.models.dbv0/0/39_meta.dbv0.0.39_meta(
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
                    aind_slurm_rest.models.dbv0/0/39_error.dbv0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.dbv0/0/39_warning.dbv0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                removed_associations = [
                    ''
                    ]
            )
        else:
            return Dbv0039ResponseAssociationsDelete(
        )
        """

    def testDbv0039ResponseAssociationsDelete(self):
        """Test Dbv0039ResponseAssociationsDelete"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
