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
                    "status": "CONNECTED",
                    "bfd_neighbor": {
                        "interface": "GigabitEthernet0/0/3",
                        "next_hop_ip": "90.1.3.2",
                        "status": "UP"
                    },
                    "mlacp_state": "CONNECTED",
                    "pseudo_mlacp_state": "CONNECTED"
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
                            "status": "UP",
                            "type": "BFD",
                            "next_hop_ip": "90.1.3.2",
                            "interface": "GigabitEthernet0/0/3"
                        }
                    }
                }
            }
        }
    }
}