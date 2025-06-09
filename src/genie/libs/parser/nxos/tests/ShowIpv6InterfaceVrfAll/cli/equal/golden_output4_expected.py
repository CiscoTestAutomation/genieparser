expected_output = {    
    "Vlan902": {
        "iod": 923,
        "interface_status": "protocol-up/link-up/admin-up",
        "vrf": "",
        "enabled": True,
        "ipv6": {
            "7:11:66:1::1/64": {
                "ip": "7:11:66:1::1",
                "prefix_length": "64",
                "status": "valid"
            },
            "ipv6_subnet": "7:11:66:1::/64",
            "ipv6_link_local": "fe80::200:12ff:fe34:5678 ",
            "ipv6_link_local_state": "default",
            "ipv6_ll_state": "valid",
            "ipv6_virtual_add": "none",
            "ipv6_multicast_routing": "disabled",
            "ipv6_report_link_local": "disabled",
            "ipv6_forwarding_feature": "disabled",
            "multicast_groups": True,
            "ipv6_multicast_groups": [
                "ff02::1",
                "ff02::1:ff00:0",
                "ff02::1:ff00:1",
                "ff02::1:ff34:5678",
                "ff02::2"
            ],
            "ipv6_mtu": 1500,
            "ipv6_unicast_rev_path_forwarding": "none",
            "ipv6_load_sharing": "none",
            "ipv6_last_reset": "never",
            "counters": {
                "unicast_packets_forwarded": 0,
                "unicast_packets_originated": 0,
                "unicast_packets_consumed": 0,
                "unicast_bytes_forwarded": 0,
                "unicast_bytes_originated": 0,
                "unicast_bytes_consumed": 0,
                "multicast_packets_forwarded": 0,
                "multicast_packets_originated": 3399,
                "multicast_packets_consumed": 99323,
                "multicast_bytes_forwarded": 0,
                "multicast_bytes_originated": 414438,
                "multicast_bytes_consumed": 8043228
            }
        }
    },
    "Vlan2401": {
        "iod": 1175,
        "interface_status": "protocol-up/link-up/admin-up",
        "vrf": "",
        "enabled": True,
        "ipv6": {
            "rfc_compliant": False,
            "ipv6_link_local": "0:: ",
            "ipv6_link_local_state": "default",
            "ipv6_ll_state": "none",
            "ipv6_virtual_add": "none",
            "ipv6_multicast_routing": "disabled",
            "ipv6_report_link_local": "disabled",
            "ipv6_forwarding_feature": "enabled",
            "ipv6_mtu": 1500,
            "ipv6_unicast_rev_path_forwarding": "none",
            "ipv6_load_sharing": "none",
            "ipv6_last_reset": "never",
            "counters": {
                "unicast_packets_forwarded": 0,
                "unicast_packets_originated": 0,
                "unicast_packets_consumed": 0,
                "unicast_bytes_forwarded": 0,
                "unicast_bytes_originated": 0,
                "unicast_bytes_consumed": 0,
                "multicast_packets_forwarded": 0,
                "multicast_packets_originated": 0,
                "multicast_packets_consumed": 0,
                "multicast_bytes_forwarded": 0,
                "multicast_bytes_originated": 0,
                "multicast_bytes_consumed": 0
            }
        }
    }
}