

expected_output = {
    'segment_id': {
        '0021.22ff.2020.1010.1010': {
            'interface': {
                'Bundle-Ether10': {
                    'next_hops': ['192.168.99.21', '192.168.99.22'],
                    'es_to_bgp_gates': 'Ready',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'Bundle-Ether10',
                        'interface_mac': '00bc.60ff.7122',
                        'if_handle': '0x08004054',
                        'state': 'Up',
                        'redundancy': 'Not Defined'
                    },
                    'esi': {
                        'type': '0',
                        'value': '21.2210.10ff.2020.1010'
                    },
                    'es_import_rt': '2122.10ff.2020 (from ESI)',
                    'source_mac': '0000.0000.0000 (N/A)',
                    'topology': {
                        'operational': 'MH, All-active',
                        'configured': 'All-active (AApF) (default)'
                    },
                    'service_carving': 'Auto-selection',
                    'multicast': 'Disabled',
                    'convergence': 'NH-Tracking',
                    'tracked_nexthop': '192.168.99.22',
                    'peering_details': ['2', 'Nexthops'],
                    'checkpoint_info': {
                        'nexthop': ['192.168.99.21 [MOD:P:7fff:T]', '192.168.99.22 [MOD:P:00:T]']
                    },
                    'mode': 'NONE',
                    'service_carving_results': {
                        'forwarders': 11,
                        'elected': {
                            'num_of_total': 7
                        },
                        'not_elected': {
                            'num_of_total': 4
                        }
                    },
                    'evpn_vpws_service_carving_results': {
                        'primary': '0',
                        'backup': '0',
                        'non_df': '0'
                    },
                    'mac_flushing_mode': 'STP-TCN',
                    'peering_timer': '10 sec [not running]',
                    'recovery_timer': '30 sec [not running]',
                    'carving_timer': '0 sec [not running]',
                    'local_shg_label': '28105',
                    'remote_shg_labels': {
                        '1': {
                            'label': {
                                '28105': {
                                    'nexthop': '192.168.99.22'
                                }
                            }
                        }
                    }
                }
            }
        },
        '0021.22ff.2222.1111.1111': {
            'interface': {
                'Bundle-Ether11': {
                    'next_hops': ['192.168.99.21', '192.168.99.22'],
                    'es_to_bgp_gates': 'Ready',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'Bundle-Ether11',
                        'interface_mac': '00bc.60ff.7121',
                        'if_handle': '0x080040b4',
                        'state': 'Standby',
                        'redundancy': 'Not Defined'
                    },
                    'esi': {
                        'type': '0',
                        'value': '21.2211.11ff.2222.1111'
                    },
                    'es_import_rt': '2122.11ff.2222 (from ESI)',
                    'source_mac': '0000.0000.0000 (N/A)',
                    'topology': {
                        'operational': 'MH',
                        'configured': 'Port-Active'
                    },
                    'service_carving': 'Auto-selection',
                    'multicast': 'Disabled',
                    'peering_details': ['2', 'Nexthops'],
                    'checkpoint_info': {
                        'nexthop': ['192.168.99.21 [MOD:P:00:T]', '192.168.99.22 [MOD:P:00:T]']
                    },
                    'mode': 'NTP_SCT',
                    'service_carving_results': {
                        'forwarders': 1,
                        'elected': {
                            'num_of_total': 0
                        },
                        'not_elected': {
                            'num_of_total': 1
                        }
                    },
                    'evpn_vpws_service_carving_results': {
                        'primary': '0',
                        'backup': '0',
                        'non_df': '0'
                    },
                    'mac_flushing_mode': 'STP-TCN',
                    'peering_timer': '10 sec [not running]',
                    'recovery_timer': '30 sec [not running]',
                    'carving_timer': '0 sec [not running]',
                    'local_shg_label': '28139',
                    'remote_shg_labels': {
                        '1': {
                            'label': {
                                '28139': {
                                    'nexthop': '192.168.99.22'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
