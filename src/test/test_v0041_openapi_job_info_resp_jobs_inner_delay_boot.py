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

from aind_slurm_rest.models.v0041_openapi_job_info_resp_jobs_inner_delay_boot import V0041OpenapiJobInfoRespJobsInnerDelayBoot

class TestV0041OpenapiJobInfoRespJobsInnerDelayBoot(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerDelayBoot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerDelayBoot:
        """Test V0041OpenapiJobInfoRespJobsInnerDelayBoot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerDelayBoot`
        """
        model = V0041OpenapiJobInfoRespJobsInnerDelayBoot()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerDelayBoot(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerDelayBoot(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerDelayBoot(self):
        """Test V0041OpenapiJobInfoRespJobsInnerDelayBoot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
