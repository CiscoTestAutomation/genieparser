expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "bidir": {
                            "interface_df_election": {
                                "10.10.0.2 Ethernet3/3": {
                                    "df_address": "10.4.0.2",
                                    "metric": 0,
                                    "df_uptime": "00:03:49",
                                    "address": "10.10.0.2",
                                    "winner_metric": 0,
                                    "interface_name": "Ethernet3/3",
                                },
                                "10.10.0.3 Ethernet3/3": {
                                    "df_address": "10.4.0.3",
                                    "metric": 0,
                                    "df_uptime": "00:01:49",
                                    "address": "10.10.0.3",
                                    "winner_metric": 0,
                                    "interface_name": "Ethernet3/3",
                                },
                                "10.10.0.3 Ethernet3/4": {
                                    "df_address": "10.5.0.2",
                                    "metric": 409600,
                                    "df_uptime": "00:02:32",
                                    "address": "10.10.0.3",
                                    "winner_metric": 409600,
                                    "interface_name": "Ethernet3/4",
                                },
                                "10.10.0.5 Ethernet3/4": {
                                    "df_address": "10.5.0.2",
                                    "metric": 435200,
                                    "df_uptime": "00:02:16",
                                    "address": "10.10.0.5",
                                    "winner_metric": 435200,
                                    "interface_name": "Ethernet3/4",
                                },
                                "10.10.0.2 Loopback0": {
                                    "df_address": "10.10.0.2",
                                    "metric": 0,
                                    "df_uptime": "00:03:49",
                                    "address": "10.10.0.2",
                                    "winner_metric": 0,
                                    "interface_name": "Loopback0",
                                },
                                "10.10.0.2 Ethernet3/4": {
                                    "df_address": "10.5.0.2",
                                    "metric": 0,
                                    "df_uptime": "00:03:49",
                                    "address": "10.10.0.2",
                                    "winner_metric": 0,
                                    "interface_name": "Ethernet3/4",
                                },
                                "10.10.0.3 Loopback0": {
                                    "df_address": "10.10.0.2",
                                    "metric": 409600,
                                    "df_uptime": "00:02:32",
                                    "address": "10.10.0.3",
                                    "winner_metric": 409600,
                                    "interface_name": "Loopback0",
                                },
                                "10.10.0.5 Loopback0": {
                                    "df_address": "10.10.0.2",
                                    "metric": 435200,
                                    "df_uptime": "00:02:16",
                                    "address": "10.10.0.5",
                                    "winner_metric": 435200,
                                    "interface_name": "Loopback0",
                                },
                                "10.10.0.5 Ethernet3/3": {
                                    "df_address": "10.4.0.4",
                                    "metric": 409600,
                                    "df_uptime": "00:01:49",
                                    "address": "10.10.0.5",
                                    "winner_metric": 409600,
                                    "interface_name": "Ethernet3/3",
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
