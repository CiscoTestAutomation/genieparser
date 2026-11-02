expected_output = {
    "entry": {
        "2001:db8:1::/64": {
            "ip": "2001:db8:1::",
            "mask": "64",
            "known_via": "bgp 65001",
            "distance": "200",
            "metric": "0",
            "route_count": "1/1",
            "share_count": "0",
            "paths": {
                1: {
                    "fwd_ip": "FE80::1",
                    "fwd_intf": "Ethernet0/0",
                    "age": "00:00:12",
                },
            },
        },
    },
    "total_prefixes": 1,
}
