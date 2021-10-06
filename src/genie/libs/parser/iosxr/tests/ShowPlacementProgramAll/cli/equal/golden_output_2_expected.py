

expected_output = {
    "program": {
        "auto_ip_ring": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1156",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "bfd": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1158",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "bgp": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1051",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                },
                "test": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "Group_10_bgp2",
                    "jid": "1052",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                },
                "test1": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "Group_5_bgp3",
                    "jid": "1053",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                },
                "test2": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "Group_5_bgp4",
                    "jid": "1054",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                },
            }
        },
        "bgp_epe": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1159",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "bpm": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1066",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "bundlemgr_distrib": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1157",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "domain_services": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1160",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "es_acl_mgr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1169",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "eth_gl_cfg": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1151",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ethernet_stats_controller_edm": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1161",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ftp_fs": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1162",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "icpe_satmgr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1163",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "igmp": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1208",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "intf_mgbl": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1143",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv4_connected": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1152",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv4_local": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1153",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv4_mfwd_ma": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1204",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv4_mpa": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1149",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv4_rib": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1146",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv4_rump": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1167",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv4_static": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1043",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv6_connected": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v6-routing",
                    "jid": "1154",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv6_local": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v6-routing",
                    "jid": "1155",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv6_mfwd_ma": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1205",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv6_mpa": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1150",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv6_rib": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v6-routing",
                    "jid": "1147",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ipv6_rump": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v6-routing",
                    "jid": "1168",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "l2tp_mgr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1176",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "l2vpn_mgr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1175",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "mld": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1209",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "mpls_ldp": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1199",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "mpls_static": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1142",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "mrib": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1206",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "mrib6": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1207",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "netconf": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1189",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "nfmgr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1145",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ospf": {
            "instance": {
                "1": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1018",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ospf_uv": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1114",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "pbr_ma": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1171",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "pim": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1210",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "pim6": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1211",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "policy_repository": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1148",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "python_process_manager": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1164",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "qos_ma": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1172",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "rcp_fs": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1165",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "rt_check_mgr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1170",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "schema_server": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1177",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "snmppingd": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1195",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "spa_cfg_hlpr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1130",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ssh_conf_verifier": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1183",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "ssh_server": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1184",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "statsd_manager_g": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "netmgmt",
                    "jid": "1144",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "telemetry_encoder": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1194",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "tty_verifyd": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1166",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "vservice_mgr": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1173",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "wanphy_proc": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1178",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
        "xtc_agent": {
            "instance": {
                "default": {
                    "active": "0/RSP1/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1174",
                    "standby": "0/RSP0/CPU0",
                    "standby_state": "RUNNING",
                }
            }
        },
    }
}
