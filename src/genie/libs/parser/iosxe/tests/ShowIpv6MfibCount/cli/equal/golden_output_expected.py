expected_output = {
    'ip_multicast_statistics': {
        'total_routes': 54,
        'total_groups': 7,
        'average_sources_per_group': 0.14,
        'forwarding_counts_description': 'Pkt Count/Pkts per second/Avg Pkt Size/Kilobits per second',
        'other_counts_description': 'Total/RPF failed/Other drops(OIF-null, rate-limit etc)',
        'groups': {
            'FF00::/8': {
                'rp_tree': {
                    'forwarding': {
                        'pkt_count': 0,
                        'pkts_per_second': 0,
                        'avg_pkt_size': 0,
                        'kilobits_per_second': 0,
                    },
                    'other': {
                        'total': 0,
                        'rpf_failed': 0,
                        'other_drops': 0,
                    }
                }
            },
            'FF00::/15': {
                'rp_tree': {
                    'forwarding': {
                        'pkt_count': 0,
                        'pkts_per_second': 0,
                        'avg_pkt_size': 0,
                        'kilobits_per_second': 0,
                    },
                    'other': {
                        'total': 0,
                        'rpf_failed': 0,
                        'other_drops': 0,
                    }
                }
            },
            'FF05::1': {
                'rp_tree': {
                    'forwarding': {
                        'pkt_count': 2,
                        'pkts_per_second': 0,
                        'avg_pkt_size': 100,
                        'kilobits_per_second': 0,
                    },
                    'other': {
                        'total': 0,
                        'rpf_failed': 0,
                        'other_drops': 0,
                    }
                },
                'sources': {
                    '10::1:1:200': {
                        'forwarding': {
                            'pkt_count': 367,
                            'pkts_per_second': 10,
                            'avg_pkt_size': 100,
                            'kilobits_per_second': 7,
                        },
                        'other': {
                            'total': 0,
                            'rpf_failed': 0,
                            'other_drops': 0,
                        }
                    }
                },
                'total_shown': {
                    'source_count': 1,
                    'pkt_count': 369,
                }
            },
            'FF10::/15': {
                'rp_tree': {
                    'forwarding': {
                        'pkt_count': 0,
                        'pkts_per_second': 0,
                        'avg_pkt_size': 0,
                        'kilobits_per_second': 0,
                    },
                    'other': {
                        'total': 0,
                        'rpf_failed': 0,
                        'other_drops': 0,
                    }
                }
            },
            'FF20::/15': {
                'rp_tree': {
                    'forwarding': {
                        'pkt_count': 0,
                        'pkts_per_second': 0,
                        'avg_pkt_size': 0,
                        'kilobits_per_second': 0,
                    },
                    'other': {
                        'total': 0,
                        'rpf_failed': 0,
                        'other_drops': 0,
                    }
                }
            }
        }
    }
}