expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv4": {
                    "rp": {
                        "bidir": {
                            "interface_df_election": {
                                "10.186.0.1 Tunnel9": {
                                    "address": "10.186.0.1",
                                    "interface_name": "Tunnel9",
                                    "metric": 20,
                                    "df_address": "0.0.0.0",
                                    "df_uptime": "00:00:00",
                                    "winner_metric": 20,
                                },
                                "10.186.0.1 Ethernet0/1": {
                                    "address": "10.186.0.1",
                                    "interface_name": "Ethernet0/1",
                                    "metric": 20,
                                    "df_address": "10.4.0.4",
                                    "df_uptime": "00:00:39",
                                    "winner_metric": 20,
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
