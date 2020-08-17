expected_output = {
    "cache_type": "Normal (Platform cache)",
    "cache_size": 200000,
    "current_entries": 1,
    "high_water_mark": 3,
    "flows_added": 16,
    "flows_aged": {"total": 15, "inactive_timeout": 15, "inactive_timeout_secs": 15},
    "entries": {
        1: {
            "ip_vrf_id_input": "0          (DEFAULT)",
            "ipv4_src_addr": "192.168.189.254",
            "ipv4_dst_addr": "192.168.189.253",
            "intf_input": "Null",
            "intf_output": "TenGigabitEthernet0/0/0.1003",
            "pkts": 2,
        },
        2: {
            "ip_vrf_id_input": "0          (DEFAULT)",
            "ipv4_src_addr": "192.168.16.254",
            "ipv4_dst_addr": "192.168.16.253",
            "intf_input": "Null",
            "intf_output": "TenGigabitEthernet0/0/0.1001",
            "pkts": 3,
        },
        3: {
            "ip_vrf_id_input": "0          (DEFAULT)",
            "ipv4_src_addr": "192.168.229.254",
            "ipv4_dst_addr": "192.168.229.253",
            "intf_input": "Null",
            "intf_output": "TenGigabitEthernet0/0/0.1002",
            "pkts": 3,
        },
    },
}
