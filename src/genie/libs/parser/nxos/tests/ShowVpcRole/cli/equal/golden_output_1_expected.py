expected_output = {
    'vpc_role_status': {
        'vpc_role': 'primary',
        'dual_active_detection_status': '0',
        'system_mac': '00:11:22:aa:bb:cc',
        'system_priority': '32667',
        'vpc_local': {
            'system_mac': '00:11:22:aa:bb:cc',
            'role_priority': '10',
            'config_role_priority': '10'
        },
        'vpc_peer': {
            'system_mac': '33:44:55:dd:ee:ff',
            'role_priority': '20',
            'config_role_priority': '20'
        }
    }
}