expected_output = {
    'index': {
        1: {
            'original_ipv4': '---',
            'original_ipv6': '[2001:1::2]:1234',
            'proto': 'tcp',
            'translated_ipv4': '---',
            'translated_ipv6': '1.1.1.2:100'
        },
        2: {
            'original_ipv4': '---',
            'original_ipv6': '[2001:1::2]:1234',
            'proto': 'udp',
            'translated_ipv4': '---',
            'translated_ipv6': '1.1.1.2:100'
        },
        3: {
            'original_ipv4': '---',
            'original_ipv6': '[2011:1::2]:1234',
            'proto': 'tcp',
            'translated_ipv4': '---',
            'translated_ipv6': '1.1.2.2:100'
        }
    },
    'total_no_of_translations': 3
}