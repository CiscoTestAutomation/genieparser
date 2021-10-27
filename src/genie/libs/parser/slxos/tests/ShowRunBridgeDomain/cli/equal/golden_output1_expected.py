expected_output = {
    "bridge_domains": {
        20: {
            "bpdu_drop_enable": True,
            "bridge_domain_id": 20,
            "bridge_domain_type": "p2mp",
            "local_switching": True,
            "logical_interfaces": {
                "ethernet": {
                    "0/30.1": {"lif_bind_id": "Ethernet 0/30.1"},
                    "0/30.2": {"lif_bind_id": "Ethernet 0/30.2"},
                },
                "port_channel": {
                    "100.1": {"pc_lif_bind_id": "Port-channel 100.1"},
                    "100.2": {"pc_lif_bind_id": "Port-channel 100.2"},
                },
            },
            "mac_address": {"withdrawal": True},
            "peers": {
                "1.1.1.1": {
                    "lsps": {
                        "abc": {"lsp_name": "abc"},
                        "def": {"lsp_name": "def"},
                        "ed": {"lsp_name": "ed"},
                    },
                    "peer_ip": "1.1.1.1",
                },
                "3.3.3.3": {
                    "lsps": {
                        "1": {"lsp_name": "1"},
                        "abc": {"lsp_name": "abc"},
                        "cos": {"lsp_name": "cos"},
                    },
                    "peer_ip": "3.3.3.3",
                },
                "4.4.4.4": {
                    "control_word": True,
                    "cos": 4,
                    "flow_label": True,
                    "load_balance": True,
                    "lsps": {
                        "abc": {"lsp_name": "abc"},
                        "ds": {"lsp_name": "ds"}
                    },
                    "peer_ip": "4.4.4.4",
                },
            },
            "pw_profile_name": "default",
            "statistics": True,
            "suppress_arp": {"suppress_arp_enable": True},
            "suppress_nd": {"suppress_nd_enable": True},
            "vc_id_num": 20,
        },
        30: {
            "bridge_domain_id": 30,
            "bridge_domain_type": "p2p",
            "logical_interfaces": {
                "ethernet": {},
                "port_channel": {
                    "1.300": {
                        "pc_lif_bind_id": "Port-channel 1.300"
                    }
                },
            },
            "peers": {
                "100.1.234.6": {
                    "control_word": True,
                    "cos": 1,
                    "flow_label": True,
                    "load_balance": True,
                    "peer_ip": "100.1.234.6",
                }
            },
            "pw_profile_name": "class-fat",
            "vc_id_num": 20030,
        },
        40: {
            "bpdu_drop_enable": True,
            "bridge_domain_id": 40,
            "bridge_domain_type": "p2mp",
            "description": "test",
            "local_switching": True,
            "mac_address": {"withdrawal": True},
            "pw_profile_name": "default",
            "statistics": True,
        },
    }
}
