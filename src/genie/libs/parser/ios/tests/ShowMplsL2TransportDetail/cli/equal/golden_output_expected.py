expected_output = {
    "interface": {
        "VFI TEST VFI": {
            "status": "up",
            "destination_address": {
                "10.1.1.1": {
                    "vc_id": {"1000": {"vc_status": "up"}},
                    "output_interface": "Serial2/0",
                    "imposed_label_stack": "{17}",
                    "preferred_path": "not configured",
                    "default_path": "active",
                    "next_hop": "point2point",
                }
            },
            "create_time": "00:04:34",
            "last_status_change_time": "00:04:15",
            "signaling_protocol": {
                "LDP": {
                    "peer_id": "10.1.1.1:0",
                    "peer_state": "up",
                    "targeted_hello_ip": "10.1.1.1",
                    "id": "10.1.1.1",
                    "mpls_vc_labels": {"local": "16", "remote": "17"},
                    "group_id": {"local": "0", "remote": "0"},
                    "mtu": {"local": "1500", "remote": "1500"},
                    "mac_withdraw": {"sent": 5, "received": 3},
                }
            },
            "sequencing": {"received": "disabled", "sent": "disabled"},
            "statistics": {
                "packets": {"received": 0, "sent": 0},
                "bytes": {"received": 0, "sent": 0},
                "packets_drop": {"received": 0, "sent": 0},
            },
        }
    }
}
