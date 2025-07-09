expected_output = {
    'acl': {
        'ACL1': {
            'aces': {
                'access-list ACL1 line 1 extended permit tcp object-group Net_Obj_Grp_1 object-group Net_Obj_Grp_2 eq www (hitcnt=0) 0x3c26de2e': {
                    'comments': [],
                    'elements': {
                        'access-list ACL1 line 1 extended permit tcp 10.0.0.0 255.255.255.0 10.0.10.0 255.255.255.0 eq www (hitcnt=0) 0x3325dd4d': {
                            'action': 'permit',
                            'destinations': ['10.0.10.0/24'],
                            'hitcnt': 0,
                            'port_range': (80, 80),
                            'proto': 'tcp',
                            'sources': ['10.0.0.0/24'],
                        },
                        'access-list ACL1 line 1 extended permit tcp 10.0.0.0 255.255.255.0 host 10.0.10.1 eq www (hitcnt=0) 0x72ad2f06': {
                            'action': 'permit',
                            'destinations': ['10.0.10.1/32'],
                            'hitcnt': 0,
                            'port_range': (80, 80),
                            'proto': 'tcp',
                            'sources': ['10.0.0.0/24'],
                        },
                        'access-list ACL1 line 1 extended permit tcp host 10.0.0.1 10.0.10.0 255.255.255.0 eq www (hitcnt=0) 0x5dd24e82': {
                            'action': 'permit',
                            'destinations': ['10.0.10.0/24'],
                            'hitcnt': 0,
                            'port_range': (80, 80),
                            'proto': 'tcp',
                            'sources': ['10.0.0.1/32'],
                        },
                        'access-list ACL1 line 1 extended permit tcp host 10.0.0.1 host 10.0.10.1 eq www (hitcnt=0) 0x918b772a': {
                            'action': 'permit',
                            'destinations': ['10.0.10.1/32'],
                            'hitcnt': 0,
                            'port_range': (80, 80),
                            'proto': 'tcp',
                            'sources': ['10.0.0.1/32'],
                        },
                    },
                },
                'access-list ACL1 line 2 extended permit tcp any object Range_obj_2 eq ssh (hitcnt=0) 0x672ce198': {
                    'comments': [],
                    'elements': {
                        'access-list ACL1 line 2 extended permit tcp any range 10.0.10.10 10.0.10.120 eq ssh (hitcnt=0) 0x672ce198': {
                            'action': 'permit',
                            'destinations': ['10.0.10.10/31', '10.0.10.12/30', '10.0.10.16/28', '10.0.10.32/27', '10.0.10.64/27', '10.0.10.96/28', '10.0.10.112/29', '10.0.10.120/32'],
                            'hitcnt': 0,
                            'port_range': (22, 22),
                            'proto': 'tcp',
                            'sources': ['0.0.0.0/0'],
                        },
                    },
                },
                'access-list ACL1 line 3 extended permit ip object Range_obj object Range_obj_2 (hitcnt=0) 0x8844b8b1': {
                    'comments': [],
                    'elements': {
                        'access-list ACL1 line 3 extended permit ip range 10.0.0.10 10.0.0.120 range 10.0.10.10 10.0.10.120 (hitcnt=0) 0x8844b8b1': {
                            'action': 'permit',
                            'destinations': ['10.0.10.10/31', '10.0.10.12/30', '10.0.10.16/28', '10.0.10.32/27', '10.0.10.64/27', '10.0.10.96/28', '10.0.10.112/29', '10.0.10.120/32'],
                            'hitcnt': 0,
                            'port_range': ('10.0.10.10', '10.0.10.120'),
                            'proto': 'ip',
                            'sources': ['10.0.0.10/31', '10.0.0.12/30', '10.0.0.16/28', '10.0.0.32/27', '10.0.0.64/27', '10.0.0.96/28', '10.0.0.112/29', '10.0.0.120/32'],
                        },
                    },
                },
                'access-list ACL1 line 4 extended permit object-group Svc_Grp_1 host 10.0.0.1 host 10.0.0.2 (hitcnt=0) 0xf3072431': {
                    'comments': [],
                    'elements': {
                        'access-list ACL1 line 4 extended permit icmp host 10.0.0.1 host 10.0.0.2 (hitcnt=0) 0x642d7cc1': {
                            'action': 'permit',
                            'destinations': ['10.0.0.2/32'],
                            'hitcnt': 0,
                            'port_range': (0, 0),
                            'proto': 'icmp',
                            'sources': ['10.0.0.1/32'],
                        },
                        'access-list ACL1 line 4 extended permit tcp host 10.0.0.1 host 10.0.0.2 eq domain (hitcnt=0) 0x0799d244': {
                            'action': 'permit',
                            'destinations': ['10.0.0.2/32'],
                            'hitcnt': 0,
                            'port_range': (53, 53),
                            'proto': 'tcp',
                            'sources': ['10.0.0.1/32'],
                        },
                        'access-list ACL1 line 4 extended permit tcp host 10.0.0.1 host 10.0.0.2 eq ssh (hitcnt=0) 0x4806dae0': {
                            'action': 'permit',
                            'destinations': ['10.0.0.2/32'],
                            'hitcnt': 0,
                            'port_range': (22, 22),
                            'proto': 'tcp',
                            'sources': ['10.0.0.1/32'],
                        },
                        'access-list ACL1 line 4 extended permit udp host 10.0.0.1 host 10.0.0.2 (hitcnt=0) 0x0b55e3d0': {
                            'action': 'permit',
                            'destinations': ['10.0.0.2/32'],
                            'hitcnt': 0,
                            'port_range': (0, 0),
                            'proto': 'udp',
                            'sources': ['10.0.0.1/32'],
                        },
                        'access-list ACL1 line 4 extended permit udp host 10.0.0.1 host 10.0.0.2 eq domain (hitcnt=0) 0xd33de0fe': {
                            'action': 'permit',
                            'destinations': ['10.0.0.2/32'],
                            'hitcnt': 0,
                            'port_range': (53, 53),
                            'proto': 'udp',
                            'sources': ['10.0.0.1/32'],
                        },
                    },
                },
                'access-list ACL1 line 7 extended permit ip host 10.0.0.1 10.0.10.0 255.255.255.0 (hitcnt=0) 0x885d07d4': {
                    'comments': ['access-list ACL1 line 5 remark Test Comments', 'access-list ACL1 line 6 remark Test Comments Line 2'],
                    'elements': {
                        'access-list ACL1 line 7 extended permit ip host 10.0.0.1 10.0.10.0 255.255.255.0 (hitcnt=0) 0x885d07d4': {
                            'action': 'permit',
                            'destinations': ['10.0.10.0/24'],
                            'hitcnt': 0,
                            'port_range': (0, 0),
                            'proto': 'ip',
                            'sources': ['10.0.0.1/32'],
                        },
                    },
                },
            },
        },
    },
}