expected_output = {
    "vrf": {
        "default": {
            "source_address": "172.16.10.13",
            "path": {
                "172.16.121.10 BRI0": {
                    "neighbor_address": "172.16.121.10",
                    "neighbor_host": "sj1.cisco.com",
                    "distance_preferred_lookup": True,
                    "recursion_count": 0,
                    "interface_name": "BRI0",
                    "originated_topology": "ipv4 unicast base",
                    "lookup_topology": "ipv4 multicast base",
                    "route_mask": "172.16.0.0/16",
                    "table_type": "unicast",
                }
            },
            "source_host": "host1",
        }
    }
}
