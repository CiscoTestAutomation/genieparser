expected_output = {
    "lisp_router_instances": {
        0: {
            "service": {
                "ipv4": {
                    "etr": {
                        "local_eids": {
                            "101": {
                                "dynamic_eids": {
                                    "10.10.10.0/24": {
                                        "dynamic_eid_name": "CC-CA01-C-603",
                                        "eid_address": {"virtual_network_id": "blue"},
                                        "global_map_server": True,
                                        "id": "10.10.10.0/24",
                                        "last_dynamic_eid": {
                                            "10.10.10.85": {
                                                "eids": {
                                                    "10.10.10.83": {
                                                        "discovered_by": "packet reception",
                                                        "interface": "Port-channel1.125",
                                                        "last_activity": "00:00:29",
                                                        "uptime": "03:28:27",
                                                    },
                                                    "10.10.10.84": {
                                                        "discovered_by": "packet reception",
                                                        "interface": "Port-channel1.125",
                                                        "last_activity": "00:00:14",
                                                        "uptime": "00:14:10",
                                                    },
                                                    "10.10.10.86": {
                                                        "discovered_by": "packet reception",
                                                        "interface": "Port-channel1.125",
                                                        "last_activity": "00:00:07",
                                                        "uptime": "03:40:08",
                                                    },
                                                },
                                                "last_dynamic_eid_discovery_elaps_time": "00:00:40",
                                            }
                                        },
                                        "num_of_roaming_dynamic_eid": 3,
                                        "registering_more_specific": True,
                                        "rlocs": "CC-CA04-C",
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
