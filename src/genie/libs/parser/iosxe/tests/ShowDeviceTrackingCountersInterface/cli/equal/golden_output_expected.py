expected_output = {
    "interface": {
        "Twe1/0/42": {
            "received": {
                "ndp": {
                    "RS": 70160,
                    "NS": 20760,
                    "NA": 14
                },
                "acd&dad": 20760
            },
            "received_broadcast_multicast": {
                "ndp": {
                    "RS": 70160,
                    "NS": 20760,
                    "NA": 14
                }
            },
            "bridged": {
                "ndp": {
                    "RS": 58360,
                    "NS": 40648
                },
                "arp": {
                    "REQ": 3
                },
                "acd&dad": 20713
            },
            "broadcast_multicast_to_unicast": {},
            "probe": {
                "probe_send": {
                    "NS": 19935,
                    "REQ": 3
                },
                "probe_reply": {
                    "NA": 14
                }
            },
            "limited_broadcast_to_local": {},
            "dropped": {
                "Flooding Suppress": {
                    "protocol": "ndp",
                    "message": "ns",
                    "dropped": 35
                },
                "ACD&DAD": {
                    "protocol": "--",
                    "message": "--",
                    "dropped": 47
                }
            },
            "faults": ["DHCPv6_REBIND_NAK"]
        }
    }
}