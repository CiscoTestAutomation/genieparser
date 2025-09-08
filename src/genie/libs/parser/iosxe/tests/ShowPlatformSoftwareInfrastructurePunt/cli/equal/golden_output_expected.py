expected_output={
        'lsmpi_interface_internal_stats': {
            'enabled': 0,
            'disabled': 0,
            'throttled': 0,
            'unthrottled': 0,
            'state': 'ready',
            'input_buffers': 2955942,
            'output_buffers': 327045,
            'rxdone_count': 2955942,
            'txdone_count': 327043,
            'rx_no_particletype_count': 0,
            'tx_no_particletype_count': 0,
            'txbuf_from_shadow_count': 0,
            'no_start_of_packet': 0,
            'no_end_of_packet': 0
        },
        'punt_drop_stats': {
            'bad_version': 0,
            'bad_type': 0,
            'had_feature_header': 0,
            'had_platform_header': 0,
            'feature_header_missing': 0,
            'common_header_mismatch': 0,
            'bad_total_length': 0,
            'bad_packet_length': 0,
            'bad_network_offset': 0,
            'not_punt_header': 0,
            'unknown_link_type': 0,
            'no_swidb': 3,
            'bad_ess_feature_header': 0,
            'no_ess_feature': 0,
            'no_sslvpn_feature': 0,
            'no_ppp_bridge_feature': 0,
            'punt_for_ppp_bridge_type_packets': 0,
            'punt_for_us_type_unknown': 0,
            'epc_cp_rx_pkt_cleansed': 0,
            'punt_cause_out_of_range': 0
        },
        'rp_punt_stats': {
            'layer2_control_and_legacy_packets': 1370,
            'arp_request_or_response_packets': 60566,
            'for_us_data_packets': 268,
            'ipv6_hop_by_hop_options_packets': 612,
            'rp<_>qfp_keepalive_packets': 4332,
            'for_us_control_packets': 1426555,
            'layer2_bridge_domain_data_packet_packets': 9390,
            'layer2_control_protocols_packets': 62519,
            'snoop_packets_packets': 414
        },
        'control_ipv4_protocol_stats': {
            '0': 1407344
        },
        'control_ipv6_protocol_stats': {
            'hop_by_hop_packets': 19211
        },
        'packet_histogram': {
            'bytes_per_bin': 500,
            'avg_in': 541,
            'avg_out': 197,
            'pak_size': {
            '0+': {
                'in_count': 393823,
                'out_count': 317524
            },
            '500+': {
                'in_count': 1123362,
                'out_count': 3749
            },
            '1000+': {
                'in_count': 48841,
                'out_count': 0
            }
        }
    }    
}
