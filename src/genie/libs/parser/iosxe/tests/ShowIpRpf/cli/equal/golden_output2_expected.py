expected_output = {
    "vrf": {
        "VRF1": {
            "source_host": "?",
            "source_address": "10.1.1.100",
            "path": {
                "10.1.1.5 Ethernet3/0": {
                    "neighbor_address": "10.1.1.5",
                    "table_feature": "rip",
                    "neighbor_host": "?",
                    "interface_name": "Ethernet3/0",
                    "table_type": "unicast",
                    "lookup_vrf": "blue",
                    "recursion_count": 0,
                    "distance_preferred_lookup": True,
                    "route_mask": "10.1.1.0/24",
                }
            },
        }
    }
}
