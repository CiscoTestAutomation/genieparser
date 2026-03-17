expected_output = {
    'TEST-1': {
        'boot_file': 'dapcfg.txt',
        'dhcp_excludes': {
            1: {
                'end': '1.1.1.2',
                'start': '1.1.1.2',
            },
            2: {
                'end': '1.1.1.10',
                'start': '1.1.1.3',
            },
        },
        'dhcp_options': {
            1: {
                'data': '4.4.4.4 5.5.5.5',
                'option': '150',
                'type': 'ip',
            },
        },
        'dns_servers': ['8.8.8.8', '9.9.9.9'],
        'domain': 'TEST.com',
        'gateway': '1.1.1.1',
        'lease_time': '1',
        'netbios_servers': ['2.2.2.2', '3.3.3.3'],
        'networks': {
            1: {
                'ip': '1.1.1.0',
                'secondary': False,
                'subnet_mask': '255.255.255.0',
            },
        },
        'vrf': 'ABC',
    },
    'TEST-12': {
        'dhcp_excludes': {
            1: {
                'end': '12.1.1.201',
                'start': '12.1.1.200',
            },
        },
        'dhcp_options': {
            1: {
                'data': '4.4.4.4 5.5.5.5',
                'option': '150',
                'type': 'ip',
            },
        },
        'dns_servers': ['8.8.8.8', '9.9.9.9'],
        'domain': 'TEST.com',
        'gateway': '1.1.1.1',
        'lease_time': '1',
        'netbios_servers': ['2.2.2.2', '3.3.3.3'],
        'networks': {
            1: {
                'ip': '12.1.1.0',
                'secondary': False,
                'subnet_mask': '255.255.255.0',
            },
        },
    },
}
