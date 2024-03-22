expected_output = {
    "vlanid":{
        20:{
            "received":{
                "ndp":{
                    "RA":5,
                    "NS":12,
                    "NA":8
                },
                "dhcpv6":{
                    "SOL":1,
                    "ADV":1,
                    "REQ":1,
                    "REN":42,
                    "REB":1,
                    "REP":44
                },
                "arp":{
                    "REQ":1,
                    "REP":3
                },
                "dhcpv4":{
                    "DIS":1,
                    "OFFR":1,
                    "REQ4":1,
                    "ACK":1
                },
                "acd&dad":3
            },
            "received_broadcast_multicast":{
                "ndp":{
                    "RA":5,
                    "NS":6,
                    "NA":2
                },
                "dhcpv6":{
                    "SOL":1,
                    "REQ":1,
                    "REN":42,
                    "REB":1
                },
                "arp":{
                    "REQ":1,
                    "REP":2
                },
                "dhcpv4":{
                    "DIS":1,
                    "OFFR":1,
                    "REQ4":1,
                    "ACK":1
                }
            },
            "bridged":{
                "ndp":{
                    "NS":12,
                    "NA":8
                },
                "dhcpv6":{
                    "SOL":1,
                    "ADV":1,
                    "REQ":1,
                    "REN":42,
                    "REB":1,
                    "REP":44
                },
                "acd&dad":3
            },
            "broadcast_multicast_to_unicast":{
                
            },
            "probe":{
                
            },
            "limited_broadcast_to_local":{
                
            },
            "dropped":{
                "RA guard":{
                    "protocol":"ndp",
                    "message":"ra",
                    "dropped":5,
                    "reason": {
                        1: {
                            "reason": "Message unauthorized on port"
                        }
                    }
                }
            },
            "faults":[
                
            ]
        }
    }
}
