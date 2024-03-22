expected_output = {
    'interface': {
        'TwentyFiveGigE1/0/42': {
            'message_type': {
                'bridged': {
                    'protocols': {
                        'acd_dad': 1,
                        'dhcpv6': {
                            'ren': 11,
                            'req': 1,
                            'sol': 1,
                        },
                        'ndp': {
                            'na': 2,
                            'ns': 5,
                        },
                    },
                },
                'broadcast_multicast_to_unicast': {
                },
                'dropped': {
                    'feature': {
                        'RA guard': {
                            'dropped': 3,
                            'message': 'ra',
                            'protocol': 'ndp',
                            'reason': 'Message unauthorized on port',
                        },
                    },
                },
                'faults': [],
                'limited_broadcast_to_local': {
                },
                'probe': {
                },
                'received': {
                    'protocols': {
                        'acd_dad': 1,
                        'arp': {
                            'rep': 2,
                            'req': 1,
                        },
                        'dhcpv4': {
                            'dis': 1,
                            'req4': 1,
                        },
                        'dhcpv6': {
                            'ren': 11,
                            'req': 1,
                            'sol': 1,
                        },
                        'ndp': {
                            'na': 2,
                            'ns': 5,
                            'ra': 3,
                        },
                    },
                },
                'received_broadcast_multicast': {
                    'protocols': {
                        'arp': {
                            'rep': 2,
                            'req': 1,
                        },
                        'dhcpv4': {
                            'dis': 1,
                            'req4': 1,
                        },
                        'dhcpv6': {
                            'ren': 11,
                            'req': 1,
                            'sol': 1,
                        },
                        'ndp': {
                            'na': 1,
                            'ns': 4,
                            'ra': 3,
                        },
                    },
                },
            },
        },
    },
}