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

from aind_slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_step import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep(
                id = '',
                name = ''
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
