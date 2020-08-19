expected_output = {
    "mst_instances": {
        0: {
            "bridge_priority": 32768,
            "interfaces": {
                "GigabitEthernet1/0/23": {
                    "designated_regional_root_cost": 0,
                    "port_priority": 128,
                    "designated_root_priority": 32768,
                    "designated_bridge_port_id": "128.23",
                    "designated_bridge_priority": 32768,
                    "forward_delay": 0,
                    "port_id": "128.23",
                    "name": "GigabitEthernet1/0/23",
                    "designated_regional_root_priority": 32768,
                    "forward_transitions": 1,
                    "counters": {"bpdu_sent": 493, "bpdu_received": 0},
                    "designated_regional_root_address": "3820.56ff.e15b",
                    "status": "designated forwarding",
                    "designated_root_cost": 0,
                    "designated_bridge_address": "3820.56ff.e15b",
                    "designated_root_address": "3820.56ff.e15b",
                    "cost": 20000,
                    "message_expires": 0,
                }
            },
            "operational": {
                "max_age": 35,
                "tx_hold_count": 20,
                "hello_time": 10,
                "forward_delay": 30,
            },
            "sysid": 0,
            "root": "CIST",
            "bridge_address": "3820.56ff.e15b",
            "configured": {
                "max_age": 35,
                "forward_delay": 30,
                "hello_time": 10,
                "max_hops": 10,
            },
            "mst_id": 0,
            "vlan": "1-99,201-4094",
        },
        10: {
            "bridge_priority": 61450,
            "interfaces": {
                "GigabitEthernet1/0/23": {
                    "port_priority": 128,
                    "designated_root_priority": 61450,
                    "designated_bridge_port_id": "128.23",
                    "designated_bridge_priority": 61450,
                    "forward_delay": 0,
                    "port_id": "128.23",
                    "name": "GigabitEthernet1/0/23",
                    "forward_transitions": 1,
                    "counters": {"bpdu_sent": 493, "bpdu_received": 0},
                    "message_expires": 0,
                    "status": "designated forwarding",
                    "designated_root_cost": 0,
                    "designated_bridge_address": "3820.56ff.e15b",
                    "designated_root_address": "3820.56ff.e15b",
                    "cost": 20000,
                }
            },
            "sysid": 10,
            "root": "MST10",
            "bridge_address": "3820.56ff.e15b",
            "mst_id": 10,
            "vlan": "100-200",
        },
    }
}
