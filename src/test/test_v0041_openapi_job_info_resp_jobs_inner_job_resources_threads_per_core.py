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

from aind_slurm_rest.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core import V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore

class TestV0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore:
        """Test V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore`
        """
        model = V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore(self):
        """Test V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
