expected_output = {
    "vlanid": {
        39: {
            "received": {
                "ndp": {
                    "RS": 72027,
                    "NS": 24009,
                    "NA": 19
                },
                "acd&dad": 24009
            },
            "received_broadcast_multicast": {
                "ndp": {
                    "RS": 72027,
                    "NS": 24009,
                    "NA": 19
                }
            },
            "bridged": {
                "ndp": {
                    "RS": 68084,
                    "NS": 34315
                },
                "arp": {
                    "REQ": 132
                },
                "acd&dad": 23994
            },
            "broadcast_multicast_to_unicast": {},
            "probe": {
                "probe_send": {
                    "NS": 10321,
                    "REQ": 132
                },
                "probe_reply": {
                    "NA": 19
                }
            },
            "limited_broadcast_to_local": {},
            "dropped":{
                "Device-tracking":{
                    "protocol":"ndp",
                    "message":"ns",
                    "dropped":15,
                    "reason":{
                        1:{
                            "reason":"Silent drop"
                        },
                        2:{
                            "reason":"Silent drop"
                        }
                    }
                },
                "ACD&DAD":{
                    "protocol":"--",
                    "message":"--",
                    "dropped":15
                }
            },
            "faults": []
        }
    }
}
