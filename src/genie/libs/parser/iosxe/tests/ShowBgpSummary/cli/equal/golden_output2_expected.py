expected_output = {
    "bgp_id": 5918,
    "vrf": {
        "L3VPN-0051": {
            "neighbor": {
                "192.168.10.253": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "activity_paths": "23637710/17596802",
                            "activity_prefixes": "11724891/9708585",
                            "as": 65555,
                            "attribute_entries": "5101/4700",
                            "bgp_table_version": 33086714,
                            "cache_entries": {
                                "filter-list": {"memory_usage": 0, "total_entries": 0},
                                "route-map": {"memory_usage": 0, "total_entries": 0},
                            },
                            "community_entries": {
                                "memory_usage": 60120,
                                "total_entries": 2303,
                            },
                            "entries": {
                                "AS-PATH": {"memory_usage": 4824, "total_entries": 201},
                                "rrinfo": {"memory_usage": 20080, "total_entries": 502},
                            },
                            "input_queue": 0,
                            "local_as": 5918,
                            "msg_rcvd": 619,
                            "msg_sent": 695,
                            "output_queue": 0,
                            "path": {"memory_usage": 900480, "total_entries": 7504},
                            "prefixes": {"memory_usage": 973568, "total_entries": 3803},
                            "route_identifier": "192.168.10.254",
                            "routing_table_version": 33086714,
                            "scan_interval": 60,
                            "state_pfxrcd": "100",
                            "tbl_ver": 33086714,
                            "total_memory": 3305736,
                            "up_down": "05:07:37",
                            "version": 4,
                        }
                    }
                }
            }
        }
    },
}
