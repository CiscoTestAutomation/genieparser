expected_output = {
    "bgp_id": 5918,
    "vrf": {
        "L3VPN-1151": {
            "neighbor": {
                "192.168.10.253": {
                    "address_family": {
                        "vpnv4": {
                            "activity_paths": "5564978/1540171",
                            "activity_prefixes": "2722671/700066",
                            "as": 61100,
                            "attribute_entries": "5101/4901",
                            "bgp_table_version": 9370786,
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
                            "msg_rcvd": 0,
                            "msg_sent": 0,
                            "output_queue": 0,
                            "path": {"memory_usage": 24360, "total_entries": 203},
                            "prefixes": {"memory_usage": 26112, "total_entries": 102},
                            "route_identifier": "192.168.10.254",
                            "routing_table_version": 9370786,
                            "scan_interval": 60,
                            "state_pfxrcd": "Idle",
                            "tbl_ver": 1,
                            "total_memory": 1482160,
                            "up_down": "never",
                            "version": 4,
                        }
                    }
                }
            }
        }
    },
}
