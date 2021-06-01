expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "IPv4 Unicast": {
                    "nexthop": {
                        "10.4.16.16": {
                            "nexthop_id": "0x6000074",
                            "version": "0x0",
                            "nexthop_flags": "0x00000000",
                            "nexthop_handle": "0x7fba00aafccc",
                            "rib_related_information": {
                                "first_interface_handle": {
                                    "0x0c001cc0": {
                                        "gateway_tbl_id": "0xe0000000",
                                        "gateway_flags": "0x00000080",
                                        "gateway_handle": "0x7fba14059ce0",
                                        "gateway": "reachable, non-Connected route, prefix length 32",
                                        "resolving_route": "10.4.16.16/32 (static)",
                                        "paths": 0,
                                        "rib_nexthop_id": "0x0",
                                        "status": "[Reachable][Not Connected][Not Local]",
                                        "metric": 0,
                                        "registration": "Asynchronous",
                                        "completed": "00:02:15",
                                        "events": "Critical (1)/Non-critical (0)",
                                        "last_received": "00:02:14 (Critical)",
                                        "last_gw_update": "(Crit-notif) 00:02:14(rib)",
                                        "reference_count": 1,
                                    }
                                }
                            },
                            "prefix_related_information": {
                                "active_tables": "IPv4 Unicast",
                                "metrics": "0x0",
                                "reference_counts": 1,
                            },
                            "interface_handle": "0x0",
                            "attr_ref_count": 4,
                        }
                    }
                }
            }
        }
    }
}