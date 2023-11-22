expected_output = {
    'app_id': 'thousandeyes_enterprise_agent',
    'owner': 'iox',
    'state': 'RUNNING',
    'application': {
        'thousandeyes_enterprise_agent': {
            'type': 'docker',
            'version': '4.3.0',
            'author': 'ThousandEyes <support@thousandeyes.com>',
            'path': 'flash:thousandeyes-enterprise-agent-4.3.0.cisco.tar'
        }
    },
    'activated_profile_name': 'custom',
    'resource_reservation': {
        'memory': '500 MB',
        'disk': '1 MB',
        'cpu': 1850,
        'vcpu': 1
    },
    'attached_devices': {
        'iox_console_shell': {
            'type': 'serial/shell',
            'alias': 'serial0'
        },
        'iox_console_aux': {
            'type': 'serial/aux',
            'alias': 'serial1'
        },
        'iox_syslog': {
            'type': 'serial/syslog',
            'alias': 'serial2'
        },
        'iox_trace': {
            'type': 'serial/trace',
            'alias': 'serial3'
        }
    },
    'network_interfaces': {
        'Eth0': {
            'mac_address': '52:54:dd:d:38:3d',
            'network_name': 'mgmt-bridge-v21'
        }
    },
    'application_health': {
        'status': '0'
    }
}