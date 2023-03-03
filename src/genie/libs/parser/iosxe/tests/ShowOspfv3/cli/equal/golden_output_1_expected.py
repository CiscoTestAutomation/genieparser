expected_output = {
"vrf": {
        None: {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "5": {
                            "database_control": {
                                "max_lsa": 200,
                                "max_lsa_current": 8,
                                "max_lsa_current_count": 0,
                                "max_lsa_ignore_count": 2,
                                "max_lsa_ignore_time": 300,
                                "max_lsa_reset_time": 600,
                                "max_lsa_threshold_value": 75,
                                "max_lsa_warning_only": False,
                            },
                            "enable": True,
                            "redistribution": {
                                "bgp": {
                                    "bgp_id": 100
                                    },
                                "connected": {
                                    "enabled": True
                                    },
                                "isis": {
                                    "isis_pid": "1"
                                    },
                            },
                            "router_id": "21.1.1.1",
                        }
                    }
                },
                "ipv6": {
                    "instance": {
                        "5": {
                            "database_control": {
                                "max_lsa": 4294967295,
                                "max_lsa_current": 5,
                                "max_lsa_current_count": 0,
                                "max_lsa_ignore_count": 65535,
                                "max_lsa_ignore_time": 300,
                                "max_lsa_reset_time": 600,
                                "max_lsa_threshold_value": 75,
                                "max_lsa_warning_only": False,
                            },
                            "enable": True,
                            "redistribution": {
                                "connected": {
                                    "enabled": True
                                    },
                                "max_prefix": {
                                    "num_of_prefix": 10101,
                                    "prefix_thld": 75,
                                    "warn_only": True,
                                },
                            },
                            "router_id": "21.1.1.1",
                        }
                    }
                },
            }
        }
    }
}