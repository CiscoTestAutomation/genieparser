expected_output = {
    "entry": {
        "192.168.154.0/24": {
            "mask": "24",
            "type": "internal",
            "known_via": "eigrp 1",
            "ip": "192.168.154.0",
            "redist_via": "eigrp",
            "distance": "130",
            "metric": "10880",
            "redist_via_tag": "1",
            "update": {"age": "2w3d", "interface": "Vlan101", "from": "192.168.151.2"},
            "paths": {
                1: {
                    "age": "2w3d",
                    "interface": "Vlan101",
                    "from": "192.168.151.2",
                    "metric": "10880",
                    "share_count": "1",
                    "nexthop": "192.168.151.2",
                    "prefer_non_rib_labels": False,
                    "merge_labels": False,
                }
            },
        }
    },
    "total_prefixes": 1,
}
