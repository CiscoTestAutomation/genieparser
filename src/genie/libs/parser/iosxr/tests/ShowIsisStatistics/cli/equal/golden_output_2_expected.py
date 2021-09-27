

expected_output = {
    'isis': {
        'COEUR': {
            'csnp_cache': {
                'hits': 0,
                'tries': 49,
                'updates': 66,
            },
            'interface': {
                'Bundle-Ether10': {
                    'level': {
                        1: {
                            'csnp': {
                                'received': 24,
                                'sent': 24,
                            },
                            'lsps_sourced': {
                                'arrival_time_throttled': 0,
                                'flooding_duplicates': 162,
                                'received': 57776373,
                                'sent': 2218410,
                            },
                            'psnp': {
                                'received': 1576294,
                                'sent': 33297781,
                            },
                        },
                    },
                },
                'Bundle-Ether11': {
                    'level': {
                        1: {
                            'csnp': {
                                'received': 36,
                                'sent': 25,
                            },
                            'lsps_sourced': {
                                'arrival_time_throttled': 0,
                                'flooding_duplicates': 15,
                                'received': 57701052,
                                'sent': 2724240,
                            },
                            'psnp': {
                                'received': 1761310,
                                'sent': 33274400,
                            },
                        },
                    },
                },
                'Loopback0': {
                },
                'Loopback6': {
                },
            },
            'level': {
                1: {
                    'address_family': {
                        'IPv4 Unicast': {
                            'full_spf_calculation': 331056,
                            'ispf_calculation': 0,
                            'next_hop_calculation': 4,
                            'partial_route_calculation': 891257,
                            'periodic_spf_calculation': 39298,
                            'total_spf_calculation': 1222317,
                        },
                        'IPv6 Unicast': {
                            'full_spf_calculation': 177541,
                            'ispf_calculation': 0,
                            'next_hop_calculation': 4,
                            'partial_route_calculation': 57170,
                            'periodic_spf_calculation': 43596,
                            'total_spf_calculation': 234715,
                        },
                    },
                    'lsp': {
                        'new': 9140,
                        'refresh': 117187,
                    },
                },
            },
            'lsp': {
                'checksum_errors_received': 0,
                'dropped': 0,
            },
            'process_time': {
                'csnp': {
                    'average_process_time_nsec': 1249805,
                    'average_process_time_sec': 0,
                    'rate_per_sec': 0,
                },
                'hello': {
                    'average_process_time_nsec': 999833,
                    'average_process_time_sec': 0,
                    'rate_per_sec': 0,
                },
                'lsp': {
                    'average_process_time_nsec': 999840,
                    'average_process_time_sec': 0,
                    'rate_per_sec': 0,
                },
                'psnp': {
                    'average_process_time_nsec': 999835,
                    'average_process_time_sec': 0,
                    'rate_per_sec': 0,
                },
            },
            'psnp_cache': {
                'hits': 57508538,
                'tries': 115477425,
            },
            'snp': {
                'dropped': 0,
            },
            'transmit_time': {
                'csnp': {
                    'average_transmit_time_nsec': 0,
                    'average_transmit_time_sec': 0,
                    'rate_per_sec': 0,
                },
                'hello': {
                    'average_transmit_time_nsec': 999840,
                    'average_transmit_time_sec': 0,
                    'rate_per_sec': 0,
                },
                'lsp': {
                    'average_transmit_time_nsec': 999840,
                    'average_transmit_time_sec': 0,
                    'rate_per_sec': 0,
                },
                'psnp': {
                    'average_transmit_time_nsec': 999836,
                    'average_transmit_time_sec': 0,
                    'rate_per_sec': 0,
                },
            },
            'upd': {
                'max_queue_size': 20,
            },
        },
    },
}
