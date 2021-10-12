

expected_output = {
    'Ethernet4/1':
        {'address_family':
            {'ipv4':
                {'version':
                    {2:
                        {'groups':
                            {0:
                                {'active_router': 'unknown',
                                'authentication': 'cisco123',
                                'configured_priority': 110,
                                'group_number': 0,
                                'hsrp_router_state': 'initial',
                                'hsrp_router_state_reason': 'interface down',
                                'last_state_change': 'never',
                                'lower_fwd_threshold': 1,
                                'num_state_changes': 0,
                                'preempt': True,
                                'primary_ipv4_address':
                                    {'address': '192.168.1.254',
                                    'virtual_ip_learn': False},
                                'priority': 110,
                                'session_name': 'hsrp-Eth4/1-0',
                                'standby_router': 'unknown',
                                'timers':
                                    {'hello_msec_flag': False,
                                    'hello_sec': 1,
                                    'hold_msec_flag': False,
                                    'hold_sec': 3},
                                'upper_fwd_threshold': 110,
                                'virtual_mac_address': '0000.0cff.909f',
                                'virtual_mac_address_status': 'default'},
                            },
                        },
                    },
                },
            },
        'interface': 'Ethernet4/1',
        'use_bia': False},
    }
