expected_output = {
    "interface": {
        "Vlan11": {
            "group": {
                2: {
                    "address_family": {
                        "ipv6": {
                            "description": 'State change reason is VRRP_PRIORITY',
                            "state": "MASTER",
                            "state_duration": {
                                "minutes": 0,
                                "seconds": 49.507
                            },
                            "virtual_ip_address": "FE80:11::3",
                            "virtual_mac_address": "0000.5E00.0202",
                            "advertise_interval_secs": 0.11,
                            "preemption": "enabled",
                            "priority": 150,
                            "master_router_ip": "FE80::2AAF:FDFF:FEEA:CCDF",
                            "master_router": "local",
                            "master_router_priority": 150,
                            "master_advertisement_interval_secs": 0.11,
                            "master_advertisement_expiration_secs": 0.089,
                            "master_down_interval_secs": "unknown",
                            "flags": "1/1",
                        }
                    }
                }
            }
        }
    }
}