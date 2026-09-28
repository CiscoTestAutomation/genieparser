expected_output = {
    'pvst': {
        'vlans': {
            100: {
                'bridge': {
                    'address': '8061.320b.7d61',
                    'aging_time': 30,
                    'configured_bridge_priority': 32768,
                    'forward_delay': 15,
                    'hello_time': 2,
                    'max_age': 20,
                    'priority': 32868,
                    'sys_id_ext': 100,
                },
                'interfaces': {
                    'TenGigabitEthernet0/0/18': {
                        'cost': 2,
                        'port_num': 32,
                        'port_priority': 128,
                        'port_state': 'learning',
                        'role': 'root',
                        'type': 'P2p',
                    },
                    'TenGigabitEthernet0/0/19': {
                        'cost': 2,
                        'port_num': 33,
                        'port_priority': 128,
                        'port_state': 'blocking',
                        'role': 'alternate',
                        'type': 'P2p',
                    },
                },
                'root': {
                    'address': '14bc.68c3.d261',
                    'cost': 2,
                    'forward_delay': 15,
                    'hello_time': 2,
                    'interface': 'TenGigabitEthernet0/0/18',
                    'max_age': 20,
                    'port': 32,
                    'priority': 32868,
                },
            },
            200: {
                'bridge': {
                    'address': '8061.320b.7d61',
                    'aging_time': 30,
                    'configured_bridge_priority': 32768,
                    'forward_delay': 15,
                    'hello_time': 2,
                    'max_age': 20,
                    'priority': 32968,
                    'sys_id_ext': 200,
                },
                'interfaces': {
                    'TenGigabitEthernet0/0/19': {
                        'cost': 2,
                        'port_num': 33,
                        'port_priority': 128,
                        'port_state': 'learning',
                        'role': 'root',
                        'type': 'P2p',
                    },
                },
                'root': {
                    'address': '14bc.68c3.d261',
                    'cost': 2,
                    'forward_delay': 15,
                    'hello_time': 2,
                    'interface': 'TenGigabitEthernet0/0/19',
                    'max_age': 20,
                    'port': 33,
                    'priority': 32968,
                },
            },
        },
    },
}