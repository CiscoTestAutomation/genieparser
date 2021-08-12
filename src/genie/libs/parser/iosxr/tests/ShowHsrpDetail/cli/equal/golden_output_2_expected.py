expected_output = {
    'GigabitEthernet0/0/0/2': {
        'address_family': {
            'ipv4': {
                'version': {
                    1: {
                        'groups': {
                            0: {
                                'active_ip_address': 'local',
                                'active_priority': 110,
                                'active_router': 'local',
                                'authentication': 'cisco123',
                                'group_number': 0,
                                'hsrp_router_state': 'active',
                                'preempt': True,
                                'primary_ipv4_address': {
                                    'address': '192.168.1.254'
                                },
                                'priority': 110,
                                'standby_expire': '00:00:02',
                                'standby_ip_address': '192.168.1.2',
                                'standby_router': '192.168.1.2',
                                'standby_state': 'active',
                                'statistics': {
                                    'last_coup_received': 'Never',
                                    'last_coup_sent': 'Aug '
                                    '11 '
                                    '08:26:25.272 '
                                    'UTC',
                                    'last_resign_received': 'Aug '
                                    '11 '
                                    '08:26:25.272 '
                                    'UTC',
                                    'last_resign_sent': 'Never',
                                    'last_state_change': '01:18:43',
                                    'num_state_changes': 2
                                },
                                'timers': {
                                    'cfgd_hello_msec': 1000,
                                    'cfgd_hold_msec': 3000,
                                    'hello_msec': 1000,
                                    'hello_msec_flag': True,
                                    'hold_msec': 3000,
                                    'hold_msec_flag': True
                                },
                                'virtual_mac_address': '0000.0cff.b307'
                            }
                        }
                    }
                }
            },
            'ipv6': {
                'version': {
                    2: {
                        'groups': {
                            1: {
                                'active_ip_address': 'local',
                                'active_priority': 120,
                                'active_router': 'local',
                                'group_number': 1,
                                'hsrp_router_state': 'active',
                                'link_local_ipv6_address': {
                                    'address': 'fe80::205:73ff:feff:a0a1'
                                },
                                'preempt': True,
                                'priority': 120,
                                'standby_expire': '00:00:02',
                                'standby_ipv6_address': 'fe80::5000:1cff:feff:a0b, '
                                '5200.1cff.0a0b',
                                'standby_router': 'fe80::5000:1cff:feff:a0b, '
                                '5200.1cff.0a0b',
                                'standby_state': 'active',
                                'statistics': {
                                    'last_coup_received': 'Never',
                                    'last_coup_sent': 'Aug '
                                    '11 '
                                    '09:28:07.334 '
                                    'UTC',
                                    'last_resign_received': 'Aug '
                                    '11 '
                                    '09:28:07.334 '
                                    'UTC',
                                    'last_resign_sent': 'Never',
                                    'last_state_change': '00:17:01',
                                    'num_state_changes': 2
                                },
                                'timers': {
                                    'cfgd_hello_msec': 1000,
                                    'cfgd_hold_msec': 3000,
                                    'hello_msec': 1000,
                                    'hello_msec_flag': True,
                                    'hold_msec': 3000,
                                    'hold_msec_flag': True
                                },
                                'virtual_mac_address': '0005.73ff.a0a1'
                            }
                        }
                    }
                }
            }
        },
        'delay': {
            'minimum_delay': 5, 'reload_delay': 10
        },
        'interface': 'GigabitEthernet0/0/0/2',
        'redirects_disable': False,
        'use_bia': False
    }
}