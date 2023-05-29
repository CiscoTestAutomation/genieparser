expected_output = {
    "interface": {
        "TwentyFiveGigE1/0/42": {
            "message_type": {
                "received": {
                    'protocols': {
                        "ndp": {
                            "rs": 70160,
                            "ns": 20760,
                            "na": 14
                        },
                        "acd_dad": 20760
                    },
                },
                "received_broadcast_multicast": {
                    'protocols': {
                        "ndp": {
                            "rs": 70160,
                            "ns": 20760,
                            "na": 14
                        },
                    },
                },
                "bridged": {
                    'protocols': {
                        "ndp": {
                            "rs": 58360,
                            "ns": 40648
                        },
                        "arp": {
                            "req": 3
                        },
                        "acd_dad": 20713
                    },
                },
                "broadcast_multicast_to_unicast": {},
                "probe": {
                    'protocols': {
                        "probe_send": {
                            "ns": 19935,
                            "req": 3
                        },
                        "probe_reply": {
                            "na": 14
                        },
                    },
                },
                "limited_broadcast_to_local": {},
                "dropped": {
                    "feature": {
                        "Flooding Suppress": {
                            "protocol": "ndp",
                            "message": "ns",
                            "dropped": 35,
                            "reason": "NS Owner on input interface"
                        },
                        "ACD_DAD": {
                            "protocol": "--",
                            "message": "--",
                            "dropped": 47
                        }
                    }
                },
                "faults": ["DHCPv6_REBIND_NAK"]
            }
        }
    }
}