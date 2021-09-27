expected_output = {
    'vrf': {
        'default': {
            'interface': {
                'GigabitEthernet0/0/0/0.115': {
                    'group': {
                        'ff35::232:2:2:22': {
                            'host_mode': 'include',
                            'last_reporter': '::',
                            'router_mode': 'include',
                            'source': {
                                'fc00::10:255:134:44': {
                                    'expire': 'expired',
                                    'flags': 'Local a',
                                    'forward': False,
                                    'up_time': '00:01:21'
                                }
                            },
                            'suppress': 0,
                            'up_time': '00:01:21'
                        }
                    },
                    'static_group': {
                        'ff35::232:2:2:22 fc00::10:255:134:44': {
                            'group': 'ff35::232:2:2:22',
                            'source': 'fc00::10:255:134:44'
                        }
                    }
                }
            }
        }
    }
}
