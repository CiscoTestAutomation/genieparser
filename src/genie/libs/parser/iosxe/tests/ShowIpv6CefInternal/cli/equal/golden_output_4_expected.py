expected_output = {
    'vrf': {
        'red': {
            'address_family': {
                'ipv6': {
                    'prefix': {
                        '2001:192:168:1::2/128': {
                            'output_chain': {},
                            'feature_space': {
                                'iprm':'0x00058000'
                            },
                            'epoch': 0,
                            'flags': [
                                'att',
                                'sc'
                            ],
                            'sharing': 'per-destination',
                            'rib': '[D]',
                            'refcnt': 4,
                            'sources': [
                                'RIB,',
                                'Adj,',
                                'IPL'
                            ],
                            'subblocks': {
                                'LISP': {
                                    'smr_enabled': False
                                }
                             },
                            'path_list': {
                                '7F80D5A40B80': {
                                    'locks': 3,
                                    'sharing': 'per-destination',
                                    'flags': '0x49 [shble, rif, hwcn]',
                                    'path': {
                                        '7F80D59EFE88': {
                                            'share': '1/1',
                                            'type': 'attached nexthop',
                                            'for': 'IPv6',
                                            'nexthop': {
                                                '2001:192:168:1::2': {
                                                    'outgoing_interface': {
                                                        'Vlan101': {}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}