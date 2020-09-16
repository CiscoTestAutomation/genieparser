expected_output = {
    "bgp_id": 5918,
    "vrf": {
        "default": {
            "neighbor": {
                "192.168.10.253": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "activity_paths": "5564772/1540171",
                            "activity_prefixes": "2722567/700066",
                            "as": 60103,
                            "attribute_entries": "5098/4898",
                            "bgp_table_version": 9370482,
                            "cache_entries": {
                                "filter-list": {"memory_usage": 0, "total_entries": 0},
                                "route-map": {"memory_usage": 0, "total_entries": 0},
                            },
                            "community_entries": {
                                "memory_usage": 60056,
                                "total_entries": 2301,
                            },
                            "entries": {
                                "AS-PATH": {"memory_usage": 4824, "total_entries": 201},
                                "rrinfo": {"memory_usage": 20080, "total_entries": 502},
                            },
                            "input_queue": 0,
                            "local_as": 5918,
                            "msg_rcvd": 0,
                            "msg_sent": 0,
                            "output_queue": 0,
                            "path": {
                                "memory_usage": 482879760,
                                "total_entries": 4023998,
                            },
                            "prefixes": {
                                "memory_usage": 517657344,
                                "total_entries": 2022099,
                            },
                            "route_identifier": "10.169.197.254",
                            "routing_table_version": 9370482,
                            "scan_interval": 60,
                            "state_pfxrcd": "Idle",
                            "tbl_ver": 1,
                            "total_memory": 1001967936,
                            "up_down": "never",
                            "version": 4,
                        }
                    }
                }
            }
        }
    },
}
