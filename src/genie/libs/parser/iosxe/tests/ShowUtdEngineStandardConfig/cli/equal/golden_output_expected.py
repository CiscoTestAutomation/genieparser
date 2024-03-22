expected_output = {
    'utd_eng_std_config': {
        'unified_policy': 'Enabled',
        'url_filtering_cloud_lookup': 'Enabled',
        'url_filtering_on_box_lookup': 'Disabled',
        'file_reputation_cloud_lookup': 'Disabled',
        'file_analysis_cloud_submission': 'Disabled',
        'utd_tls_decryption_dataplane_policy': 'Enabled',
        'normalizer': 'Enabled',
        'flow_logging': 'Disabled',
        'utd_policy_table_entries': {
            'polciy': {
                'name': 'AIP1',
                'threat_profile': 'IPPuni1'
            }
        },
        'virtual_port_group_id': 1,
        'utd_threat_inspection_profile_table_entries': {
            'threat_profile': {
                'threat_profile_name': 'IPPuni1',
                'mode': 'Intrusion Detection',
                'policy': 'Balanced',
                'logging_level': 'Error'
            }
        }
    }
}
