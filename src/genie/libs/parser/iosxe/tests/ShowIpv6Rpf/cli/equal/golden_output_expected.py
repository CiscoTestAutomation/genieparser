expected_output = {
    "vrf": {
        "default": {
            "source_address": "2001:99:99::99",
            "path": {
                "2001:99:99::99 GigabitEthernet1 128": {
                    "table_type": "mroute",
                    "admin_distance": "128",
                    "recursion_count": 0,
                    "interface_name": "GigabitEthernet1",
                    "metric": 0,
                    "neighbor_address": "2001:99:99::99",
                    "route_mask": "2001:99:99::99/128",
                }
            },
        }
    }
}
