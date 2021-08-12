expected_output = {
    'GigabitEthernet0/0/0/1': {
        'address_family': {
            'ipv4': {
                'version': {
                    1: {
                        'groups': {
                            5: {
                                'active_ip_address': 'local',
                                'active_priority': 49,
                                'active_router': 'local',
                                'authentication': 'cisco123',
                                'group_number': 5,
                                'hsrp_router_state': 'active',
                                'preempt': True,
                                'primary_ipv4_address': {
                                    'address': '192.168.1.254'
                                },
                                'priority': 49,
                                'standby_ip_address': '192.168.1.5',
                                'standby_router': '192.168.1.5',
                                'standby_expire': '00:00:03',
                                'standby_state': 'active',
                                'statistics': {
                                    'last_coup_received': 'Never',
                                    'last_coup_sent': 'Never',
                                    'last_resign_received': 'Never',
                                    'last_resign_sent': 'Never',
                                    'last_state_change': '2d07h',
                                    'num_state_changes': 4
                                },
                                'timers': {
                                    'cfgd_hello_msec': 1000,
                                    'cfgd_hold_msec': 3000,
                                    'hello_msec': 1000,
                                    'hello_msec_flag': True,
                                    'hold_msec': 3000,
                                    'hold_msec_flag': True
                                },
                                'tracked_objects': {
                                    '1': {
                                        'object_name': '1',
                                        'priority_decrement': 20
                                    },
                                    'apple': {
                                        'object_name': 'apple',
                                        'priority_decrement': 55
                                    },
                                    'banana': {
                                        'object_name': 'banana',
                                        'priority_decrement': 6
                                    },
                                    'num_tracked_objects': 3,
                                    'num_tracked_objects_up': 1
                                },
                                'virtual_mac_address': '0000.0cff.b30c'
                            }
                        }
                    }
                }
            }
        },
        'delay': {
            'minimum_delay': 5, 
            'reload_delay': 10
        },
        'interface': 'GigabitEthernet0/0/0/1',
        'redirects_disable': False,
        'use_bia': False
    },
    'GigabitEthernet0/0/0/2': {
        'address_family': {
            'ipv4': {
                'version': {
                    1: {
                        'groups': {
                            8: {
                                'active_ip_address': '192.168.1.2',
                                'active_router': '192.168.1.2',
                                'active_expire': '00:00:02',
                                'authentication': 'cisco123',
                                'group_number': 8,
                                'hsrp_router_state': 'init',
                                'preempt': True,
                                'preempt_delay': 10,
                                'primary_ipv4_address': {
                                    'address': '192.168.2.254'
                                },
                                'priority': 115,
                                'standby_ip_address': 'unknown',
                                'standby_router': 'unknown',
                                'standby_state': 'stored',
                                'statistics': {
                                    'last_coup_received': 'Never',
                                    'last_coup_sent': 'Never',
                                    'last_resign_received': 'Never',
                                    'last_resign_sent': 'Never',
                                    'last_state_change': 'never',
                                    'num_state_changes': 0
                                },
                                'timers': {
                                    'hello_msec': 3000,
                                    'hello_msec_flag': True,
                                    'hold_msec': 10000,
                                    'hold_msec_flag': True
                                },
                                'virtual_mac_address': '0000.0cff.b30f'
                            }
                        }
                    }
                }
            }
        },
        'delay': {
            'minimum_delay': 5, 'reload_delay': 15
        },
        'interface': 'GigabitEthernet0/0/0/2',
        'redirects_disable': False,
        'use_bia': False
    }
}
