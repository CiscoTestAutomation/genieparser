expected_output = {
    'settings': {
        'server': 'Enabled',
        'server_port': 50052,
        'secure_server': 'Enabled',
        'secure_server_port': 9339,
        'secure_client_authentication': 'Disabled',
        'secure_trustpoint': 'foobar1',
        'secure_client_trustpoint': None,
        'secure_password_authentication': 'Disabled',
    },
    'gnmi': {
        'admin_state': 'Enabled',
        'oper_status': 'Down',
        'state': 'Provisioned',
        'grpc_server': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
        },
        'configuration_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Down',
        },
        'telemetry_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Down',
        }
    },
    'gnoi': {
        'cert_management_service': {
            'admin_state': 'Enabled',
            'oper_status': 'Up',
        }
    }
}
