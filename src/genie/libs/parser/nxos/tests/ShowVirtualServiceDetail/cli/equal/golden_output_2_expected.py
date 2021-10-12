

expected_output = {
    'service': {
        'lxc_8': {
            'state': 'installed',
            'package_information': {
                'name': 'c7ulxc_kstack.ova',
                'path': 'bootflash:/c7ulxc_kstack.ova',
                'application': {
                    'name': 'Centos7Kstack',
                    'version': '1.0; (devtest)',
                    'description': 'centos distro (kstack)',
                },
                'signing': {
                    'key_type': 'Cisco development key',
                    'method': 'SHA-1',
                },
                'licensing': {
                    'name': 'None',
                    'version': 'None',
                },
            },
            'resource_reservation': {
                'disk_mb': 126,
                'memory_mb': 0,
                'cpu_percent': 0,
            },
            'attached_devices': {
                1: {
                    'type': 'Disk',
                    'name': '_rootfs',
                },
                2: {
                    'type': 'Disk',
                    'name': '/var/sysmgr/tmp',
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
            },
        },
    },
}
