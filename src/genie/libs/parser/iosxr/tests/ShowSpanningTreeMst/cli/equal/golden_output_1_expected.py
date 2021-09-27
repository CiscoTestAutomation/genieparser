

expected_output = {
        'mstp': {
            'test': {
                'mst_instances': {
                    '0': {
                        'mst_id': '0',
                        'vlan': '1-4094',
                        'cist_root_priority': 32768,
                        'cist_root_address': '0021.1bff.0e05',
                        'cist_root_cost': 2000,
                        'designated_root_priority': 32768,
                        'designated_root_address': 'd867.d9ff.e420',
                        'this_bridge_is': 'the root',
                        'root_cost': 0,
                        'root_max_age': 20,
                        'root_forward_delay': 15,
                        'bridge_priority': 32768,
                        'sys_id_ext': 0,
                        'bridge_address': 'd867.d9ff.e420',
                        'bridge_max_age': 20,
                        'bridge_forward_delay': 15,
                        'bridge_max_hops': 20,
                        'bridge_transmit_hold_count': 6,
                        'interfaces': {
                            'TenGigabitEthernet0/0/0/16': {
                                'name': 'TenGigabitEthernet0/0/0/16',
                                'cost': 2000,
                                'role': 'ROOT',
                                'port_priority': 128,
                                'port_num': 1,
                                'port_state': 'FWD',
                                'designated_bridge_priority': 32768,
                                'designated_bridge_address': '0021.1bff.0e05',
                                'designated_port_priority': 128,
                                'designated_port_num': 1,
                                },
                            'TenGigabitEthernet0/0/0/17': {
                                'name': 'TenGigabitEthernet0/0/0/17',
                                'cost': 2000,
                                'role': 'ALT',
                                'port_priority': 128,
                                'port_num': 2,
                                'port_state': 'BLK',
                                'designated_bridge_priority': 32768,
                                'designated_bridge_address': '0021.1bff.0e05',
                                'designated_port_priority': 128,
                                'designated_port_num': 2,
                                },
                            },
                        },
                    },
                },
            },
        }
