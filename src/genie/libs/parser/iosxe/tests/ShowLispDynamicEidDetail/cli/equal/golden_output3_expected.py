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
                                        "eid_address": {"virtual_network_id": "green"},
                                        "id": "192.168.0.0/24",
                                        "last_dynamic_eid": {
                                            "192.168.0.1": {
                                                "eids": {
                                                    "192.168.0.1": {
                                                        "discovered_by": "packet reception",
                                                        "interface": "GigabitEthernet5",
                                                        "last_activity": "00:00:15",
                                                        "uptime": "11:56:56",
                                                    }
                                                },
                                                "last_dynamic_eid_discovery_elaps_time": "11:56:56",
                                            }
                                        },
                                        "mapping_servers": {
                                            "10.64.4.4": {"proxy_reply": True},
                                            "10.144.6.6": {},
                                        },
                                        "num_of_roaming_dynamic_eid": 1,
                                        "registering_more_specific": True,
                                        "rlocs": "RLOC",
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
