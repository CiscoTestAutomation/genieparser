expected_output = {
    "instance": {
        "test": {
            "is_type": "level-1",
            "system_id": "1111.11ff.2222",
            "nsel": "00",
            "manual_area_address": ["49.0001"],
            "routing_for_area_address": ["49.0001"],
            "interfaces": {
                "GigabitEthernet0/1": {"topology": ["ipv4", "ipv6"]},
                "Loopback0": {"topology": ["ipv4", "ipv6"]},
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
