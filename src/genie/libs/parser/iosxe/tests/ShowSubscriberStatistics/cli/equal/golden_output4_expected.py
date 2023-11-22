expected_output = {

        'subscriber_statistics':{
            'sessions_currently_up': 6001,
            'sessions_currently_pending': 0,
            'sessions_currently_authenticated': 6000,
            'sessions_currently_unauthenticated': 1,
            'highest_number_of_sessions': 6001,
            'mean_up_time_duration_session': "00:04:00",
            'number_of_sessions_up_so_far': 6001,
            'mean_call_rate_per_minute': 500,
            'mean_call_rate_per_hour': 6000,
            'number_of_calls_in_last_one_hour': 6000,
            'number_of_sessions_failed': 0
        },
        'lite_session_statistics': {
            'lite_sessions_currently_up': 34000,
            'lite_number_of_sessions_up_so_far': 40000,
            'full_session': 6000,
            'conversion_in_progress': 0,
            'failed_to_convert': 0,
            'account_logons_failed': 0,
            'mean_call_rate_per_minute': 3333,
            'mean_call_rate_per_hour': 40000,
            'number_of_sessions_failed': 0,
            'pbhk_zero': 0,
            'not_in_connected_state': 0
        },
        'current_flow_statistics': {
            'number_of_flows_currently_up': 18004,
            'highest_number_of_flows_ever_up': 18007,
            'mean_up_time_duration_flow': "00:02:09",
            'number_of_flows_failed': 0,
            'flows_up_so_far': 36004
        },
        'access_type_based_session_count': {
            'ip_interface': 1
        },

        'ip_dhcp_session_type_count': {
            'dhcpv4': 6000
        },

        'feature_installation_count':{
            1: {
                'feature_name': 'Absolute Timeout',
                'none': 6000,
                'direction_inbound': 0,
                'direction_outbound': 0
            },
            2: {
                'feature_name': 'Idle Timeout',
                'none': 0,
                'direction_inbound': 0,
                'direction_outbound': 6000                
            },
            3: {
                'feature_name': 'Accounting',
                'none': 0,
                'direction_inbound': 6000,
                'direction_outbound': 6000                
            },
            4: {
                'feature_name': 'L4 Redirect',
                'none': 0,
                'direction_inbound': 2,
                'direction_outbound': 1
            },
            5: {
                'feature_name': 'Policing',
                'none': 0,
                'direction_inbound': 6000,
                'direction_outbound': 6000
            },
            6: {
                'feature_name': 'Portbundle Hostkey',
                'none': 0,
                'direction_inbound': 6001,
                'direction_outbound': 0
            },
            7: {
                'feature_name': 'Forced Flow Routing',
                'none': 0,
                'direction_inbound': 6001,
                'direction_outbound': 0
            },

        },
        'switch_id_cleanup_statistics': {
            'invalid_smgr_handle': 0,
            'invalid_policy_handle': 0,
            'invalid_lterm_handle': 0,
            'invalid_sip_handle': 0
        },
        'lterm_session_delete_errors': {
        },
        'shdbs_in_use': 6004,       
        'shdbs_allocated': 301175,   
        'shdbs_freed': 295171,
        'shdb_handle_with_client_counts': {
            'lterm': 6001,       
            'aaa': 6001,       
            'ccm': 6004,      
            'sss fm': 6001,
            'ipsub': 6000,
            'ip_if': 1,
            'coa': 6000,
            'coa cluster': 0,             
            'isg classifier': 6001,       
            'ccm group': 6004,       
            'pm': 6001,       
            'pm cluster': 0,
            'dhcp': 6000,
            'dhcp sip': 6000,
            'eogre': 6000  
        }
}

