expected_output = {
    'index': {
        1: {
          'original_ipv4': '1.1.1.2:60',
          'original_ipv6': '[2009::2]:60',
          'proto': 'tcp',
          'translated_ipv4': '[1001::101:102]:60',
          'translated_ipv6': '5.5.5.5:60'
        },
        2: {
            'original_ipv4': '1.1.1.2:63',
            'original_ipv6': '[2009::2]:63',
            'proto': 'udp',
            'translated_ipv4': '[1001::101:102]:63',
            'translated_ipv6': '5.5.5.5:63'
        },
        3: {
            'original_ipv4': '---',
            'original_ipv6': '2009::2',
            'proto': '---',
            'translated_ipv4': '---',
            'translated_ipv6': '5.5.5.5'
        }
    },
    'total_no_of_translations': 3
}