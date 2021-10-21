
expected_output = {
    'vrf': {
        'default': {
            'interface': {
                'GigabitEthernet0/0/0/0': {
                    'group': {
                        'ff02::16': {
                            'expire': 'never',
                            'router_mode': 'exclude',
                            'host_mode': 'exclude',
                            'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                            'up_time': '1d06h'
                        },
                        'ff02::1:ff28:cd4b': {
                            'expire': '01:00:01',
                            'router_mode': 'exclude',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                            'up_time': '1d06h'
                        },
                        'ff02::1:ff60:50aa': {
                            'expire': '01:00:01',
                            'router_mode': 'exclude',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                            'up_time': '1d06h'
                        },
                        'ff02::1:ffae:4aba': {
                            'expire': '01:00:01',
                            'router_mode': 'exclude',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                            'up_time': '1d06h'
                        },
                        'ff02::1:ffd7:c01f': {
                            'expire': '00:29:15',
                            'router_mode': 'exclude',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::5054:ff:fed7:c01f',
                            'up_time': '00:33:19'
                        },
                        'ff02::1:ffda:f428': {
                            'expire': '01:00:01',
                            'router_mode': 'exclude',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::eca7:a4ff:fe28:cd4b',
                            'up_time': '06:27:46'
                        },
                        'ff02::2': {
                            'expire': 'never',
                            'router_mode': 'exclude',
                            'host_mode': 'exclude',
                            'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                            'up_time': '1d06h'
                        },
                        'ff02::d': {
                            'expire': 'never',
                            'router_mode': 'exclude',
                            'host_mode': 'exclude',
                            'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                            'up_time': '1d06h'
                        },
                        'ff15:1::1': {
                            'router_mode': 'include',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                            'source': {
                                '2001:db8:2:2::2': {
                                    'expire': '01:00:00',
                                    'flags': 'Remote Local 2d',
                                    'forward': True,
                                    'up_time': '08:06:00'
                                }
                            },
                            'up_time': '08:06:00'
                        },
                        'ff25:2::1': {
                            'expire': 'never',
                            'router_mode': 'exclude',
                            'host_mode': 'exclude',
                            'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                            'up_time': '08:06:00'
                        },
                        'ff35:1::1': {
                            'router_mode': 'include',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                            'source': {
                                '2001:db8:3:3::3': {
                                    'expire': '01:00:00',
                                    'flags': 'Remote Local e',
                                    'forward': True,
                                    'up_time': '00:33:28'
                                }
                            },
                            'up_time': '00:33:28'
                        },
                        'ff45:1::1': {
                            'expire': 'never',
                            'router_mode': 'exclude',
                            'host_mode': 'exclude',
                            'last_reporter': 'fe80::5054:ff:fefa:9ad7',
                            'up_time': '00:33:28'
                        },
                        'fffe::1': {
                            'expire': '00:59:49',
                            'router_mode': 'exclude',
                            'host_mode': 'include',
                            'last_reporter': 'fe80::5054:ff:fed7:c01f',
                            'up_time': '07:59:31'
                        }
                    },
                    'join_group': {
                        'ff15:1::1 2001:db8:2:2::2': {
                            'group': 'ff15:1::1',
                            'source': '2001:db8:2:2::2'
                        }
                    },
                    'static_group': {
                        'ff35:1::1 2001:db8:3:3::3': {
                            'group': 'ff35:1::1',
                            'source': '2001:db8:3:3::3'
                        }
                    }
                }
            }
        }
    }
}
