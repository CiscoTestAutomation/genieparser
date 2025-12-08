expected_output = {
    "global": {
        "address": "0x020001a1",
        "ha_state": "Allow-New-Sess",
        "fw_configured": "0x00000020",
        "init_done": "0x00000080",
        "init_requested": "0x00000100",
        "syslog_deployed": "0x02000000"
    },
    "global2": {
        "address": "0x190000b7",
        "salt": 183,
        "global_num_simul_pkt_per_sess_allowed": 0,
        "default_num_simul_pkt_per_sess_allowed": 25
    },
    "global3": {
        "address": "0x00000009",
        "same_zone_policy": "0x00000001",
        "vpn_zone_security": "0x00000008",
        "teardowns": 0,
        "pam_cce": "0x0 00000000",
        "num_zp_with_policy": 1,
        "high_priority_recycle_queue_addr": "0x84969ea0",
        "low_priority_recycle_queue_addr": "0x84969eb0",
        "lock_upgrades": 0,
        "half_open_aggressive_aging": 0,
        "num_ack_exceeds_limit": 0,
        "num_rst_exceeds_limit": 0,
        "unknown_vrf_limit_exceeds": 0,
        "syncookie_over_rate_cnt": 0,
        "fw_tcp_session_termination_rst_segment_control": {
            "halfopen": {
                "rst_sent": 0,
                "blocked": 0
            },
            "idle": {
                "rst_sent": 0,
                "blocked": 0
            },
            "halfclose": {
                "rst_sent": 0,
                "blocked": 0
            }
        },
        "nat_caching": {
            "nat_registration": 1,
            "nat_unregistration": 1,
            "too_many_nat_sessions": 0,
            "cant_register_with_nat": 0,
            "invalid_nat_session": 0,
            "no_nat_session_caching": 0,
            "nat_cached_session": 0
        },
        "l2_firewall": {
            "l2_unknown_encap": 0,
            "l2_skip_tcp_pkt": 0,
            "timer_stop_failed": 0
        },
        "vrf_global_action_block": {
            "l7_inspection_disable_flags": "0x0"
        },
        "total_sessions": {
            "max_limit": 4294967295,
            "current_count": 0,
            "exceed": 0,
            "aggr_age_high_watermark": 4294967295,
            "aggr_age_low_watermark": 0,
            "num_times_enter_aggr_age": 0,
            "aggr_age_period": "off"
        },
        "tcp_syn_cookie": {
            "max_limit": 4294967295,
            "current_count": 0,
            "exceed": 0
        },
        "total_half_open_sessions": {
            "max_limit": 4294967295,
            "current_count": 0,
            "exceed": 0,
            "aggr_age_high_watermark": 4294967295,
            "aggr_age_low_watermark": 0,
            "num_times_enter_aggr_age": 0,
            "aggr_age_period": "off"
        },
        "tcp_half_open_sessions": {
            "max_limit": 4294967295,
            "current_count": 0,
            "exceed": 0
        },
        "udp_half_open_sessions": {
            "max_limit": 4294967295,
            "current_count": 0,
            "exceed": 0
        },
        "icmp_half_open_sessions": {
            "max_limit": 4294967295,
            "current_count": 0,
            "exceed": 0
        },
        "domain_flags": "0x0",
        "box_action_block": {
            "l7_inspection_disable_flags": "0x0"
        },
        "current_count": {
            "total_sessions": 0,
            "aggr_age_high_watermark": 4294967295,
            "aggr_age_low_watermark": 0,
            "num_times_enter_aggr_age": 0,
            "aggr_age_period": "off",
            "tcp_syn_cookie": {
                "max_limit": 4294967295,
                "current_count": 0,
                "exceed": 0
            },
            "total_half_open_sessions": {
                "max_limit": 4294967295,
                "current_count": 0,
                "exceed": 0,
                "aggr_age_high_watermark": 4294967295,
                "aggr_age_low_watermark": 0,
                "num_times_enter_aggr_age": 0,
                "aggr_age_period": "off"
            },
            "tcp_half_open_sessions": {
                "max_limit": 4294967295,
                "current_count": 0,
                "exceed": 0
            },
            "udp_half_open_sessions": {
                "max_limit": 4294967295,
                "current_count": 0,
                "exceed": 0
            },
            "icmp_half_open_sessions": {
                "max_limit": 4294967295,
                "current_count": 0,
                "exceed": 0
            },
            "domain_flags": "0x0"
        },
        "fw_persona_alert_rlimit": 0,
        "backpressure": "0x0",
        "invalid_rg_exceeds_max_rg": 0,
        "invalid_ha_message_version": 0,
        "rii_hash_table": {
            "address": "0x093c9c10",
            "size": 128
        },
        "vrf_action_table": {
            "address": "0x0x1237c000",
            "size": 4096
        },
        "avc_stats_table_index_out_of_range": 0
    },
    "vrf_id_name_table": [
        {
            "id": 4106,
            "name": "__Platform_iVRF:ID00",
            "vrf_namehash": "9f30f5f1fd89b0f0",
            "ipv4": 4106,
            "ipv6": 65535
        },
        {
            "id": 3,
            "name": "1",
            "vrf_namehash": "c4ca4238a0b92382",
            "ipv4": 3,
            "ipv6": 503316481
        },
        {
            "id": 4,
            "name": "Mgmt-intf",
            "vrf_namehash": "712b9b92383e5f4",
            "ipv4": 4,
            "ipv6": 503316482
        },
        {
            "id": 1,
            "name": "65528",
            "vrf_namehash": "3fc6d55e4445affa",
            "ipv4": 1,
            "ipv6": 65535
        }
    ],
    "w_persona": "0x84969ec0",
    "vpn_zone_table": {
        "address": "0x13b00400",
        "size": 65536
    },
    "vpn_to_zone_mappings": [
        {
            "vpn": 1,
            "zone": 1
        },
        {
            "vpn": 65526,
            "zone": 65534
        },
        {
            "vpn": 65528,
            "zone": 65534
        },
        {
            "vpn": 65534,
            "zone": 65535
        }
    ]
}