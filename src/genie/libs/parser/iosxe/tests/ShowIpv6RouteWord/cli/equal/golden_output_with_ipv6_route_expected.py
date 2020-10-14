expected_output = {
    "total_prefixes": 1,
    "entry": {
        "2001:db8:400:4::4:1/128": {
            "ip": "2001:db8:400:4::4:1",
            "type": "level-2",
            "distance": "115",
            "metric": "20",
            "known_via": "isis",
            "mask": "128",
            "paths": {
                1: {
                    "age": "2w4d",
                    "fwd_intf": "Vlan202",
                    "from": "FE80::EEBD:1DFF:FE09:56C2",
                    "fwd_ip": "FE80::EEBD:1DFF:FE09:56C2",
                }
            },
            "share_count": "0",
            "route_count": "1/1",
        }
    },
}
