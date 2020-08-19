expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "Port-channel1.100": {
                    "address_family": {
                        "ipv4": {
                            "neighbors": {
                                "192.168.4.1": {
                                    "dr_priority": 1,
                                    "state_refresh_capable": True,
                                    "proxy_capable": True,
                                    "interface": "Port-channel1.100",
                                    "genid_capable": True,
                                    "version": "v2",
                                    "expiration": "00:01:40",
                                    "up_time": "4w4d",
                                }
                            }
                        }
                    }
                },
                "GigabitEthernet0/2/3.100": {
                    "address_family": {
                        "ipv4": {
                            "neighbors": {
                                "192.168.205.2": {
                                    "dr_priority": 1,
                                    "designated_router": True,
                                    "proxy_capable": True,
                                    "interface": "GigabitEthernet0/2/3.100",
                                    "bidir_capable": True,
                                    "expiration": "00:01:19",
                                    "version": "v2",
                                    "state_refresh_capable": True,
                                    "genid_capable": True,
                                    "up_time": "4w4d",
                                }
                            }
                        }
                    }
                },
            }
        }
    }
}
