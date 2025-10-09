expected_output = {
    'acl': {
        'entries': [
            {
                'ipv4_src': {
                    'value': '110.80.0.1',
                    'mask': '255.255.255.255'
                },
                'ipv4_dst': {
                    'value': '210.100.0.1',
                    'mask': '255.255.255.255'
                },
                'proto': '0x0',
                'tos': '0x0',
                'tcp_flg': '0x0',
                'ttl': '0x0',
                'ipv4_flags': '0x0',
                'src_port': '0x0',
                'dst_port': '0x0',
                'result_action': {
                    'punt': 'N',
                    'drop': 'N',
                    'mirror': 'N',
                    'counter': '0x0',
                    'counter_value': 0
                }
            },
            {
                'ipv4_src': {
                    'value': '110.80.0.2',
                    'mask': '255.255.255.255'
                },
                'ipv4_dst': {
                    'value': '210.100.0.2',
                    'mask': '255.255.255.255'
                },
                'proto': '0x0',
                'tos': '0x0',
                'tcp_flg': '0x0',
                'ttl': '0x0',
                'ipv4_flags': '0x0',
                'src_port': '0x0',
                'dst_port': '0x0',
                'result_action': {
                    'punt': 'N',
                    'drop': 'N',
                    'mirror': 'N',
                    'counter': '0x0',
                    'counter_value': 0
                }
            }
        ],
        'no_of_aces': 30001,
        'oid': '0x453'
    },
    'cg_id': 11,
    'cg_name': 'aclscale-30',
    'direction': 'Ingress',
    'feature': 'Racl',
    'interface_name': 'Vl300',
    'protocol': 'IPv4'
}