expected_output = {
    'key_address': '2001::1',
    'translations': {
        '1': {
            'protocol': 'tcp',
            'original_ipv4': '198.51.100.10:80',
            'translated_ipv4': '[2001::1]:80',
            'translated_ipv6': '203.0.113.5:8080',
            'original_ipv6': '[2001::1]:8080',
        },
        '2': {
            'protocol': 'udp',
            'original_ipv4': '198.51.100.20:53',
            'translated_ipv4': '[2001::1]:53',
            'translated_ipv6': '203.0.113.6:5353',
            'original_ipv6': '[2001::1]:5353',
        }
    },
    'total_translations': 2,
}
