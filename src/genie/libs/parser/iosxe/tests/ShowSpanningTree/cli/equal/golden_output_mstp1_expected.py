expected_output = {
    'mstp': {
        'mst_instances': {
            1: {
                'bridge': {
                    'address': 'cc7f.763d.9a00',
                    'configured_bridge_priority': 32768,
                    'priority': 32769,
                },
                'interfaces': {
                    'TwoGigabitEthernet1/0/2': {
                        'cost': 20000,
                        'port_num': 2,
                        'port_priority': 128,
                        'port_state': 'blocking',
                        'role': 'alternate',
                        'type': 'P2p',
                    },
                    'TwoGigabitEthernet1/0/23': {
                        'cost': 20000,
                        'port_num': 23,
                        'port_priority': 128,
                        'port_state': 'forwarding',
                        'role': 'root',
                        'type': 'P2p',
                    },
                },
                'root': {
                    'address': '40b5.c11e.e000',
                    'configured_bridge_priority': 4096,
                    'cost': 20000,
                    'interface': 'TwoGigabitEthernet1/0/23',
                    'priority': 4097,
                    'rem_hops': 19,
                },
                'vlans_mapped': '2-25',
            },
        },
    },
}
