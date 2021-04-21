expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "GigabitEthernet1": {
                    "address_family": {
                        "ipv4": {
                            "bfd": {"enable": False},
                            "hello_interval": 30,
                            "hello_packets_in": 8,
                            "hello_packets_out": 10,
                            "oper_status": "up",
                            "enable": True,
                            "neighbor_filter": "7",
                            "address": ["10.1.2.1/24"],
                            "multicast": {
                                "switching": "fast",
                                "packets_in": 5,
                                "packets_out": 0,
                                "ttl_threshold": 0,
                                "tag_switching": False,
                            },
                            "pim_status": "enabled",
                            "version": 2,
                            "mode": "sparse",
                            "sm": {},
                            "dr_address": "10.1.2.2",
                            "neighbor_count": 1,
                            "jp_interval": 60,
                            "state_refresh_processing": "enabled",
                            "state_refresh_origination": "disabled",
                            "nbma_mode": "disabled",
                            "atm_multipoint_signalling": "disabled",
                            "bsr_border": False,
                            "neighbors_rpf_proxy_capable": True,
                            "none_dr_join": False,
                        }
                    }
                },
                "GigabitEthernet2": {
                    "address_family": {
                        "ipv4": {
                            "bfd": {"enable": False},
                            "hello_interval": 30,
                            "hello_packets_in": 7,
                            "hello_packets_out": 10,
                            "oper_status": "up",
                            "enable": True,
                            "address": ["10.1.3.1/24"],
                            "multicast": {
                                "switching": "fast",
                                "packets_in": 5,
                                "packets_out": 0,
                                "ttl_threshold": 0,
                                "tag_switching": False,
                            },
                            "pim_status": "enabled",
                            "version": 2,
                            "mode": "dense",
                            "dm": {},
                            "dr_address": "10.1.3.3",
                            "neighbor_count": 1,
                            "jp_interval": 60,
                            "state_refresh_processing": "enabled",
                            "state_refresh_origination": "disabled",
                            "nbma_mode": "disabled",
                            "atm_multipoint_signalling": "disabled",
                            "bsr_border": False,
                            "neighbors_rpf_proxy_capable": True,
                            "none_dr_join": False,
                        }
                    }
                },
                "Loopback0": {
                    "address_family": {
                        "ipv4": {
                            "bfd": {"enable": False},
                            "hello_interval": 30,
                            "hello_packets_in": 8,
                            "hello_packets_out": 8,
                            "oper_status": "up",
                            "enable": True,
                            "address": ["10.4.1.1/32"],
                            "multicast": {
                                "switching": "fast",
                                "packets_in": 0,
                                "packets_out": 0,
                                "ttl_threshold": 0,
                                "tag_switching": False,
                            },
                            "pim_status": "enabled",
                            "version": 2,
                            "mode": "sparse",
                            "sm": {},
                            "dr_address": "10.4.1.1",
                            "neighbor_count": 0,
                            "jp_interval": 60,
                            "state_refresh_processing": "enabled",
                            "state_refresh_origination": "disabled",
                            "nbma_mode": "disabled",
                            "atm_multipoint_signalling": "disabled",
                            "bsr_border": False,
                            "neighbors_rpf_proxy_capable": False,
                            "none_dr_join": False,
                        }
                    }
                },
            }
        }
    }
}
