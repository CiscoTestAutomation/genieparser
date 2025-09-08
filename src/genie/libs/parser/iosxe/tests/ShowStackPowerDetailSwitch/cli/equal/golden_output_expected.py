expected_output = {
    'power_stack': {
        'Powerstack-1': {
            'alloc_pwr': 575,
            'num_ps': 1,
            'num_sw': 1,
            'rsvd_pwr': 0,
            'stack_mode': 'Power sharing',
            'stack_topology': 'Standalone',
            'sw_avail_pwr': 525,
            'switches': {
                1: {
                    'high_port_priority_value': 13,
                    'low_port_priority_value': 22,
                    'neighbor': {
                        'port_1': '0000.0000.0000',
                        'port_2': '0000.0000.0000',
                    },
                    'port_status': {
                        'port_1': 'Shut',
                        'port_2': 'Shut',
                    },
                    'power_allocated': 575,
                    'power_budget': 1100,
                    'switch_priority_value': 4,
                },
            },
            'total_powr': 1100,
        },
    },
}