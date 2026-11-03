expected_output = {
    "cg_name": {
        "racl_permit_ingress": {
            "cg_id": 15,
            "feature": "Racl",
            "prot": "IPv4",
            "region": "0x7c079cd8",
            "dir": "Ingress",
            "sdk_handles": [{"asic": 0, "oid": "0xB44"}],
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
                        "dst_port": "0x0",
                    },
                    "tos": {
                        "value": "0x0",
                        "mask": "0x0",
                        "ttl": "0x0",
                        "cos": "0x0",
                        "v4_opt": "0x0",
                        "src_obj": "0x0",
                        "dst_obj": "0x0",
                    },
                    "counter_handles": [{"asic": 0, "oid": "0xB45"}],
                    "action": "DENY",
                    "logging": "NO_LOG",
                }
            },
        }
    }
}
