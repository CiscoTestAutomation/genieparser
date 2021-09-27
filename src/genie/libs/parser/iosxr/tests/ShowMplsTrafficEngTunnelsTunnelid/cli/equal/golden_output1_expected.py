expected_output={
    "tunnel": {
        "tunnel-te50000": {
            "destination": "109.109.109.109",
            "ifhandle": "0x20e0",
            "signalled_name": "50000_F17-ASR9922_F109-ASR9001",
            "status": {
                "admin": "up",
                "oper": "up",
                "path": "valid",
                "signalling": "connected",
                "path_option": {
                    10: {
                        "type": "explicit",
                        "path_weight": 160,
                        "accumulative_metrics": {"te": 160, "igp": 160, "path": 600000},
                    },
                    20: {"type": "explicit"},
                    100: {"type": "dynamic"},
                },
                "last_pcalc_error": {
                    "time": " Tue Apr 27 16:21:21 2021",
                    "info": "No path to destination",
                    "reverselink": "109.109.109.109",
                },
                "g_pid": "0x0800",
                "bandwidth_requested": 0,
                "bandwidth_requested_unit": "kbps",
                "creation_time": "Tue Apr 27 16:21:14 2021 (01:36:30 ago)",
            },
            "config_parameters": {
                "bandwidth": 0,
                "bandwidth_unit": "kbps",
                "priority": 3,
                "affinity": "0x0/0xffff",
                "metric_type": "IGP (interface)",
                "path_selection": {"tiebreaker": "Min-fill (default)"},
                "hop_limit": "disabled",
                "cost_limit": "disabled",
                "delay_limit": "disabled",
                "delay_measurement": "disabled",
                "path_invalidation_timeout": 10000,
                "path_invalidation_timeout_unit": "msec",
                "action": "Tear",
                "autoroute": "enabled",
                "lockdown": "disabled  ",
                "policy_class": "not set",
                "forward_class": 0,
                "forward_class_state": "not enabled",
                "forwarding_adjacency": "disabled",
                "autoroute_destinations": 0,
                "loadshare": 0,
                "loadshare_state": "equal loadshares",
                "auto_bw": "disabled",
                "auto_capacity": "Disabled",
                "fast_reroute": "Enabled",
                "protection_desired": "Any",
                "path_protection": "Not Enabled",
                "bfd_fast_detection": "Disabled",
                "reoptimization_after_affinity_failure": "Enabled",
                "soft_preemption": "Disabled",
            },
            "history": {
                "tunnel_up_time": "01:36:23 (since Tue Apr 27 16:21:21 JST 2021)",
                "current_lsp": {
                    "uptime": "00:26:32 (since Tue Apr 27 17:31:12 JST 2021)"
                },
                "reopt_lsp": {
                    "lsp_failure": {
                        "lsp": "not signalled",
                        "lsp_status": "identical to the [CURRENT] LSP",
                        "date_time": "Tue Apr 27 16:26:11 JST 2021 [01:31:33 ago]",
                    }
                },
                "prior_lsp": {
                    "id": 5,
                    "path_option": 20,
                    "removal_trigger": "reoptimization completed",
                },
            },
            "path_info": {
                "OSPF mpls1 area 0": {
                    "node_hop_count": 2,
                    "hop": {
                        0: {"ip_address": "20.50.0.1"},
                        1: {"ip_address": "21.50.0.2"},
                        2: {"ip_address": "109.109.109.109"},
                    },
                }
            },
            "displayed": {
                "heads_displayed": 1,
                "total_heads": 9,
                "midpoints_displayed": 0,
                "total_midpoints": 10,
                "tails_displayed": 0,
                "total_tails": 6,
                "status": {"up": 1, "down": 0, "recovering": 0, "recovered_heads": 0},
            },
        }
    }
}

