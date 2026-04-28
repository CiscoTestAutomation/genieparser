expected_output = {
    "redundancy": {
        "4294967295": {
            "group": {
                "id": 4294967295,
                "id_hex": "0xFFFFFFFF"
            },
            "applications_connected": [
                "mLACP",
                "Pseudo-mLACP"
            ],
            "monitor_mode": "BFD",
            "members": {
                "88.1.1.2": {
                    "name": "Router",
                    "status": "CONNECTING",
                    "mlacp_state": "AUTO_CONNECT",
                    "pseudo_mlacp_state": "AUTO_CONNECT"
                }
            },
            "backbone_interfaces": {
                "TenGigabitEthernet0/0/2": {
                    "status": "UP",
                    "protocol": "IP"
                }
            },
            "icrm_fast_failure_detection": {
                "neighbor_table": {
                    "neighbors": {
                        "88.1.1.2": {
                            "status": "DOWN",
                            "type": "RW"
                        }
                    }
                }
            }
        }
    }
}