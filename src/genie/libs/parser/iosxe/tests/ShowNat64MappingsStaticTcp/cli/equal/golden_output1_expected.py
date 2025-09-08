expected_output = {
    'protocol': 'tcp',
    'translations': {
        '1': {
            'original_ipv4': '203.0.113.1:8080',
            'translated_ipv4': '[2001:db8:1::1]:80',
            'translated_ipv6': '198.51.100.1:80',
            'original_ipv6': '[2001:db8:1::2]:8080',
        },
        '2': {
            'original_ipv4': '198.51.100.2:22',
            'translated_ipv4': '[2001:db8:1::3]:22',
            'translated_ipv6': '203.0.113.2:2222',
            'original_ipv6': '[2001:db8:1::4]:2222',
        }
    },
    'total_translations': 2,
}
