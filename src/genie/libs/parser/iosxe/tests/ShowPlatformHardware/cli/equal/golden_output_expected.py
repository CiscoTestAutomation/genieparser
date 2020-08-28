expected_output = {
    "TenGigabitEthernet0/0/0": {
        "if_h": 7,
        "index": {
            "0": {
                "queue_id": "0xcc8",
                "name": "TenGigabitEthernet0/0/0",
                "software_control_info": {
                    "cache_queue_id": "0x00000cc8",
                    "wred": "0x5218622c",
                    "qlimit_bytes": 65625002,
                    "parent_sid": "0x28194",
                    "debug_name": "TenGigabitEthernet0/0/0",
                    "sw_flags": "0x08000011",
                    "sw_state": "0x00000801",
                    "port_uidb": 262137,
                    "orig_min": 0,
                    "min": 1050000000,
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
                    "cp_ppe_addr": "0x00000000",
                },
                "statistics": {
                    "tail_drops_bytes": 0,
                    "tail_drops_packets": 0,
                    "total_enqs_bytes": 19215977960,
                    "total_enqs_packets": 82176494,
                    "queue_depth_bytes": 0,
                    "lic_throughput_oversub_drops_bytes": 0,
                    "lic_throughput_oversub_drops_packets": 0,
                },
            }
        },
    }
}
