expected_output = {
    'interfaces': {
        'GigabitEthernet0/5/6': {
            'description': 'wan_pyats', 
            'ipv4': {
                'ip': '192.168.168.1',
                'netmask': '255.255.255.252'
            },
            'load_interval': '30', 
            'negotiation_auto': True, 
            'cdp': 'enable', 
            'mpls_ip': 'enabled', 
            'output_policy': 'PYATS_TEST'
        }
    }
}


         