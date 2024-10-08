expected_output = {
    'cg_name': {
        'racl_permitv6_egress': {
            'cg_id': 8,
            'dir': 'Egress',
            'feature': 'Racl',
            'prot': 'IPv6',
            'region': '0xa005f158',
            'sdk_handles': [{'asic': 0, 'oid': '0x89D'}],
            'seq': {
                '10': {
                    'action': 'DENY',
                    'counter_handles': [{'asic': 0, 'oid': '0xA60'}],
                    'ipv6_dst_value': '0x00300000.0x00000000.0x00000000.0x00010000',
                    'ipv6_src_mask': '0xffffffff.0xffffffff.0xffffffff.0xffffff00',
                    'ipv6_src_value': '0x00100000.0x00000000.0x00000000.0x00010000',
                    'logging': 'NO_LOG',
                    'proto': {
                        'dst_port': '0x0',
                        'mask': '0x0',
                        'src_port': '0x0',
                        'tcp_flg': '0x0',
                        'tcp_op': '0x0',
                        'value': '0x0',
                    },
                    'tos': {
                        'cos': '0x0',
                        'dst_obj': '0x0',
                        'mask': '0x0',
                        'src_obj': '0x0',
                        'ttl': '0x0',
                        'v4_opt': '0x0',
                        'value': '0x0',
                    },
                },
                '20': {
                    'action': 'PERMIT',
                    'ipv6_dst_value': '0x00300000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_mask': '0xffffffff.0xffffffff.0xffffffff.0xffffff00',
                    'ipv6_src_value': '0x00100000.0x00000000.0x00000000.0x00000000',
                    'logging': 'NO_LOG',
                    'proto': {
                        'dst_port': '0x0',
                        'mask': '0x0',
                        'src_port': '0x0',
                        'tcp_flg': '0x0',
                        'tcp_op': '0x0',
                        'value': '0x0',
                    },
                    'tos': {
                        'cos': '0x0',
                        'dst_obj': '0x0',
                        'mask': '0x0',
                        'src_obj': '0x0',
                        'ttl': '0x0',
                        'v4_opt': '0x0',
                        'value': '0x0',
                    },
                },
                '30': {
                    'action': 'PERMIT',
                    'ipv6_dst_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_mask': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'logging': 'NO_LOG',
                    'proto': {
                        'dst_port': '0x0',
                        'mask': '0x0',
                        'src_port': '0x0',
                        'tcp_flg': '0x0',
                        'tcp_op': '0x0',
                        'value': '0xff',
                    },
                    'tos': {
                        'cos': '0x0',
                        'dst_obj': '0x0',
                        'mask': '0x0',
                        'src_obj': '0x0',
                        'ttl': '0x0',
                        'v4_opt': '0xff',
                        'value': '0x0',
                    },
                },
                '40': {
                    'action': 'PERMIT',
                    'ipv6_dst_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_mask': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'logging': 'NO_LOG',
                    'proto': {
                        'dst_port': '0x0',
                        'mask': '0x0',
                        'src_port': '0x0',
                        'tcp_flg': '0x0',
                        'tcp_op': '0x0',
                        'value': '0xff',
                    },
                    'tos': {
                        'cos': '0x0',
                        'dst_obj': '0x0',
                        'mask': '0x0',
                        'src_obj': '0x0',
                        'ttl': '0x0',
                        'v4_opt': '0xff',
                        'value': '0x0',
                    },
                },
                '4294967293': {
                    'action': 'PERMIT',
                    'ipv6_dst_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_mask': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'logging': 'NONE',
                    'proto': {
                        'dst_port': '0x0',
                        'mask': '0x0',
                        'src_port': '0xffff',
                        'tcp_flg': '0x0',
                        'tcp_op': '0x0',
                        'value': '0xff',
                    },
                    'tos': {
                        'cos': '0x0',
                        'dst_obj': '0x0',
                        'mask': '0x0',
                        'src_obj': '0x0',
                        'ttl': '0x0',
                        'v4_opt': '0xff',
                        'value': '0x0',
                    },
                },
                '4294967294': {
                    'action': 'PERMIT',
                    'ipv6_dst_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_mask': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'logging': 'NONE',
                    'proto': {
                        'dst_port': '0x0',
                        'mask': '0x0',
                        'src_port': '0xffff',
                        'tcp_flg': '0x0',
                        'tcp_op': '0x0',
                        'value': '0xff',
                    },
                    'tos': {
                        'cos': '0x0',
                        'dst_obj': '0x0',
                        'mask': '0x0',
                        'src_obj': '0x0',
                        'ttl': '0x0',
                        'v4_opt': '0xff',
                        'value': '0x0',
                    },
                },
                '4294967295': {
                    'action': 'DENY',
                    'counter_handles': [{'asic': 0, 'oid': '0xA69'}],
                    'ipv6_dst_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_mask': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'ipv6_src_value': '0x00000000.0x00000000.0x00000000.0x00000000',
                    'logging': 'NONE',
                    'proto': {
                        'dst_port': '0x0',
                        'mask': '0x0',
                        'src_port': '0x0',
                        'tcp_flg': '0x0',
                        'tcp_op': '0x0',
                        'value': '0x0',
                    },
                    'tos': {
                        'cos': '0x0',
                        'dst_obj': '0x0',
                        'mask': '0x0',
                        'src_obj': '0x0',
                        'ttl': '0x0',
                        'v4_opt': '0x0',
                        'value': '0x0',
                    },
                },
            },
        },
    },
}