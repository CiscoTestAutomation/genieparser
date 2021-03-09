expected_output = {
    "interface": {
        "GigabitEthernet1": {
            "group": {
                100: {
                    "advertise_interval_secs": 1.0,
                    "auth_text": "hash",
                    "description": "DC-LAN Subnet",
                    "master_advertisement_interval_secs": 1.0,
                    "master_down_interval_secs": 3.531,
                    "master_router": "local",
                    "master_router_ip": "192.168.1.233",
                    "master_router_priority": 120,
                    "preemption": "enabled",
                    "priority": 120,
                    "state": "Master",
                    "virtual_ip_address": "192.168.10.1",
                    "virtual_mac_address": "0000.5eff.0164",  
                    "vrrs_name": {
                        "DC_LAN": {
                            "track_object":
                               {1:
                                   {"decrement": 30,
                                    "state": "Up"}}
                        }
                    },
                }
            }
        }
    }
}