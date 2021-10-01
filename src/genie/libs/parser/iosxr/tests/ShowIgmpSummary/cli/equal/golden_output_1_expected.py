

expected_output = {
    'vrf': {
        'default': {
            'disabled_interfaces': 6,
            'enabled_interfaces': 3,
            'no_of_group_x_interface': 16,
            'interfaces': {
                'Loopback0': {
                    'max_groups': 25000,
                    'number_groups': 6 
                },
                'GigabitEthernet0/0/0/0.90': {
                    'max_groups': 25000,
                    'number_groups': 1
                },
                'GigabitEthernet0/0/0/1.90': {
                    'max_groups': 25000,
                    'number_groups': 1
                },
                'GigabitEthernet0/0/0/0.110': {
                    'max_groups': 25000,
                    'number_groups': 6
                },
                'GigabitEthernet0/0/0/0.115': {
                    'max_groups': 25000,
                    'number_groups': 4
                },
                'GigabitEthernet0/0/0/0.120': {
                    'max_groups': 25000,
                    'number_groups': 1
                },
                'GigabitEthernet0/0/0/1.110': {
                    'max_groups': 25000,
                    'number_groups': 5
                },
                'GigabitEthernet0/0/0/1.115': {
                    'max_groups': 25000,
                    'number_groups': 0
                },
                'GigabitEthernet0/0/0/1.120': {
                    'max_groups': 25000,
                    'number_groups': 1
                }
            },
            'mte_tuple_count': 0,
            'maximum_number_of_groups_for_vrf': 50000,
            'robustness_value': 2,
            'supported_interfaces': 9,
            'unsupported_interfaces': 0,
            }
        }
    }
