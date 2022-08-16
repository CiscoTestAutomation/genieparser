expected_output = {
    'GigabitEthernet0/0/0/3': {
        'address_family': {
            'ipv4': {
                'version': {
                    1: {
                        'groups': {
                            2: {
                                'active_ip_address': 'local',
                                'active_priority': 100,
                                'active_router': 'local',
                                'authentication': 'ciscov4',
                                'group_number': 2,
                                'hsrp_router_state': 'active',
                                'num_of_slaves': 1,
                                'preempt': True,
                                'primary_ipv4_address': {
                                    'address': '12.0.0.1',
                                },
                                'priority': 100,
                                'session_name': 's1',
                                'standby_ip_address': 'unknown',
                                'standby_router': 'unknown',
                                'standby_state': 'active',
                                'statistics': {
                                    'last_coup_received': 'Never',
                                    'last_coup_sent': 'Never',
                                    'last_resign_received': 'Never',
                                    'last_resign_sent': 'Never',
                                    'last_state_change': '13:36:27',
                                    'num_state_changes': 5,
                                },
                                'timers': {
                                    'cfgd_hello_msec': 1000,
                                    'cfgd_hold_msec': 2000,
                                    'hello_msec': 1000,
                                    'hello_msec_flag': True,
                                    'hold_msec': 2000,
                                    'hold_msec_flag': True,
                                },
                                'virtual_mac_address': '549f.c66e.9aa3',
                            },
                        },
                    },
                },
            },
        },
        'delay': {
            'minimum_delay': 1,
            'reload_delay': 5,
        },
        'interface': 'GigabitEthernet0/0/0/3',
        'redirects_disable': False,
        'use_bia': False,
    },
    'GigabitEthernet0/0/0/3.20': {
        'address_family': {
            'ipv4': {
                'version': {
                    1: {
                        'groups': {
                        },
                        'slave_groups': {
                            20: {
                                'follow': 's1',
                                'group_number': 20,
                                'hsrp_router_state': 'active',
                                'primary_ipv4_address': {
                                    'address': '19.0.0.1',
                                },
                                'priority': 100,
                                'standby_state': 'active',
                                'virtual_mac_address': '0000.0c07.ac14',
                            },
                        },
                    },
                },
            },
        },
        'interface': 'GigabitEthernet0/0/0/3.20',
        'use_bia': False,
    },
}

