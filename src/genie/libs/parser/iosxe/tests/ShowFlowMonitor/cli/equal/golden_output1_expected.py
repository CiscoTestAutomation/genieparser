expected_output = {
    "cache_type": "Normal (Platform cache)",
    "cache_size": 16,
    "current_entries": 1,
    "high_water_mark": 1,
    "flows_added": 1,
    "flows_aged": 0,
    "ipv4_src_addr": {
        "10.4.1.10": {
            "ipv4_dst_addr": {
                "10.4.10.1": {
                    "index": {
                        1: {
                            "trns_src_port": 0,
                            "trns_dst_port": 0,
                            "ip_tos": "0xC0",
                            "ip_port": 89,
                            "bytes_long": 100,
                            "pkts_long": 1,
                        },
                        2: {
                            "trns_src_port": 1,
                            "trns_dst_port": 1,
                            "ip_tos": "0xC0",
                            "ip_port": 89,
                            "bytes_long": 100,
                            "pkts_long": 1,
                        },
                    }
                }
            }
        },
        "10.4.1.11": {
            "ipv4_dst_addr": {
                "10.4.10.2": {
                    "index": {
                        1: {
                            "trns_src_port": 0,
                            "trns_dst_port": 0,
                            "ip_tos": "0xC0",
                            "ip_port": 89,
                            "bytes_long": 100,
                            "pkts_long": 1,
                        }
                    }
                }
            }
        },
    },
}
