expected_output = {
    'hardware_encryption': 'ACTIVE',
    'number_of_hardware_crypto_engines': 1,
    'crypto_engines': {
        'IOSXE-ESG(9)': {
            'name': 'IOSXE-ESG(9)',
            'state': 'Active',
            'capability': [
                'DES',
                '3DES',
                'AES',
                'GCM',
                'GMAC',
                'Manual IPsec key',
                'OSPFv3 manual keying',
                'RSA',
                'IPv6',
                'GDOI',
                'FAILCLOSE',
                'ESN'
            ],
            'ipsec_session': {
                'active': 2,
                'max': 16000,
                'failed': 0,
                'created': 2
            },
            'number_of_dh_pregenerated': 4,
            'dh_lifetime_seconds': 86400,
            'dh_calculations': {
                'p1': 1,
                'ss': 1
            }
        }
    },
    'software_crypto_engines': {
        '1': {
            'name': 'Software Crypto Engine',
            'dh_in_use': 1,
            'dh_freeing': 0,
            'dh_free': 16049
        }
    }
}