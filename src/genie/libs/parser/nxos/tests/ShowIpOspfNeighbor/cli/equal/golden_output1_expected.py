expected_output = {
    'vrf': {
        'blue': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '100': {
                            'total_neighbors': 5,
                            'interfaces': {
                                'Ethernet1/49': {
                                    'neighbors': {
                                        '3.3.3.3': {
                                            'neighbor_router_id': '3.3.3.3',
                                            'priority': 1,
                                            'state': 'FULL/DR',
                                            'up_time': '02:18:00',
                                            'address': '40.1.1.2',
                                        },
                                    },
                                },
                                'Vlan13': {
                                    'neighbors': {
                                        '3.3.3.3': {
                                            'neighbor_router_id': '3.3.3.3',
                                            'priority': 1,
                                            'state': 'FULL/DR',
                                            'up_time': '02:17:39',
                                            'address': '41.1.1.2',
                                        },
                                    },
                                },
                                'Ethernet1/30.7': {
                                    'neighbors': {
                                        '3.3.3.3': {
                                            'neighbor_router_id': '3.3.3.3',
                                            'priority': 1,
                                            'state': 'FULL/DR',
                                            'up_time': '02:17:40',
                                            'address': '42.1.1.2',
                                        },
                                    },
                                },
                                'Port-channel8': {
                                    'neighbors': {
                                        '3.3.3.3': {
                                            'neighbor_router_id': '3.3.3.3',
                                            'priority': 1,
                                            'state': 'FULL/DR',
                                            'up_time': '02:17:26',
                                            'address': '43.1.1.2',
                                        },
                                    },
                                },
                                'Port-channel9.9': {
                                    'neighbors': {
                                        '3.3.3.3': {
                                            'neighbor_router_id': '3.3.3.3',
                                            'priority': 1,
                                            'state': 'FULL/DR',
                                            'up_time': '02:17:27',
                                            'address': '44.1.1.2',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
