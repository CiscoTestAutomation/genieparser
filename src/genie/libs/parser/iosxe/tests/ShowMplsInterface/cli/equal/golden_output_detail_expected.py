expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "GigabitEthernet0/0/0": {
                    "type": "Unknown",
                    "session": "ldp",
                    "ip_labeling_enabled": {
                        True: {"ldp": True, "interface_config": True}
                    },
                    "lsp_tunnel_labeling_enabled": False,
                    "lp_frr_labeling_enabled": False,
                    "bgp_labeling_enabled": False,
                    "mtu": 1552,
                    "mpls_operational": True,
                }
            }
        }
    }
}
