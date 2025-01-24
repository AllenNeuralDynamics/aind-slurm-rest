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

from aind_slurm_rest.models.v0039_user_default import V0039UserDefault

class TestV0039UserDefault(unittest.TestCase):
    """V0039UserDefault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039UserDefault:
        """Test V0039UserDefault
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039UserDefault`
        """
        model = V0039UserDefault()
        if include_optional:
            return V0039UserDefault(
                account = '',
                wckey = ''
            )
        else:
            return V0039UserDefault(
        )
        """

    def testV0039UserDefault(self):
        """Test V0039UserDefault"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
