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

from aind_slurm_rest.models.v0041_openapi_partition_resp_partitions_inner_defaults_time import V0041OpenapiPartitionRespPartitionsInnerDefaultsTime

class TestV0041OpenapiPartitionRespPartitionsInnerDefaultsTime(unittest.TestCase):
    """V0041OpenapiPartitionRespPartitionsInnerDefaultsTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiPartitionRespPartitionsInnerDefaultsTime:
        """Test V0041OpenapiPartitionRespPartitionsInnerDefaultsTime
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiPartitionRespPartitionsInnerDefaultsTime`
        """
        model = V0041OpenapiPartitionRespPartitionsInnerDefaultsTime()
        if include_optional:
            return V0041OpenapiPartitionRespPartitionsInnerDefaultsTime(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiPartitionRespPartitionsInnerDefaultsTime(
        )
        """

    def testV0041OpenapiPartitionRespPartitionsInnerDefaultsTime(self):
        """Test V0041OpenapiPartitionRespPartitionsInnerDefaultsTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
