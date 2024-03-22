expected_output = {
    'nat64_stats': {
        'active_sessions': 0,
        'active_translations': {
            'dynamic': 0,
            'extended': 1,
            'static': 14,
            'total_translations': 15
        },
        'dynamic_mapping_statistics': {
            'access_list': {
                'acl_1': {
                    'pool': {
                        'n64_pool': {
                            'allocated': 0,
                            'end_ip': '135.0.0.100',
                            'nat64_pool_name': 'n64_pool',
                            'packet_count': 0,
                            'percent': 0,
                            'start_ip': '135.0.0.1',
                            'total_address': 100
                        }
                    },
                    'refcount': 0
                },
                'acl_2': {
                    'pool': {
                        'n64_pool2': {
                            'allocated': 0,
                            'end_ip': '136.0.0.100',
                            'nat64_pool_name': 'n64_pool2',
                            'packet_count': 0,
                            'percent': 0,
                            'start_ip': '136.0.0.1',
                            'total_address': 100
                        }
                    },
                    'refcount': 0
                }
            }
        },
        'expired_sessions': 0,
        'global_statistics': {
            'prefix': {
                '1001::/96': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 0,
                        'v6_to_v4': 14
                    }
                },
                '64:FF9B::/64': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 10,
                        'v6_to_v4': 20
                    }
                },
                '64:FF9B::/96': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 0,
                        'v6_to_v4': 0
                    }
                }
            }
        },
        'hits_misses': {
            'hit_pkts': 0, 
            'miss_pkts': 0
        },
        'interface_statistics': {
            'TenGigabitEthernet5/0/12': {
                'stateful_prefix': {
                    '2010:1::/96': {
                        'packets_dropped': 0,
                        'packets_translated': {
                            'v4_to_v6': 20,
                            'v6_to_v4': 1
                        }
                    },
                'ipv4': 'not configured',
                'ipv6': 'not configured'
                }
            }
        },
        'nat64_enabled_interfaces': 1,
        'number_of_packets': {
            'cef_punted_pkts': 0,
            'cef_translated_pkts': 0,
            'dropped_pkts': 3461156,
            'hits_misses': {
                'hit_pkts': 131486,
                'miss_pkts': 3461164
            }
        }
    }
}