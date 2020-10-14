expected_output = {
    "interface": {
        "FastEthernet2/1/1.2": {
            "ethernet_vlan": {2: {"status": "up"}},
            "status": "up",
            "destination_address": {
                "10.2.2.2": {
                    "default_path": "active",
                    "imposed_label_stack": "{16}",
                    "next_hop": "point2point",
                    "output_interface": "Serial2/0/2",
                    "tunnel_label": "imp-null",
                    "vc_id": {"1002": {"vc_status": "up"}},
                    "preferred_path": "not configured",
                }
            },
            "last_status_change_time": "1d00h",
            "line_protocol_status": "up",
            "signaling_protocol": {
                "LDP": {
                    "peer_id": "10.2.2.2:0",
                    "remote_interface_description": "xconnect to PE2",
                    "group_id": {"local": "0", "remote": "0"},
                    "peer_state": "up",
                    "mtu": {"local": "1500", "remote": "1500"},
                    "mpls_vc_labels": {"local": "21", "remote": "16"},
                }
            },
            "create_time": "1d00h",
            "statistics": {
                "bytes": {"received": 4322368, "sent": 5040220},
                "packets": {"received": 3466, "sent": 12286},
                "packets_drop": {"received": 0, "sent": 0},
            },
            "sequencing": {"received": "disabled", "sent": "disabled"},
        }
    }
}
