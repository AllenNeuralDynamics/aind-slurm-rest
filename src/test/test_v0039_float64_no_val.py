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

from aind_slurm_rest.models.v0039_float64_no_val import V0039Float64NoVal

class TestV0039Float64NoVal(unittest.TestCase):
    """V0039Float64NoVal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039Float64NoVal:
        """Test V0039Float64NoVal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039Float64NoVal`
        """
        model = V0039Float64NoVal()
        if include_optional:
            return V0039Float64NoVal(
                set = True,
                infinite = True,
                number = 1.337
            )
        else:
            return V0039Float64NoVal(
        )
        """

    def testV0039Float64NoVal(self):
        """Test V0039Float64NoVal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
