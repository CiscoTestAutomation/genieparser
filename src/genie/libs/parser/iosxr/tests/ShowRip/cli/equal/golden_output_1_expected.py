

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip': {
                            'active': 'Yes',
                            'added_to_socket': 'Yes',
                            'out_of_memory_state': 'Normal',
                            'version': 2,
                            'default_metric': '3',
                            'maximum_paths': 4,
                            'auto_summarize': 'No',
                            'broadcast_for_v2': 'No',
                            'packet_source_validation': 'Yes',
                            'nsf': 'Disabled',
                            'timers': {
                                'until_next_update': 7,
                                'update_interval': 10,
                                'invalid_interval': 31,
                                'holddown_interval': 32,
                                'flush_interval': 33
                            }
                        }
                    }
                }
            }
        }
    }
}
