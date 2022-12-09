expected_output = {
    'sw_distrib': {
        'dist_mode': 'NSFBD',
        'inactive_ppes': '4-9',
        'rx_stats': {
            'source_id': {
                '0': {
                    'name': 'DST',
                    'pmask': '0x3f0',
                    'port': {
                        '4': {
                            'port_name': '(fpe0/GigabitEthernet0/0/0)',
                            'classifier': 'L4TUPLE',
                            'credit_error': '-',
                            'pp': {
                                '0': {
                                    'flushes': '699898',
                                    'flushed': '699920',
                                    'spin': '-',
                                    'sw_hash': '699920',
                                    'coff_directed': '-',
                                    'total': '699920'
                                },
                                '1': {
                                    'flushes': '1104357',
                                    'flushed': '1109143',
                                    'spin': '-',
                                    'sw_hash': '1109143',
                                    'coff_directed': '-',
                                    'total': '1109143'
                                },
                                '2': {
                                    'flushes': '62',
                                    'flushed': '62',
                                    'spin': '-',
                                    'sw_hash': '62',
                                    'coff_directed': '-',
                                    'total': '62'
                                },
                                '3': {
                                    'flushes': '154',
                                    'flushed': '154',
                                    'spin': '-',
                                    'sw_hash': '154',
                                    'coff_directed': '-',
                                    'total': '154'
                                },
                                '11': {
                                    'flushes': '-',
                                    'flushed': '-',
                                    'spin': '-',
                                    'sw_hash': '-',
                                    'coff_directed': '5392126',
                                    'total': '5392126'
                                }
                            }
                        },
                        '5': {
                            'port_name': '(fpe1/GigabitEthernet0/0/1)',
                            'classifier': 'L4TUPLE',
                            'credit_error': '-',
                            'pp': {
                                '0': {
                                    'flushes': '437963',
                                    'flushed': '438170',
                                    'spin': '-',
                                    'sw_hash': '438170',
                                    'total': '438170'
                                },
                                '1': {
                                    'flushes': '1117613',
                                    'flushed': '1118379',
                                    'spin': '-',
                                    'sw_hash': '1118379',
                                    'total': '1118379'
                                },
                                '2': {
                                    'flushes': '705275',
                                    'flushed': '706125',
                                    'spin': '-',
                                    'sw_hash': '706125',
                                    'total': '706125'
                                },
                                '3': {
                                    'flushes': '684700',
                                    'flushed': '684997',
                                    'spin': '-',
                                    'sw_hash': '684997',
                                    'total': '684997'
                                }
                            }
                        },
                        '6': {
                            'port_name': '(fpe2/GigabitEthernet0/0/2)',
                            'classifier': 'L4TUPLE',
                            'credit_error': '-',
                            'pp': {
                                '0': {
                                    'flushes': '4767356568',
                                    'flushed': '7460738787',
                                    'spin': '-',
                                    'sw_hash': '7460738787',
                                    'total': '7460738787'
                                },
                                '1': {
                                    'flushes': '3731300598',
                                    'flushed': '3733800638',
                                    'spin': '-',
                                    'sw_hash': '3733800638',
                                    'total': '3733800638'
                                },
                                '2': {
                                    'flushes': '7374181015',
                                    'flushed': '11196023108',
                                    'spin': '-',
                                    'sw_hash': '11196023108',
                                    'total': '11196023108'
                                },
                                '3': {
                                    'flushes': '3727057997',
                                    'flushed': '3727069386',
                                    'spin': '-',
                                    'sw_hash': '3727069386',
                                    'total': '3727069386'
                                }
                            }
                        },
                        '7': {
                            'port_name': '(fpe3/GigabitEthernet0/0/3)',
                            'classifier': 'L4TUPLE',
                            'credit_error': '-',
                            'pp': {
                                '3': {
                                    'flushes': '322255',
                                    'flushed': '322255',
                                    'spin': '-',
                                    'sw_hash': '322255',
                                    'total': '322255'
                                }
                            }
                        },
                        '8': {
                            'port_name': '(fpe4/GigabitEthernet0/0/4)',
                            'classifier': 'L4TUPLE',
                            'credit_error': '-',
                            'pp': {
                                '0': {
                                    'flushes': '36664',
                                    'flushed': '36664',
                                    'spin': '-',
                                    'sw_hash': '36664',
                                    'coff_directed': '-',
                                    'total': '36664'
                                },
                                '1': {
                                    'flushes': '388',
                                    'flushed': '388',
                                    'spin': '-',
                                    'sw_hash': '388',
                                    'coff_directed': '-',
                                    'total': '388'
                                },
                                '2': {
                                    'flushes': '644558',
                                    'flushed': '644563',
                                    'spin': '-',
                                    'sw_hash': '644563',
                                    'coff_directed': '-',
                                    'total': '644563'
                                },
                                '3': {
                                    'flushes': '94489',
                                    'flushed': '102255',
                                    'spin': '-',
                                    'sw_hash': '102255',
                                    'coff_directed': '-',
                                    'total': '102255'
                                },
                                '11': {
                                    'flushes': '-',
                                    'flushed': '-',
                                    'spin': '-',
                                    'sw_hash': '-',
                                    'coff_directed': '5392172',
                                    'total': '5392172'
                                }
                            }
                        }
                    }
                },
                '1': {
                    'name': 'RCL',
                    'pmask': '0x02',
                    'port': {
                        '1': {
                            'port_name': '(rcl0/rcl0)',
                            'classifier': 'RECYCLE',
                            'credit_error': '-',
                            'pp': {
                                '0': {
                                    'flushes': '19535941',
                                    'flushed': '19540871',
                                    'spin': '-',
                                    'sw_hash': '19540871',
                                    'total': '19540871'
                                },
                                '1': {
                                    'flushes': '8336076',
                                    'flushed': '8405908',
                                    'spin': '-',
                                    'sw_hash': '8405908',
                                    'total': '8405908'
                                },
                                '2': {
                                    'flushes': '576095587',
                                    'flushed': '1165557978',
                                    'spin': '-',
                                    'sw_hash': '1165557978',
                                    'total': '1165557978'
                                },
                                '3': {
                                    'flushes': '1360299',
                                    'flushed': '1365775',
                                    'spin': '-',
                                    'sw_hash': '1365775',
                                    'total': '1365775'
                                }
                            }
                        }
                    }
                },
                '2': {
                    'name': 'IPC',
                    'pmask': '0x04',
                    'port': {
                        '2': {
                            'port_name': '(ipc/ipc)',
                            'classifier': 'IPC',
                            'credit_error': '4939494',
                            'pp': {
                                '0': {
                                    'flushes': '920888',
                                    'flushed': '920888',
                                    'spin': '-',
                                    'sw_hash': '920888',
                                    'total': '920888'
                                },
                                '1': {
                                    'flushes': '920888',
                                    'flushed': '920888',
                                    'spin': '-',
                                    'sw_hash': '920888',
                                    'total': '920888'
                                },
                                '2': {
                                    'flushes': '920888',
                                    'flushed': '920888',
                                    'spin': '-',
                                    'sw_hash': '920888',
                                    'total': '920888'
                                },
                                '3': {
                                    'flushes': '920887',
                                    'flushed': '920887',
                                    'spin': '-',
                                    'sw_hash': '920887',
                                    'total': '920887'
                                }
                            }
                        }
                    }
                },
                '3': {
                    'name': 'LSMPI',
                    'pmask': '0x08',
                    'port': {
                        '3': {
                            'port_name': '(vxe_punti/vxe_puntif)',
                            'classifier': 'LSMPI',
                            'credit_error': '-',
                            'pp': {
                                '0': {
                                    'flushes': '105424',
                                    'flushed': '124727',
                                    'spin': '-',
                                    'sw_hash': '124727',
                                    'coff_directed': '-',
                                    'total': '124727'
                                },
                                '1': {
                                    'flushes': '691463',
                                    'flushed': '760512',
                                    'spin': '-',
                                    'sw_hash': '760512',
                                    'coff_directed': '-',
                                    'total': '760512'
                                },
                                '2': {
                                    'flushes': '1811684',
                                    'flushed': '2086691',
                                    'spin': '-',
                                    'sw_hash': '2086691',
                                    'coff_directed': '-',
                                    'total': '2086691'
                                },
                                '3': {
                                    'flushes': '359390',
                                    'flushed': '379228',
                                    'spin': '-',
                                    'sw_hash': '33498',
                                    'coff_directed': '345730',
                                    'total': '379228'
                                }
                            }
                        }
                    }
                },
                '5': {
                    'name': 'SVC',
                    'pmask': '0xc00',
                    'port': {
                        '10': {
                            'port_name': '(vpg0/vpg0)',
                            'classifier': 'SVC_ENGINE_PI',
                            'credit_error': '-',
                            'pp': {
                                '1': {
                                    'flushes': '1',
                                    'flushed': '1',
                                    'spin': '-',
                                    'sw_hash': '1',
                                    'total': '1'
                                },
                                '2': {
                                    'flushes': '93',
                                    'flushed': '94',
                                    'spin': '-',
                                    'sw_hash': '94',
                                    'total': '94'
                                }
                            }
                        },
                        '11': {
                            'port_name': '(vpg1/vpg1)',
                            'classifier': 'SVC_ENGINE_PI',
                            'credit_error': '-',
                            'pp': {
                                '0': {
                                    'flushes': '95',
                                    'flushed': '96',
                                    'spin': '-',
                                    'sw_hash': '96',
                                    'total': '96'
                                },
                                '2': {
                                    'flushes': '1',
                                    'flushed': '1',
                                    'spin': '-',
                                    'sw_hash': '1',
                                    'total': '1'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
