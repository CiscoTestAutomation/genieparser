

expected_output = {
    'segment_id': {
        '0001.00ff.aaab.00ff.0003': {
            'interface': {
                'Bundle-Ether3': {
                    'next_hops': ['10.154.219.84'],
                    'es_to_bgp_gates': 'M',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'Bundle-Ether3',
                        'interface_mac': '00c1.64ff.a415',
                        'if_handle': '0x080002a0',
                        'state': 'Down',
                        'redundancy': 'Not Defined',
                    },
                    'esi': {
                        'type': '0',
                        'value': '01.0000.aaff.abab.0003',
                    },
                    'es_import_rt': 'aaab.00ff.0003 (Local)',
                    'source_mac': '0000.0000.0000 (N/A)',
                    'topology': {
                        'operational': 'SH',
                        'configured': 'All-active (AApF) (default)',
                    },
                    'service_carving': 'Auto-selection',
                    'peering_details': ['10.154.219.84[MOD:P:00]'],
                    'service_carving_results': {
                        'forwarders': 1,
                        'permanent': 0,
                        'elected': {
                            'num_of_total': 0,
                        },
                        'not_elected': {
                            'num_of_total': 1,
                        },
                    },
                    'mac_flushing_mode': 'STP-TCN',
                    'peering_timer': '3 sec [not running]',
                    'recovery_timer': '30 sec [not running]',
                    'carving_timer': '0 sec [not running]',
                    'local_shg_label': '100564',
                    'remote_shg_labels': {
                        '0': {
                        },
                    },
                },
            },
        },
        '0001.00ff.aaab.00ff.0004': {
            'interface': {
                'Bundle-Ether4': {
                    'next_hops': ['10.154.219.84'],
                    'es_to_bgp_gates': 'Ready',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'Bundle-Ether4',
                        'interface_mac': '00c1.64ff.a414',
                        'if_handle': '0x080002e0',
                        'state': 'Up',
                        'redundancy': 'Not Defined',
                    },
                    'esi': {
                        'type': '0',
                        'value': '01.0000.aaff.abab.0004',
                    },
                    'es_import_rt': 'aaab.00ff.0004 (Local)',
                    'source_mac': '0000.0000.0000 (N/A)',
                    'topology': {
                        'operational': 'SH',
                        'configured': 'All-active (AApF) (default)',
                    },
                    'service_carving': 'Auto-selection',
                    'peering_details': ['10.154.219.84[MOD:P:00]'],
                    'service_carving_results': {
                        'forwarders': 1,
                        'permanent': 0,
                        'elected': {
                            'num_of_total': 1,
                        },
                        'not_elected': {
                            'num_of_total': 0,
                        },
                    },
                    'mac_flushing_mode': 'STP-TCN',
                    'peering_timer': '3 sec [not running]',
                    'recovery_timer': '30 sec [not running]',
                    'carving_timer': '0 sec [not running]',
                    'local_shg_label': '100565',
                    'remote_shg_labels': {
                        '0': {
                        },
                    },
                },
            },
        },
        'N/A': {
            'interface': {
                'GigabitEthernet0/0/0/12': {
                    'next_hops': ['10.154.219.84'],
                    'es_to_bgp_gates': 'Ready',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'GigabitEthernet0/0/0/12',
                        'interface_mac': '00c1.64ff.7f67',
                        'if_handle': '0x000005c0',
                        'state': 'Up',
                        'redundancy': 'Not Defined',
                    },
                    'esi': {
                        'type': 'Invalid',
                    },
                    'es_import_rt': '0000.0000.0000 (Incomplete Configuration)',
                    'source_mac': '00c1.64ff.a411 (PBB BSA, no ESI)',
                    'topology': {
                        'operational': 'SH',
                        'configured': 'Single-active (AApS) (default)',
                    },
                    'service_carving': 'Auto-selection',
                    'peering_details': ['10.154.219.84[MOD:P:00]'],
                    'service_carving_results': {
                        'forwarders': 1,
                        'permanent': 1,
                        'elected': {
                            'num_of_total': 0,
                        },
                        'not_elected': {
                            'num_of_total': 0,
                        },
                    },
                    'mac_flushing_mode': 'STP-TCN',
                    'peering_timer': '3 sec [not running]',
                    'recovery_timer': '30 sec [not running]',
                    'carving_timer': '0 sec [not running]',
                    'local_shg_label': 'None',
                    'remote_shg_labels': {
                        '0': {
                        },
                    },
                },
            },
        },
    },
}
