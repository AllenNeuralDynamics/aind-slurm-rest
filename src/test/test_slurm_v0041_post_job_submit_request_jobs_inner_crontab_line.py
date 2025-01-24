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

from aind_slurm_rest.models.slurm_v0041_post_job_submit_request_jobs_inner_crontab_line import SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine

class TestSlurmV0041PostJobSubmitRequestJobsInnerCrontabLine(unittest.TestCase):
    """SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine:
        """Test SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine`
        """
        model = SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine()
        if include_optional:
            return SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine(
                start = 56,
                end = 56
            )
        else:
            return SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine(
        )
        """

    def testSlurmV0041PostJobSubmitRequestJobsInnerCrontabLine(self):
        """Test SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
