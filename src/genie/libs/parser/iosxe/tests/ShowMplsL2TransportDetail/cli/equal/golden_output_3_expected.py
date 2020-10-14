expected_output = {
    "interface": {
        "GigabitEthernet3": {
            "state": "up",
            "line_protocol_status": "up",
            "protocol_status": {"Ethernet": "up"},
            "destination_address": {
                "10.4.1.1": {
                    "vc_id": {"888": {"vc_status": "up"}},
                    "output_interface": "GigabitEthernet2",
                    "imposed_label_stack": "{32}",
                    "preferred_path": "not configured",
                    "default_path": "active",
                    "next_hop": "10.1.2.1",
                }
            },
            "create_time": "00:00:22",
            "last_status_change_time": "00:00:10",
            "last_label_fsm_state_change_time": "00:00:10",
            "signaling_protocol": {
                "LDP": {
                    "peer_id": "10.4.1.1:0",
                    "peer_state": "up",
                    "targeted_hello_ip": "10.16.2.2",
                    "id": "10.4.1.1",
                    "status": "UP",
                    "mpls_vc_labels": {"local": "17", "remote": "32"},
                    "group_id": {"local": "n/a", "remote": "0"},
                    "mtu": {"local": "1500", "remote": "1500"},
                }
            },
            "graceful_restart": "not configured and not enabled",
            "non_stop_routing": "not configured and not enabled",
            "status_tlv_support": "enabled/supported",
            "ldp_route_enabled": "enabled",
            "label_state_machine": "established, LruRru",
            "last_status_name": {
                "local_dataplane": {"received": "No fault"},
                "bfd_dataplane": {"received": "Not sent"},
                "bfd_peer_monitor": {"received": "No fault"},
                "local_ac__circuit": {"received": "No fault", "sent": "No fault"},
                "local_pw_if_circ": {"received": "No fault"},
                "local_ldp_tlv": {"sent": "No fault"},
                "remote_ldp_tlv": {"received": "No fault"},
                "remote_ldp_adj": {"received": "No fault"},
            },
            "sequencing": {"received": "disabled", "sent": "disabled"},
            "statistics": {
                "packets": {"received": 0, "sent": 0},
                "bytes": {"received": 0, "sent": 0},
                "packets_drop": {"received": 0, "seq_error": 0, "sent": 0},
            },
        }
    }
}
