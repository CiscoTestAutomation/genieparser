expected_output = {
    "mstp": {
        "mst_instances": {
            3: {
                "root": {
                    "max_age": 20,
                    "interface": "GigabitEthernet3/8",
                    "forward_delay": 15,
                    "priority": 32771,
                    "cost": 20000,
                    "port": 136,
                    "address": "0050.14ff.1cbb",
                    "hello_time": 2,
                },
                "bridge": {
                    "max_age": 20,
                    "priority": 32771,
                    "forward_delay": 15,
                    "configured_bridge_priority": 32768,
                    "sys_id_ext": 3,
                    "address": "00d0.00ff.c73f",
                    "hello_time": 2,
                },
                "interfaces": {
                    "GigabitEthernet3/8": {
                        "port_num": 136,
                        "role": "root",
                        "port_state": "forwarding",
                        "type": "P2p",
                        "port_priority": 128,
                        "cost": 20000,
                    },
                    "Port-channel1": {
                        "port_num": 833,
                        "role": "designated",
                        "port_state": "forwarding",
                        "type": "P2p",
                        "port_priority": 128,
                        "cost": 20000,
                    },
                },
            }
        }
    }
}
