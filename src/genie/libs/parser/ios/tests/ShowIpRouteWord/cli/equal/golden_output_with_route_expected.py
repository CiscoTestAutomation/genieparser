expected_output = {
    "entry": {
        "192.168.234.0/24": {
            "mask": "24",
            "type": "internal",
            "known_via": "eigrp 1",
            "ip": "192.168.234.0",
            "redist_via": "eigrp",
            "distance": "90",
            "metric": "3072",
            "redist_via_tag": "1",
            "update": {
                "age": "3d04h",
                "interface": "GigabitEthernet0/2.4",
                "from": "192.168.9.2",
            },
            "paths": {
                1: {
                    "age": "3d04h",
                    "interface": "GigabitEthernet0/2.4",
                    "from": "192.168.9.2",
                    "metric": "3072",
                    "share_count": "1",
                    "nexthop": "192.168.9.2",
                    "merge_labels": False,
                    "prefer_non_rib_labels": False,
                }
            },
        }
    },
    "total_prefixes": 1,
}
