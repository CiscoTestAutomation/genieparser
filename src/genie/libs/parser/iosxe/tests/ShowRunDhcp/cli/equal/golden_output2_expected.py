expected_output = {
    'TEST-1': {'networks': {
        1: {'ip': '1.1.1.0', 'subnet_mask': '255.255.255.0', 'secondary': False}},
        'dhcp_options': {1: {'option': '150', 'type': 'ip',
                             'data': '4.4.4.4 5.5.5.5'}},
        'dhcp_excludes': {
            1: {'start': '1.1.1.2', 'end': '1.1.1.2'},
            2: {'start': '1.1.1.3', 'end': '1.1.1.10'}},
        'vrf': 'ABC', 'gateway': '1.1.1.1',
        'dns_servers': ['8.8.8.8', '9.9.9.9'],
        'netbios_servers': ['2.2.2.2', '3.3.3.3'],
        'lease_time': '1', 'domain': 'TEST.com'}, 'TEST-12': {
        'networks': {
            1: {'ip': '12.1.1.0', 'subnet_mask': '255.255.255.0', 'secondary': False}},
        'dhcp_options': {1: {'option': '150', 'type': 'ip', 'data': '4.4.4.4 5.5.5.5'}},
        'dhcp_excludes': {1: {'start': '12.1.1.200', 'end': '12.1.1.201'}},
        'gateway': '1.1.1.1', 'dns_servers': ['8.8.8.8', '9.9.9.9'],
        'netbios_servers': ['2.2.2.2', '3.3.3.3'], 'lease_time': '1',
        'domain': 'TEST.com'}}