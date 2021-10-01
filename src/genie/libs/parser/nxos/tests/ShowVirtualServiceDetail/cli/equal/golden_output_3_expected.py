

expected_output = {
    'service': {
        'watchdog_lxc': {
            'state': 'activated',
            'package_information': {
                'name': 'ft_mv_no_onep.ova',
                'path': 'bootflash:/ft_mv_no_onep.ova',
                'application': {
                    'name': 'TestingApp',
                    'version': '45.67.A.01',
                    'description': 'Testing Application Suite',
                },
                'signing': {
                    'key_type': 'Cisco development key',
                    'method': 'SHA-1'
                },
                'licensing': {
                    'name': 'None',
                    'version': 'None',
                },
            },
            'resource_reservation': {
                'disk_mb': 87,
                'memory_mb': 256,
                'cpu_percent': 1,
            },
            'attached_devices': {
                1: {
                    'type': 'Disk',
                    'name': '_rootfs',
                },
                2: {
                    'type': 'Disk',
                    'name': '/mnt/data_disk',
                },
                3: {
                    'type': 'Disk',
                    'name': '/var/sysmgr/tmp',
                },
                4: {
                    'type': 'Disk',
                    'name': '/mnt/config_disk',
                },
                5: {
                    'type': 'Serial/shell',
                },
                6: {
                    'type': 'Serial/aux',
                },
                7: {
                    'type': 'Serial/Syslog',
                    'alias': 'serial2',
                },
                8: {
                    'type': 'Serial/Trace',
                    'alias': 'serial3',
                },
                9: {
                    'type': 'Watchdog',
                },
            },
        }
    }
}
