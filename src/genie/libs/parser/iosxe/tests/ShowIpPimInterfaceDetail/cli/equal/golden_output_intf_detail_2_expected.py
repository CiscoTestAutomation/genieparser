expected_output = {
    "vrf": {
        "VRF1": {
            "interfaces": {
                "GigabitEthernet3": {
                    "address_family": {
                        "ipv4": {
                            "bfd": {"enable": False},
                            "hello_interval": 30,
                            "hello_packets_in": 6,
                            "hello_packets_out": 6,
                            "oper_status": "up",
                            "enable": True,
                            "address": ["10.1.5.1/24"],
                            "multicast": {
                                "switching": "fast",
                                "packets_in": 4,
                                "packets_out": 0,
                                "ttl_threshold": 0,
                                "tag_switching": False,
                            },
                            "pim_status": "enabled",
                            "version": 2,
                            "mode": "passive",
                            "sm": {"passive": True},
                            "dr_address": "10.1.5.5",
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
                }
            }
        }
    }
}
