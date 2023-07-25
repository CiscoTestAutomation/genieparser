
expected_output = {
    'Ethernet0/0': {
        'candidate_paths': {
            0: {
                'active': 'No',
                'ap_min_run_per_probe': 3,
                'current_probe': {
                    'measured_delays': {
                        'average': 249,
                        'maximum': 499,
                        'minimum': 1,
                        'variance': 248
                    },
                    'packets': {
                        'packets_received': 6,
                        'packets_sent': 6
                    }
                },
                'discriminator': 0,
                'last_advertisement': {
                    'advertised_at': {
                        'day': 20,
                        'hour': 9,
                        'minute': 6,
                        'second': 42,
                        'seconds_ago': 92796,
                        'year': 2021
                    },
                    'advertised_delays': {
                        'average': 465,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 464
                    }
                },
                'last_probe': {
                    'measured_delays': {
                        'average': 233,
                        'maximum': 499,
                        'minimum': 1,
                        'variance': 232
                    },
                    'packets': {
                        'packets_received': 30,
                        'packets_sent': 30
                    }
                },
                'max_packets_per_burst': 500,
                'max_packets_per_probe': 15000,
                'next_advertisement': {
                    'aggregate_delays': {
                        'average': 233,
                        'maximum': 499,
                        'minimum': 1,
                        'variance': 232
                    },
                    'check_schedule': {
                        'probes': 2,
                        'seconds': 120
                    }
                },
                'number_of_atomic_paths': 1,
                'number_of_live_unknown_atomic': 1,
                'number_of_live_up_atomic_paths': 1,
                'number_of_segment_lists': 1,
                'preference': 100,
                'protocol_origin': 'CLI',
                'round_robin_bursts': 1,
                'round_robin_probes': 1,
                'segment_list': {
                    'atomic_paths': {
                        0: {
                            'current_probe': {
                                'measured_delays': {
                                    'average': 249,
                                    'maximum': 499,
                                    'minimum': 1,
                                    'variance': 248
                                },
                                'packets': {
                                    'packets_received': 6,
                                    'packets_sent': 6
                                }
                            },
                            'destination': '1.1.1.7',
                            'hops': {
                                0: '1.1.1.7'
                            },
                            'labels': {
                                0: '16230'
                            },
                            'last_advertisement': {
                                'advertised_at': {
                                    'day': 20,
                                    'hour': 9,
                                    'minute': 6,
                                    'second': 42,
                                    'seconds_ago': 92796,
                                    'year': 2021
                                },
                                'advertised_delays': {
                                    'average': 465,
                                 'maximum': 999,
                                    'minimum': 1,
                                    'variance': 464
                                },
                                'advertised_reason': 'Periodic timer, avg delay threshold crossed'
                            },
                            'last_probe': {
                                'measured_delays': {
                                    'average': 233,
                                    'maximum': 499,
                                    'minimum': 1,
                                    'variance': 232
                                },
                                'packets': {
                                    'packets_received': 30,
                                    'packets_sent': 30
                                }
                            },
                            'liveness_detection': {
                                'backoff': 0,
                                'last_state_change_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 52.414
                                },
                                'loss_in_last_interval': {
                                    'percent': 0,
                                    'rx': 6,
                                    'tx': 6
                                },
                                'missed_count': 0,
                                'received_count': 101186,
                                'session_creation_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 52.222
                                },
                                'session_state': 'Up',
                                'unique_path_name': 'Path-10'
                            },
                            'max_ip_mtu': 1500,
                            'next_advertisement': {
                                'aggregate_delays': {
                                    'average': 233,
                                    'maximum': 499,
                                    'minimum': 1,
                                    'variance': 232
                                },
                                'rolling_average': 287
                            },
                            'next_hop': '110.1.1.4',
                            'outgoing_interface': 'Ethernet0/1',
                            'probe_samples': {
                                'samples': {
                                    0: {
                                        'day': 21,
                                        'delay': 0,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 18,
                                        'year': 2021
                                    },
                                    1: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 17,
                                        'year': 2021
                                    },
                                    2: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 16,
                                        'year': 2021
                                },
                                    3: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 15,
                                        'year': 2021
                                    },
                                    4: {
                                        'day': 21,
                                        'delay': 0,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 14,
                                        'year': 2021
                                    },
                                    5: {
                                        'day': 21,
                                        'delay': 0,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 13,
                                        'year': 2021
                                    }
                                }
                            },
                            'session_id': 10
                        }
                    },
                    'current_probe': {
                        'measured_delays': {
                            'average': 249,
                            'maximum': 499,
                            'minimum': 1,
                            'variance': 248
                        },
                        'packets': {
                            'packets_received': 6,
                            'packets_sent': 6
                        }
                    },
                    'last_advertisement': {
                        'advertised_at': {
                            'day': 20,
                            'hour': 9,
                            'minute': 6,
                            'second': 42,
                            'seconds_ago': 92796,
                            'year': 2021
                        },
                        'advertised_delays': {
                            'average': 465,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 464
                        }
                    },
                    'last_probe': {
                        'measured_delays': {
                            'average': 233,
                            'maximum': 499,
                            'minimum': 1,
                            'variance': 232
                        },
                        'packets': {
                            'packets_received': 30,
                            'packets_sent': 30
                        }
                    },
                    'name': 'SL7',
                    'next_advertisement': {
                        'aggregate_delays': {
                            'average': 233,
                            'maximum': 499,
                            'minimum': 1,
                            'variance': 232
                        }
                    },
                    'number_of_atomic_paths': 1
                }
            }
        },
        'color': 1235,
        'endpoint': '1.1.1.7',
        'number_of_candidate_paths': 1,
        'policy_update_timestamp': {
            'day': 20,
            'hour': 6,
            'minute': 46,
            'month': 5,
            'second': 52.222
        },
        'profile_name': 'Not configured',
        'source': '1.1.1.3'
    },
    'Ethernet0/1': {
        'candidate_paths': {
            0: {
                'active': 'No',
                'ap_min_run_per_probe': 3,
                'current_probe': {
                    'measured_delays': {
                        'average': 1000,
                        'maximum': 1000,
                        'minimum': 1000,
                        'variance': 0
                    },
                    'packets': {
                        'packets_received': 2,
                        'packets_sent': 2
                    }
                },
                'discriminator': 0,
                'last_advertisement': {
                    'advertised_at': {
                        'day': 20,
                        'hour': 6,
                        'minute': 48,
                        'second': 42,
                        'seconds_ago': 101076,
                        'year': 2021
                    },
                    'advertised_delays': {
                        'average': 566,
                        'maximum': 1000,
                        'minimum': 1,
                        'variance': 565
                    }
                },
                'last_probe': {
                    'measured_delays': {
                        'average': 100,
                        'maximum': 1000,
                        'minimum': 1,
                        'variance': 99
                    },
                    'packets': {
                        'packets_received': 10,
                        'packets_sent': 10
                    }
                },
                'max_packets_per_burst': 500,
                'max_packets_per_probe': 5000,
                'next_advertisement': {
                    'aggregate_delays': {
                        'average': 100,
                        'maximum': 1000,
                        'minimum': 1,
                        'variance': 99
                    },
                    'check_schedule': {
                        'probes': 2,
                        'seconds': 120
                    }
                },
                'number_of_atomic_paths': 1,
                'number_of_live_unknown_atomic': 1,
                'number_of_live_up_atomic_paths': 1,
                'number_of_segment_lists': 1,
                'preference': 100,
                'protocol_origin': 'CLI',
                'round_robin_bursts': 1,
                'round_robin_probes': 1,
                'segment_list': {
                    'atomic_paths': {
                        0: {
                            'current_probe': {
                                'measured_delays': {
                                    'average': 1000,
                                    'maximum': 1000,
                                    'minimum': 1000,
                                    'variance': 0
                                },
                                'packets': {
                                    'packets_received': 2,
                                    'packets_sent': 2
                                }
                            },
                            'destination': '1.1.1.7',
                            'hops': {
                                0: '1.1.1.7'
                            },
                            'labels': {
                                0: '16230'
                            },
                            'last_advertisement': {
                                'advertised_at': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 48,
                                    'second': 42,
                                    'seconds_ago': 101076,
                                    'year': 2021
                                },
                                'advertised_delays': {
                                    'average': 566,
                                    'maximum': 1000,
                                    'minimum': 1,
                                    'variance': 565
                                },
                                'advertised_reason': 'First advertisement'
                            },
                            'last_probe': {},
                            'liveness_detection': {
                                'backoff': 0,
                                'last_state_change_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 54.404
                                },
                                'loss_in_last_interval': {
                                    'percent': 0,
                                    'rx': 2,
                                    'tx': 2
                                },
                                'missed_count': 0,
                                'received_count': 33728,
                                'session_creation_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 52.222
                                },
                                'session_state': 'Up',
                                'unique_path_name': 'Path-10'
                            },
                            'max_ip_mtu': 1500,
                            'next_advertisement': {
                                'aggregate_delays': {
                                    'average': 100,
                                    'maximum': 1000,
                                    'minimum': 1,
                                    'variance': 99
                                },
                                'rolling_average': 238
                            },
                            'next_hop': '110.1.1.4',
                            'outgoing_interface': 'Ethernet0/1',
                            'probe_samples': {
                                'samples': {
                                    0: {
                                        'day': 21,
                                        'delay': 1000000,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 16,
                                        'year': 2021
                                    },
                                    1: {
                                        'day': 21,
                                        'delay': 1000000,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 13,
                                        'year': 2021
                                    }
                                }
                            },
                            'session_id': 11
                        }
                    },
                    'current_probe': {},
                    'last_advertisement': {
                        'advertised_at': {
                            'day': 20,
                            'hour': 6,
                            'minute': 48,
                            'second': 42,
                            'seconds_ago': 101076,
                            'year': 2021
                        },
                        'advertised_delays': {
                            'average': 566,
                            'maximum': 1000,
                            'minimum': 1,
                            'variance': 565
                        }
                    },
                    'last_probe': {},
                    'name': 'SL8',
                    'next_advertisement': {
                        'aggregate_delays': {
                            'average': 100,
                            'maximum': 1000,
                            'minimum': 1,
                            'variance': 99
                        }
                    },
                    'number_of_atomic_paths': 1
                }
            }
        },
        'color': 1236,
        'endpoint': '1.1.1.7',
        'number_of_candidate_paths': 1,
        'policy_update_timestamp': {
            'day': 20,
            'hour': 6,
            'minute': 46,
            'month': 5,
            'second': 52.222
        },
        'profile_name': 'E01',
        'source': '1.1.1.3'
    },
    'PM': {
        'candidate_paths': {
            0: {
                'active': 'No',
                'ap_min_run_per_probe': 3,
                'current_probe': {
                    'measured_delays': {
                        'average': 499,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 498
                    },
                    'packets': {
                        'packets_received': 6,
                        'packets_sent': 6
                    }
                },
                'discriminator': 0,
                'last_advertisement': {
                    'advertised_at': {
                        'day': 20,
                        'hour': 9,
                        'minute': 6,
                        'second': 42,
                        'seconds_ago': 92796,
                        'year': 2021
                    },
                    'advertised_delays': {
                        'average': 603,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 602
                    }
                },
                'last_probe': {
                    'measured_delays': {
                        'average': 466,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 465
                    },
                    'packets': {
                        'packets_received': 30,
                        'packets_sent': 30
                    }
                },
                'max_packets_per_burst': 500,
                'max_packets_per_probe': 15000,
                'next_advertisement': {
                    'aggregate_delays': {
                        'average': 466,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 465
                    },
                    'check_schedule': {
                        'probes': 2,
                        'seconds': 120
                    }
                },
                'number_of_atomic_paths': 1,
                'number_of_live_unknown_atomic': 1,
                'number_of_live_up_atomic_paths': 1,
                'number_of_segment_lists': 1,
                'preference': 100,
                'protocol_origin': 'CLI',
                'round_robin_bursts': 1,
                'round_robin_probes': 1,
                'segment_list': {
                    'atomic_paths': {
                        0: {
                            'current_probe': {
                                'measured_delays': {
                                    'average': 499,
                                    'maximum': 999,
                                    'minimum': 1,
                                    'variance': 498
                                },
                                'packets': {
                                    'packets_received': 6,
                                    'packets_sent': 6
                                }
                            },
                            'destination': '1.1.1.7',
                            'hops': {
                                0: '1.1.1.7'
                            },
                            'labels': {
                                0: '16230'
                            },
                            'last_advertisement': {
                                'advertised_at': {
                                    'day': 20,
                                    'hour': 9,
                                    'minute': 6,
                                    'second': 42,
                                    'seconds_ago': 92796,
                                    'year': 2021
                                },
                                'advertised_delays': {
                                    'average': 603,
                                    'maximum': 999,
                                    'minimum': 1,
                                    'variance': 229
                                },
                                'advertised_reason': 'Periodic timer, avg delay threshold crossed'
                            },
                            'last_probe': {
                                'measured_delays': {
                                    'average': 466,
                                    'maximum': 999,
                                    'minimum': 1,
                                    'variance': 465
                                },
                                'packets': {
                                    'packets_received': 30,
                                    'packets_sent': 30
                                }
                            },
                            'liveness_detection': {
                                'backoff': 0,
                                'last_state_change_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 52.382
                                },
                                'loss_in_last_interval': {
                                    'percent': 0,
                                    'rx': 6,
                                    'tx': 6
                                },
                                'missed_count': 0,
                                'received_count': 101186,
                                'session_creation_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 52.222
                                },
                                'session_state': 'Up',
                                'unique_path_name': 'Path-10'
                            },
                            'max_ip_mtu': 1500,
                            'next_advertisement': {
                                'aggregate_delays': {
                                    'average': 466,
                                    'maximum': 999,
                                    'minimum': 1,
                                    'variance': 465
                                },
                                'rolling_average': 467
                            },
                            'next_hop': '110.1.1.4',
                            'outgoing_interface': 'Ethernet0/1',
                            'probe_samples': {
                                'samples': {
                                    0: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 17,
                                        'year': 2021
                                    },
                                    1: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 16,
                                        'year': 2021
                                    },
                                    2: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 15,
                                        'year': 2021
                                    },
                                    3: {
                                        'day': 21,
                                        'delay': 999999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 14,
                                        'year': 2021
                                    },
                                    4: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 13,
                                        'year': 2021
                                    },
                                    5: {
                                        'day': 21,
                                        'delay': 0,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 12,
                                        'year': 2021
                                    }
                                }
                            },
                            'session_id': 13
                        }
                    },
                    'current_probe': {
                        'measured_delays': {
                            'average': 499,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 498
                        },
                        'packets': {
                            'packets_received': 6,
                            'packets_sent': 6
                        }
                    },
                    'last_advertisement': {
                        'advertised_at': {
                            'day': 20,
                            'hour': 9,
                            'minute': 6,
                            'second': 42,
                            'seconds_ago': 92796,
                            'year': 2021
                        },
                        'advertised_delays': {
                            'average': 603,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 602
                        }
                    },
                    'last_probe': {
                        'measured_delays': {
                            'average': 466,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 465
                        },
                        'packets': {
                            'packets_received': 30,
                            'packets_sent': 30
                        }
                    },
                    'name': 'SL6',
                    'next_advertisement': {
                        'aggregate_delays': {
                            'average': 466,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 465
                        }
                    },
                    'number_of_atomic_paths': 1
                }
            },
            1: {
                'active': 'Yes',
                'ap_min_run_per_probe': 3,
                'current_probe': {
                    'measured_delays': {
                        'average': 416,
                        'maximum': 499,
                        'minimum': 1,
                        'variance': 415
                    },
                    'packets': {
                        'packets_received': 6,
                        'packets_sent': 6
                    }
                },
                'discriminator': 0,
                'last_advertisement': {
                    'advertised_at': {
                        'day': 20,
                        'hour': 9,
                        'minute': 6,
                        'second': 42,
                        'seconds_ago': 92796,
                        'year': 2021
                    },
                    'advertised_delays': {
                        'average': 557,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 556
                    }
                },
                'last_probe': {
                    'measured_delays': {
                        'average': 516,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 515
                    },
                    'packets': {
                        'packets_received': 30,
                        'packets_sent': 30
                    }
                },
                'max_packets_per_burst': 500,
                'max_packets_per_probe': 15000,
                'next_advertisement': {
                    'aggregate_delays': {
                        'average': 516,
                        'maximum': 999,
                        'minimum': 1,
                        'variance': 515
                    },
                    'check_schedule': {
                        'probes': 2,
                        'seconds': 120
                    }
                },
                'number_of_atomic_paths': 1,
                'number_of_live_unknown_atomic': 1,
                'number_of_live_up_atomic_paths': 1,
                'number_of_segment_lists': 1,
                'preference': 200,
                'protocol_origin': 'CLI',
                'round_robin_bursts': 1,
                'round_robin_probes': 1,
                'segment_list': {
                    'atomic_paths': {
                        0: {
                            'current_probe': {
                                'measured_delays': {
                                    'average': 416,
                                    'maximum': 499,
                                    'minimum': 1,
                                    'variance': 415
                                },
                                'packets': {
                                    'packets_received': 6,
                                    'packets_sent': 6
                                }
                            },
                            'destination': '1.1.1.7',
                            'hops': {
                                0: '1.2.3.3',
                                1: '90.1.1.4',
                                2: '55.1.1.5'
                            },
                            'labels': {
                                0: '25',
                                1: '17'
                            },
                            'last_advertisement': {
                                'advertised_at': {
                                    'day': 20,
                                    'hour': 9,
                                    'minute': 6,
                                    'second': 42,
                                    'seconds_ago': 92796,
                                    'year': 2021
                                },
                                'advertised_delays': {
                                    'average': 557,
                                    'maximum': 999,
                                    'minimum': 1,
                                    'variance': 431
                                },
                                'advertised_reason': 'Periodic timer, avg delay threshold crossed'
                            },
                            'last_probe': {
                                'measured_delays': {
                                    'average': 516,
                                    'maximum': 999,
                                    'minimum': 1,
                                    'variance': 515
                                },
                                'packets': {
                                    'packets_received': 30,
                                    'packets_sent': 30
                                }
                            },
                            'liveness_detection': {
                                'backoff': 0,
                                'last_state_change_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 52.674
                                },
                                'loss_in_last_interval': {
                                    'percent': 0,
                                    'rx': 6,
                                    'tx': 6
                                },
                                'missed_count': 0,
                                'received_count': 101186,
                                'session_creation_timestamp': {
                                    'day': 20,
                                    'hour': 6,
                                    'minute': 46,
                                    'month': 5,
                                    'second': 52.222
                                },
                                'session_state': 'Up',
                                'unique_path_name': 'Path-11'
                            },
                            'max_ip_mtu': 1500,
                            'next_advertisement': {
                                'aggregate_delays': {
                                    'average': 516,
                                    'maximum': 999,
                                    'minimum': 1,
                                    'variance': 515
                                },
                                'rolling_average': 508
                            },
                            'next_hop': '1.2.3.4',
                            'outgoing_interface': 'Ethernet1/2',
                            'probe_samples': {
                                'samples': {
                                    0: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 18,
                                        'year': 2021
                                    },
                                    1: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 17,
                                        'year': 2021
                                    },
                                    2: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 16,
                                        'year': 2021
                                    },
                                    3: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 15,
                                        'year': 2021
                                    },
                                    4: {
                                        'day': 21,
                                        'delay': 499999,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 14,
                                        'year': 2021
                                    },
                                    5: {
                                        'day': 21,
                                        'delay': 0,
                                        'hour': 10,
                                        'minute': 53,
                                        'second': 13,
                                        'year': 2021
                                    }
                                }
                            },
                            'session_id': 12
                        }
                    },
                    'current_probe': {
                        'measured_delays': {
                            'average': 416,
                            'maximum': 499,
                            'minimum': 1,
                            'variance': 415
                        },
                        'packets': {
                            'packets_received': 6,
                            'packets_sent': 6
                        }
                    },
                    'last_advertisement': {
                        'advertised_at': {
                            'day': 20,
                            'hour': 9,
                            'minute': 6,
                            'second': 42,
                            'seconds_ago': 92796,
                            'year': 2021
                        },
                        'advertised_delays': {
                            'average': 557,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 556
                        }
                    },
                    'last_probe': {
                        'measured_delays': {
                            'average': 516,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 515
                        },
                        'packets': {
                            'packets_received': 30,
                            'packets_sent': 30
                        }
                    },
                    'name': 'SL5',
                    'next_advertisement': {
                        'aggregate_delays': {
                            'average': 516,
                            'maximum': 999,
                            'minimum': 1,
                            'variance': 515
                        }
                    },
                    'number_of_atomic_paths': 1
                }
            },
            2: {
                'active': 'No',
                'ap_min_run_per_probe': 3,
                'current_probe': {},
                'discriminator': 0,
                'last_advertisement': {},
                'last_probe': {},
                'max_packets_per_burst': 0,
                'max_packets_per_probe': 0,
                'next_advertisement': {
                    'check_schedule': {
                        'probes': 2,
                        'seconds': 120
                    }
                },
                'number_of_atomic_paths': 0,
                'number_of_live_unknown_atomic': 0,
                'number_of_live_up_atomic_paths': 0,
                'number_of_segment_lists': 1,
                'preference': 300,
                'protocol_origin': 'CLI',
                'round_robin_bursts': 0,
                'round_robin_probes': 0,
                'segment_list': {
                    'current_probe': {},
                    'last_advertisement': {},
                    'last_probe': {},
                    'name': 'SL4',
                    'next_advertisement': {},
                    'number_of_atomic_paths': 0
                }
            }
        },
        'color': 1234,
        'endpoint': '1.1.1.7',
        'number_of_candidate_paths': 3,
        'policy_update_timestamp': {
            'day': 21,
            'hour': 10,
            'minute': 46,
            'month': 5,
            'second': 34.131
        },
        'profile_name': 'Not configured',
        'source': '1.1.1.3'
    }
}
