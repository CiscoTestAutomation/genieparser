expected_output = {
    'interface': {
        'GigabitEthernet0/0/0/6': {
            'service_policy': {
                'input': {
                    'policy_status': 'Service Policy not installed',
                },
                'output': {
                    'policy_name': {
                        'p1': {
                            'class': {
                                'class-default': {
                                    'classification_statistics': {
                                        'matched': {
                                            'packets/bytes': '0/0',
                                            'rate/kbps': 0,
                                        },
                                        'total_dropped': {
                                            'packets/bytes': '0/0',
                                            'rate/kbps': 0,
                                        },
                                        'transmitted': {
                                            'packets/bytes': '0/0',
                                            'rate/kbps': 0,
                                        },
                                    },
                                    'queueing_statistics': {
                                        'avg_queue_len': 'N/A',
                                        'high_watermark': 'N/A',
                                        'inst_queue_len': 'N/A',
                                        'queue_conform_bytes': 0,
                                        'queue_conform_packets': 0,
                                        'queue_conform_rate': 0,
                                        'queue_id': 56,
                                        'red_random_drops_bytes': 0,
                                        'red_random_drops_packets': 0,
                                        'taildropped': '0/0',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
