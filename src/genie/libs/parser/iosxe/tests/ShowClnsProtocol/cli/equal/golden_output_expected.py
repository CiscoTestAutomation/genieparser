expected_output = {
    "instance": {
        "VRF1": {
            "system_id": "2222.22ff.4444",
            "nsel": "00",
            "process_handle": "0x10001",
            "is_type": "level-1-2",
            "manual_area_address": ["49.0001"],
            "routing_for_area_address": ["49.0001"],
            "interfaces": {
                "GigabitEthernet4": {"topology": ["ipv4", "ipv6"]},
                "Loopback1": {"topology": ["ipv4", "ipv6"]},
            },
            "redistribute": "static (on by default)",
            "distance_for_l2_clns_routes": 110,
            "rrr_level": "none",
            "metrics": {
                "generate_narrow": "none",
                "accept_narrow": "none",
                "generate_wide": "level-1-2",
                "accept_wide": "level-1-2",
            },
        }
    }
}
