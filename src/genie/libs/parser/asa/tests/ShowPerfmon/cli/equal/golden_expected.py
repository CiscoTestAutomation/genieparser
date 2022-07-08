expected_output = {
    'perfmon': {
        'setup_rates_per_sec': {
            'one_min': {
                'total': 243,
                'tcp': 140,
                'udp': 100
            },
            'five_min': {
                'total': 1200,
                'tcp': 1000,
                'udp': 150
            }
        },
        'context': {
            'context1': {
                'stats_per_sec': {
                    'xlates': {
                        'current': 15,
                        'average': 8
                    },
                    'connections': {
                        'total': {
                            'current': 100,
                            'average': 50
                        },
                        'tcp': {
                            'current': 70,
                            'average': 40
                        },
                        'udp': {
                            'current': 30,
                            'average': 10
                        },
                    },
                    'url_access': {
                        'current': 5,
                        'average': 2
                    },
                    'url_server_req': {
                        'current': 30,
                        'average': 10
                    },
                    'tcp': {
                        'intercept_established_conns': {
                            'current': 8,
                            'average': 2
                        },
                        'intercept_attempts': {
                            'current': 20,
                            'average': 5
                        },
                        'embryonic_conns_timeout': {
                            'current': 6,
                            'average': 3
                        },
                    },
                    'fixup': {
                        'tcp': {
                            'current': 2,
                            'average': 1
                        },
                        'ftp': {
                            'current': 50,
                            'average': 7
                        },
                        'http': {
                            'current': 42,
                            'average': 79
                        },
                    },
                    'aaa': {
                        'authen': {
                            'current': 143,
                            'average': 200
                        },
                        'author': {
                            'current': 140,
                            'average': 190
                        },
                        'account': {
                            'current': 141,
                            'average': 192
                        },
                    }
                }
            },
        },
        'tcp_intercept' : {
            'valid_conns_rate': {
                'current': '100.00%',
                'average': '97.38%'
            }
        }
    }
}
