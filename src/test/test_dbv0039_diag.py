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

from aind_slurm_rest.models.dbv0039_diag import Dbv0039Diag

class TestDbv0039Diag(unittest.TestCase):
    """Dbv0039Diag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039Diag:
        """Test Dbv0039Diag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039Diag`
        """
        model = Dbv0039Diag()
        if include_optional:
            return Dbv0039Diag(
                meta = aind_slurm_rest.models.dbv0/0/39_meta.dbv0.0.39_meta(
                    plugin = aind_slurm_rest.models.dbv0_0_39_meta_plugin.dbv0_0_39_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = aind_slurm_rest.models.dbv0_0_39_meta_slurm.dbv0_0_39_meta_Slurm(
                        version = aind_slurm_rest.models.dbv0_0_39_meta_slurm_version.dbv0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                errors = [
                    aind_slurm_rest.models.dbv0/0/39_error.dbv0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.dbv0/0/39_warning.dbv0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                statistics = aind_slurm_rest.models.v0/0/39_stats_rec.v0.0.39_stats_rec(
                    time_start = 56, 
                    rollups = [
                        aind_slurm_rest.models.v0_0_40_rollup_stats_inner.v0_0_40_rollup_stats_inner(
                            type = 'internal', 
                            last_run = 56, 
                            max_cycle = 56, 
                            total_time = 56, 
                            total_cycles = 56, 
                            mean_cycles = 56, )
                        ], 
                    rpcs = [
                        aind_slurm_rest.models.v0/0/39_stats_rpc.v0.0.39_stats_rpc(
                            rpc = '', 
                            count = 56, 
                            time = aind_slurm_rest.models.v0_0_39_stats_rpc_time.v0_0_39_stats_rpc_time(
                                average = 56, 
                                total = 56, ), )
                        ], 
                    users = [
                        aind_slurm_rest.models.v0/0/39_stats_user.v0.0.39_stats_user(
                            user = '', 
                            count = 56, )
                        ], )
            )
        else:
            return Dbv0039Diag(
        )
        """

    def testDbv0039Diag(self):
        """Test Dbv0039Diag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
