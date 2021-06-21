expected_output = {
    "vlanid": {
        39: {
            "received": {
                "ndp": "RS[55569] NS[18523] NA[19]",
                "acd&dad": "--[18523]"
            },
            "received_broadcast_multicast": {
                "ndp": "RS[55569] NS[18523] NA[19]"
            },
            "bridged": {
                "ndp": "RS[51626] NS[28829]",
                "arp": "REQ[108]",
                "acd&dad": "--[18508]"
            },
            "broadcast_multicast_to_unicast": {},
            "probe": {
                "probe_send": "NS[10321] REQ[108]",
                "probe_reply": "NA[19]"
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
            "fault": ["DHCPv6_REQUEST_NAK[1]"]
        }
    }
}