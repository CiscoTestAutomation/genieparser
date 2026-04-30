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
                    "status": "CONNECTED",
                    "bfd_neighbor": {
                        "interface": "TenGigabitEthernet0/0/1",
                        "next_hop_ip": "80.1.3.2",
                        "status": "UP"
                    },
                    "mlacp_state": "CONNECTED",
                    "pseudo_mlacp_state": "CONNECTED"
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
                            "status": "UP",
                            "type": "BFD",
                            "next_hop_ip": "80.1.3.2",
                            "interface": "TenGigabitEthernet0/0/1"
                        }
                    }
                }
            }
        }
    }
}