expected_output = {
    "vrf": {
        "1": {
            "vrf_id": "3",
            "vrf_state": "up",
            "vnid": "91100",
            "topo_id": "1100",
            "encap_type": "VXLAN",
            "vtep_ip": "1.1.1.1",
            "vtep_virtual_ip": "1.1.1.1",
            "vtep_vip_r": "0.0.0.0",
            "router_mac": "648f.3e27.eb89",
            "vip_derived_mac": "648f.3e27.e789",
            "router_id": "1.1.1.1",
            "conf_router_id": "0.0.0.0",
            "confed_id": 0,
            "cluster_id": "0.0.0.0",
            "num_conf_peers": 0,
            "num_pending_conf_peers": 0,
            "num_established_peers": 0,
            "vrf_rd": "1.1.1.1:3",
            "address_family": {
                "ipv4 unicast": {
                    "table_id": "0x3",
                    "table_state": "up",
                    "peers": {
                        0: {
                            "active_peers": 0,
                            "routes": 97,
                            "paths": 199,
                            "networks": 3,
                            "aggregates": 0
                        }
                    },
                    "export_rt_list": "ASnumber:100 ASnumber:91100",
                    "import_rt_list": "ASnumber:100 ASnumber:91100",
                    "evpn_export_rt_list": "ASnumber:100 ASnumber:91100",
                    "evpn_import_rt_list": "ASnumber:100 ASnumber:91100",
                    "mvpn_export_rt_list": "ASnumber:91100",
                    "mvpn_import_rt_list": "ASnumber:91100",
                    "label_mode": "per-vrf",
                    "next_hop_trigger_delay": {
                        "critical": 3000,
                        "non_critical": 10000
                    }
                },
                "ipv6 unicast": {
                    "table_id": "0x80000003",
                    "table_state": "up",
                    "peers": {
                        0: {
                            "active_peers": 0,
                            "routes": 0,
                            "paths": 0,
                            "networks": 0,
                            "aggregates": 0
                        }
                    },
                    "export_rt_list": "ASnumber:91100",
                    "import_rt_list": "ASnumber:91100",
                    "evpn_export_rt_list": "ASnumber:91100",
                    "evpn_import_rt_list": "ASnumber:91100",
                    "mvpn_export_rt_list": "ASnumber:91100",
                    "mvpn_import_rt_list": "ASnumber:91100",
                    "label_mode": "per-vrf",
                    "next_hop_trigger_delay": {
                        "critical": 3000,
                        "non_critical": 10000
                    }
                }
            }
        }
    }
}
