expected_output = {
    'dhcppool-vlan10': {
        'dhcp_excludes': {
            1: {
                'end': '10.23.25.100',
                'start': '10.23.25.1',
            },
            2: {
                'end': '10.23.25.253',
                'start': '10.23.25.240',
            },
        },
        'dhcp_options': {
            1: {
                'data': '10.23.4.15',
                'option': '150',
            },
        },
        'dns_servers': ['10.23.4.1', '10.23.4.13'],
        'domain': 'haarlem.local',
        'gateway': '10.23.25.254',
        'lease_time': 'day 12 hour 0 minute 0',
        'netbios_servers': ['1.1.1.3'],
        'networks': {
            1: {
                'ip': '10.23.25.0',
                'subnet_mask': '255.255.255.0',
            },
        },
    },
    'dhcppool-vlan101': {
        'dhcp_excludes': {
        },
        'dhcp_options': {
        },
        'domain': 'haarlem.locall',
        'networks': {
        },
    },
}
