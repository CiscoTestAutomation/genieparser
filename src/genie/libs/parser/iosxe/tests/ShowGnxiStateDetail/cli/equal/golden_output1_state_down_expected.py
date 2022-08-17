expected_output = {
    'settings': {
        'server': 'Disabled',
        'server_port': 50052,
        'secure_server': 'Disabled',
        'secure_server_port': 9339,
        'secure_client_authentication': 'Disabled',
        'secure_trustpoint': None,
        'secure_client_trustpoint': None,
        'secure_password_authentication': 'Disabled',
    },
    'gnmi': {
        'admin_state': 'Disabled',
        'oper_status': 'Down',
        'state': 'Provisioned',
        'grpc_server': {
            'admin_state': 'Disabled',
            'oper_status': 'Down',
        },
        'configuration_service': {
            'admin_state': 'Disabled',
            'oper_status': 'Down',
        },
        'telemetry_service': {
            'admin_state': 'Disabled',
            'oper_status': 'Down',
        },
    },
    'gnoi': {
        'cert_management_service': {
            'admin_state': 'Disabled',
            'oper_status': 'Down',
        },
        'factory_reset_service': {
            'admin_state': 'Disabled',
            'oper_status': 'Down',
            'supported': 'Not supported on this platform',
        },
        'os_image_service': {
            'admin_state': 'Disabled',
            'oper_status': 'Down',
            'supported': 'Not supported on this platform',
        }
    }
}
