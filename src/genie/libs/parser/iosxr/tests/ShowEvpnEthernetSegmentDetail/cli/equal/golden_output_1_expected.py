

expected_output = {
    'segment_id': {
        '0210.03ff.9e00.0210.0000': {
            'interface': {
                'GigabitEthernet0/3/0/0': {
                    'next_hops': ['10.1.100.100', '10.204.100.100'],
                    'es_to_bgp_gates': 'Ready',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'GigabitEthernet0/3/0/0',
                        'if_handle': '0x1800300',
                        'state': 'Up',
                        'redundancy': 'Not Defined',
                    },
                    'source_mac': '0001.edff.9e9f (PBB BSA)',
                    'topology': {
                        'operational': 'MHN',
                        'configured': 'A/A per service (default)',
                    },
                    'primary_services': 'Auto-selection',
                    'secondary_services': 'Auto-selection',
                    'service_carving_results': {
                        'bridge_ports': {
                            'num_of_total': 3,
                        },
                        'elected': {
                            'num_of_total': 0,
                        },
                        'not_elected': {
                            'num_of_total': 3,
                            'i_sid_ne': ['1450101', '1650205', '1850309'],
                        },
                    },
                    'mac_flushing_mode': 'STP-TCN',
                    'peering_timer': '45 sec [not running]',
                    'recovery_timer': '20 sec [not running]',
                    'flush_again_timer': '60 sec',
                },
            },
        },
        'be01.03ff.be01.ce00.0001': {
            'interface': {
                'Bundle-Ether1': {
                    'next_hops': ['10.1.100.100', '10.204.100.100'],
                    'es_to_bgp_gates': 'Ready',
                    'es_to_l2fib_gates': 'Ready',
                    'main_port': {
                        'interface': 'Bundle-Ether1',
                        'if_handle': '0x000480',
                        'state': 'Up',
                        'redundancy': 'Active',
                    },
                    'source_mac': '0024.beff.cf01 (Local)',
                    'topology': {
                        'operational': 'MHN',
                        'configured': 'A/A per flow (default)',
                    },
                    'primary_services': 'Auto-selection',
                    'secondary_services': 'Auto-selection',
                    'service_carving_results': {
                        'bridge_ports': {
                            'num_of_total': 3,
                        },
                        'elected': {
                            'num_of_total': 3,
                            'i_sid_e': ['1450102', '1650206', '1850310'],
                        },
                        'not_elected': {
                            'num_of_total': 0,
                        },
                    },
                    'mac_flushing_mode': 'STP-TCN',
                    'peering_timer': '45 sec [not running]',
                    'recovery_timer': '20 sec [not running]',
                    'flush_again_timer': '60 sec',
                },
            },
        },
    },
}
