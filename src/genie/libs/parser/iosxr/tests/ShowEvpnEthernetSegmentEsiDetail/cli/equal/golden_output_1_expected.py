

expected_output = {
    'segment_id': {
        '0047.47ff.0000.0000.2200': {
            'interface': {
                'Bundle-Ether200': {
                    'next_hops': ['10.64.4.47', '10.64.4.48'],
                    'es_to_bgp_gates': 'Ready',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'Bundle-Ether100',
                        'interface_mac': '119b.17ff.3f44',
                        'if_handle': '0x0900001c',
                        'state': 'Up',
                        'redundancy': 'Not Defined',
                    },
                    'esi': {
                        'type': '0',
                        'value': '47.4811.11ff.2222.2211',
                    },
                    'es_import_rt': '4748.11ff.2222 (from ESI)',
                    'source_mac': '1111.11ff.2222 (N/A)',
                    'topology': {
                        'operational': 'MH, All-active',
                        'configured': 'All-active (AApF) (default)',
                    },
                    'service_carving': 'Auto-selection',
                    'peering_details': ['10.64.4.47[MOD:P:00]', '10.64.4.48[MOD:P:00]'],
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
                    'local_shg_label': '75116',
                    'remote_shg_labels': {
                        '1': {
                            'label': {
                                '75116': {
                                    'nexthop': '10.64.4.48',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
