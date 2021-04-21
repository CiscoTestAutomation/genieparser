expected_output = {
    "switch": {
        "mac_address": "aaaa.ddff.dddd",
        "mac_persistency_wait_time": "indefinite",
        "stack": {
            "1": {
                "role": "active",
                "state": "ready",
                "mac_address": "aaaa.ddff.dddd",
                "priority": "15",
                "hw_ver": "V02",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 2},
                    "2": {"stack_port_status": "ok", "neighbors_num": 3},
                },
            },
            "2": {
                "role": "standby",
                "state": "ready",
                "mac_address": "aaaa.ddff.dddd",
                "priority": "14",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 3},
                    "2": {"stack_port_status": "ok", "neighbors_num": 1},
                },
            },
            "3": {
                "role": "member",
                "state": "ready",
                "mac_address": "aaaa.ddff.dddd",
                "priority": "13",
                "hw_ver": "V02",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 1},
                    "2": {"stack_port_status": "ok", "neighbors_num": 2},
                },
            },
        },
    }
}
