expected_output = {
    "vlanid": {
        "39": {
            "received": {
                "ndp": {
                    "RS": 71763,
                    "NS": 23921,
                    "NA": 19
                },
                "acd&dad": 23921
            },
            "received_broadcast_multicast": {
                "ndp": {
                    "RS": 71763,
                    "NS": 23921,
                    "NA": 19
                }
            },
            "bridged": {
                "ndp": {
                    "RS": 67820,
                    "NS": 34227
                },
                "arp": {
                    "REQ": 113
                },
                "acd&dad": 23906
            },
            "broadcast_multicast_to_unicast": {},
            "probe": {
                "probe_send": {
                    "NS": 10321,
                    "REQ": 113
                },
                "probe_reply": {
                    "NA": 19
                }
            },
            "limited_broadcast_to_local": {},
            "dropped": {
                "Device-tracking": {
                    "protocol": "ndp",
                    "message": "ns",
                    "dropped": 15
                },
                "ACD&DAD": {
                    "protocol": "--",
                    "message": "--",
                    "dropped": 15
                }
            },
            "faults": []
        }
    }
}