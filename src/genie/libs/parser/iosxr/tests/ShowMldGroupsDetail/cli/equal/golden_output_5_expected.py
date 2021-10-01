expected_output = {
    'vrf': {
        'default': {
            'interface': {
                'GigabitEthernet0/0/0/0.115': {
                    'group': {
                        'ff35::232:2:2:2': {
                            'host_mode': 'include',
                            'last_reporter': '::',
                            'router_mode': 'include',
                            'source': {
                                'fc00::10:255:134:44': {
                                    'expire': 'expired',
                                    'flags': 'Local 2b',
                                    'forward': False,
                                    'up_time': '1w1d'
                                }
                            },
                            'suppress': 0,
                            'up_time': '1w1d'
                        }
                    },
                    'join_group': {
                        'ff35::232:2:2:2 fc00::10:255:134:44': {
                            'group': 'ff35::232:2:2:2',
                            'source': 'fc00::10:255:134:44'
                        }
                    },
                    'static_group': {
                        'ff35::232:2:2:2 fc00::10:255:134:44': {
                            'group': 'ff35::232:2:2:2',
                            'source': 'fc00::10:255:134:44'
                        }
                    }
                }
            }
        }
    }
}
