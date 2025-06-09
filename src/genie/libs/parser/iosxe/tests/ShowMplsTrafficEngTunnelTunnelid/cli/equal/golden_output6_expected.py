expected_output ={ 
    "tunnel": {
        "Tunnel12831": {
            "destination": "10.166.0.1",
            "status": {
                "admin": "up",
                "oper": "up",
                "path": "valid",
                "signalling": "connected",
                "path_option": {
                    "5": {
                        "type": "explicit",
                        "path_name": "Path-BA-SM-PE-Pe",
                        "path_weight": 21
                    },
                    "10": {
                        "type": "dynamic"
                    }
                }
            },
            "config_parameters": {
                "bandwidth": 0,
                "bandwidth_unit": "kbps",
                "bandwidth_type": "Global",
                "priority": {
                    "setup_priority": 1,
                    "hold_priority": 1
                },
                "affinity": "0x0/0xFFFF",
                "metric_used": "TE",
                "metric_type": "default",
                "path_selection_tiebreaker": {
                    "global": "not set",
                    "tunnel_specific": "not set",
                    "effective": "min-fill",
                    "effective_type": "default"
                },
                "hop_limit": "disabled",
                "cost_limit": "disabled",
                "path_invalidation_timeout": 10000,
                "path_invalidation_timeout_unit": "msec",
                "path_invalidation_timeout_type": "default",
                "action": "Tear",
                "autoroute": "enabled",
                "lockdown": "disabled",
                "loadshare": 0,
                "max_load_share": 0,
                "load_share_type": "bw-based",
                "auto_bw": "disabled",
                "fault_oam": "disabled",
                "wrap_protection": "disabled",
                "wrap_capable": "No"
            },
            "active_path_option_parameters": {
                "state": {
                    "active_path": "5",
                    "path_type": "explicit"
                },
                "bandwidthoverride": "disabled",
                "lockdown": "disabled",
                "verbatim": "disabled"
            },
            "node_hop_count": 3,
            "inlabel": [
                "-"
            ],
            "next_hop": [
                "10.166.17.121"
            ],
            "frr_outlabel": [
                "Tunnel52829",
                " 10282"
            ],
            "rsvp_signalling_info": {
                "src": "10.166.0.11",
                "dst": "10.166.0.1",
                "tun_id": 12831,
                "tun_instance": 54,
                "rsvp_path_info": {
                    "my_address": "10.166.17.122",
                    "explicit_route": [
                        "10.166.17.121",
                        "10.166.16.37",
                        "10.166.16.46",
                        "10.166.0.1",
                        "10.166.16.37(16424)",
                        "10.166.0.1(0)"
                    ],
                    "record_route": "NONE",
                    "tspec": {
                        "ave_rate": 0,
                        "ave_rate_unit": "kbits",
                        "burst": 1000,
                        "burst_unit": "bytes",
                        "peak_rate": 0,
                        "peak_rate_unit": "kbits"
                    }
                },
                "rsvp_resv_info": {
                    "record_route": "10.166.0.8(10282) 10.166.0.200(16424)",
                    "fspec": {
                        "ave_rate": 0,
                        "ave_rate_unit": "kbits",
                        "burst": 0,
                        "burst_unit": "bytes",
                        "peak_rate": 0,
                        "peak_rate_unit": "kbits"
                    }
                }
            },
            "shortest_unconstrained_path_info": {
                "path_weight": "21",
                "path_weight_type": "TE",
                "explicit_route": [
                    "10.166.17.30",
                    "10.166.16.85",
                    "10.166.16.46",
                    "10.166.0.1"
                ]
            },
            "history": {
                "tunnel": {
                    "time_since_created": "49 days, 17 hours, 2 minutes",
                    "time_since_path_change": "20 days, 17 minutes",
                    "number_of_lsp_ids_used": 54
                },
                "current_lsp_id": {
                    "54": {
                        "uptime": "20 days, 17 minutes",
                        "selection": "reoptimization"
                    }
                },
                "prior_lsp_id": {
                    "53": {
                        "id": "path option unknown"
                    }
                }
            }
        }
    }
}
