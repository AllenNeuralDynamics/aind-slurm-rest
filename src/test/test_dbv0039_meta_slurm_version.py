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

from aind_slurm_rest.models.dbv0039_meta_slurm_version import Dbv0039MetaSlurmVersion

class TestDbv0039MetaSlurmVersion(unittest.TestCase):
    """Dbv0039MetaSlurmVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039MetaSlurmVersion:
        """Test Dbv0039MetaSlurmVersion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039MetaSlurmVersion`
        """
        model = Dbv0039MetaSlurmVersion()
        if include_optional:
            return Dbv0039MetaSlurmVersion(
                major = 56,
                micro = 56,
                minor = 56
            )
        else:
            return Dbv0039MetaSlurmVersion(
        )
        """

    def testDbv0039MetaSlurmVersion(self):
        """Test Dbv0039MetaSlurmVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
