expected_output = {
    "mstp": {
        "mst_instances": {
            0: {
                "bridge": {
                    "hello_time": 7,
                    "priority": 32768,
                    "forward_delay": 15,
                    "address": "ecbd.1dff.5f89",
                    "max_age": 12,
                    "configured_bridge_priority": 32768,
                    "sys_id_ext": 0,
                },
                "interfaces": {
                    "GigabitEthernet1/0/5": {
                        "port_state": "forwarding",
                        "bound": "RSTP",
                        "port_num": 5,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 20000,
                        "role": "root",
                    },
                    "Port-channel14": {
                        "port_state": "broken",
                        "bound": "PVST",
                        "port_num": 2390,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 6660,
                        "role": "designated",
                    },
                    "Port-channel24": {
                        "port_state": "forwarding",
                        "bound": "PVST",
                        "port_num": 2400,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 6660,
                        "role": "designated",
                    },
                },
                "root": {
                    "hello_time": 10,
                    "priority": 32768,
                    "forward_delay": 30,
                    "max_age": 35,
                    "cost": 20000,
                    "address": "3820.56ff.e15b",
                    "interface": "GigabitEthernet1/0/5",
                    "port": 5,
                },
            },
            10: {
                "bridge": {
                    "hello_time": 7,
                    "priority": 61450,
                    "forward_delay": 15,
                    "address": "ecbd.1dff.5f89",
                    "max_age": 12,
                    "configured_bridge_priority": 61440,
                    "sys_id_ext": 10,
                },
                "interfaces": {
                    "GigabitEthernet1/0/5": {
                        "port_state": "forwarding",
                        "bound": "RSTP",
                        "port_num": 5,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 20000,
                        "role": "master ",
                    },
                    "Port-channel14": {
                        "port_state": "broken",
                        "bound": "PVST",
                        "port_num": 2390,
                        "port_priority": 128,
                        "type": "P2p",
                        "cost": 6660,
                        "role": "designated",
                    },
                },
                "root": {
                    "hello_time": 10,
                    "priority": 61450,
                    "forward_delay": 30,
                    "address": "ecbd.1dff.5f89",
                    "max_age": 35,
                },
            },
        }
    }
}
