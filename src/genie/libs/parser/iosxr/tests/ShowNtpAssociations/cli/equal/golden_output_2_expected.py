

expected_output = {
    'clock_state': {
        'system_status': {
            'clock_state': 'unsynchronized'}
    },
    'peer': {
        '10.4.1.1': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 0.0,
                    'jitter': 15937.0,
                    'local_mode': 'client',
                    'mode': 'unsynchronized',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.AUTH.',
                    'remote': '10.4.1.1',
                    'stratum': 16}
            }
        },
        '10.16.2.2': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 69.18,
                    'jitter': 4.702,
                    'local_mode': 'client',
                    'mode': 'unsynchronized',
                    'offset': -518066.0,
                    'poll': 64,
                    'reach': 377,
                    'receive_time': 52,
                    'refid': '127.127.1.1',
                    'remote': '10.16.2.2',
                    'stratum': 9}
            }
        },
        '10.64.4.4': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 0.0,
                    'jitter': 15937.0,
                    'local_mode': 'client',
                    'mode': 'unsynchronized',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.AUTH.',
                    'remote': '10.64.4.4',
                    'stratum': 16}
            }
        },
        '10.100.5.5': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 0.0,
                    'jitter': 15937.0,
                    'local_mode': 'client',
                    'mode': 'unsynchronized',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.AUTH.',
                    'remote': '10.100.5.5',
                    'stratum': 16}
            }
        },
        '10.144.6.6': {
            'local_mode': {
                'client': {
                    'configured': True,
                    'delay': 0.0,
                    'jitter': 15937.0,
                    'local_mode': 'client',
                    'mode': 'unsynchronized',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.AUTH.',
                    'remote': '10.144.6.6',
                    'stratum': 16}
            }
        }
    },
    'vrf': {
        'VRF1': {
            'address': {
                '10.4.1.1': {
                    'isconfigured': {
                        True: {
                            'address': '10.4.1.1',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '10.4.1.1',
                            'type': 'peer',
                            'vrf': 'VRF1'}
                    }
                },
                '10.100.5.5': {
                    'isconfigured': {
                        True: {
                            'address': '10.100.5.5',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '10.100.5.5',
                            'type': 'peer',
                            'vrf': 'VRF1'}
                    }
                },
                '10.144.6.6': {
                    'isconfigured': {
                        True: {
                            'address': '10.144.6.6',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '10.144.6.6',
                            'type': 'peer',
                            'vrf': 'VRF1'}
                    }
                }
            }
        },
        'default': {
            'address': {
                '10.4.1.1': {
                    'isconfigured': {
                        True: {
                            'address': '10.4.1.1',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '10.4.1.1',
                            'type': 'peer',
                            'vrf': 'default'}
                    }
                },
                '10.16.2.2': {
                    'isconfigured': {
                        True: {
                            'address': '10.16.2.2',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '10.16.2.2',
                            'type': 'peer',
                            'vrf': 'default'}
                    }
                },
                '10.64.4.4': {
                    'isconfigured': {
                        True: {
                            'address': '10.64.4.4',
                            'isconfigured': True}
                    },
                    'type': {
                        'peer': {
                            'address': '10.64.4.4',
                            'type': 'peer',
                            'vrf': 'default'}
                    }
                }
            }
        }
    }
}
