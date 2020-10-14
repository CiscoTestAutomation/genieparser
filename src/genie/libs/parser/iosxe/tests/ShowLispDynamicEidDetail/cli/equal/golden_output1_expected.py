expected_output = {
    "lisp_router_instances": {
        0: {
            "service": {
                "ipv4": {
                    "etr": {
                        "local_eids": {
                            "101": {
                                "dynamic_eids": {
                                    "192.168.0.0/24": {
                                        "dynamic_eid_name": "192",
                                        "eid_address": {"virtual_network_id": "red"},
                                        "global_map_server": True,
                                        "id": "192.168.0.0/24",
                                        "last_dynamic_eid": {
                                            "192.168.0.1": {
                                                "eids": {
                                                    "192.168.0.1": {
                                                        "discovered_by": "packet reception",
                                                        "interface": "GigabitEthernet5",
                                                        "last_activity": "00:00:23",
                                                        "uptime": "01:17:25",
                                                    }
                                                },
                                                "last_dynamic_eid_discovery_elaps_time": "01:17:25",
                                            }
                                        },
                                        "num_of_roaming_dynamic_eid": 1,
                                        "registering_more_specific": True,
                                        "rlocs": "RLOC",
                                        "site_based_multicast_map_notify_group": "none configured",
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
