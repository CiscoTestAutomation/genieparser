expected_output = {
    "cache_type": "Normal (Platform cache)",
    "cache_size": 10000,
    "current_entries": 2,
    "flows_added": 2,
    "flows_aged": 
        {"total": 0},
    "entries": {
        1: {
            "ipv4_src_addr": "5.0.0.1",
            "ipv4_dst_addr": "5.0.0.2",
            "ip_protocol": 17,
            "trns_src_port": 1001,
            "trns_dst_port": 1002,
            "timestamp_abs_first": "22:04:52.000",
            "timestamp_abs_last": "22:05:55.000",
            "intf_input": "Null",
            "intf_output": "Null",
        },
        2: {
            "ipv4_src_addr": "5.0.0.2",
            "ipv4_dst_addr": "5.0.0.1",
            "ip_protocol": 17,
            "trns_src_port": 1002,
            "trns_dst_port": 1001,
            "timestamp_abs_first": "22:04:52.000",
            "timestamp_abs_last": "22:05:55.000",
            "intf_input": "Null",
            "intf_output": "Null",
        },
    },
}

