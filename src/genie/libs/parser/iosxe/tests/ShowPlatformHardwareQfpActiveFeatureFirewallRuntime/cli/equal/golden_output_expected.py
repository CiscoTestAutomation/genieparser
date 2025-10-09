expected_output = {
    'global': {
        'global': {
            'value': '0x020001a1',
            'ha_state': 'Allow-New-Sess',
            'fw_configured': '0x00000020',
            'init_done': '0x00000080',
            'init_requested': '0x00000100',
            'syslog_deployed': '0x02000000',
        },
        'global2': {
            'value': '0x190000c4',
            'salt': 196,
            'global_simultaneous_packets_per_session': 0,
            'default_simultaneous_packets_per_session': 25,
        },
        'global3': {
            'value': '0x00000080',
            'half_open': '0x00000080',
        }
    },
    'teardowns': 0,
    'pam_cce': '0x0 00000000',
    'num_zp_with_policy': 1,
    'high_priority_recycle_queue_address': '0x846519c0',
    'low_priority_recycle_queue_address': '0x846519d0',
    'lock_upgrades': 190,
    'half_open_aggressive_aging': 1,
    'num_ack_exceeds_limit': 0,
    'num_rst_exceeds_limit': 0,
    'unknown_vrf_limit_exceeds': 0,
    'syncookie_over_rate_cnt': 0,
    'fw_tcp_session_termination': {
        'halfopen': {
            'rst_sent': 0,
            'blocked': 0,
        },
        'idle': {
            'rst_sent': 0,
            'blocked': 0,
        },
        'halfclose': {
            'rst_sent': 0,
            'blocked': 0,
        }
    },
    'nat_caching': {
        'nat_registration': 100,
        'nat_unregistration': 100,
        'too_many_nat_sessions': 0,
        'cant_register_with_nat': 0,
        'invalid_nat_session': 0,
        'no_nat_session_caching': 0,
        'nat_cached_session': 0,
    },
    'l2_firewall': {
        'l2_unknown_encap': 0,
        'l2_skip_tcp_pkt': 0,
        'timer_stop_failed': 0,
    },
    'vrf_global_action_block': {
        'l7_inspection_disable_flags': '0x0',
        'total_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
            'aggr_age_high_watermark': 4294967295,
            'aggr_age_low_watermark': 0,
            'num_times_enter_aggr_age': 0,
            'aggr_age_period': 'off',
        },
        'tcp_syn_cookie': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'total_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
            'aggr_age_high_watermark': 4294967295,
            'aggr_age_low_watermark': 0,
            'num_times_enter_aggr_age': 0,
            'aggr_age_period': 'off',
        },
        'tcp_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'udp_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'icmp_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'domain_flags': '0x0',
    },
    'box_action_block': {
        'l7_inspection_disable_flags': '0x0',
        'total_sessions': {
            'current_count': 0,
            'aggr_age_high_watermark': 4294967295,
            'aggr_age_low_watermark': 0,
            'num_times_enter_aggr_age': 0,
            'aggr_age_period': 'off',
        },
        'tcp_syn_cookie': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'total_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
            'aggr_age_high_watermark': 4294967295,
            'aggr_age_low_watermark': 0,
            'num_times_enter_aggr_age': 0,
            'aggr_age_period': 'off',
        },
        'tcp_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'udp_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'icmp_half_open_sessions': {
            'max_limit': 4294967295,
            'current_count': 0,
            'exceed': 0,
        },
        'domain_flags': '0x0',
    },
    'fw_persona_alert_rlimit': 0,
    'fw_persona_backpressure': '0x0',
    'invalid_rg_exceeds_max': 0,
    'invalid_ha_message_version': 0,
    'rii_hash_table': {
        'address': '0xc7335810',
        'size': 128,
    },
    'vrf_action_table': {
        'address': '0x0xc80ab800',
        'size': 4096,
    },
    'avc_stats_table_index_out_of_range': 0,
    'vrf_id_name_table': {
        'vrf_1': {
            'id': 1,
            'name': 'Mgmt-intf',
            'vrf_namehash': '712b9b92383e5f4',
            'ipv4': 1,
            'ipv6': 65535,
        },
        'vrf_4095': {
            'id': 4095,
            'name': '__Platform_iVRF:_ID00_',
            'vrf_namehash': '9f30f5f1fd89b0f0',
            'ipv4': 4095,
            'ipv6': 65535,
        }
    },
    'fw_persona_address': '0x846519e0',
    'vpn_zone_table': {
        'address': '0xc873b400',
        'size': 65536,
    }
}
