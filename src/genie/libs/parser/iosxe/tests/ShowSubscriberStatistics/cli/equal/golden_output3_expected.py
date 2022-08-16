expected_output = {

        'subscriber_statistics':{
            'sessions_currently_up': 4852,
            'sessions_currently_pending': 2,
            'sessions_currently_authenticated': 4880,
            'sessions_currently_unauthenticated': 61,
            'highest_number_of_sessions': 5960,
            'mean_up_time_duration_session': "00:32:21",
            'number_of_sessions_up_so_far': 17089112,
            'mean_call_rate_per_minute': 165,
            'mean_call_rate_per_hour': 9947,
            'number_of_calls_in_last_one_hour': 11806,
            'number_of_sessions_failed': 15448402
        },
        'lite_session_statistics': {
        },
        'current_flow_statistics': {
            'number_of_flows_currently_up': 0,
            'highest_number_of_flows_ever_up': 0,
            'mean_up_time_duration_flow': "00:00:00",
            'number_of_flows_failed': 0,
            'flows_up_so_far': 0
        },
        'access_type_based_session_count': {
            'ppp': 451,
            'pppoe': 3682,
            'vpdn': 1172
        },

        'ip_dhcp_session_type_count': {
        },

        'feature_installation_count':{
            1: {
                'feature_name': 'QoS Policy Map',
                'none': 0,
                'direction_inbound': 0,
                'direction_outbound': 2502
            },
            2: {
                'feature_name': 'IP Config',
                'none': 4377,
                'direction_inbound': 0,
                'direction_outbound': 0              
            },
            3: {
                'feature_name': 'Interface Config',
                'none': 4377,
                'direction_inbound': 0,
                'direction_outbound': 0                
            },
            4: {
                'feature_name': 'Static Routes',
                'none': 4377,
                'direction_inbound': 0,
                'direction_outbound': 0
            },
        },
        'switch_id_cleanup_statistics': {
            'invalid_smgr_handle': 0,
            'invalid_policy_handle': 0,
            'invalid_lterm_handle': 15474655,
            'invalid_sip_handle': 0
        },
        'lterm_session_delete_errors': {
            'l2hw_switch': 1575
        },
        'shdbs_in_use': 4864,       
        'shdbs_allocated': 17268338,   
        'shdbs_freed': 17263474,
        'shdb_handle_with_client_counts': {
            'ppp': 4854,
            'vpdn fsp': 59,
            'pppoe': 3682,
            'lterm': 4793,       
            'aaa': 4864,       
            'ccm': 4864,
            'l2tp cc': 10,      
            'sss fm': 2502,
            'coa': 0,
            'coa cluster': 0,
            'vpdn sip': 1172,             
            'isg classifier': 3985,       
            'ccm group': 4864,       
            'pm': 0,       
            'pm cluster': 0
        }
}

