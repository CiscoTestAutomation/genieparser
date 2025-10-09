expected_output = {  
    "cg_name": {
        "racl_permit_ingress": {
            "cg_id": 11,
            "feature": "Racl",
            "prot": "IPv4",
            "region": "0x78062208",
            "dir": "Ingress",
            "sdk_handles": [
                {
                    "asic": 0,
                    "oid": "0xCA9"
                }
            ],
            "seq": {
                "20": {
                    "ipv4_src_value": "0x46000002",
                    "ipv4_src_mask": "0xffffffff",
                    "ipv4_dst_value": "0x37000000",
                    "ipv4_dst_mask": "0xffffff00",
                    "proto": {
                        "value": "0x0",
                        "mask": "0x0",
                        "tcp_flg": "0x0",
                        "tcp_op": "0x0",
                        "src_port": "0x0",
                        "dst_port": "0x0"
                    },
                    "tos": {
                        "value": "0x0",
                        "mask": "0x0",
                        "ttl": "0x0",
                        "cos": "0x0",
                        "v4_opt": "0x0",
                        "src_obj": "0x0",
                        "dst_obj": "0x0"
                    },
                    "counter_handles": [
                        {
                            "asic": 0,
                            "oid": "0xCAA"
                        }
                    ],
                    "action": "DENY",
                    "logging": "NO_LOG"
                },
                "60": {
                    "ipv4_src_value": "0x00000000",
                    "ipv4_src_mask": "0x00000000",
                    "ipv4_dst_value": "0x00000000",
                    "ipv4_dst_mask": "0x00000000",
                    "proto": {
                        "value": "0xff",
                        "mask": "0x0",
                        "tcp_flg": "0x0",
                        "tcp_op": "0x0",
                        "src_port": "0x0",
                        "dst_port": "0x0"
                    },
                    "tos": {
                        "value": "0x0",
                        "mask": "0x0",
                        "ttl": "0x0",
                        "cos": "0x0",
                        "v4_opt": "0x0",
                        "src_obj": "0x0",
                        "dst_obj": "0x0"
                    },
                    "action": "PERMIT",
                    "logging": "NO_LOG"
                },
                "4294967294": {
                    "ipv4_src_value": "0x00000000",
                    "ipv4_src_mask": "0x00000000",
                    "ipv4_dst_value": "0xe0000000",
                    "ipv4_dst_mask": "0xffffff00",
                    "proto": {
                        "value": "0x0",
                        "mask": "0x0",
                        "tcp_flg": "0x0",
                        "tcp_op": "0x0",
                        "src_port": "0x0",
                        "dst_port": "0x0"
                    },
                    "tos": {
                        "value": "0x0",
                        "mask": "0x0",
                        "ttl": "0x0",
                        "cos": "0x0",
                        "v4_opt": "0x0",
                        "src_obj": "0x0",
                        "dst_obj": "0x0"
                    },
                    "counter_handles": [
                        {
                            "asic": 0,
                            "oid": "0xCAB"
                        }
                    ],
                    "action": "PERMIT",
                    "logging": "NONE"
                }
            }
        }
    }
}