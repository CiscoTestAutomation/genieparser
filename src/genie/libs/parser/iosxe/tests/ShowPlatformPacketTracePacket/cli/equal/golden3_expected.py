expected_output = \
{
    "packets": {
        2: {
            "cbug_id": 2,
            "summary": {
                "input": "GigabitEthernet0/1/3",
                "output": "GigabitEthernet0/1/0",
                "state": "FWD",
                "start_timestamp_ns": 11086832720465,
                "start_timestamp": "07/02/2025 18:23:26.637782",
                "stop_timestamp_ns": 11086833456167,
                "stop_timestamp": "07/02/2025 18:23:26.638518"
            },
            "path_trace": {
                "ipv4_output": {
                    "input": "GigabitEthernet0/1/3",
                    "output": "GigabitEthernet0/1/0",
                    "source": "10.1.1.1",
                    "destination": "20.1.1.1",
                    "protocol": "17 (UDP)",
                    "src_port": "10001",
                    "dst_port": "20001"
                },
                "zbfw": {
                    "action": "Fwd",
                    "zone_pair_name": "in-out",
                    "class_map_name": "cmap",
                    "policy_name": "pmap",
                    "input_interface": "GigabitEthernet0/1/3",
                    "egress_interface": "GigabitEthernet0/1/0",
                    "input_vpn_id": "65535",
                    "output_vpn_id": "65535",
                    "input_vrf_id": "Name     : 0:",
                    "output_vrf_id": "Name     : 0:",
                    "avc_classification_id": "0",
                    "avc_classification_name": "N/A",
                    "utd_context_id": "0"
                }
            }
        }
    }
}