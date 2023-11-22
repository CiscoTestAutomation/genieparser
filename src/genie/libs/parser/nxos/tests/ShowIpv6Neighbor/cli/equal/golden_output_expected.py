expected_output = {
    'interfaces': {
        'Ethernet1/46': {
            'ipv6': {
                'neighbors': {
                    '2001:db8:2::3': {
                        'age': '00:00:10',
                        'ip': '2001:db8:2::3',
                        'link_layer_address': '0000.0000.0203',
                        'origin': 'dynamic',
                        'physical_interface': 'Ethernet1/46',
                        'pref': 50,
                        'source': 'icmpv6'},
                    '2001:db8:2::4': {
                        'age': '00:00:05',
                        'ip': '2001:db8:2::4',
                        'link_layer_address': '0000.0000.0204',
                        'origin': 'dynamic',
                        'physical_interface': 'Ethernet1/46',
                        'pref': 50,
                        'source': 'icmpv6'
                    }
                }
            }
        }
    },
    'statistics': {'entries_total': 2},
    'vrf': 'default'
}
