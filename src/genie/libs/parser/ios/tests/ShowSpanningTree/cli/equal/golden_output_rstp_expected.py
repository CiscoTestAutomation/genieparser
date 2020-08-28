expected_output = {
    "rapid_pvst": {
        "vlans": {
            200: {
                "bridge": {
                    "hello_time": 2,
                    "priority": 28872,
                    "forward_delay": 15,
                    "max_age": 20,
                    "aging_time": 300,
                    "address": "ecbd.1dff.5f89",
                    "configured_bridge_priority": 28672,
                    "sys_id_ext": 200,
                },
                "interfaces": {
                    "GigabitEthernet1/0/5": {
                        "peer": "STP",
                        "port_state": "forwarding",
                        "port_num": 5,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 4,
                        "role": "designated",
                    },
                    "Port-channel14": {
                        "port_state": "forwarding",
                        "port_num": 2390,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 3,
                        "role": "root",
                    },
                },
                "root": {
                    "hello_time": 2,
                    "priority": 24776,
                    "forward_delay": 15,
                    "max_age": 20,
                    "cost": 3,
                    "address": "58bf.eaff.e5b6",
                    "interface": "Port-channel14",
                    "port": 2390,
                },
            },
            201: {
                "bridge": {
                    "hello_time": 2,
                    "priority": 28873,
                    "forward_delay": 15,
                    "max_age": 20,
                    "aging_time": 300,
                    "address": "ecbd.1dff.5f89",
                    "configured_bridge_priority": 28672,
                    "sys_id_ext": 201,
                },
                "interfaces": {
                    "GigabitEthernet1/0/5": {
                        "peer": "STP",
                        "port_state": "forwarding",
                        "port_num": 5,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 4,
                        "role": "designated",
                    },
                    "Port-channel14": {
                        "port_state": "forwarding",
                        "port_num": 2390,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 3,
                        "role": "root",
                    },
                },
                "root": {
                    "hello_time": 2,
                    "priority": 24777,
                    "forward_delay": 15,
                    "max_age": 20,
                    "cost": 3,
                    "address": "58bf.eaff.e5b6",
                    "interface": "Port-channel14",
                    "port": 2390,
                },
            },
        }
    }
}
