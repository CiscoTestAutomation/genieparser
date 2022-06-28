expected_output = {
        "Vlan420": {
            "port_channel": {
                "port_channel_member": False
            },
            "link_state": "up",
            "oper_status": "up",
            "enabled": True,
            "line_protocol": "up",
            "autostate": True,
            "description": "VLAN information",
            "ipv4": {
                "10.10.10.1/24": {
                    "ip": "10.10.10.1",
                    "prefix_length": "24"
                }
            },
            "delay": 10,
            "mtu": 1500,
            "bandwidth": 1000000,
            "reliability": "255/255",
            "mac_address": "1234.5678.90ab",
            "types": "EtherSVI",
            "txload": "1/255",
            "rxload": "1/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            'last_clear_counters': 'never',
        }
    }