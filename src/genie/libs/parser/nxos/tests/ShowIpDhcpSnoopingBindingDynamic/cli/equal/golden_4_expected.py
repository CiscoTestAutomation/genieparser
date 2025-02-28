expected_output = {
    'bindings': {
        '00:10:01:01:02:01': {
            'mac_address': '00:10:01:01:02:01',
            'ip_address': '100.10.1.104',
            'lease_sec': 1931,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:01:02:02': {
            'mac_address': '00:10:01:01:02:02',
            'ip_address': '100.10.1.108',
            'lease_sec': 1931,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:01:02:03': {
            'mac_address': '00:10:01:01:02:03',
            'ip_address': '100.10.1.235',
            'lease_sec': 1932,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:01:02:04': {
            'mac_address': '00:10:01:01:02:04',
            'ip_address': '100.10.1.148',
            'lease_sec': 1932,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:03:02:01': {
            'mac_address': '00:10:01:03:02:01',
            'ip_address': '100.10.1.229',
            'lease_sec': 1942,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel11'
        },
        '00:10:01:03:02:02': {
            'mac_address': '00:10:01:03:02:02',
            'ip_address': '100.10.1.244',
            'lease_sec': 1943,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel11'
        },
        '00:10:01:03:02:03': {
            'mac_address': '00:10:01:03:02:03',
            'ip_address': '100.10.1.199',
            'lease_sec': 1942,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel11'
        },
        '00:10:01:03:02:04': {
            'mac_address': '00:10:01:03:02:04',
            'ip_address': '100.10.1.126',
            'lease_sec': 1943,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel11'
        },
        '00:10:01:04:02:01': {
            'mac_address': '00:10:01:04:02:01',
            'ip_address': '100.10.1.109',
            'lease_sec': 1951,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel10'
        },
        '00:10:01:04:02:02': {
            'mac_address': '00:10:01:04:02:02',
            'ip_address': '100.10.1.155',
            'lease_sec': 1952,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel10'
        },
        '00:10:01:04:02:03': {
            'mac_address': '00:10:01:04:02:03',
            'ip_address': '100.10.1.162',
            'lease_sec': 1952,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel10'
        },
        '00:10:01:04:02:04': {
            'mac_address': '00:10:01:04:02:04',
            'ip_address': '100.10.1.197',
            'lease_sec': 1953,
            'type': 'dhcp-snoop',
            'bd': 1001,
            'interface': 'port-channel10'
        },
        '00:10:01:01:02:05': {
            'mac_address': '00:10:01:01:02:05',
            'ip_address': '100.11.1.100',
            'lease_sec': 1932,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:01:02:06': {
            'mac_address': '00:10:01:01:02:06',
            'ip_address': '100.11.1.101',
            'lease_sec': 1932,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:01:02:07': {
            'mac_address': '00:10:01:01:02:07',
            'ip_address': '100.11.1.102',
            'lease_sec': 1932,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:01:02:08': {
            'mac_address': '00:10:01:01:02:08',
            'ip_address': '100.11.1.103',
            'lease_sec': 1932,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'Ethernet1/15/1'
        },
        '00:10:01:03:02:05': {
            'mac_address': '00:10:01:03:02:05',
            'ip_address': '100.11.1.157',
            'lease_sec': 1943,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel11'
        },
        '00:10:01:03:02:06': {
            'mac_address': '00:10:01:03:02:06',
            'ip_address': '100.11.1.250',
            'lease_sec': 1943,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel11'
        },
        '00:10:01:03:02:07': {
            'mac_address': '00:10:01:03:02:07',
            'ip_address': '100.11.1.122',
            'lease_sec': 1943,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel11'
        },
        '00:10:01:03:02:08': {
            'mac_address': '00:10:01:03:02:08',
            'ip_address': '100.11.1.194',
            'lease_sec': 1944,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel11'
        },
        '00:10:01:04:02:05': {
            'mac_address': '00:10:01:04:02:05',
            'ip_address': '100.11.1.106',
            'lease_sec': 1953,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel10'
        },
        '00:10:01:04:02:06': {
            'mac_address': '00:10:01:04:02:06',
            'ip_address': '100.11.1.104',
            'lease_sec': 1953,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel10'
        },
        '00:10:01:04:02:07': {
            'mac_address': '00:10:01:04:02:07',
            'ip_address': '100.11.1.105',
            'lease_sec': 1953,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel10'
        },
        '00:10:01:04:02:08': {
            'mac_address': '00:10:01:04:02:08',
            'ip_address': '100.11.1.107',
            'lease_sec': 1954,
            'type': 'dhcp-snoop',
            'bd': 1002,
            'interface': 'port-channel10'
        }
    }
}