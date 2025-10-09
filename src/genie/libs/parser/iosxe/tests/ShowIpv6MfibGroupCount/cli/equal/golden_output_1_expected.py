expected_output = {
    'vrf': {
        'Default': {
            'routes': 56,
            'star_g': 9,
            'star_g_m': 46,
            'group': {
                'FF03::1:1:1': {
                    'source': {
                        '10::1:1:200': {
                            'sw_forwarding': {
                                'pkt_count': 0,
                                'pkts_per_second': 0,
                                'avg_pkt_size': 0,
                                'kilobits_per_second': 0,
                            },
                            'other': {
                                'total': 0,
                                'rpf_failed': 0,
                                'other_drops': 0,
                            },
                            'hw_forwarding': {
                                'pkt_count': 5,
                                'pkts_per_second': 0,
                                'avg_pkt_size': 80,
                                'kilobits_per_second': 0,
                            },
                            'hw_other': {
                                'total': 0,
                                'rpf_failed': 0,
                                'other_drops': 0,
                            },
                        }
                    },
                    'totals': {
                        'source_count': 1,
                        'packet_count': 5,
                    }
                }
            },
            'groups': 1,
            'average_sources_per_group': 1.00,
        }
    }
}
