expected_output = {
    "process_id": {
        65109: {
            "router_id": "10.16.2.2",
            "sr_attributes": {
                "sr_label_preferred": False,
                "advertise_explicit_null": False,
            },
            "mfi_label_reservation_ack_pending": False,
            "bind_retry_timer_running": False,
            "adj_label_bind_retry_timer_running": False,
            "global_segment_routing_state": "Enabled",
            "segment_routing_enabled": {
                "area": {
                    "0.0.0.8": {
                        "topology_name": "Base",
                        "forwarding": "MPLS",
                        "strict_spf": "Capable",
                    },
                    "AS external": {
                        "topology_name": "Base",
                        "forwarding": "MPLS",
                        "strict_spf": "Not applicable",
                    },
                }
            },
            "global_block_srgb": {
                "range": {"start": 16000, "end": 23999},
                "state": "Created",
            },
            "local_block_srlb": {
                "range": {"start": 15000, "end": 15999},
                "state": "Created",
            },
            "registered_with": {
                "SR App": {
                    "client_handle": 2,
                    "sr_algo": {
                        0: {
                            "connected_map_notifications_active": {
                                "handle": "0x0",
                                "bit_mask": "0x1",
                            },
                            "active_policy_map_notifications_active": {
                                "handle": "0x2",
                                "bit_mask": "0xC",
                            },
                        },
                        1: {
                            "connected_map_notifications_active": {
                                "handle": "0x1",
                                "bit_mask": "0x1",
                            },
                            "active_policy_map_notifications_active": {
                                "handle": "0x3",
                                "bit_mask": "0xC",
                            },
                        },
                    },
                },
                "MPLS": {"client_id": 100},
            },
            "max_labels": {
                "platform": 16,
                "available": 13,
                "pushed_by_ospf": {"uloop_tunnels": 10, "ti_lfa_tunnels": 10},
            },
            "srp_app_locks_requested": {"srgb": 0, "srlb": 0},
            "teapp": {"te_router_id": "10.16.2.2"},
        }
    }
}
