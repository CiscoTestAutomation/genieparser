expected_output = {
    "legend": "pp = Partially Programmed.",
    "bridge_group": {
        "Genie-service": {
            "bridge_domain": {
                "genie100": {
                    "state": "up",
                    "id": 0,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "BVI",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled",
                    },
                    "mac_aging_time": 300,
                    "mac_aging_type": "inactivity",
                    "mac_limit": 4000,
                    "mac_limit_action": "none",
                    "mac_limit_notification": "syslog",
                    "mac_limit_reached": "no",
                    "mac_limit_threshold": "75%",
                    "mac_port_down_flush": "enabled",
                    "mac_secure": "disabled",
                    "mac_secure_logging": "disabled",
                    "split_horizon_group": "none",
                    "dynamic_arp_inspection": "disabled",
                    "dynamic_arp_logging": "disabled",
                    "ip_source_guard": "disabled",
                    "ip_source_logging": "disabled",
                    "dhcp_v4_snooping": "disabled",
                    "dhcp_v4_snooping_profile": "none",
                    "igmp_snooping": "disabled",
                    "igmp_snooping_profile": "none",
                    "mld_snooping_profile": "none",
                    "storm_control": "bridge-domain policer",
                    "bridge_mtu": "1500",
                    "mid_cvpls_config_index": "1",
                    "p2mp_pw": "disabled",
                    "create_time": "12/06/2019 11:46:11 (18w5d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "BVI100": {
                                "state": "up",
                                "type": "Routed-Interface",
                                "mtu": 1514,
                                "xc_id": "0x800001ab",
                                "interworking": "none",
                                "bvi_mac_address": ["78ba.f9ff.106d"],
                                "virtual_mac_address": ["0000.5eff.0101"],
                                "split_horizon_group": "Access",
                            },
                            "GigabitEthernet0/4/0/1.100": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": ["100", "100"],
                                "mtu": 1500,
                                "xc_id": "0x32001a8",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled",
                                },
                                "mac_aging_time": 300,
                                "mac_aging_type": "inactivity",
                                "mac_limit": 4000,
                                "mac_limit_action": "none",
                                "mac_limit_notification": "syslog",
                                "mac_limit_reached": "no",
                                "mac_limit_threshold": "75%",
                                "split_horizon_group": "none",
                                "dhcp_v4_snooping": "disabled",
                                "dhcp_v4_snooping_profile": "none",
                                "igmp_snooping": "disabled",
                                "igmp_snooping_profile": "none",
                                "mld_snooping_profile": "none",
                                "statistics": {
                                    "packet_totals": {
                                        "receive": 3894,
                                        "send": 13809438,
                                    },
                                    "byte_totals": {
                                        "receive": 291930,
                                        "send": 798698446,
                                    },
                                    "mac_move": "0",
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0",
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0",
                                    },
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0",
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0",
                                },
                            },
                        },
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "vfi100": {
                            "state": "up",
                            "neighbor": {
                                "10.229.11.11": {
                                    "pw_id": {
                                        "100100": {
                                            "state": "up ( established )",
                                            "pw_class": "link1",
                                            "xc_id": "0xa0000007",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.151.22.22",
                                            "pw_type": "Ethernet",
                                            "control_word": "disabled",
                                            "interworking": "none",
                                            "sequencing": "not set",
                                            "mpls": {
                                                "label": {
                                                    "local": "100037",
                                                    "remote": "100059",
                                                },
                                                "group_id": {
                                                    "local": "0x0",
                                                    "remote": "0xed",
                                                },
                                                "interface": {
                                                    "local": "vfi100",
                                                    "remote": "vfi100",
                                                },
                                                "mtu": {
                                                    "local": "1500",
                                                    "remote": "1500",
                                                },
                                                "control_word": {
                                                    "local": "disabled",
                                                    "remote": "disabled",
                                                },
                                                "pw_type": {
                                                    "local": "Ethernet",
                                                    "remote": "Ethernet",
                                                },
                                                "vccv_cv_type": {
                                                    "local": "0x2",
                                                    "remote": "0x2",
                                                    "local_type": [
                                                        "LSP ping verification"
                                                    ],
                                                    "remote_type": [
                                                        "LSP ping verification"
                                                    ],
                                                },
                                                "vccv_cc_type": {
                                                    "local": "0x6",
                                                    "remote": "0x6",
                                                    "local_type": [
                                                        "router alert label",
                                                        "TTL expiry",
                                                    ],
                                                    "remote_type": [
                                                        "router alert label",
                                                        "TTL expiry",
                                                    ],
                                                },
                                                "mib": {
                                                    "local": "cpwVcIndex:",
                                                    "remote": "2684354567",
                                                },
                                            },
                                            "status_code": "0x0 (Up)",
                                            "create_time": "12/06/2019 11:46:11 (18w5d ago)",
                                            "last_time_status_changed": "12/06/2019 12:08:57 (18w5d ago)",
                                            "mac_withdraw_message": {
                                                "send": 0,
                                                "receive": 0,
                                            },
                                            "forward_class": "0",
                                            "statistics": {
                                                "packet_totals": {
                                                    "receive": 759749,
                                                    "send": 13054472,
                                                },
                                                "byte_totals": {
                                                    "receive": 48596976,
                                                    "send": 695167614,
                                                },
                                                "mac_move": "0",
                                            },
                                            "storm_control_drop_counters": {
                                                "packets": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0",
                                                },
                                                "bytes": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0",
                                                },
                                            },
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none",
                                        }
                                    }
                                }
                            },
                            "statistics": {
                                "drop": {"illegal_vlan": 0, "illegal_length": 0}
                            },
                        },
                    },
                    "pw": {"num_pw": 1, "num_pw_up": 1},
                    "pbb": {"num_pbb": 0, "num_pbb_up": 0},
                    "vni": {"num_vni": 0, "num_vni_up": 0},
                }
            }
        }
    },
}
