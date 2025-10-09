expected_output = {
    "vrf": {
        "Campus": {
            "source_address": "1.1.1.1",
            "source_host": "?",
            "path": {
                "172.19.1.64 LISP0.4099": {
                    "interface_name": "LISP0.4099",
                    "neighbor_host": "?",
                    "neighbor_address": "172.19.1.64",
                    "route_mask": "0.0.0.0/5",
                    "table_type": "unicast",
                    "distance_preferred_lookup": True,
                    "lookup_topology": "ipv4 multicast base"
                }
            }
        }
    }
}
