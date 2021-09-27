

expected_output = {
    'state': 'activated',
    'package_information': {
        'name': 'guestshell.ova',
        'path': '/isanboot/bin/guestshell.ova',
        'application': {
            'name': 'GuestShell',
            'version': '2.4(0.0)',
            'description': 'Cisco Systems Guest Shell',
        },
        'signing': {
            'key_type': 'Cisco release key',
            'method': 'SHA-1'
        },
        'licensing': {
            'name': 'None',
            'version': 'None',
        },
    },
    'resource_reservation': {
        'disk_mb': 1000,
        'memory_mb': 500,
        'cpu_percent': 1,
    },
    'attached_devices': {
        1: {
            'type': 'Disk',
            'name': '_rootfs',
        },
        2: {
            'type': 'Disk',
            'name': '/cisco/cor',
        },
        3: {
            'type': 'Serial/shell',
        },
        4: {
            'type': 'Serial/aux',
        },
        5: {
            'type': 'Serial/Syslog',
            'alias': 'serial2',
        },
        6: {
            'type': 'Serial/Trace',
            'alias': 'serial3',
        },
    }
}
