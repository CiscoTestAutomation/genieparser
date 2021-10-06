

expected_output = {
    'Ethernet1/3':
        {'address_family':
            {'ipv4':
                {'version':
                    {2:
                        {'groups':
                            {0:
                                {'active_priority': 110,
                                'active_router': 'local',
                                'authentication': 'cisco123',
                                'configured_priority': 110,
                                'group_number': 0,
                                'hsrp_router_state': 'active',
                                'last_state_change': '00:01:43',
                                'lower_fwd_threshold': 0,
                                'num_state_changes': 10,
                                'preempt': True,
                                'primary_ipv4_address':
                                    {'address': '192.168.1.254',
                                    'virtual_ip_learn': False},
                                'priority': 110,
                                'session_name': 'hsrp-Eth1/3-0',
                                'standby_expire': 2.429,
                                'standby_ip_address': '192.168.1.2',
                                'standby_priority': 90,
                                'standby_router': '192.168.1.2',
                                'timers': {
                                    'hello_msec_flag': False,
                                    'hello_sec': 1,
                                    'hold_msec_flag': False,
                                    'hold_sec': 3},
                                'tracked_objects':
                                    {1:
                                        {'object_name': 1,
                                        'priority_decrement': 22,
                                        'status': 'UP'},
                                    },
                                'upper_fwd_threshold': 110,
                                'virtual_mac_address': '0000.0cff.909f',
                                'virtual_mac_address_status': 'default'
                                },
                            2:
                                {'active_router': 'unknown',
                                'authentication': 'cisco',
                                'configured_priority': 1,
                                'group_number': 2,
                                'hsrp_router_state': 'disabled',
                                'hsrp_router_state_reason': 'virtual ip not cfged',
                                'last_state_change': 'never',
                                'lower_fwd_threshold': 0,
                                'num_state_changes': 0,
                                'priority': 1,
                                'session_name': 'hsrp-Eth1/3-2',
                                'standby_router': 'unknown',
                                'timers':
                                    {'hello_msec_flag': False,
                                    'hello_sec': 3,
                                    'hold_msec_flag': False,
                                    'hold_sec': 10},
                                'upper_fwd_threshold': 1,
                                'virtual_mac_address': '0000.0cff.90a1',
                                'virtual_mac_address_status': 'default'},
                            },
                        },
                    },
                },
            'ipv6':
                {'version':
                    {2:
                        {'groups':
                            {2:
                                {'active_priority': 100,
                                'active_router': 'local',
                                'authentication': 'cisco',
                                'configured_priority': 100,
                                'global_ipv6_addresses':
                                    {'2001:db8:7746:fa41::1':
                                        {'address': '2001:db8:7746:fa41::1'
                                  }
                                },
                                'group_number': 2,
                                'hsrp_router_state': 'active',
                                'last_state_change': '02:43:40',
                                'link_local_ipv6_address':
                                    {'address': 'fe80::5:73ff:feff:a0a2',
                                    'auto_configure': True},
                                'lower_fwd_threshold': 0,
                                'num_state_changes': 2,
                                'priority': 100,
                                'secondary_vips': ['2001:db8:7746:fa41::1'],
                                'session_name': 'hsrp-Eth1/3-2-V6',
                                'standby_expire': 8.96,
                                'standby_ipv6_address': 'fe80::20c:29ff:fe69:14bb',
                                'standby_priority': 90,
                                'standby_router': 'fe80::20c:29ff:fe69:14bb',
                                'timers':
                                    {'hello_msec_flag': False,
                                    'hello_sec': 3,
                                    'hold_msec_flag': False,
                                    'hold_sec': 10},
                                'upper_fwd_threshold': 100,
                                'virtual_mac_address': '0005.73ff.a0a2',
                                'virtual_mac_address_status': 'default'},
                            },
                        },
                    },
                },
            },
        'interface': 'Ethernet1/3',
        'use_bia': False},
        }
