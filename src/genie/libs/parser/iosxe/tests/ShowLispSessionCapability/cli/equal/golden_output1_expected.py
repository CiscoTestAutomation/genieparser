expected_output = {
    'vrf': {
        'default': {
            'peer': {
                '44.44.44.44': [{
                    'port': 4342,
                    'tx_flags': '0x1FF',
                    'rx_flags': '0x1FF',
                    'rx_count': 1,
                    'err_count': 0
                    }],
                '66.66.66.66': [{
                    'port': 4342,
                    'tx_flags': '0x1FF',
                    'rx_flags': '0x1FF',
                    'rx_count': 1,
                    'err_count': 0
                    }, {
                        'port': 44538,
                        'tx_flags': '0x1FF',
                        'rx_flags': '0x1FF',
                        'rx_count': 1,
                        'err_count': 0
                        }],
                '100.100.100.100': [{
                    'port': 4342,
                    'tx_flags': '0x1FF',
                    'rx_flags': '0x1FF',
                    'rx_count': 1,
                    'err_count': 0
                    }]
                }
            }
        }
    }