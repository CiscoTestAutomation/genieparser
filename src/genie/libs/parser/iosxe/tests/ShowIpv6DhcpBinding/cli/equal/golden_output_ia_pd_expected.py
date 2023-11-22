expected_output = {
    'client': {
        'FE80::A8BB:1FF:FE03:11': {
            'duid': '00030001AABB01030011',
            'username': 'unassigned',
            'vrf': 'default',
            'ia_na': {
                '0x00150001': {
                    'ia_id': '0x00150001',
                    't1': 43200,
                    't2': 69120,
                    'address': {
                        '2001:103::FDAF:5C5C:AB4D:180': {
                            'preferred_lifetime': 86400,
                            'valid_lifetime': 172800,
                            'expires': {
                                'month': 'Apr',
                                'day': 6,
                                'year': 2022,
                                'time': '01:59 AM',
                                'remaining_seconds': 172672
                            }
                        }
                    }
                }
            }
        },
        'FE80::A8BB:CCFF:FE80:88FF': {
            'duid': '00030001AABBCC008800',
            'username': 'unassigned',
            'vrf': 'default',
            'interface': 'Ethernet0/0',
            'ia_pd': {
                '0x00100001': {
                    'ia_id': '0x00100001',
                    't1': 302400,
                    't2': 483840,
                    'prefix': {
                        '2001:4::/48': {
                            'preferred_lifetime': 604800,
                            'valid_lifetime': 2592000,
                            'expires': {
                                'month': 'May',
                                'day': 4,
                                'year': 2022,
                                'time': '02:00 AM',
                                'remaining_seconds': 2591938
                            }
                        }
                    }
                }
            }
        }
    }
}
