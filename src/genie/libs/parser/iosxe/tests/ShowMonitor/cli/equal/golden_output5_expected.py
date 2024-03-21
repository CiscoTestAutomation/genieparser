expected_output = {
    'session': {
        '10': {
            'destination_ports': 'Gi4/0/2',
            'source_ports': {
                'rx_only': 'Gi3/0/27',
            },
            'type': 'Local Session',
        },
        '20': {
            'destination_ports': 'Gi3/0/28',
            'source_ports': {
                'rx_only': 'Gi3/0/27',
            },
            'type': 'Local Session',
        },
        '30': {
            'destination_ports': 'Gi1/0/1',
            'source_ports': {
                'rx_only': 'Gi3/0/27',
            },
            'type': 'Local Session',
        },
        '40': {
            'dest_rspan_vlan': 300,
            'source_ports': {
                'rx_only': 'Gi3/0/27',
            },
            'type': 'Remote Source Session',
        },
        '52': {
            'destination_erspan_id': '12',
            'destination_ip_address': '1.1.1.20',
            'mtu': 1500,
            'origin_ip_address': '1.1.1.2',
            'source_ports': {
                'rx_only': 'Gi3/0/27',
            },
            'status': 'Admin Enabled',
            'type': 'ERSPAN Source Session',
        },
    },
}