expected_output = {
    'map_t_domain': {
        'domain_id': '1',
        'mode': 'MAP-T',
        'default_mapping_rule': {
            'ipv6_prefix': '2001:DA8:B001:FFFF::/64',
        },
        'basic_mapping_rule': {
            'ipv6_prefix': '2001:DA8:B001::/56',
            'ipv4_prefix': '202.1.0.128/28',
            'port_parameters': {
                'share_ratio': 16,
                'contiguous_ports': 64,
                'start_port': 1024,
                'share_ratio_bits': 4,
                'contiguous_ports_bits': 6,
                'port_offset_bits': 6,
            }
        }
    }
}
