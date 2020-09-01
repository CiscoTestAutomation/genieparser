expected_output = {
    "interface": {
        "VFIPE1-VPLS-A": {
            "signaling_protocol": {
                "LDP": {
                    "mtu": {"remote": "1500", "local": "1500"},
                    "group_id": {"remote": "0", "local": "0"},
                    "peer_id": "10.2.2.2:0",
                    "peer_state": "up",
                    "mpls_vc_labels": {"remote": "18", "local": "18"},
                }
            },
            "last_status_change_time": "1d03h",
            "status": "up",
            "destination_address": {
                "10.2.2.2": {
                    "imposed_label_stack": "{18}",
                    "output_interface": "Serial2/0",
                    "next_hop": "point2point",
                    "vc_id": {"100": {"vc_status": "up"}},
                    "tunnel_label": "imp-null",
                }
            },
            "statistics": {
                "packets_drop": {"received": 0, "sent": 0},
                "packets": {"received": 0, "sent": 0},
                "bytes": {"received": 0, "sent": 0},
            },
            "sequencing": {"received": "disabled", "sent": "disabled"},
            "create_time": "3d15h",
        }
    }
}
