expected_output= {
    'vrf': {
        'blue': {
            'protocols': ['ipv4', 'ipv6'],
            'route_distinguisher': '1.1.1.1:1',
            'route_distinguisher_auto': True,
        },
        'green': {
            'interfaces': ['Loopback11', 'Vlan113', 'Vlan114', 'Vlan123', 'Vlan124', 'Vlan212', 'Vlan222'],
            'protocols': ['ipv4', 'ipv6'],
            'route_distinguisher': '200:101',
        },
        'red': {
            'interfaces': ['Loopback10', 'Vlan111', 'Vlan112', 'Vlan121', 'Vlan122', 'Vlan211', 'Vlan221'],
            'protocols': ['ipv4', 'ipv6'],
            'route_distinguisher': '100:101',
        },
    },
}