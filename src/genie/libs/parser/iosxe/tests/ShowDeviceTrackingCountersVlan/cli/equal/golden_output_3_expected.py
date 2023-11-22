expected_output = {
    "vlanid":{
        101:{
            "received":{
                "arp":{
                    "REQ":357478,
                    "REP":937
                }
            },
            "received_broadcast_multicast":{
                "arp":{
                    "REQ":19
                }
            },
            "bridged":{
                "arp":{
                    "REQ":1017
                }
            },
            "broadcast_multicast_to_unicast":{
                "arp":{
                    "REQ":19
                }
            },
            "probe":{
                "probe_send":{
                    "REQ":1017
                },
                "probe_reply":{
                    "REP":901
                }
            },
            "limited_broadcast_to_local":{

            },
            "dropped":{
                "Device-tracking":{
                    "protocol":"arp",
                    "message":"req",
                    "dropped":346176,
                    "reason":{
                        1:{
                            "reason":"Address Family limit per mac reached"
                        },
                        2:{
                            "reason":"Packet accepted but not forwarded"
                        },
                        3:{
                            "reason":"Packet is throttled"
                        },
                        4:{
                            "reason":"Silent drop"
                        },
                        5:{
                            "reason":"Packet accepted but not forwarded"
                        }
                    }
                }
            },
            "faults":[

            ]
        }
    }
}
