expected_output = {
    'index': {
        1: {
            'original_ipv4': '1.1.1.2:0',
            'original_ipv6': '[2009::2]:0',
            'proto': 'icmp',
            'translated_ipv4': '[1001::101:102]:0',
            'translated_ipv6': '5.5.5.5:0'
        },
        2: {
            'original_ipv4': '1.1.1.2:63',
            'original_ipv6': '[2009::2]:63',
            'proto': 'udp',
            'translated_ipv4': '[1001::101:102]:63',
            'translated_ipv6': '5.5.5.5:63'
        }
    },
    'total_no_of_translations': 2
}