expected_output = {
    'http_server': {
        'status': 'Enabled',
        'port': 80,
        'supplementary_listener_ports': 21111,
        'authentication_method': 'enable',
        'auth_retry': 0,
        'time_window': 0,
        'digest_algorithm': 'md5',
        'access_class': '0',
        'ipv4_access_class': 'None',
        'ipv6_access_class': 'None',
        'file_upload_status': 'Disabled',
        'max_connections_allowed': 300,
        'max_secondary_connections': 50,
        'idle_timeout': 180,
        'life_timeout': 180,
        'session_idle_timeout': 600,
        'max_requests_allowed': 25,
        'linger_timeout': 60,
        'active_session_modules': 'ALL',
        'application_session_modules': {
            'http_ifs': {
                'handle': 1,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'HTTP based IOS File Server'
            },
            'sl_http': {
                'handle': 2,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'HTTP REST IOS-XE Smart License Server'
            },
            'openresty_pki': {
                'handle': 3,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'IOS OpenResty PKI Server'
            },
            'home_page': {
                'handle': 4,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'IOS Homepage Server'
            },
            'banner_page': {
                'handle': 5,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'HTTP Banner Page Server'
            },
            'web_exec': {
                'handle': 6,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'HTTP based IOS EXEC Server'
            },
            'nbar2': {
                'handle': 7,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'NBAR2 HTTP(S) Server'
            },
            'gsi7b8d0a8d6518_web': {
                'handle': 8,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'wsma infra'
            },
            'gsi7b8d054ade20_web': {
                'handle': 9,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'wsma infra'
            },
            'ng_webui': {
                'handle': 10,
                'status': 'Active',
                'secure_status': 'Active',
                'description': 'Web GUI'
            }
        },
        'current_connections': {
            '127.0.0.1:21111': {
                'remote_ipaddress_port': '127.0.0.1:58764',
                'in_bytes': 0,
                'out_bytes': 0
            }
        },
        'nginx_internal_counters': {
            'pool': 915,
            'active_connection': 1,
            'pool_available': 898,
            'maximum_connection_hit': 0
        },
        'statistics': {
            'accepted_connections': 1,
            'server_accepts_handled_requests': '2 2 2',
            'reading': 0,
            'writing': 1,
            'waiting': 0
        },
        'history': {
            'index': {
                '0': {
                    'local_ip_address_port': '127.0.0.1:21111',
                    'remote_ip_address_port': '127.0.0.1:58764',
                    'in_bytes': 0,
                    'out_bytes': 404,
                    'end_time': '11:56:11 17/03'
                },
                '1': {
                    'local_ip_address_port': '127.0.0.1:21111',
                    'remote_ip_address_port': '127.0.0.1:58778',
                    'in_bytes': 0,
                    'out_bytes': 277,
                    'end_time': '11:56:13 17/03'
                }
            }
        },
        'conn_history_current_pos': 2
    },
    'http_secure_server': {
        'capability': 'Present',
        'status': 'Enabled',
        'port': 443,
        'ciphersuite': [
            'rsa-aes-cbc-sha2', 
            'rsa-aes-gcm-sha2',
            'dhe-aes-cbc-sha2', 
            'dhe-aes-gcm-sha2', 
            'ecdhe-rsa-aes-cbc-sha2',
            'ecdhe-rsa-aes-gcm-sha2', 
            'ecdhe-ecdsa-aes-gcm-sha2', 
            'tls13-aes128-gcm-sha256',
            'tls13-aes256-gcm-sha384', 
            'tls13-chacha20-poly1305-sha256'
        ],
        'tls_version': ['TLSv1.3', 'TLSv1.2'],
        'client_authentication': 'Disabled',
        'piv_authentication': 'Disabled',
        'piv_authorization': 'Disabled',
        'trustpoint': 'INVALID_TP',
        'ecdhe_curve': 'secp256r1',
        'active_session_modules': 'ALL'
    }
}