expected_output = {
    "bgp_id": 65109,
    "vrf": {
        "VRF1": {
            "neighbor": {
                "192.168.10.253": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "version": 4,
                            "as": 65555,
                            "msg_rcvd": 20,
                            "msg_sent": 12,
                            "tbl_ver": 189,
                            "input_queue": 0,
                            "output_queue": 0,
                            "up_down": "00:03:52",
                            "state_pfxrcd": "13",
                            "route_identifier": "192.168.10.254",
                            "local_as": 65109,
                            "bgp_table_version": 189,
                            "routing_table_version": 189,
                            "attribute_entries": "110/106",
                            "prefixes": {"total_entries": 25, "memory_usage": 6400},
                            "path": {"total_entries": 38, "memory_usage": 5168},
                            "total_memory": 47488,
                            "activity_prefixes": "226/0",
                            "activity_paths": "339/0",
                            "scan_interval": 60,
                            "cache_entries": {
                                "route-map": {"total_entries": 0, "memory_usage": 0},
                                "filter-list": {"total_entries": 0, "memory_usage": 0},
                            },
                            "entries": {
                                "rrinfo": {"total_entries": 1, "memory_usage": 40},
                                "AS-PATH": {"total_entries": 1, "memory_usage": 24},
                                "community": {"total_entries": 2, "memory_usage": 48},
                            },
                            "community_entries": {
                                "total_entries": 102,
                                "memory_usage": 3248,
                            },
                        }
                    }
                }
            }
        }
    },
}
