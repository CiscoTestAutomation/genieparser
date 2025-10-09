expected_output = {
    'parameter_map_type_inspect_global': {
        'log_dropped_packet': 'off',
        'log_flow': 'no',
        'log_flow_export_fnf': 'no',
        'log_flow_export_template_timeout_rate': 300,
        'alert': 'off',
        'lisp_inner_packet_inspection': 'off',
        'multi_tenancy': 'off',
        'icmp_unreachable': 'drop',
        'session_reclassify': 'disable',
    },
    'vpn_zone_security': 'disable',
    'vpn_disallow_dia': {
        'aggressive_aging': 'disabled',
        'syn_flood_limit': 'unlimited',
        'tcp_window_scaling_enforcement': 'loose on',
        'zone_mismatch_drop': 'off',
        'max_incomplete': 'unlimited',
        'max_incomplete_tcp': 'unlimited',
        'max_incomplete_udp': 'unlimited',
        'max_incomplete_icmp': 'unlimited',
        'application_inspect': 'all',
        'vrf_inspect': 'vrf-default'
    }
}