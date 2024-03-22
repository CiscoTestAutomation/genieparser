
expected_output = {
    'Ethernet0/0': {
        'delay_measurement': {
            'current_probe': {
                'measured_delays': {
                    'average': 0,
                    'maximum': 0,
                    'minimum': 0,
                    'variance': 0
                },
                'next_burst_packet': 2,
                'next_probe_scheduled': {
                    'day': 18,
                    'hour': 13,
                    'minute': 11,
                    'month': 10,
                    'remaining_seconds': 14,
                    'second': 47,
                    'year': 2021
                },
                'packets': {
                    'packets_received': 0,
                    'packets_sent': 6
                },
                'probe_samples': {
                    'no_history': True
                },
                'started_at': {
                    'day': 18,
                    'hour': 13,
                    'minute': 11,
                    'month': 10,
                    'second': 17,
                    'seconds_ago': 16,
                    'year': 2021
                }
            },
            'last_advertisement': {
                'no_advertisements': True
            },
            'last_error': {
                'error': '0 0 packet sent error. INVALID_OUT_IF',
                'timestamp': {
                    'day': 18,
                    'hour': 13,
                    'minute': 11,
                    'month': 10,
                    'second': 32,
                    'year': 2021
                }
            },
            'liveness_detection': {
                'backoff': 1,
                'last_state_change_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 58,
                    'month': 10,
                    'second': 47.578
                },
                'loss_in_last_interval': {
                    'percent': 100,
                    'rx': 0,
                    'tx': 6
                },
                'missed_count': 296,
                'received_count': 0,
                'session_creation_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 56,
                    'month': 10,
                    'second': 46.731
                },
                'session_state': 'Down',
                'unique_path_name': 'Path-1'
            },
            'next_advertisement': {
                'check_scheduled': {
                    'check_scheduled': 120,
                    'in_n_more_probes': 2
                },
                'no_probes': True
            },
            'profile_name': 'Not configured',
            'session_id': 1
        },
        'delay_measurement_enabled': 'Enabled',
        'ifh': '0x2',
        'local_ipv4_address': '19.1.1.3',
        'local_ipv6_address': '::',
        'loss_measurement_enabled': 'Disabled',
        'mpls_caps': 'Not created',
        'state': 'Up'
    },
    'Ethernet0/1': {
        'delay_measurement': {
            'current_probe': {
                'burst_completed': True,
                'measured_delays': {
                    'average': 410,
                    'maximum': 436,
                    'minimum': 353,
                    'variance': 57
                },
                'next_probe_scheduled': {
                    'day': 2,
                    'hour': 6,
                    'minute': 37,
                    'month': 11,
                    'remaining_seconds': 18,
                    'second': 41,
                    'year': 2021
                },
                'packets': {
                    'packets_received': 4,
                    'packets_sent': 4
                },
                'probe_samples': {
                    0: {
                        'day': 2,
                        'hour': 6,
                        'measured_delay': 432500,
                        'minute': 37,
                        'month': 11,
                        'second': 21,
                        'year': 2021
                    },
                    1: {
                        'day': 2,
                        'hour': 6,
                        'measured_delay': 436500,
                        'minute': 37,
                        'month': 11,
                        'second': 18,
                        'year': 2021
                    },
                    2: {
                        'day': 2,
                        'hour': 6,
                        'measured_delay': 419000,
                        'minute': 37,
                        'month': 11,
                        'second': 15,
                        'year': 2021
                    },
                    3: {
                        'day': 2,
                        'hour': 6,
                        'measured_delay': 353500,
                        'minute': 37,
                        'month': 11,
                        'second': 12,
                        'year': 2021
                    }
                },
                'started_at': {
                    'day': 2,
                    'hour': 6,
                    'minute': 37,
                    'month': 11,
                    'second': 12,
                    'seconds_ago': 11,
                    'year': 2021
                }
            },
            'last_advertisement': {
                'advertised_at': {
                    'day': 2,
                    'hour': 5,
                    'minute': 15,
                    'month': 11,
                    'second': 42,
                    'seconds_ago': 4901,
                    'year': 2021
                },
                'advertised_delays': {
                    'average': 752,
                    'maximum': 947,
                    'minimum': 575,
                    'variance': 99
                },
                'advertised_reason': 'First advertisement',
                'advertised_anomaly': 'INACTIVE'
            },
            'last_error': {
                'error': 'Unknown destination address type 0.',
                'timestamp': {
                    'day': 2,
                    'hour': 5,
                    'minute': 14,
                    'month': 11,
                    'second': 27,
                    'year': 2021
                }
            },
            'liveness_detection': {
                'backoff': 0,
                'last_state_change_timestamp': {
                    'day': 2,
                    'hour': 5,
                    'minute': 14,
                    'month': 11,
                    'second': 30.696
                },
                'loss_in_last_interval': {
                    'percent': 0,
                    'rx': 4,
                    'tx': 4
                },
                'missed_count': 0,
                'received_count': 1658,
                'session_creation_timestamp': {
                    'day': 2,
                    'hour': 5,
                    'minute': 14,
                    'month': 11,
                    'second': 11.582
                },
                'session_state': 'Up',
                'unique_path_name': 'Path-3'
            },
            'next_advertisement': {
                'aggregated_delays': {
                    'average': 383,
                    'maximum': 499,
                    'minimum': 313,
                    'variance': 51
                },
                'check_scheduled': 120,
                'rolling_average': 395
            },
            'profile_name': 'Not configured',
            'session_id': 3
        },
        'delay_measurement_enabled': 'Enabled',
        'ifh': '0x8',
        'local_ipv4_address': '1.2.3.3',
        'local_ipv6_address': '1:2:3:3::1',
        'loss_measurement_enabled': 'Enabled',
        'mpls_caps': 'Not created',
        'state': 'Up'
    },
    'Ethernet1/2': {
        'delay_measurement': {
            'current_probe': {
                'measured_delays': {
                    'average': 779,
                    'maximum': 879,
                    'minimum': 738,
                    'variance': 41
                },
                'next_burst_packet': 1,
                'next_probe_scheduled': {
                    'day': 18,
                    'hour': 13,
                    'minute': 11,
                    'month': 10,
                    'remaining_seconds': 13,
                    'second': 46,
                    'year': 2021
                },
                'packets': {
                    'packets_received': 6,
                    'packets_sent': 6
                },
                'probe_samples': {
                    0: {
                        'day': 18,
                        'hour': 13,
                        'measured_delay': 879500,
                        'minute': 11,
                        'month': 10,
                        'second': 32,
                        'year': 2021
                    },
                    1: {
                        'day': 18,
                        'hour': 13,
                        'measured_delay': 742500,
                        'minute': 11,
                        'month': 10,
                        'second': 29,
                        'year': 2021
                    },
                    2: {
                        'day': 18,
                        'hour': 13,
                        'measured_delay': 738500,
                        'minute': 11,
                        'month': 10,
                        'second': 26,
                        'year': 2021
                    },
                    3: {
                        'day': 18,
                        'hour': 13,
                        'measured_delay': 768000,
                        'minute': 11,
                        'month': 10,
                        'second': 23,
                        'year': 2021
                    },
                    4: {
                        'day': 18,
                        'hour': 13,
                        'measured_delay': 781500,
                        'minute': 11,
                        'month': 10,
                        'second': 20,
                        'year': 2021
                    },
                    5: {
                        'day': 18,
                        'hour': 13,
                        'measured_delay': 768000,
                        'minute': 11,
                        'month': 10,
                        'second': 17,
                        'year': 2021
                    }
                },
                'started_at': {
                    'day': 18,
                    'hour': 13,
                    'minute': 11,
                    'month': 10,
                    'second': 17,
                    'seconds_ago': 16,
                    'year': 2021
                }
            },
            'last_advertisement': {
                'advertised_at': {
                    'day': 18,
                    'hour': 12,
                    'minute': 58,
                    'month': 10,
                    'second': 47,
                    'seconds_ago': 766,
                    'year': 2021
                },
                'advertised_delays': {
                    'average': 747,
                    'maximum': 5628,
                    'minimum': 496,
                    'variance': 234
                },
                'advertised_reason': 'First advertisement',
                'advertised_anomaly': 'INACTIVE'
            },
            'last_error': {
                'error': 'Unknown destination address type 0.',
                'timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 5,
                    'year': 2021
                }
            },
            'liveness_detection': {
                'backoff': 0,
                'last_state_change_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 8.097
                },
                'loss_in_last_interval': {
                    'percent': 0,
                    'rx': 6,
                    'tx': 6
                },
                'missed_count': 0,
                'received_count': 289,
                'session_creation_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 56,
                    'month': 10,
                    'second': 46.732
                },
                'session_state': 'Up',
                'unique_path_name': 'Path-3'
            },
            'next_advertisement': {
                'aggregated_delays': {
                    'average': 758,
                    'maximum': 872,
                    'minimum': 683,
                    'variance': 75
                },
                'check_scheduled': {
                    'check_scheduled': 120,
                    'in_n_more_probes': 2
                },
                'rolling_average': 757
            },
            'profile_name': 'Not configured',
            'session_id': 3
        },
        'delay_measurement_enabled': 'Enabled',
        'ifh': '0x8',
        'local_ipv4_address': '1.2.3.3',
        'local_ipv6_address': '1:2:3:3::1',
        'loss_measurement': {
            'current_probe': {
                'measured_loss': {
                    'average': 0.0,
                    'capped': 50.331642,
                    'maximum': 0.0,
                    'minimum': 0.0,
                    'variance': 0.0
                },
                'next_burst_packet': 13,
                'next_probe_scheduled': {
                    'day': 18,
                    'hour': 13,
                    'minute': 11,
                    'month': 10,
                    'remaining_seconds': 13,
                    'second': 46,
                    'year': 2021
                },
                'packets': {
                    'packets_received': 4,
                    'packets_sent': 4
                },
                'probe_samples': {
                    0: {
                        'co': 0,
                        'day': 18,
                        'hour': 13,
                        'loss': 0.0,
                        'minute': 11,
                        'month': 10,
                        'rx0': 56,
                        'rx1': 57,
                        'second': 17,
                        'tx0': 55,
                        'tx1': 56,
                        'year': 2021
                    },
                    1: {
                        'co': 1,
                        'day': 18,
                        'hour': 13,
                        'loss': 0.0,
                        'minute': 11,
                        'month': 10,
                        'rx0': 55,
                        'rx1': 56,
                        'second': 2,
                        'tx0': 54,
                        'tx1': 55,
                        'year': 2021
                    }
                },
                'started_at': {
                    'day': 18,
                    'hour': 13,
                    'minute': 10,
                    'month': 10,
                    'second': 47,
                    'seconds_ago': 46,
                    'year': 2021
                }
            },
            'last_advertisement': {
                'advertised_at': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 47,
                    'seconds_ago': 826,
                    'year': 2021
                },
                'advertised_loss': {
                    'average': 0.0,
                    'capped': 50.331642,
                    'maximum': 0.0,
                    'minimum': 0.0,
                    'variance': 0.0
                },
                'advertised_reason': 'First advertisement',
                'advertised_anomaly': 'INACTIVE'
            },
            'last_error': {
                'error': 'Unknown destination address type 0.',
                'timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 2,
                    'year': 2021
                }
            },
            'liveness_detection': {
                'backoff': 0,
                'last_state_change_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 57,
                    'month': 10,
                    'second': 17.221
                },
                'loss_in_last_interval': {
                    'percent': 0,
                    'rx': 4,
                    'tx': 4
                },
                'missed_count': 0,
                'received_count': 58,
                'session_creation_timestamp': {
                    'day': 18,
                    'hour': 12,
                    'minute': 56,
                    'month': 10,
                    'second': 46.732
                },
                'session_state': 'Up',
                'unique_path_name': 'Path-3'
            },
            'next_advertisement': {
                'aggregated_loss': {
                    'average': 0.0,
                    'capped': 50.331642,
                    'maximum': 0.0,
                    'minimum': 0.0,
                    'variance': 0.0
                },
                'check_scheduled': 120,
                'rolling_average': 0.0
            },
            'profile_name': 'Not configured',
            'session_id': 4
        },
        'loss_measurement_enabled': 'Enabled',
        'mpls_caps': 'Not created',
        'state': 'Up'
    },
    'Serial2/0': {
        'delay_measurement_enabled': 'Disabled',
        'ifh': '0xA',
        'local_ipv4_address': '0.0.0.0',
        'local_ipv6_address': '::',
        'loss_measurement_enabled': 'Disabled',
        'mpls_caps': 'Not created',
        'state': 'Down'
    }
}
