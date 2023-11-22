expected_output = {
    'settings': {
        'server': 'Enabled',
        'server_port': 50052,
        'secure_server': 'Disabled',
        'secure_server_port': 9339,
        'secure_client_authentication': 'Disabled',
        'secure_trustpoint': None,
        'secure_client_trustpoint': None,
        'secure_password_authentication': 'Disabled',
    },
    'gnmi': {
        'admin_state': 'Enabled',
        'oper_status': 'Up',
        'state': 'Provisioned',
        'grpc_server': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
        },
        'configuration_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
        },
        'telemetry_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
        }
    },
    'gnoi': {
        'cert_management_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
        },
        'os_image_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
            'supported': 'Supported',
        },
        'factory_reset_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
            'supported': 'Supported',
        }
    }
}
