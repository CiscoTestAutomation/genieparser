expected_output = {
    "redundancy": {
        "100": {
            "group": {
                "id": 100,
                "id_hex": "0x64"
            },
            "applications_connected": [
                "mLACP",
                "Pseudo-mLACP"
            ],
            "monitor_mode": "BFD",
            "members": {
                "99.1.1.2": {
                    "name": "Router",
                    "status": "CONNECTING",
                    "mlacp_state": "AUTO_CONNECT",
                    "pseudo_mlacp_state": "AUTO_CONNECT"
                }
            },
            "backbone_interfaces": {
                "GigabitEthernet0/0/4": {
                    "status": "UP",
                    "protocol": "IP"
                }
            },
            "icrm_fast_failure_detection": {
                "neighbor_table": {
                    "neighbors": {
                        "99.1.1.2": {
                            "status": "DOWN",
                            "type": "RW"
                        }
                    }
                }
            }
        }
    }
}