expected_output = {
    "bit_stats": {
        "firstword": 217,
        "scan": 4,
        "scanread": 132
    },
    "tcp_alg_ports": [
        "5060", "1723", "1720", "139", "137", "135", "389", "111", "8554", "53", "554", "21", "514", "513", "512"
    ],
    "udp_alg_ports": [
        "5060", "1719", "1718", "138", "137", "111", "8554", "69", "53", "554", "496"
    ],
    "if_overload": {
        1: {
            "gaddr": "100.64.100.2",
            "proto": 17,
            "pool_id": "0x490400",
            "mapping_id": "0x2",
            "vrf_id": 0,
            "flags": "0x1",
            "max_ports_available": {
                "lo": 512,
                "hi": "58k"
            },
            "ports_allocated_nat": 1097,
            "ports_used": {
                "lo": 0,
                "hi": 0
            },
            "ports_free": {
                "lo": 73,
                "hi": 1024
            }
        },
        2: {
            "gaddr": "176.16.100.88",
            "proto": 6,
            "pool_id": "0x490400",
            "mapping_id": "0x1",
            "vrf_id": 0,
            "flags": "0x1",
            "max_ports_available": {
                "lo": 512,
                "hi": "58k"
            },
            "ports_allocated_nat": 1097,
            "ports_used": {
                "lo": 0,
                "hi": 0
            },
            "ports_free": {
                "lo": 73,
                "hi": 1024
            }
        },
        3: {
            "gaddr": "100.64.100.2",
            "proto": 1,
            "pool_id": "0xf0000",
            "mapping_id": "0x2",
            "vrf_id": 0,
            "flags": "0xf",
            "max_ports_available": {
                "lo": 1024,
                "hi": "64k"
            },
            "ports_allocated_nat": 65535,
            "ports_used": {
                "lo": 0,
                "hi": 0
            },
            "ports_free": {
                "lo": 0,
                "hi": 65535
            }
        },
        4: {
            "gaddr": "176.16.100.88",
            "proto": 1,
            "pool_id": "0x0",
            "mapping_id": "0x1",
            "vrf_id": 0,
            "flags": "0xf",
            "max_ports_available": {
                "lo": 1024,
                "hi": "64k"
            },
            "ports_allocated_nat": 65535,
            "ports_used": {
                "lo": 0,
                "hi": 0
            },
            "ports_free": {
                "lo": 0,
                "hi": 65535
            }
        },
        5: {
            "gaddr": "100.64.100.2",
            "proto": 6,
            "pool_id": "0x4903fd",
            "mapping_id": "0x2",
            "vrf_id": 0,
            "flags": "0x1",
            "max_ports_available": {
                "lo": 512,
                "hi": "58k"
            },
            "ports_allocated_nat": 1097,
            "ports_used": {
                "lo": 0,
                "hi": 3
            },
            "ports_free": {
                "lo": 73,
                "hi": 1021
            }
        },
        6: {
            "gaddr": "176.16.100.88",
            "proto": 17,
            "pool_id": "0x4903ff",
            "mapping_id": "0x1",
            "vrf_id": 0,
            "flags": "0x1",
            "max_ports_available": {
                "lo": 512,
                "hi": "58k"
            },
            "ports_allocated_nat": 1097,
            "ports_used": {
                "lo": 0,
                "hi": 1
            },
            "ports_free": {
                "lo": 73,
                "hi": 1023
            }
        }
    }
}
