expected_output = {
    'instance': {
        '1': {
            'process_id': '1',
            'instance': '0',
            'vrf': {
                'default': {
                    'system_id': '0000.0000.0000',
                    'is_levels': 'level-2-only',
                    'non_stop_forwarding': 'Disabled',
                    'most_recent_startup_mode': 'Cold Restart',
                    'te_connection_status': 'Up',
                    'topology': {
                        'IPv4 Unicast': {
                            'vrf': {
                                'default': {
                                    'protocols_redistributed': False,
                                    'distance': 115,
                                    'adv_passive_only': False
                                }
                            }
                        }
                    },
                    'srlb': {
                        'start': 15000,
                        'end': 15999
                    },
                    'srgb': {
                        'start': 16000,
                        'end': 23999
                    },
                    'interfaces': {
                        'GigabitEthernet0/0/0/1': {
                            'running_state': 'disabled',
                            'configuration_state': 'active in configuration'
                        }
                    }
                }
            }
        },
        '10': {
            'process_id': '10',
            'instance': '0',
            'vrf': {
                'default': {
                    'system_id': '1620.1600.1001',
                    'is_levels': 'level-2-only',
                    'manual_area_address': ['49.0001', '49.0002'],
                    'routing_area_address': ['49.0001', '49.0002'],
                    'non_stop_forwarding': 'IETF',
                    'most_recent_startup_mode': 'Cold Restart',
                    'te_connection_status': 'Up',
                    'topology': {
                        'IPv4 Unicast': {
                            'vrf': {
                                'default': {
                                    'level': {
                                        2: {
                                            'generate_style': 'Wide',
                                            'accept_style': 'Wide',
                                            'metric': 10
                                        }
                                    },
                                    'protocols_redistributed': False,
                                    'distance': 115,
                                    'adv_passive_only': False
                                }
                            }
                        },
                        'IPv6 Unicast': {
                            'vrf': {
                                'default': {
                                    'level': {
                                        2: {
                                            'metric': 10
                                        }
                                    },
                                    'protocols_redistributed': False,
                                    'distance': 115,
                                    'adv_passive_only': False
                                }
                            }
                        }
                    },
                    'srlb': {
                        'start': 15000,
                        'end': 15999
                    },
                    'srgb': {
                        'start': 16000,
                        'end': 23999
                    },
                    'interfaces': {
                        'Bundle-Ether10': {
                            'running_state': 'running actively',
                            'configuration_state': 'active in configuration'
                        },
                        'Bundle-Ether10.10': {
                            'running_state': 'running actively',
                            'configuration_state': 'active in configuration'
                        },
                        'GigabitEthernet0/0/0/1.10': {
                            'running_state': 'disabled',
                            'configuration_state': 'active in configuration'
                        },
                        'GigabitEthernet0/0/0/1.19': {
                            'running_state': 'disabled',
                            'configuration_state': 'active in configuration'
                        }
                    }
                }
            }
        },
        '99': {
            'process_id': '99',
            'instance': '0',
            'vrf': {
                'default': {
                    'system_id': '1620.1600.5005',
                    'is_levels': 'level-1',
                    'manual_area_address': ['49.0001'],
                    'routing_area_address': ['49.0001'],
                    'non_stop_forwarding': 'Disabled',
                    'most_recent_startup_mode': 'Cold Restart',
                    'te_connection_status': 'Up',
                    'topology': {
                        'IPv4 Unicast': {
                            'vrf': {
                                'default': {
                                    'level': {
                                        1: {
                                            'generate_style': 'Wide',
                                            'accept_style': 'Wide',
                                            'metric': 10
                                        }
                                    },
                                    'protocols_redistributed': False,
                                    'distance': 115,
                                    'adv_passive_only': False
                                }
                            }
                        }
                    },
                    'interfaces': {
                        'GigabitEthernet0/0/0/6': {
                            'running_state': 'disabled',
                            'configuration_state': 'active in configuration'
                        }
                    }
                }
            }
        }
    }
}