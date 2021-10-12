

expected_output = {
    'instance': {
        'isp': {
            'address_family': {
                'IPv4 Unicast': {
                    'spf_log': {
                        1: {
                            'type': 'FSPF',
                            'time_ms': 1,
                            'level': 1,
                            'total_nodes': 1,
                            'trigger_count': 1,
                            'first_trigger_lsp': '12a5.00-00',
                            'triggers': 'NEWLSP0',
                            'start_timestamp': 'Mon Aug 16 2004 19:25:35.140',
                            'delay': {
                                'since_first_trigger_ms': 51,
                            },
                            'spt_calculation': {
                                'cpu_time_ms': 0,
                                'real_time_ms': 0,
                            },
                            'prefix_update': {
                                'cpu_time_ms': 1,
                                'real_time_ms': 1,
                            },
                            'new_lsp_arrivals': 0,
                            'next_wait_interval_ms': 200,
                            'results': {
                                'nodes': {
                                    'reach': 1,
                                    'unreach': 0,
                                    'total': 1,
                                },
                                'prefixes': {
                                    'items': {
                                        'critical_priority': {
                                            'reach': 0,
                                            'unreach': 0,
                                            'total': 0,
                                        },
                                        'high_priority': {
                                            'reach': 0,
                                            'unreach': 0,
                                            'total': 0,
                                        },
                                        'medium_priority': {
                                            'reach': 0,
                                            'unreach': 0,
                                            'total': 0,
                                        },
                                        'low_priority': {
                                            'reach': 0,
                                            'unreach': 0,
                                            'total': 0,
                                        },
                                        'all_priority': {
                                            'reach': 0,
                                            'unreach': 0,
                                            'total': 0,
                                        },
                                    },
                                    'routes': {
                                        'critical_priority': {
                                            'reach': 0,
                                            'total': 0,
                                        },
                                        'high_priority': {
                                            'reach': 0,
                                            'total': 0,
                                        },
                                        'medium_priority': {
                                            'reach': 0,
                                            'total': 0,
                                        },
                                        'low_priority': {
                                            'reach': 0,
                                            'total': 0,
                                        },
                                        'all_priority': {
                                            'reach': 0,
                                            'total': 0,
                                        },
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
