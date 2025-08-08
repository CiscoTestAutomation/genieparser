expected_output = {
    "sessions": {
        "0x00000000": {
            "source_address": "10.1.1.1",
            "source_port": 10001,
            "destination_address": "20.1.1.1",
            "destination_port": 20001,
            "protocol_id": 17,
            "protocol_name": "udp",
            "session_type": "sc",
            "pscb": "0x87408c0",
            "key1_flags": "0x00000000",
            "bucket": "35805",
            "prev": "0x0",
            "next": "0x0",
            "fw_flags": [
                "0x00000004",
                "0x20419841"
            ],
            "vrf_flags": "VRF1-rsrc-limit",
            "proto_state": "Resp-Init No-halfopen-list Active-cnt Session-db Max-session",
            "icmp_error": {
                "count": 0,
                "unreachable_arrived": "no"
            },
            "scb": {
                "state": "active",
                "nxt_timeout": 6000,
                "refcnt": 1
            },
            "ha": {
                "nak_cnt": 0,
                "rg": 0
            },
            "hostdb": "0x0",
            "l7": "0x0",
            "stats": "0x4b851080",
            "child": "0x0",
            "octets": {
                "in": 7000,
                "in_pkts": 70,
                "out": 0,
                "out_pkts": 0
            },
            "cl6_word_1": "0x00000000",
            "proto_hex": "0002",
            "drop_flag": "0x010",
            "root_scb": "0x0",
            "act_blk": "0x4b849000",
            "interfaces": {
                "ingress": "GigabitEthernet0/1/3",
                "ingress_id": 1014,
                "egress": "GigabitEthernet0/1/0",
                "egress_id": 131061
            },
            "timestamps": {
                "current_time": 62063252479,
                "create_time": 61024838182,
                "last_access": 62059920130
            },
            "nat": {
                "out_local": {
                    "ip": "0.0.0.0",
                    "port": 0
                },
                "in_global": {
                    "ip": "0.0.0.0",
                    "port": 0
                }
            },
            "syncookie_fixup": "0x0",
            "halfopen_linkage": [
                "0x0",
                "0x0"
            ],
            "cxsc_cft_fid": "0x00000000",
            "tw_timer": [
                "0x00000000",
                "0x00000000",
                "0x00000000",
                "0x020ab109"
            ],
            "domain_ab1": "0x7045aad0",
            "avc_class_id": 0,
            "sgt": 0,
            "dgt": 0,
            "nat_handles": {
                "handle1": "0x00000000",
                "handle2": "0x00000000"
            },
            "flowdb": {
                "in2out": "0x00000000",
                "in2out_epoch": 0,
                "out2in": "0x00000000",
                "out2in_epoch": 0,
                "ppe_tid": 0
            },
            "session_summary": {
                "icmp_err_time": 0,
                "utd_context_id": 0,
                "action": "block",
                "epoch": "0x1",
                "avc_class_stats": "0x0",
                "vpn_id": {
                    "src": 65535,
                    "dst": 65535
                }
            }
        },
        "0x00000001": {
            "source_address": "10.1.1.2",
            "source_port": 10001,
            "destination_address": "20.1.1.2",
            "destination_port": 20001,
            "protocol_id": 17,
            "protocol_name": "udp",
            "session_type": "sc",
            "pscb": "0x8740a20",
            "key1_flags": "0x00000000",
            "bucket": "37347",
            "prev": "0x0",
            "next": "0x0",
            "fw_flags": [
                "0x00000004",
                "0x20419841"
            ],
            "vrf_flags": "VRF1-rsrc-limit",
            "proto_state": "Resp-Init No-halfopen-list Active-cnt Session-db Max-session",
            "icmp_error": {
                "count": 0,
                "unreachable_arrived": "no"
            },
            "scb": {
                "state": "active",
                "nxt_timeout": 6000,
                "refcnt": 1
            },
            "ha": {
                "nak_cnt": 0,
                "rg": 0
            },
            "hostdb": "0x0",
            "l7": "0x0",
            "stats": "0x4b851080",
            "child": "0x0",
            "octets": {
                "in": 6900,
                "in_pkts": 69,
                "out": 0,
                "out_pkts": 0
            },
            "cl6_word_1": "0x00000000",
            "proto_hex": "0002",
            "drop_flag": "0x010",
            "root_scb": "0x0",
            "act_blk": "0x4b849000",
            "interfaces": {
                "ingress": "GigabitEthernet0/1/3",
                "ingress_id": 1014,
                "egress": "GigabitEthernet0/1/0",
                "egress_id": 131061
            },
            "timestamps": {
                "current_time": 62063292631,
                "create_time": 61032340322,
                "last_access": 62052419485
            },
            "nat": {
                "out_local": {
                    "ip": "0.0.0.0",
                    "port": 0
                },
                "in_global": {
                    "ip": "0.0.0.0",
                    "port": 0
                }
            },
            "syncookie_fixup": "0x0",
            "halfopen_linkage": [
                "0x0",
                "0x0"
            ],
            "cxsc_cft_fid": "0x00000000",
            "tw_timer": [
                "0x00000000",
                "0x00000000",
                "0x00000000",
                "0x02085111"
            ],
            "domain_ab1": "0x7045aad0",
            "avc_class_id": 0,
            "sgt": 0,
            "dgt": 0,
            "nat_handles": {
                "handle1": "0x00000000",
                "handle2": "0x00000000"
            },
            "flowdb": {
                "in2out": "0x00000000",
                "in2out_epoch": 0,
                "out2in": "0x00000000",
                "out2in_epoch": 0,
                "ppe_tid": 0
            },
            "session_summary": {
                "icmp_err_time": 0,
                "utd_context_id": 0,
                "action": "block",
                "epoch": "0x1",
                "avc_class_stats": "0x0",
                "vpn_id": {
                    "src": 65535,
                    "dst": 65535
                }
            }
        }
    }
}
