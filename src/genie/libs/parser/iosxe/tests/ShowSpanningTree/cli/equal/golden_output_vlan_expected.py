expected_output = {
    'rapid_pvst': {
        'vlans': {
            10: {
                'bridge': {
                    'address': '00a5.bf53.d400',
                    'aging_time': 300,
                    'configured_bridge_priority': 32768,
                    'forward_delay': 15,
                    'hello_time': 2,
                    'max_age': 20,
                    'priority': 32778,
                    'sys_id_ext': 10,
                },
                'interfaces': {
                    'GigabitEthernet1/0/4': {
                        'cost': 20000,
                        'port_num': 4,
                        'port_priority': 128,
                        'port_state': 'forwarding',
                        'role': 'designated',
                        'type': 'P2p Edge',
                    },
                    'Port-channel1': {
                        'cost': 10000,
                        'port_num': 3049,
                        'port_priority': 128,
                        'port_state': 'forwarding',
                        'role': 'designated',
                        'type': 'P2p',
                    },
                },
                'root': {
                    'address': '00a5.bf53.d400',
                    'forward_delay': 15,
                    'hello_time': 2,
                    'max_age': 20,
                    'priority': 32778,
                },
            },
        },
    },
}