expected_output = {
    "hsr_ring": {
        "HS1": {
            "layer_type": "L2",
            "operation_mode": "mode-H",
            "ports": "2",
            "maxports": "2",
            "port_state": "In",
            "protocol": "Disabled",
            "redbox_mode": "hsr-hsr",
            "ports_in_ring": {
                "Gi1/4": {
                    "logical_slot_port": "1/4",
                    "port_state": "Not-In",
                    "protocol": "Disabled"
                },
                "Gi1/5": {
                    "logical_slot_port": "1/5",
                    "port_state": "Not-In",
                    "protocol": "Disabled"
                }
            },
            "ring_parameters": {
                "redbox_macaddr": "0000.0003.0004",
                "node_forget_time": "60000 ms",
                "node_reboot_interval": "500 ms",
                "entry_forget_time": "400 ms",
                "proxy_node_forget_time": "60000 ms",
                "supervision_frame_cos_option": "0",
                "supervision_frame_cfi_option": "0",
                "supervision_vlan_tag_option": "Disabled",
                "supervision_frame_macda": "0x00",
                "supervision_frame_vlan_id": "0",
                "supervision_frame_time": "3 ms",
                "life_check_interval": "1600 ms",
                "pause_time": "25 ms",
                "fpgamode_dualuplinkenhancement": "Enabled"
            }
        },
        "HS2": {
            "layer_type": "L2",
            "operation_mode": "mode-H",
            "ports": "2",
            "maxports": "2",
            "port_state": "In",
            "protocol": "Disabled",
            "redbox_mode": "hsr-hsr",
            "ports_in_ring": {
                "Gi1/6": {
                    "logical_slot_port": "1/6",
                    "port_state": "Not-In",
                    "protocol": "Disabled"
                },
                "Gi1/7": {
                    "logical_slot_port": "1/7",
                    "port_state": "Not-In",
                    "protocol": "Disabled"
                }
            },
            "ring_parameters": {
                "redbox_macaddr": "0000.0003.0006",
                "node_forget_time": "60000 ms",
                "node_reboot_interval": "500 ms",
                "entry_forget_time": "400 ms",
                "proxy_node_forget_time": "60000 ms",
                "supervision_frame_cos_option": "0",
                "supervision_frame_cfi_option": "0",
                "supervision_vlan_tag_option": "Disabled",
                "supervision_frame_macda": "0x00",
                "supervision_frame_vlan_id": "0",
                "supervision_frame_time": "3 ms",
                "life_check_interval": "1600 ms",
                "pause_time": "25 ms",
                "fpgamode_dualuplinkenhancement": "Enabled"
            }
        }
    }
}
