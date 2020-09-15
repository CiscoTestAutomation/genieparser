expected_output = {
    "GigabitEthernet4": {
        "if_h": 9,
        "index": {
            "0": {
                "queue_id": "0x70",
                "name": "GigabitEthernet4",
                "software_control_info": {
                    "cache_queue_id": "0x00000070",
                    "wred": "0xe73cfde0",
                    "qlimit_pkts": 418,
                    "parent_sid": "0x8d",
                    "debug_name": "GigabitEthernet4",
                    "sw_flags": "0x08000011",
                    "sw_state": "0x00000c01",
                    "port_uidb": 65527,
                    "orig_min": 0,
                    "min": 105000000,
                    "min_qos": 0,
                    "min_dflt": 0,
                    "orig_max": 0,
                    "max": 0,
                    "max_qos": 0,
                    "max_dflt": 0,
                    "share": 1,
                    "plevel": 0,
                    "priority": 65535,
                    "defer_obj_refcnt": 0,
                },
                "statistics": {
                    "tail_drops_bytes": 0,
                    "tail_drops_packets": 0,
                    "total_enqs_bytes": 108648448,
                    "total_enqs_packets": 1697632,
                    "queue_depth_pkts": 0,
                    "lic_throughput_oversub_drops_bytes": 0,
                    "lic_throughput_oversub_drops_packets": 0,
                },
            }
        },
    }
}
