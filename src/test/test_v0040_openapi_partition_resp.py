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

from aind_slurm_rest.models.v0040_openapi_partition_resp import V0040OpenapiPartitionResp

class TestV0040OpenapiPartitionResp(unittest.TestCase):
    """V0040OpenapiPartitionResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiPartitionResp:
        """Test V0040OpenapiPartitionResp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiPartitionResp`
        """
        model = V0040OpenapiPartitionResp()
        if include_optional:
            return V0040OpenapiPartitionResp(
                partitions = [
                    aind_slurm_rest.models.v0/0/40_partition_info.v0.0.40_partition_info(
                        nodes = aind_slurm_rest.models.v0_0_40_partition_info_nodes.v0_0_40_partition_info_nodes(
                            allowed_allocation = '', 
                            configured = '', 
                            total = 56, ), 
                        accounts = aind_slurm_rest.models.v0_0_40_partition_info_accounts.v0_0_40_partition_info_accounts(
                            allowed = '', 
                            deny = '', ), 
                        groups = aind_slurm_rest.models.v0_0_40_partition_info_groups.v0_0_40_partition_info_groups(
                            allowed = '', ), 
                        qos = aind_slurm_rest.models.v0_0_40_partition_info_qos.v0_0_40_partition_info_qos(
                            allowed = '', 
                            deny = '', 
                            assigned = '', ), 
                        alternate = '', 
                        tres = aind_slurm_rest.models.v0_0_40_partition_info_tres.v0_0_40_partition_info_tres(
                            billing_weights = '', 
                            configured = '', ), 
                        cluster = '', 
                        cpus = aind_slurm_rest.models.v0_0_40_partition_info_cpus.v0_0_40_partition_info_cpus(
                            task_binding = 56, 
                            total = 56, ), 
                        defaults = aind_slurm_rest.models.v0_0_40_partition_info_defaults.v0_0_40_partition_info_defaults(
                            memory_per_cpu = 56, 
                            partition_memory_per_cpu = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            partition_memory_per_node = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            time = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            job = '', ), 
                        grace_time = 56, 
                        maximums = aind_slurm_rest.models.v0_0_40_partition_info_maximums.v0_0_40_partition_info_maximums(
                            cpus_per_node = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            cpus_per_socket = , 
                            memory_per_cpu = 56, 
                            shares = 56, 
                            oversubscribe = aind_slurm_rest.models.v0_0_40_partition_info_maximums_oversubscribe.v0_0_40_partition_info_maximums_oversubscribe(
                                jobs = 56, 
                                flags = [
                                    'force'
                                    ], ), 
                            over_time_limit = aind_slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        minimums = aind_slurm_rest.models.v0_0_40_partition_info_minimums.v0_0_40_partition_info_minimums(), 
                        name = '', 
                        node_sets = '', 
                        priority = aind_slurm_rest.models.v0_0_40_partition_info_priority.v0_0_40_partition_info_priority(
                            job_factor = 56, 
                            tier = 56, ), 
                        timeouts = aind_slurm_rest.models.v0_0_40_partition_info_timeouts.v0_0_40_partition_info_timeouts(
                            resume = aind_slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspend = , ), 
                        partition = aind_slurm_rest.models.v0_0_40_partition_info_partition.v0_0_40_partition_info_partition(
                            state = [
                                'INACTIVE'
                                ], ), 
                        suspend_time = , )
                    ],
                last_update = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                meta = aind_slurm_rest.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_plugin.slurm_v0041_get_shares_200_response_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_client.slurm_v0041_get_shares_200_response_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_slurm.slurm_v0041_get_shares_200_response_meta_slurm(
                        version = aind_slurm_rest.models.slurm_v0041_get_shares_200_response_meta_slurm_version.slurm_v0041_get_shares_200_response_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    aind_slurm_rest.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    aind_slurm_rest.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiPartitionResp(
                partitions = [
                    aind_slurm_rest.models.v0/0/40_partition_info.v0.0.40_partition_info(
                        nodes = aind_slurm_rest.models.v0_0_40_partition_info_nodes.v0_0_40_partition_info_nodes(
                            allowed_allocation = '', 
                            configured = '', 
                            total = 56, ), 
                        accounts = aind_slurm_rest.models.v0_0_40_partition_info_accounts.v0_0_40_partition_info_accounts(
                            allowed = '', 
                            deny = '', ), 
                        groups = aind_slurm_rest.models.v0_0_40_partition_info_groups.v0_0_40_partition_info_groups(
                            allowed = '', ), 
                        qos = aind_slurm_rest.models.v0_0_40_partition_info_qos.v0_0_40_partition_info_qos(
                            allowed = '', 
                            deny = '', 
                            assigned = '', ), 
                        alternate = '', 
                        tres = aind_slurm_rest.models.v0_0_40_partition_info_tres.v0_0_40_partition_info_tres(
                            billing_weights = '', 
                            configured = '', ), 
                        cluster = '', 
                        cpus = aind_slurm_rest.models.v0_0_40_partition_info_cpus.v0_0_40_partition_info_cpus(
                            task_binding = 56, 
                            total = 56, ), 
                        defaults = aind_slurm_rest.models.v0_0_40_partition_info_defaults.v0_0_40_partition_info_defaults(
                            memory_per_cpu = 56, 
                            partition_memory_per_cpu = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            partition_memory_per_node = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            time = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            job = '', ), 
                        grace_time = 56, 
                        maximums = aind_slurm_rest.models.v0_0_40_partition_info_maximums.v0_0_40_partition_info_maximums(
                            cpus_per_node = aind_slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            cpus_per_socket = , 
                            memory_per_cpu = 56, 
                            shares = 56, 
                            oversubscribe = aind_slurm_rest.models.v0_0_40_partition_info_maximums_oversubscribe.v0_0_40_partition_info_maximums_oversubscribe(
                                jobs = 56, 
                                flags = [
                                    'force'
                                    ], ), 
                            over_time_limit = aind_slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        minimums = aind_slurm_rest.models.v0_0_40_partition_info_minimums.v0_0_40_partition_info_minimums(), 
                        name = '', 
                        node_sets = '', 
                        priority = aind_slurm_rest.models.v0_0_40_partition_info_priority.v0_0_40_partition_info_priority(
                            job_factor = 56, 
                            tier = 56, ), 
                        timeouts = aind_slurm_rest.models.v0_0_40_partition_info_timeouts.v0_0_40_partition_info_timeouts(
                            resume = aind_slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspend = , ), 
                        partition = aind_slurm_rest.models.v0_0_40_partition_info_partition.v0_0_40_partition_info_partition(
                            state = [
                                'INACTIVE'
                                ], ), 
                        suspend_time = , )
                    ],
                last_update = aind_slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
        )
        """

    def testV0040OpenapiPartitionResp(self):
        """Test V0040OpenapiPartitionResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
