expected_output = {
    "interface": {
        "TenGigabitEthernet1/0/1": {
            "cgid": "0x738310",
            "no_of_classes": 1,
            "tcg_ref_count": 1,
            "filter_state": "UP TO DATE",
            "vmr_state": "UP TO DATE",
        }
    },
    "ipv4_acl": {
        "oid": "0x908",
        "number_of_aces": 1,
        "ace": {
            0: {
                "class_id": "0x0",
                "ipv4_src_address": "0.0.0.0",
                "ipv4_src_mask": "0.0.0.0",
                "ipv4_dst_address": "0.0.0.0",
                "ipv4_dst_mask": "0.0.0.0",
                "protocol": "0x0",
                "protocol_mask": "0x0",
                "dscp": "0x0",
                "dscp_mask": "0x0",
                "ttl_start": "0x0",
                "ttl_end": "0x0",
                "tcp_flags": "0x0",
                "tcp_mask": "0x0",
                "ip_flags": "0x0",
                "ip_mask": "0x0",
                "src_port_start": "0x0",
                "src_port_end": "0x0",
                "dst_port_start": "0x0",
                "dst_port_end": "0x0",
            }
        },
    },
}
