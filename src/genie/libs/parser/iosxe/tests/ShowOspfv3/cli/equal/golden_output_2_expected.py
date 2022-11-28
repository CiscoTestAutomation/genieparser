expected_output = {
"vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "5": {
                            "database_control": {
                                "max_lsa": 300000,
                                "max_lsa_current": 0,
                                "max_lsa_current_count": 0,
                                "max_lsa_ignore_count": 5,
                                "max_lsa_ignore_time": 300,
                                "max_lsa_reset_time": 660,
                                "max_lsa_threshold_value": 75,
                                "max_lsa_warning_only": False,
                            },
                            "enable": True,
                            "redistribution": {
                                "connected": {
                                    "enabled": True
                                    }
                                },
                            "router_id": "12.1.1.2",
                        }
                    }
                },
                "ipv6": {
                    "instance": {
                        "5": {
                            "database_control": {
                                "max_lsa": 200000,
                                "max_lsa_current": 2,
                                "max_lsa_current_count": 0,
                                "max_lsa_ignore_count": 5,
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
                                    "num_of_prefix": 388899,
                                    "prefix_thld": 76,
                                    "warn_only": False,
                                },
                            },
                            "router_id": "12.1.1.2",
                        }
                    }
                },
            }
        }
    }
}