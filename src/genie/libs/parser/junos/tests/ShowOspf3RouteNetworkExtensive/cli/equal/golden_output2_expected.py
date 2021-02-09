expected_output = {
    'ospf3-route-information': {
        'ospf-topology-route-table': {
            'ospf3-route': [{
                'ospf3-route-entry': {
                    'address-prefix': '2001::1/128',
                    'route-path-type': 'Intra',
                    'route-type': 'Network',
                    'next-hop-type': 'IP',
                    'interface-cost': '0',
                    'ospf-next-hop': {
                        'next-hop-name': {
                            'interface-name': 'lo0.0'
                        }
                    },
                    'ospf-area': '0.0.0.0',
                    'route-origin': '10.4.1.1',
                    'route-priority': 'low'
                }
            }, {
                'ospf3-route-entry': {
                    'address-prefix': '2001::4/128',
                    'route-path-type': 'Intra',
                    'route-type': 'Network',
                    'next-hop-type': 'IP',
                    'interface-cost': '1',
                    'ospf-next-hop': {
                        'next-hop-name': {
                            'interface-name': 'ge-0/0/0.0'
                        },
                        'next-hop-address': {
                            'interface-address': 'fe80::250:56ff:fe8d:e8e8'
                        }
                    },
                    'ospf-area': '0.0.0.0',
                    'route-origin': '10.64.4.4',
                    'route-priority': 'medium'
                }
            }, {
                'ospf3-route-entry': {
                    'address-prefix': '2001:30::/64',
                    'route-path-type': 'Intra',
                    'route-type': 'Network',
                    'next-hop-type': 'IP',
                    'interface-cost': '1',
                    'ospf-next-hop': {
                        'next-hop-name': {
                            'interface-name': 'ge-0/0/1.0'
                        }
                    },
                    'ospf-area': '0.0.0.0',
                    'route-origin': '10.4.1.1',
                    'route-priority': 'low'
                }
            }, {
                'ospf3-route-entry': {
                    'address-prefix': '2001:40::/64',
                    'route-path-type': 'Intra',
                    'route-type': 'Network',
                    'next-hop-type': 'IP',
                    'interface-cost': '1',
                    'ospf-next-hop': {
                        'next-hop-name': {
                            'interface-name': 'ge-0/0/0.0'
                        }
                    },
                    'ospf-area': '0.0.0.0',
                    'route-origin': '10.64.4.4',
                    'route-priority': 'low'
                }
            }, {
                'ospf3-route-entry': {
                    'address-prefix': '2001:50::/64',
                    'route-path-type': 'Intra',
                    'route-type': 'Network',
                    'next-hop-type': 'IP',
                    'interface-cost': '2',
                    'ospf-next-hop': {
                        'next-hop-name': {
                            'interface-name': 'ge-0/0/0.0'
                        },
                        'next-hop-address': {
                            'interface-address': 'fe80::250:56ff:fe8d:e8e8'
                        }
                    },
                    'ospf-area': '0.0.0.0',
                    'route-origin': '10.64.4.4',
                    'route-priority': 'medium'
                }
            }]
        }
    }
}
