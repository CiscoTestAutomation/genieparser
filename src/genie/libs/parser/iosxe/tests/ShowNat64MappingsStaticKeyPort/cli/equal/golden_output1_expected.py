expected_output = {
    'protocol': 'tcp',
    'key_port': '21',
    'translations': {
        '1': {
            'original_ipv4': '203.0.113.10:21',
            'translated_ipv4': '[2001:db8:abcd::1]:21',
            'translated_ipv6': '198.51.100.10:21',
            'original_ipv6': '[2001:db8:abcd::2]:21',
        },
        '2': {
            'original_ipv4': '203.0.113.20:21',
            'translated_ipv4': '[2001:db8:abcd::3]:21',
            'translated_ipv6': '198.51.100.20:21',
            'original_ipv6': '[2001:db8:abcd::4]:21',
        }
    },
    'total_translations': 2,
}
