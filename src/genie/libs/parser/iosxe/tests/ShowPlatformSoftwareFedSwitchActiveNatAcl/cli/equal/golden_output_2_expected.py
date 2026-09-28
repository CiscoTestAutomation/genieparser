expected_output = {
    'ace_count': 4,
    'index': {
        1: {
            'dst_addr': '0.0.0.0',
            'dst_port': '-',
            'protocol': 'any',
            'src_addr': '192.168.121.20',
            'src_port': '-',
            'type': 'SNAT',
            'vrf': 0
        },
        2: {
            'dst_addr': '10.10.10.1',
            'dst_port': '-',
            'protocol': 'any',
            'src_addr': '0.0.0.0',
            'src_port': '-',
            'type': 'DNAT',
            'vrf': 0
        },
        3: {
            'dst_addr': '20.20.20.1',
            'dst_port': '-',
            'protocol': 'any',
            'src_addr': '0.0.0.0',
            'src_port': '-',
            'type': 'DNAT',
            'vrf': 0
        },
        4: {
            'dst_addr': '0.0.0.0',
            'dst_port': '-',
            'protocol': 'any',
            'src_addr': '192.168.21.20',
            'src_port': '-',
            'type': 'SNAT',
            'vrf': 0
        }
    },
    'oid': '0x2f2'
}
