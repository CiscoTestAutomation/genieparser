expected_output = {
    "vrf": {
        "VRF1": {
            "interfaces": {
                "GigabitEthernet15": {
                    "address_family": {
                        "ipv4": {
                            "enable": False,
                            "oper_status": "down",
                            "internet_protocol_processing": False,
                        }
                    }
                },
                "GigabitEthernet16": {
                    "address_family": {
                        "ipv4": {
                            "atm_multipoint_signalling": "disabled",
                            "bfd": {"enable": False},
                            "bsr_border": False,
                            "dr_address": "0.0.0.0",
                            "enable": False,
                            "hello_interval": 30,
                            "hello_packets_in": 0,
                            "hello_packets_out": 0,
                            "jp_interval": 60,
                            "mode": "sparse",
                            "multicast": {
                                "packets_in": 0,
                                "packets_out": 0,
                                "switching": "fast",
                                "tag_switching": False,
                                "ttl_threshold": 0,
                            },
                            "nbma_mode": "disabled",
                            "neighbor_count": 0,
                            "neighbors_rpf_proxy_capable": False,
                            "none_dr_join": False,
                            "oper_status": "down",
                            "pim_status": "enabled",
                            "sm": {},
                            "state_refresh_origination": "disabled",
                            "state_refresh_processing": "enabled",
                            "version": 2,
                        }
                    }
                },
                "Loopback0": {
                    "address_family": {
                        "ipv4": {
                            "address": ["10.4.4.14/32"],
                            "atm_multipoint_signalling": "disabled",
                            "bfd": {"enable": False},
                            "bsr_border": False,
                            "dr_address": "10.4.4.14",
                            "enable": True,
                            "hello_interval": 30,
                            "hello_packets_in": 45876,
                            "hello_packets_out": 45876,
                            "jp_interval": 60,
                            "mode": "sparse",
                            "multicast": {
                                "packets_in": 0,
                                "packets_out": 0,
                                "switching": "fast",
                                "tag_switching": False,
                                "ttl_threshold": 0,
                            },
                            "nbma_mode": "disabled",
                            "neighbor_count": 0,
                            "neighbors_rpf_proxy_capable": False,
                            "none_dr_join": False,
                            "oper_status": "up",
                            "pim_status": "enabled",
                            "sm": {},
                            "state_refresh_origination": "disabled",
                            "state_refresh_processing": "enabled",
                            "version": 2,
                        }
                    }
                },
                "Loopback8": {
                    "address_family": {
                        "ipv4": {
                            "enable": True,
                            "oper_status": "up",
                            "internet_protocol_processing": False,
                        }
                    }
                },
            }
        }
    }
}
