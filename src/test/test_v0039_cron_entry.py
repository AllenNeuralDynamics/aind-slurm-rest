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

from aind_slurm_rest.models.v0039_cron_entry import V0039CronEntry

class TestV0039CronEntry(unittest.TestCase):
    """V0039CronEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039CronEntry:
        """Test V0039CronEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039CronEntry`
        """
        model = V0039CronEntry()
        if include_optional:
            return V0039CronEntry(
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
                line = aind_slurm_rest.models.v0_0_39_cron_entry_line.v0_0_39_cron_entry_line(
                    start = 56, 
                    end = 56, )
            )
        else:
            return V0039CronEntry(
        )
        """

    def testV0039CronEntry(self):
        """Test V0039CronEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
