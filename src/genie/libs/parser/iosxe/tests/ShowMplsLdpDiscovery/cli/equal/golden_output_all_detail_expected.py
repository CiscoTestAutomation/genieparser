expected_output = {
    "vrf": {
        "default": {
            "local_ldp_identifier": {
                "10.169.197.254:0": {
                    "discovery_sources": {
                        "interfaces": {
                            "GigabitEthernet0/0/0": {
                                "session": "ldp",
                                "hello_interval_ms": 5000,
                                "transport_ip_addr": "10.169.197.254",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {
                                    "10.169.197.252:0": {
                                        "reachable_via": "10.169.197.252/32",
                                        "password": "not required, none, in use",
                                        "holdtime_sec": 15,
                                        "transport_ip_address": "10.169.197.252",
                                        "proposed_peer": 15,
                                        "clients": "IPv4, mLDP",
                                        "source_ip_address": "10.169.197.93",
                                        "proposed_local": 15,
                                    }
                                },
                                "enabled": "Interface config",
                            },
                            "GigabitEthernet0/0/2": {
                                "hello_interval_ms": 5000,
                                "transport_ip_addr": "10.169.197.254",
                                "session": "ldp",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {
                                    "10.169.197.253:0": {
                                        "reachable_via": "10.169.197.253/32",
                                        "password": "not required, none, in use",
                                        "holdtime_sec": 15,
                                        "transport_ip_address": "10.169.197.253",
                                        "proposed_peer": 15,
                                        "clients": "IPv4, mLDP",
                                        "source_ip_address": "10.169.197.97",
                                        "proposed_local": 15,
                                    }
                                },
                                "enabled": "Interface config",
                            },
                        }
                    }
                }
            }
        }
    }
}
