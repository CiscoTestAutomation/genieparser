expected_output = {
    "vrf": {
        "default": {
            "source_address": "192.168.16.226",
            "source_host": "?",
            "mofrr": "Enabled",
            "path": {
                "192.168.145.2 Ethernet1/4": {
                    "interface_name": "Ethernet1/4",
                    "neighbor_host": "?",
                    "neighbor_address": "192.168.145.2",
                    "table_type": "unicast",
                    "table_feature": "ospf",
                    "table_feature_instance": "200",
                    "distance_preferred_lookup": True,
                    "lookup_topology": "ipv4 multicast base",
                    "originated_topology": "ipv4 unicast base",
                }
            },
        }
    }
}
