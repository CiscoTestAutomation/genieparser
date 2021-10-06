

expected_output = {
    'instance': {
        'Cisco': {
            'process_id': 'Cisco',
            'instance': '0',
            'vrf': {
                'default': {
                    'system_id': '1781.81ff.43c7',
                    'is_levels': 'level-2-only',
                    'manual_area_address': ['49.0000'],
                    'routing_area_address': ['49.0000'],
                    'non_stop_forwarding': 'Disabled',
                    'most_recent_startup_mode': 'Cold Restart',
                    'te_connection_status': 'Up',
                    'topology': {
                        'IPv4 Unicast': {
                            'vrf': {
                                'default': {
                                    'level': {
                                        2: {
                                            'generate_style': 'Wide',
                                            'accept_style': 'Wide',
                                            'metric': 100000,
                                            'ispf_status': 'Disabled',
                                        },
                                    },
                                    'protocols_redistributed': True,
                                    'redistributing': ['Connected', 'Static', 'OSPF process 65001', 'OSPF process 65002', 'OSPF process 65003'],
                                    'distance': 115,
                                    'adv_passive_only': True,
                                },
                            },
                        },
                    },
                    'srlb': {
                        'start': 15000,
                        'end': 15999,
                    },
                    'srgb': {
                        'start': 16000,
                        'end': 81534,
                    },
                    'interfaces': {
                        'Bundle-Ether1': {
                            'running_state': 'running suppressed',
                            'configuration_state': 'active in configuration',
                        },
                        'Bundle-Ether2': {
                            'running_state': 'running suppressed',
                            'configuration_state': 'active in configuration',
                        },
                        'Loopback0': {
                            'running_state': 'running passively',
                            'configuration_state': 'passive in configuration',
                        },
                        'TenGigE0/0/1/2': {
                            'running_state': 'running suppressed',
                            'configuration_state': 'active in configuration',
                        },
                        'TenGigE0/0/1/3': {
                            'running_state': 'disabled',
                            'configuration_state': 'active in configuration',
                        },
                        'TenGigE0/5/0/1': {
                            'running_state': 'disabled',
                            'configuration_state': 'active in configuration',
                        },
                    },
                },
            },
        },
    },
}
