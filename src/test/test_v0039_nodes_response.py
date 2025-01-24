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

from aind_slurm_rest.models.v0039_nodes_response import V0039NodesResponse

class TestV0039NodesResponse(unittest.TestCase):
    """V0039NodesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039NodesResponse:
        """Test V0039NodesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039NodesResponse`
        """
        model = V0039NodesResponse()
        if include_optional:
            return V0039NodesResponse(
                meta = aind_slurm_rest.models.v0/0/39_meta.v0.0.39_meta(
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
                    aind_slurm_rest.models.v0/0/39_error.v0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.v0/0/39_warning.v0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                nodes = [
                    aind_slurm_rest.models.v0/0/39_node.v0.0.39_node(
                        architecture = '', 
                        burstbuffer_network_address = '', 
                        boards = 56, 
                        boot_time = 56, 
                        cluster_name = '', 
                        cores = 56, 
                        specialized_cores = 56, 
                        cpu_binding = 56, 
                        cpu_load = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        free_mem = aind_slurm_rest.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        cpus = 56, 
                        effective_cpus = 56, 
                        specialized_cpus = '', 
                        energy = aind_slurm_rest.models.v0/0/39_acct_gather_energy.v0.0.39_acct_gather_energy(
                            average_watts = 56, 
                            base_consumed_energy = 56, 
                            consumed_energy = 56, 
                            current_watts = aind_slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            previous_consumed_energy = 56, 
                            last_collected = 56, ), 
                        external_sensors = aind_slurm_rest.models.v0/0/39_ext_sensors_data.v0.0.39_ext_sensors_data(), 
                        extra = '', 
                        power = aind_slurm_rest.models.v0/0/39_power_mgmt_data.v0.0.39_power_mgmt_data(), 
                        features = [
                            ''
                            ], 
                        active_features = [
                            ''
                            ], 
                        gres = '', 
                        gres_drained = '', 
                        gres_used = '', 
                        last_busy = 56, 
                        mcs_label = '', 
                        specialized_memory = 56, 
                        name = '', 
                        next_state_after_reboot = [
                            'INVALID'
                            ], 
                        address = '', 
                        hostname = '', 
                        state = [
                            'INVALID'
                            ], 
                        operating_system = '', 
                        owner = '', 
                        partitions = , 
                        port = 56, 
                        real_memory = 56, 
                        comment = '', 
                        reason = '', 
                        reason_changed_at = 56, 
                        reason_set_by_user = '', 
                        resume_after = aind_slurm_rest.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        reservation = '', 
                        alloc_memory = 56, 
                        alloc_cpus = 56, 
                        alloc_idle_cpus = 56, 
                        tres_used = '', 
                        tres_weighted = 1.337, 
                        slurmd_start_time = 56, 
                        sockets = 56, 
                        threads = 56, 
                        temporary_disk = 56, 
                        weight = 56, 
                        tres = '', 
                        version = '', )
                    ]
            )
        else:
            return V0039NodesResponse(
        )
        """

    def testV0039NodesResponse(self):
        """Test V0039NodesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
