expected_output = {
    'fqdn_database': {
        'fqdn_name': {
            '*.msft404.com': {
                'ip_address': [
                    '4.1.1.24',
                    '2001:db8:4:1::1/64'
                ],
                'type': [
                    'IPv4',
                    'IPv6'
                ],
                'ttl': [
                    '67/100',
                    '72/100'
                ],
                'matched_fqdn': [
                    '1',
                    '2'
                ]
            },
            'cisco.msf04.com': {
                'ip_address': [
                    '4.1.1.24',
                    '2001:db8:4:1::1/64'
                ],
                'type': [
                    'IPv4',
                    'IPv6'
                ],
                'ttl': [
                    '67/100',
                    '77/99'
                ],
                'matched_fqdn': [
                    '1',
                    '1'
                ]
            }
        }
    }
}

