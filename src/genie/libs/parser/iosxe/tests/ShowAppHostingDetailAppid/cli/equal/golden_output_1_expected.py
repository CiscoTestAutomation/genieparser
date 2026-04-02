expected_output = {
    'activated_profile_name': 'custom',
    'app_id': 'guestshell',
    'application': {
        'guestshell': {
            'author': 'Cisco Systems',
            'description': 'Cisco Systems Guest Shell XE for armv7l',
            'path': '/guestshell/:guestshell.tar',
            'type': 'lxc',
            'version': '3.2.0',
        },
    },
    'attached_devices': {
        'iox_console_aux': {
            'alias': 'serial1',
            'type': 'serial/aux',
        },
        'iox_console_shell': {
            'alias': 'serial0',
            'type': 'serial/shell',
        },
        'iox_syslog': {
            'alias': 'serial2',
            'type': 'serial/syslog',
        },
        'iox_trace': {
            'alias': 'serial3',
            'type': 'serial/trace',
        },
    },
    'network_interfaces': {
        'Eth0': {
            'mac_address': '52:54:dd:8e:f7:aa',
            'network_name': 'mgmt-bridge200',
        },
    },
    'owner': 'iox',
    'resource_reservation': {
        'cpu': 800,
        'disk': '1 MB',
        'memory': '256 MB',
        'vcpu': 1,
    },
    'state': 'RUNNING',
}
 
