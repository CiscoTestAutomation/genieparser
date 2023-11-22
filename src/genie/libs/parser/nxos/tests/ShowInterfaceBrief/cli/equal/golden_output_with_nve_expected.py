expected_output = {
    'interface': {
        'ethernet': {
            'Ethernet1/1': {
                'mode': 'routed',
                'port_ch': '--',
                'reason': 'none',
                'speed': '1000(D)',
                'status': 'up',
                'type': 'eth',
                'vlan': '--'
            },
            'Ethernet1/3': {
                'mode': 'access',
                'port_ch': '--',
                'reason': 'Administratively '
                          'down',
                'speed': 'auto(D)',
                'status': 'down',
                'type': 'eth',
                'vlan': '1'
            },
            'Ethernet1/6': {
                'mode': 'access',
                'port_ch': '--',
                'reason': 'Link not '
                          'connected',
                'speed': 'auto(D)',
                'status': 'down',
                'type': 'eth',
                'vlan': '1'
            }
        },
        'loopback': {
            'Loopback0': {
                'description': '--',
                'status': 'up'
            }
        },
        'port': {
            'mgmt0': {
                'ip_address': '172.25.143.76',
                'mtu': 1500,
                'speed': '1000',
                'status': 'up',
                'vrf': '--'
            }
        },
        'nve': {
            'nve1': {
                'mtu': '9216',
                'reason': 'none',
                'status': 'up'
            }
        },
        'port_channel': {
            'Port-channel8': {
                'mode': 'access',
                'protocol': 'none',
                'reason': 'No operational '
                          'members',
                'speed': 'auto(I)',
                'status': 'down',
                'type': 'eth',
                'vlan': '1'
            }
        },
        'vlan': {
            'Vlan2': {
                'reason': 'VLAN/BD is down',
                'status': 'down',
                'type': '--'
            }
        }
    }
}
