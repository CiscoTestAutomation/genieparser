expected_output = {
    'ace_count': 2,
    'index': {
        1: {
            'dst_addr': '0.0.0.0',
            'dst_port': '-',
            'protocol': 'any',
            'src_addr': '12.0.0.0',
            'src_port': '-',
            'type': 'SNAT'
        },
        2: {
            'dst_addr': '36.0.0.2',
            'dst_port': '-',
            'protocol': 'any',
            'src_addr': '0.0.0.0',
            'src_port': '-',
            'type': 'DNAT'
        }
    },
    'oid': '1082'
}