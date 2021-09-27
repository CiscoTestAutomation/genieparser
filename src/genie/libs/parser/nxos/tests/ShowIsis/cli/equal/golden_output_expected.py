

expected_output = {
    'instance': {
        'test': {
            'isis_process': 'test',
            'instance_number': 1,
            'uuid': '1090519320',
            'process_id': 1581,
            'vrf': {
                'default': {
                    'vrf': 'default',
                    'system_id': '3333.33ff.6666',
                    'is_type': 'L1-L2',
                    'sap': 412,
                    'queue_handle': 15,
                    'maximum_lsp_mtu': 1492,
                    'stateful_ha': 'enabled',
                    'graceful_restart': {
                        'enable': True,
                        'state': 'Inactive',
                        'last_gr_status': 'none',
                    },
                    'start_mode': 'Complete',
                    'bfd_ipv4': 'globally disabled',
                    'bfd_ipv6': 'globally disabled',
                    'topology_mode': 'Multitopology',
                    'metric_type': {
                        'advertise': ['wide'],
                        'accept': ['narrow', 'wide'],
                    },
                    'area_address': ['49.0001'],
                    'process': 'up and running',
                    'vrf_id': 1,
                    'during_non_graceful_controlled_restart': 'Stale routes',
                    'resolution_of_l3_to_l2': 'Enable',
                    'sr_ipv4': 'not configured and disabled',
                    'sr_ipv6': 'not configured and disabled',
                    'supported_interfaces': ['Loopback0', 'Ethernet1/1.115', 'Ethernet1/2.115'],
                    'topology': {
                        0: {
                            'address_family': {
                                'ipv4_unicast': {
                                    'number_of_interface': 3,
                                    'distance': 115,
                                },
                                'ipv6_unicast': {
                                    'number_of_interface': 0,
                                    'distance': 115,
                                },
                            },
                        },
                        2: {
                            'address_family': {
                                'ipv6_unicast': {
                                    'number_of_interface': 3,
                                    'distance': 115,
                                },
                            },
                        },
                    },
                    'authentication': {
                        'level_1': {
                            'auth_check': 'set',
                        },
                        'level_2': {
                            'auth_check': 'set',
                        },
                    },
                    'l1_next_spf': '00:00:07',
                    'l2_next_spf': '00:00:04',
                },
                'VRF1': {
                    'vrf': 'VRF1',
                    'system_id': '3333.33ff.6666',
                    'is_type': 'L1-L2',
                    'sap': 412,
                    'queue_handle': 15,
                    'maximum_lsp_mtu': 1492,
                    'stateful_ha': 'enabled',
                    'graceful_restart': {
                        'enable': True,
                        'state': 'Inactive',
                        'last_gr_status': 'none',
                    },
                    'start_mode': 'Complete',
                    'bfd_ipv4': 'globally disabled',
                    'bfd_ipv6': 'globally disabled',
                    'topology_mode': 'Multitopology',
                    'metric_type': {
                        'advertise': ['wide'],
                        'accept': ['narrow', 'wide'],
                    },
                    'area_address': ['49.0001'],
                    'process': 'up and running',
                    'vrf_id': 3,
                    'during_non_graceful_controlled_restart': 'Stale routes',
                    'resolution_of_l3_to_l2': 'Enable',
                    'sr_ipv4': 'not configured and disabled',
                    'sr_ipv6': 'not configured and disabled',
                    'supported_interfaces': ['Loopback300', 'Ethernet1/1.415', 'Ethernet1/2.415'],
                    'topology': {
                        0: {
                            'address_family': {
                                'ipv4_unicast': {
                                    'number_of_interface': 3,
                                    'distance': 115,
                                },
                                'ipv6_unicast': {
                                    'number_of_interface': 0,
                                    'distance': 115,
                                },
                            },
                        },
                        2: {
                            'address_family': {
                                'ipv6_unicast': {
                                    'number_of_interface': 3,
                                    'distance': 115,
                                },
                            },
                        },
                    },
                    'authentication': {
                        'level_1': {
                            'auth_check': 'set',
                        },
                        'level_2': {
                            'auth_check': 'set',
                        },
                    },
                    'l1_next_spf': 'Inactive',
                    'l2_next_spf': 'Inactive',
                },
            },
        },
    },
}
