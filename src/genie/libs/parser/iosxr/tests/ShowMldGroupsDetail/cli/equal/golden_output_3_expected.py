
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
                                    'flags': 'Local 29',
                                    'forward': False,
                                    'up_time': '07:17:10'
                                }
                            },
                            'suppress': 0,
                            'up_time': '07:17:10'
                        }
                    },
                    'join_group': {
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
