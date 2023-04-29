expected_output = {
    'global_mld_snooping_configuration': {
        'mld_snooping': 'Disabled', 
        'global_pim_snooping': 'Disabled', 
        'mldv2_snooping': 'Disabled', 
        'listener_message_suppression': 
        'Disabled', 
        'tcn_solicit_query': 'Disabled', 
        'tcn_flood_query_count': '2', 
        'robustness_variable': '2', 
        'last_listener_query_count': '2', 
        'last_listener_query_interval': '1000'
    }, 
    'vlans': {
        'vlan_1': {
            'mld_snooping': 'Disabled', 
            'pim_snooping': 'Disabled', 
            'mld_immediate_leave': 'Disabled', 
            'robustness_variable': '2', 
            'last_listener_query_count': '2', 
            'last_listener_query_interval': '1000'
        }
    }
}