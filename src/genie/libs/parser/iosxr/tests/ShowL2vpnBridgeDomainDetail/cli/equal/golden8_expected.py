expected_output = {
    "legend": "pp = Partially Programmed.",
    "bridge_group": {
        "BS": {
            "bridge_domain": {
                "BS_1700": {
                    "state": "up",
                    "id": 385,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "386",
                    "p2mp_pw": "disabled",
                    "create_time": "08/12/2020 12:50:08 (26w5d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether3.1700": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1700",
                                    "1700"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000548",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "TenGigE0/2/0/14.1700": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1700",
                                    "1700"
                                ],
                                "mtu": 1526,
                                "xc_id": "0x1200556",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "BS_2016": {
                    "state": "up",
                    "id": 406,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "407",
                    "p2mp_pw": "disabled",
                    "create_time": "20/05/2021 10:30:35 (3w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether3.2016": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2016",
                                    "2016"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc00005a0",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "TenGigE0/2/0/14.2016": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2016",
                                    "2016"
                                ],
                                "mtu": 1526,
                                "xc_id": "0x12005a4",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        },
        "B2C": {
            "bridge_domain": {
                "SEG180": {
                    "state": "up",
                    "id": 138,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
                    },
                    "mac_aging_time": 300,
                    "mac_aging_type": "inactivity",
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
                    "mid_cvpls_config_index": "139",
                    "p2mp_pw": "disabled",
                    "create_time": "22/05/2020 03:04:51 (1y03w ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether10.180": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4096",
                                    "4096"
                                ],
                                "mtu": 9004,
                                "xc_id": "0xc000019e",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
                                },
                                "mac_aging_time": 300,
                                "mac_aging_type": "inactivity",
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
                                        "receive": 109,
                                        "send": 173009
                                    },
                                    "byte_totals": {
                                        "receive": 6976,
                                        "send": 13241479
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether101.180": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4096",
                                    "4096"
                                ],
                                "mtu": 9104,
                                "xc_id": "0xc000063a",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
                                },
                                "mac_aging_time": 300,
                                "mac_aging_type": "inactivity",
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
                                        "receive": 211212449,
                                        "send": 106570486
                                    },
                                    "byte_totals": {
                                        "receive": 261086986801,
                                        "send": 38098935003
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "SEG180": {
                            "state": "up",
                            "neighbor": {
                                "10.11.44.92": {
                                    "pw_id": {
                                        "99180": {
                                            "state": "up ( established )",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa0000133",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "26304",
                                                        "remote": "24276"
                                                    },
                                                    "group_id": {
                                                        "local": "0x8a",
                                                        "remote": "0xa5"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "SEG180",
                                                        "remote": "SEG180"
                                                    },
                                                    "mtu": {
                                                        "local": "1500",
                                                        "remote": "1500"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "enabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x2",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x7",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684354867"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 10/06/2021 02:44:34 (3d20h",
                                                        "remote": "ago)"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=1,Rx=1)"
                                            },
                                            "status_code": "0x0 (Up)",
                                            "create_time": "22/05/2020 03:04:51 (1y03w ago)",
                                            "last_time_status_changed": "10/06/2021 02:53:01 (3d20h ago)",
                                            "mac_withdraw_message": {
                                                "send": 47,
                                                "receive": 38
                                            },
                                            "forward_class": "0",
                                            "statistics": {
                                                "packet_totals": {
                                                    "receive": 106567054,
                                                    "send": 211212390
                                                },
                                                "byte_totals": {
                                                    "receive": 38096946147,
                                                    "send": 261086280143
                                                },
                                                "mac_move": "0"
                                            },
                                            "storm_control_drop_counters": {
                                                "packets": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                },
                                                "bytes": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                }
                                            },
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none"
                                        }
                                    }
                                }
                            },
                            "statistics": {
                                "drop": {
                                    "illegal_vlan": 0,
                                    "illegal_length": 0
                                }
                            }
                        }
                    },
                    "access_pw": {
                        "SEG180": {
                            "neighbor": {
                                "10.11.44.8": {
                                    "pw_id": {
                                        "180": {
                                            "state": "standby ( all ready )",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa0000131",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "pw_backup_disable_delay": 0,
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "26303",
                                                        "remote": "31"
                                                    },
                                                    "group_id": {
                                                        "local": "0x8a",
                                                        "remote": "0x8"
                                                    },
                                                    "interface": {
                                                        "local": "Access PW",
                                                        "remote": "[B2C]"
                                                    },
                                                    "mtu": {
                                                        "local": "1500",
                                                        "remote": "1500"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "enabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x12",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x3",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "control word",
                                                            "router alert label"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684354865"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 10/06/2021 02:53:01 (3d20h",
                                                        "remote": "ago)"
                                                    },
                                                    "mac_limit:": {
                                                        "local": "4000, Action: none, Notification: syslog,",
                                                        "remote": "trap"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=0,Rx=0)"
                                            },
                                            "status_code": "0x20 (Standby)",
                                            "create_time": "22/05/2020 03:04:51 (1y03w ago)",
                                            "last_time_status_changed": "10/06/2021 02:53:01 (3d20h ago)",
                                            "mac_withdraw_message": {
                                                "send": 0,
                                                "receive": 22
                                            },
                                            "forward_class": "0",
                                            "mac_learning": "enabled",
                                            "flooding": {
                                                "broadcast_multicast": "enabled",
                                                "unknown_unicast": "enabled"
                                            },
                                            "mac_aging_time": 300,
                                            "mac_aging_type": "inactivity",
                                            "mac_limit_reached": "no",
                                            "mac_limit_threshold": "75%",
                                            "mac_port_down_flush": "enabled",
                                            "mac_secure": "disabled",
                                            "mac_secure_logging": "disabled",
                                            "split_horizon_group": "none",
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none",
                                            "storm_control": "bridge-domain policer"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "pw": {
                        "num_pw": 2,
                        "num_pw_up": 1
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "SEG242": {
                    "state": "up",
                    "id": 252,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
                    },
                    "mac_aging_time": 300,
                    "mac_aging_type": "inactivity",
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
                    "bridge_mtu": "1600",
                    "mid_cvpls_config_index": "253",
                    "p2mp_pw": "disabled",
                    "create_time": "06/08/2020 03:00:38 (44w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether10.242": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4096",
                                    "4096"
                                ],
                                "mtu": 9004,
                                "xc_id": "0xc0000308",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
                                },
                                "mac_aging_time": 300,
                                "mac_aging_type": "inactivity",
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
                                        "receive": 0,
                                        "send": 123583
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 8618629
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether101.242": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4096",
                                    "4096"
                                ],
                                "mtu": 9104,
                                "xc_id": "0xc00006b0",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
                                },
                                "mac_aging_time": 300,
                                "mac_aging_type": "inactivity",
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
                                        "receive": 316478673,
                                        "send": 154259031
                                    },
                                    "byte_totals": {
                                        "receive": 455595024880,
                                        "send": 16267549475
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "SEG242": {
                            "state": "up",
                            "neighbor": {
                                "10.11.44.92": {
                                    "pw_id": {
                                        "99242": {
                                            "state": "up ( established )",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa000022b",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "26469",
                                                        "remote": "24341"
                                                    },
                                                    "group_id": {
                                                        "local": "0xfc",
                                                        "remote": "0xe0"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "SEG242",
                                                        "remote": "SEG242"
                                                    },
                                                    "mtu": {
                                                        "local": "1600",
                                                        "remote": "1600"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "enabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x2",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x7",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684355115"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 10/06/2021 02:44:34 (3d20h",
                                                        "remote": "ago)"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=1,Rx=1)"
                                            },
                                            "status_code": "0x0 (Up)",
                                            "create_time": "06/08/2020 03:00:38 (44w3d ago)",
                                            "last_time_status_changed": "10/06/2021 02:53:01 (3d20h ago)",
                                            "mac_withdraw_message": {
                                                "send": 39,
                                                "receive": 49
                                            },
                                            "forward_class": "0",
                                            "statistics": {
                                                "packet_totals": {
                                                    "receive": 154264643,
                                                    "send": 316478076
                                                },
                                                "byte_totals": {
                                                    "receive": 16268069399,
                                                    "send": 455594105126
                                                },
                                                "mac_move": "0"
                                            },
                                            "storm_control_drop_counters": {
                                                "packets": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                },
                                                "bytes": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                }
                                            },
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none"
                                        }
                                    }
                                },
                            },
                            "statistics": {
                                "drop": {
                                    "illegal_vlan": 0,
                                    "illegal_length": 0
                                }
                            }
                        }
                    },
                    "access_pw": {
                        "SEG242": {
                            "neighbor": {
                                "10.11.44.12": {
                                    "pw_id": {
                                        "242": {
                                            "state": "standby ( all ready )",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa0000229",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "pw_backup_disable_delay": 0,
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "26468",
                                                        "remote": "65"
                                                    },
                                                    "group_id": {
                                                        "local": "0xfc",
                                                        "remote": "0x16"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "Access PW",
                                                        "remote": "[B2C]"
                                                    },
                                                    "mtu": {
                                                        "local": "1600",
                                                        "remote": "1600"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "enabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x12",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x3",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "control word",
                                                            "router alert label"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684355113"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 10/06/2021 02:53:01 (3d20h",
                                                        "remote": "ago)"
                                                    },
                                                    "mac_limit:": {
                                                        "local": "4000, Action: none, Notification: syslog,",
                                                        "remote": "trap"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=0,Rx=0)"
                                            },
                                            "status_code": "0x20 (Standby)",
                                            "create_time": "06/08/2020 03:00:38 (44w3d ago)",
                                            "last_time_status_changed": "10/06/2021 02:53:01 (3d20h ago)",
                                            "mac_withdraw_message": {
                                                "send": 0,
                                                "receive": 23
                                            },
                                            "forward_class": "0",
                                            "mac_learning": "enabled",
                                            "flooding": {
                                                "broadcast_multicast": "enabled",
                                                "unknown_unicast": "enabled"
                                            },
                                            "mac_aging_time": 300,
                                            "mac_aging_type": "inactivity",
                                            "mac_limit_reached": "no",
                                            "mac_limit_threshold": "75%",
                                            "mac_port_down_flush": "enabled",
                                            "mac_secure": "disabled",
                                            "mac_secure_logging": "disabled",
                                            "split_horizon_group": "none",
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none",
                                            "storm_control": "bridge-domain policer"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "pw": {
                        "num_pw": 2,
                        "num_pw_up": 1
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "SEG244": {
                    "state": "up",
                    "id": 253,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
                    },
                    "mac_aging_time": 300,
                    "mac_aging_type": "inactivity",
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
                    "bridge_mtu": "1600",
                    "mid_cvpls_config_index": "254",
                    "p2mp_pw": "disabled",
                    "create_time": "06/08/2020 03:00:38 (44w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether10.244": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4096",
                                    "4096"
                                ],
                                "mtu": 9004,
                                "xc_id": "0xc000030a",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
                                },
                                "mac_aging_time": 300,
                                "mac_aging_type": "inactivity",
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
                                        "receive": 168583,
                                        "send": 4000182
                                    },
                                    "byte_totals": {
                                        "receive": 10789312,
                                        "send": 507734366
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether101.244": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4096",
                                    "4096"
                                ],
                                "mtu": 9104,
                                "xc_id": "0xc00006b2",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
                                },
                                "mac_aging_time": 300,
                                "mac_aging_type": "inactivity",
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
                                        "receive": 171074,
                                        "send": 3705157
                                    },
                                    "byte_totals": {
                                        "receive": 10948736,
                                        "send": 469726393
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "SEG244": {
                            "state": "up",
                            "neighbor": {
                                "10.11.44.92": {
                                    "pw_id": {
                                        "99244": {
                                            "state": "up ( established )",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa000022f",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "26471",
                                                        "remote": "24343"
                                                    },
                                                    "group_id": {
                                                        "local": "0xfd",
                                                        "remote": "0xe2"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "SEG244",
                                                        "remote": "SEG244"
                                                    },
                                                    "mtu": {
                                                        "local": "1600",
                                                        "remote": "1600"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "enabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x2",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x7",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684355119"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=1,Rx=1)"
                                            },
                                            "status_code": "0x0 (Up)",
                                            "create_time": "06/08/2020 03:00:38 (44w3d ago)",
                                            "last_time_status_changed": "10/06/2021 10:37:03 (3d12h ago)",
                                            "mac_withdraw_message": {
                                                "send": 0,
                                                "receive": 3
                                            },
                                            "forward_class": "0",
                                            "statistics": {
                                                "packet_totals": {
                                                    "receive": 4193762,
                                                    "send": 339660
                                                },
                                                "byte_totals": {
                                                    "receive": 768650456,
                                                    "send": 21738240
                                                },
                                                "mac_move": "0"
                                            },
                                            "storm_control_drop_counters": {
                                                "packets": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                },
                                                "bytes": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                }
                                            },
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none"
                                        }
                                    }
                                }
                            },
                            "statistics": {
                                "drop": {
                                    "illegal_vlan": 0,
                                    "illegal_length": 0
                                }
                            }
                        }
                    },
                    "access_pw": {
                        "SEG244": {
                            "neighbor": {
                                "10.11.44.12": {
                                    "pw_id": {
                                        "244": {
                                            "state": "standby ( all ready )",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa000022d",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "pw_backup_disable_delay": 0,
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "26470",
                                                        "remote": "177"
                                                    },
                                                    "group_id": {
                                                        "local": "0xfd",
                                                        "remote": "0x18"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "Access PW",
                                                        "remote": "[B2C]"
                                                    },
                                                    "mtu": {
                                                        "local": "1600",
                                                        "remote": "1600"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "enabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x12",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x3",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "control word",
                                                            "router alert label"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684355117"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 05/09/2020 21:19:41 (40w1d",
                                                        "remote": "ago)"
                                                    },
                                                    "mac_limit:": {
                                                        "local": "4000, Action: none, Notification: syslog,",
                                                        "remote": "trap"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=0,Rx=0)"
                                            },
                                            "status_code": "0x20 (Standby)",
                                            "create_time": "06/08/2020 03:00:38 (44w3d ago)",
                                            "last_time_status_changed": "10/06/2021 10:46:08 (3d12h ago)",
                                            "mac_withdraw_message": {
                                                "send": 1,
                                                "receive": 1
                                            },
                                            "forward_class": "0",
                                            "mac_learning": "enabled",
                                            "flooding": {
                                                "broadcast_multicast": "enabled",
                                                "unknown_unicast": "enabled"
                                            },
                                            "mac_aging_time": 300,
                                            "mac_aging_type": "inactivity",
                                            "mac_limit_reached": "no",
                                            "mac_limit_threshold": "75%",
                                            "mac_port_down_flush": "enabled",
                                            "mac_secure": "disabled",
                                            "mac_secure_logging": "disabled",
                                            "split_horizon_group": "none",
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none",
                                            "storm_control": "bridge-domain policer"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "pw": {
                        "num_pw": 2,
                        "num_pw_up": 1
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        },
        "LAB": {
            "bridge_domain": {
                "9001": {
                    "state": "up",
                    "id": 0,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "create_time": "01/10/2019 14:18:18 (1y36w ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "Bundle-Ether10.3999": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1101",
                                    "1101"
                                ],
                                "mtu": 9004,
                                "xc_id": "0xc0000002",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "Seg101": {
                            "state": "up",
                            "neighbor": {
                                "10.11.44.92": {
                                    "pw_id": {
                                        "5000": {
                                            "state": "up ( established )",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa0000009",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "25636",
                                                        "remote": "24201"
                                                    },
                                                    "group_id": {
                                                        "local": "0x0",
                                                        "remote": "0x11c"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "Seg101",
                                                        "remote": "Seg101"
                                                    },
                                                    "mtu": {
                                                        "local": "1500",
                                                        "remote": "1500"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "enabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x2",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x7",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684354569"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 10/06/2021 02:44:34 (3d20h",
                                                        "remote": "ago)"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=1,Rx=1)"
                                            },
                                            "status_code": "0x0 (Up)",
                                            "create_time": "22/11/2019 11:48:50 (1y29w ago)",
                                            "last_time_status_changed": "10/06/2021 02:53:01 (3d20h ago)",
                                            "mac_withdraw_message": {
                                                "send": 16,
                                                "receive": 14
                                            },
                                            "forward_class": "0",
                                            "statistics": {
                                                "packet_totals": {
                                                    "receive": 0,
                                                    "send": 0
                                                },
                                                "byte_totals": {
                                                    "receive": 0,
                                                    "send": 0
                                                },
                                                "mac_move": "0"
                                            },
                                            "storm_control_drop_counters": {
                                                "packets": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                },
                                                "bytes": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                }
                                            },
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none"
                                        }
                                    }
                                }
                            },
                            "statistics": {
                                "drop": {
                                    "illegal_vlan": 0,
                                    "illegal_length": 0
                                }
                            }
                        }
                    },
                    "pw": {
                        "num_pw": 3,
                        "num_pw_up": 1
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    },
                    "access_pw": {
                        "9001": {
                            "neighbor": {
                                "10.11.44.81": {
                                    "pw_id": {
                                        "9001": {
                                            "state": "down ( local ready ) (Transport LSP Down)",
                                            "pw_class": "PW_DEFAULT",
                                            "xc_id": "0xa0000003",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "enabled",
                                            "interworking": "none",
                                            "pw_backup_disable_delay": 0,
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Down",
                                                "mpls": {
                                                    "label": {
                                                        "local": "24000",
                                                        "remote": "unknown"
                                                    },
                                                    "group_id": {
                                                        "local": "0x0",
                                                        "remote": "0x0"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "Access PW",
                                                        "remote": "unknown"
                                                    },
                                                    "mtu": {
                                                        "local": "1500",
                                                        "remote": "unknown"
                                                    },
                                                    "control_word": {
                                                        "local": "enabled",
                                                        "remote": "unknown"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "unknown"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x0",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "none"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x7",
                                                        "remote": "0x0",
                                                        "local_type": [
                                                            "control word",
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "none"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684354563"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 21/10/2020 13:18:37 (33w4d",
                                                        "remote": "ago)"
                                                    }
                                                }
                                            },
                                            "flow_label_flags": {
                                                "configured": "(Tx=1,Rx=1)",
                                                "negotiated": "(Tx=0,Rx=0)"
                                            },
                                            "create_time": "01/10/2019 14:18:18 (1y36w ago)",
                                            "last_time_status_changed": "21/10/2020 13:24:35 (33w4d ago)",
                                            "mac_withdraw_message": {
                                                "send": 13,
                                                "receive": 0
                                            },
                                            "forward_class": "0",
                                            "mac_learning": "enabled",
                                            "flooding": {
                                                "broadcast_multicast": "enabled",
                                                "unknown_unicast": "enabled"
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
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none",
                                            "storm_control": "bridge-domain policer"
                                        }
                                    }
                                },
                                "10.11.44.82": {
                                    "pw_id": {
                                        "9001": {
                                            "state": "down ( local ready ) (Transport LSP Down)",
                                            "pw_class": "not set",
                                            "xc_id": "0xa0000005",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "disabled",
                                            "interworking": "none",
                                            "pw_backup_disable_delay": 0,
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Down",
                                                "pw": {
                                                    "load_balance": {
                                                        "local": "Hashing:",
                                                        "remote": "src-dst-ip"
                                                    },
                                                    "pw_status_tlv": {
                                                        "local": "in",
                                                        "remote": "use"
                                                    }
                                                },
                                                "mpls": {
                                                    "label": {
                                                        "local": "24001",
                                                        "remote": "unknown"
                                                    },
                                                    "group_id": {
                                                        "local": "0x0",
                                                        "remote": "0x0"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "Access PW",
                                                        "remote": "unknown"
                                                    },
                                                    "mtu": {
                                                        "local": "1500",
                                                        "remote": "unknown"
                                                    },
                                                    "control_word": {
                                                        "local": "disabled",
                                                        "remote": "unknown"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "unknown"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x0",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "none"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x6",
                                                        "remote": "0x0",
                                                        "local_type": [
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "none"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684354565"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 10/06/2020 01:50:32 (1y00w",
                                                        "remote": "ago)"
                                                    }
                                                }
                                            },
                                            "create_time": "01/10/2019 14:18:18 (1y36w ago)",
                                            "last_time_status_changed": "10/06/2020 01:53:52 (1y00w ago)",
                                            "mac_withdraw_message": {
                                                "send": 0,
                                                "receive": 0
                                            },
                                            "forward_class": "0",
                                            "mac_learning": "enabled",
                                            "flooding": {
                                                "broadcast_multicast": "enabled",
                                                "unknown_unicast": "enabled"
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
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none",
                                            "storm_control": "bridge-domain policer"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "B1-B": {
            "bridge_domain": {
                "B1-B": {
                    "state": "up",
                    "id": 1,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "2",
                    "p2mp_pw": "disabled",
                    "create_time": "15/11/2019 03:52:31 (1y30w ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 1,
                        "num_ac_up": 1,
                        "interfaces": {
                            "Bundle-Ether10.4000": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4000",
                                    "4000"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc000000e",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 2263727831,
                                        "send": 2601947451
                                    },
                                    "byte_totals": {
                                        "receive": 1695425622592,
                                        "send": 2615912696704
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 1,
                        "B1-B": {
                            "state": "up",
                            "neighbor": {
                                "10.11.44.92": {
                                    "pw_id": {
                                        "104001": {
                                            "state": "up ( established )",
                                            "pw_class": "not set",
                                            "xc_id": "0xa0000007",
                                            "encapsulation": "MPLS",
                                            "protocol": "LDP",
                                            "source_address": "10.11.44.91",
                                            "pw_type": "Ethernet",
                                            "control_word": "disabled",
                                            "interworking": "none",
                                            "sequencing": "not set",
                                            "lsp": {
                                                "state": "Up",
                                                "mpls": {
                                                    "label": {
                                                        "local": "24748",
                                                        "remote": "24344"
                                                    },
                                                    "group_id": {
                                                        "local": "0x1",
                                                        "remote": "0x118"
                                                    },
                                                    "monitor_interface": {
                                                        "local": "B1-B",
                                                        "remote": "B1-B"
                                                    },
                                                    "mtu": {
                                                        "local": "1500",
                                                        "remote": "1500"
                                                    },
                                                    "control_word": {
                                                        "local": "disabled",
                                                        "remote": "disabled"
                                                    },
                                                    "pw_type": {
                                                        "local": "Ethernet",
                                                        "remote": "Ethernet"
                                                    },
                                                    "vccv_cv_type": {
                                                        "local": "0x2",
                                                        "remote": "0x2",
                                                        "local_type": [
                                                            "LSP ping verification"
                                                        ],
                                                        "remote_type": [
                                                            "LSP ping verification"
                                                        ]
                                                    },
                                                    "vccv_cc_type": {
                                                        "local": "0x6",
                                                        "remote": "0x6",
                                                        "local_type": [
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ],
                                                        "remote_type": [
                                                            "router alert label",
                                                            "TTL expiry"
                                                        ]
                                                    },
                                                    "mib": {
                                                        "local": "cpwVcIndex:",
                                                        "remote": "2684354567"
                                                    },
                                                    "last_time_pw": {
                                                        "local": "went down: 10/06/2021 02:44:34 (3d20h",
                                                        "remote": "ago)"
                                                    }
                                                }
                                            },
                                            "status_code": "0x0 (Up)",
                                            "create_time": "15/11/2019 03:52:31 (1y30w ago)",
                                            "last_time_status_changed": "10/06/2021 02:53:01 (3d20h ago)",
                                            "mac_withdraw_message": {
                                                "send": 13,
                                                "receive": 0
                                            },
                                            "forward_class": "0",
                                            "statistics": {
                                                "packet_totals": {
                                                    "receive": 2601882205,
                                                    "send": 2263733637
                                                },
                                                "byte_totals": {
                                                    "receive": 2605419757847,
                                                    "send": 1695428286863
                                                },
                                                "mac_move": "0"
                                            },
                                            "storm_control_drop_counters": {
                                                "packets": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                },
                                                "bytes": {
                                                    "broadcast": "0",
                                                    "multicast": "0",
                                                    "unknown_unicast": "0"
                                                }
                                            },
                                            "dhcp_v4_snooping": "disabled",
                                            "dhcp_v4_snooping_profile": "none",
                                            "igmp_snooping": "disabled",
                                            "igmp_snooping_profile": "none",
                                            "mld_snooping_profile": "none"
                                        }
                                    }
                                }
                            },
                            "statistics": {
                                "drop": {
                                    "illegal_vlan": 0,
                                    "illegal_length": 0
                                }
                            }
                        }
                    },
                    "pw": {
                        "num_pw": 1,
                        "num_pw_up": 1
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        },
        "Management": {
            "bridge_domain": {
                "4010": {
                    "state": "up",
                    "id": 263,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "264",
                    "p2mp_pw": "disabled",
                    "create_time": "24/09/2020 03:22:47 (37w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether20.4010": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4010",
                                    "4010"
                                ],
                                "mtu": 1500,
                                "xc_id": "0xc000042a",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 868,
                                        "send": 1017603
                                    },
                                    "byte_totals": {
                                        "receive": 55552,
                                        "send": 61874928
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.4010": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4010",
                                    "4010"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc000033c",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 1017608,
                                        "send": 868
                                    },
                                    "byte_totals": {
                                        "receive": 61875220,
                                        "send": 55552
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "4090": {
                    "state": "up",
                    "id": 264,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "265",
                    "p2mp_pw": "disabled",
                    "create_time": "24/09/2020 03:22:47 (37w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether20.4090": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4090",
                                    "4090"
                                ],
                                "mtu": 1500,
                                "xc_id": "0xc000042c",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 35510779266,
                                        "send": 67290609967
                                    },
                                    "byte_totals": {
                                        "receive": 14204488780501,
                                        "send": 83879978440066
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.4090": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "4090",
                                    "4090"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc000033e",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 67289104995,
                                        "send": 35510093704
                                    },
                                    "byte_totals": {
                                        "receive": 83878025586583,
                                        "send": 14204351236525
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        },
        "Subscriber": {
            "bridge_domain": {
                "Elf_1124": {
                    "state": "up",
                    "id": 396,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "397",
                    "p2mp_pw": "disabled",
                    "create_time": "20/04/2021 11:22:55 (7w5d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether20.20011124": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1124",
                                    "1124"
                                ],
                                "mtu": 1500,
                                "xc_id": "0xc000058c",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 398255446,
                                        "send": 166337423
                                    },
                                    "byte_totals": {
                                        "receive": 539316094013,
                                        "send": 36890820969
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.20011124": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1124",
                                    "1124"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000570",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 166337150,
                                        "send": 398251507
                                    },
                                    "byte_totals": {
                                        "receive": 36890796499,
                                        "send": 539311615942
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "Recom_2213": {
                    "state": "up",
                    "id": 371,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "372",
                    "p2mp_pw": "disabled",
                    "create_time": "24/09/2020 03:22:47 (37w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether20.21002213": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2213",
                                    "2213"
                                ],
                                "mtu": 1500,
                                "xc_id": "0xc00004fe",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.21002213": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2213",
                                    "2213"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000410",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "Recom_2215": {
                    "state": "up",
                    "id": 373,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "374",
                    "p2mp_pw": "disabled",
                    "create_time": "24/09/2020 03:22:47 (37w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether20.21002215": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2215",
                                    "2215"
                                ],
                                "mtu": 1500,
                                "xc_id": "0xc0000502",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.21002215": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2215",
                                    "2215"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000414",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "Recom_2217": {
                    "state": "up",
                    "id": 376,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "377",
                    "p2mp_pw": "disabled",
                    "create_time": "25/09/2020 09:43:41 (37w2d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether20.21002217": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2217",
                                    "2217"
                                ],
                                "mtu": 1500,
                                "xc_id": "0xc0000508",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 1857545,
                                        "send": 1284464
                                    },
                                    "byte_totals": {
                                        "receive": 1984810970,
                                        "send": 281697660
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.2217": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "2217",
                                    "2217"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000506",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 1284475,
                                        "send": 1857554
                                    },
                                    "byte_totals": {
                                        "receive": 276560922,
                                        "send": 1977382049
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        },
        "Subscriber_MTS": {
            "bridge_domain": {
                "1266": {
                    "state": "up",
                    "id": 256,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "257",
                    "p2mp_pw": "disabled",
                    "create_time": "17/09/2020 03:58:27 (38w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether10.1266": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1266",
                                    "1266"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000318",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 3245556280,
                                        "send": 1465216351
                                    },
                                    "byte_totals": {
                                        "receive": 4339841715578,
                                        "send": 344268595837
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.1266": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1266",
                                    "1266"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000314",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 1465145657,
                                        "send": 3245432086
                                    },
                                    "byte_totals": {
                                        "receive": 338398661284,
                                        "send": 4326687483580
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "1267": {
                    "state": "up",
                    "id": 257,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "258",
                    "p2mp_pw": "disabled",
                    "create_time": "17/09/2020 03:58:27 (38w3d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether10.1267": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1267",
                                    "1267"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc000031a",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 4603415788,
                                        "send": 2355034330
                                    },
                                    "byte_totals": {
                                        "receive": 5820136906653,
                                        "send": 818805396762
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.1267": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1267",
                                    "1267"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000316",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 2354966866,
                                        "send": 4603284751
                                    },
                                    "byte_totals": {
                                        "receive": 809357601016,
                                        "send": 5801561953485
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "1268": {
                    "state": "up",
                    "id": 36,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "37",
                    "p2mp_pw": "disabled",
                    "create_time": "13/12/2019 02:49:09 (1y26w ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether10.1268": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1268",
                                    "1268"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc000009a",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "Bundle-Ether3.1268": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1268",
                                    "1268"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc000007c",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        },
        "Other_Connect_Tmp": {
            "bridge_domain": {
                "1270": {
                    "state": "up",
                    "id": 157,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "158",
                    "p2mp_pw": "disabled",
                    "create_time": "04/06/2020 13:20:08 (1y01w ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether3.1270": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1270",
                                    "1270"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc0000242",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 117707,
                                        "send": 0
                                    },
                                    "byte_totals": {
                                        "receive": 8004076,
                                        "send": 0
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "TenGigE0/2/0/11.1270": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "1270",
                                    "1270"
                                ],
                                "mtu": 1526,
                                "xc_id": "0x1200220",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 0,
                                        "send": 117708
                                    },
                                    "byte_totals": {
                                        "receive": 0,
                                        "send": 8004144
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                },
                "BS_3986": {
                    "state": "up",
                    "id": 259,
                    "shg_id": 0,
                    "mst_i": 0,
                    "coupled_state": "disabled",
                    "vine_state": "Default",
                    "mac_learning": "enabled",
                    "mac_withdraw": "enabled",
                    "mac_withdraw_for_access_pw": "enabled",
                    "mac_withdraw_sent_on": "bridge port up",
                    "mac_withdraw_relaying": "disabled",
                    "flooding": {
                        "broadcast_multicast": "enabled",
                        "unknown_unicast": "enabled"
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
                    "mid_cvpls_config_index": "260",
                    "p2mp_pw": "disabled",
                    "create_time": "21/09/2020 15:58:08 (37w6d ago)",
                    "status_changed_since_creation": "No",
                    "ac": {
                        "num_ac": 2,
                        "num_ac_up": 2,
                        "interfaces": {
                            "Bundle-Ether3.3986": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "3986",
                                    "3986"
                                ],
                                "mtu": 9000,
                                "xc_id": "0xc000031e",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 3901995,
                                        "send": 6335822
                                    },
                                    "byte_totals": {
                                        "receive": 275112570,
                                        "send": 7269237551
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            },
                            "TenGigE0/2/0/11.3986": {
                                "state": "up",
                                "type": "VLAN",
                                "vlan_num_ranges": "1",
                                "rewrite_tags": "",
                                "vlan_ranges": [
                                    "3986",
                                    "3986"
                                ],
                                "mtu": 1526,
                                "xc_id": "0x1200322",
                                "interworking": "none",
                                "mac_learning": "enabled",
                                "flooding": {
                                    "broadcast_multicast": "enabled",
                                    "unknown_unicast": "enabled"
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
                                        "receive": 6335693,
                                        "send": 3901902
                                    },
                                    "byte_totals": {
                                        "receive": 7269096652,
                                        "send": 275105988
                                    },
                                    "mac_move": "0"
                                },
                                "storm_control_drop_counters": {
                                    "packets": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    },
                                    "bytes": {
                                        "broadcast": "0",
                                        "multicast": "0",
                                        "unknown_unicast": "0"
                                    }
                                },
                                "dynamic_arp_inspection_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                },
                                "ip_source_guard_drop_counters": {
                                    "packets": "0",
                                    "bytes": "0"
                                }
                            }
                        }
                    },
                    "vfi": {
                        "num_vfi": 0
                    },
                    "pw": {
                        "num_pw": 0,
                        "num_pw_up": 0
                    },
                    "pbb": {
                        "num_pbb": 0,
                        "num_pbb_up": 0
                    },
                    "vni": {
                        "num_vni": 0,
                        "num_vni_up": 0
                    }
                }
            }
        }
    }
}
