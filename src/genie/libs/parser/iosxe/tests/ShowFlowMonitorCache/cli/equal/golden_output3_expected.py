expected_output =  {
    'cache_size': 10000,
    'cache_type': 'Normal (Platform cache)',
    'current_entries': 3,
    'flows_added': 11,
    'flows_aged': {
        'active_timeout': 7,
        'active_timeout_secs': 15,
        'inactive_timeout': 1,
        'inactive_timeout_secs': 15,
        'total': 8,
    },
    'proto_entries': {
        1: {
            'dst_port': 0,
            'ip_dst_addr': '224.0.0.5',
            'ip_port': 89,
            'ip_src_addr': '30.1.1.6',
            'src_port': 0,
        },
        2: {
            'dst_port': 0,
            'ip_dst_addr': '100.1.1.100',
            'ip_port': 17,
            'ip_src_addr': '200.1.1.100',
            'src_port': 0,
        },
        3: {
            'dst_port': 1024,
            'ip_dst_addr': '100.1.1.100',
            'ip_port': 17,
            'ip_src_addr': '200.1.1.100',
            'src_port': 1024,
        },
    },
}
