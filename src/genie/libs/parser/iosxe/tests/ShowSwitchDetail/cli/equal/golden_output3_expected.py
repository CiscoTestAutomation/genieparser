expected_output = {
    "switch": {
        "mac_address": "aaaa.ddff.dddd",
        "stack": {
            "1": {
                "role": "master",
                "state": "ready",
                "mac_address": "aaaa.ddff.dddd",
                "priority": "15",
                "hw_ver": "4",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 2},
                    "2": {"stack_port_status": "ok", "neighbors_num": 5},
                },
            },
            "2": {
                "role": "member",
                "state": "ready",
                "mac_address": "aaaa.ddff.dddd",
                "priority": "1",
                "hw_ver": "4",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 3},
                    "2": {"stack_port_status": "ok", "neighbors_num": 1},
                },
            },
        },
    }
}
