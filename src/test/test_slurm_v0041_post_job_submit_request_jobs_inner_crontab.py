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

from aind_slurm_rest.models.slurm_v0041_post_job_submit_request_jobs_inner_crontab import SlurmV0041PostJobSubmitRequestJobsInnerCrontab

class TestSlurmV0041PostJobSubmitRequestJobsInnerCrontab(unittest.TestCase):
    """SlurmV0041PostJobSubmitRequestJobsInnerCrontab unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlurmV0041PostJobSubmitRequestJobsInnerCrontab:
        """Test SlurmV0041PostJobSubmitRequestJobsInnerCrontab
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlurmV0041PostJobSubmitRequestJobsInnerCrontab`
        """
        model = SlurmV0041PostJobSubmitRequestJobsInnerCrontab()
        if include_optional:
            return SlurmV0041PostJobSubmitRequestJobsInnerCrontab(
                flags = [
                    'WILD_MINUTE'
                    ],
                minute = '',
                hour = '',
                day_of_month = '',
                month = '',
                day_of_week = '',
                specification = '',
                command = '',
                line = aind_slurm_rest.models.slurm_v0041_post_job_submit_request_jobs_inner_crontab_line.slurm_v0041_post_job_submit_request_jobs_inner_crontab_line(
                    start = 56, 
                    end = 56, )
            )
        else:
            return SlurmV0041PostJobSubmitRequestJobsInnerCrontab(
        )
        """

    def testSlurmV0041PostJobSubmitRequestJobsInnerCrontab(self):
        """Test SlurmV0041PostJobSubmitRequestJobsInnerCrontab"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
