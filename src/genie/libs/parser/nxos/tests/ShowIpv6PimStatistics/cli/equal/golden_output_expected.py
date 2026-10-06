expected_output = {
    'vrf': {
        'default': {
            'last_reset': 'never',
            'register_processing': {
                'registers': {
                    'sent': 0,
                    'received': 0,
                },
                'null_registers': {
                    'sent': 0,
                    'received': 0,
                },
                'register_stops': {
                    'sent': 0,
                    'received': 0,
                },
                'registers_received_and_not_rp': 0,
                'registers_received_for_ssm_groups': 0,
                'registers_received_for_bidir_groups': 0,
            },
            'bsr_processing': {
                'bootstraps': {
                    'sent': 0,
                    'received': 0,
                },
                'candidate_rps': {
                    'sent': 0,
                    'received': 0,
                },
                'bootstraps_from_non_neighbors': 0,
                'bootstraps_from_border_interfaces': 0,
                'bootstrap_length_errors': 0,
                'bootstraps_which_rpf_failed': 0,
                'bootstraps_received_but_not_listen_configured': 0,
                'candidate_rps_from_border_interfaces': 0,
                'candidate_rps_received_but_not_listen_configured': 0,
            },
            'general_errors': {
                'control_plane_rpf_failure_due_to_no_route_found': 5,
                'data_plane_rpf_failure_due_to_no_route_found': 0,
                'data_plane_no_multicast_state_found': 0,
                'data_plane_create_route_state_count': 0,
            },
        },
    },
}
