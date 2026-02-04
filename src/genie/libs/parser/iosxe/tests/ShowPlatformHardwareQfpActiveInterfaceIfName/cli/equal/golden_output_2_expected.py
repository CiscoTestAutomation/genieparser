expected_output = {
    'interface': {
        'NVI0': {
            'channel': 0,
            'interface_state': 'VALID',
            'members': [
                'icmp_svr',
                'ipfrag_svr',
                'ipreass_svr',
                'ipv6reass_svr',
                'icmp6_svr',
                'nat64_svr',
                'ipvfr_svr',
                'ipv6vfr_svr'
            ],
            'platform_interface_handle': 39,
            'protocols': {
                'ipv4_input': {
                    'cp_handle': '0x5e6f36267508',
                    'dp_handle': '0x39fda280',
                    'features': [
                        'IPV4_INPUT_DST_LOOKUP_ISSUE',
                        'IPV4_INPUT_ARL_SANITY',
                        'IPV4_INPUT_DST_LOOKUP_CONSUME',
                        'IPV4_INPUT_FOR_US_MARTIAN',
                        'IPV4_INPUT_LOOKUP_PROCESS',
                        'IPV4_INPUT_IPOPTIONS_PROCESS',
                        'IPV4_INPUT_GOTO_OUTPUT_FEATURE'
                    ]
                },
                'ipv4_output': {
                    'cp_handle': '0x5e6f36267198',
                    'dp_handle': '0x39fe0000',
                    'features': [
                        'IPV4_OUTPUT_VFR',
                        'NAT64_XLATE_V4V6',
                        'IPV4_VFR_REFRAG',
                        'IPV4_OUTPUT_L2_REWRITE',
                        'IPV4_OUTPUT_FRAG',
                        'IPV4_OUTPUT_DROP_POLICY',
                        'DEF_IF_DROP_FIA'
                    ]
                },
                'ipv6_input': {
                    'cp_handle': '0x5e6f36267418',
                    'dp_handle': '0x39fdbc00',
                    'features': [
                        'IPV6_INPUT_SANITY_CHECK',
                        'IPV6_INPUT_DST_LOOKUP_ISSUE',
                        'IPV6_INPUT_ARL',
                        'IPV6_INPUT_DST_LOOKUP_CONT',
                        'IPV6_INPUT_DST_LOOKUP_CONSUME',
                        'IPV6_INPUT_FOR_US',
                        'IPV6_INPUT_LOOKUP_PROCESS',
                        'IPV6_INPUT_LINK_LOCAL_CHECK',
                        'IPV6_INPUT_GOTO_OUTPUT_FEATURE'
                    ]
                },
                'ipv6_output': {
                    'cp_handle': '0x5e6f362671e8',
                    'dp_handle': '0x39fdf780',
                    'features': [
                        'IPV6_OUTPUT_VFR',
                        'NAT64_XLATE_V6V4',
                        'IPV6_VFR_REFRAG',
                        'IPV6_OUTPUT_L2_REWRITE',
                        'IPV6_OUTPUT_FRAG',
                        'IPV6_OUTPUT_DROP_POLICY',
                        'DEF_IF_DROP_FIA'
                    ]
                }
            },
            'qfp_interface_handle': 31,
            'rx_uidb': 262139,
            'tx_uidb': 262113
        }
    }
}
