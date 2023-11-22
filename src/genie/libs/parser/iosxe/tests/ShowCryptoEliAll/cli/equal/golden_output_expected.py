expected_output={
                'crypto_eng': {
                    'crypto_engine': 'Software Crypto Engine',
                    'crypto_engine_num': 1,
                    'dh_in_free': 41008,
                    'dh_in_freeing': 0,
                    'dh_in_use': 0
                    },
                'crypto_engine': {
                    'IOSXE-ESP(14)': {
                        'capability': 'DES, 3DES, AES, GCM, GMAC, RSA, IPv6, GDOI, FAILCLOSE, ESN',
                        'dtlsv1': [],
                        'ipsec_session': {
                            'active': 6004,
                            'created': 414018,
                            'failed': 0,
                            'max': 40958
                            },
                        'max_ssl_connec': 10000,
                        'ssl_support': 'Yes',
                        'ssl_versions': 'TLSv1.0',
                        'sslv3': [],
                        'state': 'Active',
                        'tlsv1': [
                            'TLS_RSA_WITH_3DES_EDE_CBC_SHA',
                            'TLS_RSA_WITH_AES_128_CBC_SHA',
                            'TLS_RSA_WITH_AES_256_CBC_SHA'
                            ]
                        },
                'Software Crypto Engine': {
                    'capability': 'IPPCP, DES, 3DES, AES, SEAL, GCM, GMAC, RSA, P-256, P-384, P-521, IPv6, GDOI, FAILCLOSE, HA',
                        'dh': {
                            'active': 0,
                            'created': 320010,
                            'failed': 0,
                            'max': 41008
                            },
                        'dtlsv1': [
                            'TLS_RSA_WITH_3DES_EDE_CBC_SHA',
                            'TLS_RSA_WITH_AES_128_CBC_SHA',
                            'TLS_RSA_WITH_AES_256_CBC_SHA'
                            ],
                        'ike_session': {
                            'active': 0,
                            'created': 319288,
                            'failed': 0,
                            'max': 41058
                            },
                        'ikev2_session': {
                            'active': 3002,
                            'created': 319288,
                            'failed': 0,
                            'max': 41058
                            },
                        'ipsec_session': {
                            'active': 0,
                            'created': 0,
                            'failed': 0,
                            'max': 1000
                            },
                        'max_ssl_connec': 1000,
                        'ssl_namespace': 1,
                        'ssl_support': 'Yes',
                        'sslv3': [
                            'TLS_RSA_WITH_3DES_EDE_CBC_SHA',
                            'TLS_RSA_WITH_AES_128_CBC_SHA',
                            'TLS_RSA_WITH_AES_256_CBC_SHA'
                            ],
                        'state': 'Active',
                        'tlsv1': [
                            'TLS_RSA_WITH_3DES_EDE_CBC_SHA',
                            'TLS_RSA_WITH_AES_128_CBC_SHA',
                            'TLS_RSA_WITH_AES_256_CBC_SHA'
                            ]
                        },
                'act2': {
                    'capability': 'RSA', 
                    'state': 'Active'
                    }
                    },
                'crypto_engines_num': 3,
                'dh_calculations': {
                    'p1': 722, 
                    'ss': 319288
                    },
                'dh_lifetime_seconds': 86400,
                'hardware_encryption': 'ACTIVE',
                'number_dh_pregenerated': 4
            }