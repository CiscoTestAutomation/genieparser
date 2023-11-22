expected_output = {
    'vrf': {
        '4': {
            'prefixes': {
                '10.0.0.0/8': {
                    'prefix': '10.0.0.0/8', 
                    'from_peer': {
                        '1.1.1.3': {
                            'peer': '1.1.1.3',
                            'path_list': {
                                1: {
                                    'index': 1, 
                                    'path_id': '936', 
                                    'label': '1002', 
                                    'status': ['C', 'I', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.1.1.1', 
                                    'color': 'green', 
                                    'encap': 'ipsec', 
                                    'preference': '200'
                                }, 
                                2: {
                                    'index': 2, 
                                    'path_id': '937', 
                                    'label': '1002', 
                                    'status': ['C', 'I', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.1.1.1', 
                                    'color': 'blue', 
                                    'encap': 'ipsec', 
                                    'preference': '200'
                                }, 
                                3: {
                                    'index': 3, 
                                    'path_id': '938', 
                                    'label': '1002', 
                                    'status': ['C', 'I', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.1.1.2', 
                                    'color': 'green', 
                                    'encap': 'ipsec', 
                                    'preference': '200'
                                }, 
                                4: {
                                    'index': 4, 
                                    'path_id': '939', 
                                    'label': '1002', 
                                    'status': ['C', 'I', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.1.1.2', 
                                    'color': 'blue', 
                                    'encap': 'ipsec', 
                                    'preference': '200'
                                }, 
                                5: {
                                    'index': 5, 
                                    'path_id': '940', 
                                    'label': '1002', 
                                    'status': ['R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.2.1.1', 
                                    'color': 'green', 
                                    'encap': 'ipsec', 
                                    'preference': '100'
                                }, 
                                6: {
                                    'index': 6, 
                                    'path_id': '941', 
                                    'label': '1002', 
                                    'status': ['R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.2.1.1', 
                                    'color': 'blue', 
                                    'encap': 'ipsec', 
                                    'preference': '100'
                                }, 
                                7: {
                                    'index': 7, 
                                    'path_id': '942', 
                                    'label': '1002', 
                                    'status': ['R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.2.1.2', 
                                    'color': 'green', 
                                    'encap': 'ipsec', 
                                    'preference': '100'
                                }, 
                                8: {
                                    'index': 8, 
                                    'path_id': '943', 
                                    'label': '1002', 
                                    'status': ['R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '100.2.1.2', 
                                    'color': 'blue', 
                                    'encap': 'ipsec', 
                                    'preference': '100'
                                }
                            }
                        }
                    }
                }, 
                '10.1.1.0/24': {
                    'prefix': '10.1.1.0/24', 
                    'from_peer': {
                        '0.0.0.0': {
                            'peer': '0.0.0.0',
                            'path_list': {
                                1: {
                                    'index': 1, 
                                    'path_id': '73', 
                                    'label': '1002', 
                                    'status': ['C', 'Red', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '10.1.1.1', 
                                    'color': 'green', 
                                    'encap': 'ipsec', 
                                    'preference': '-'
                                }, 
                                2: {
                                    'index': 2, 
                                    'path_id': '74', 
                                    'label': '1002', 
                                    'status': ['C', 'Red', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '10.1.1.1', 
                                    'color': 'blue', 
                                    'encap': 'ipsec', 
                                    'preference': '-'
                                }
                            }
                        }
                    }
                }
            }
        }, 
        '511': {
            'prefixes': {
                '192.168.1.0/24': {
                    'prefix': '192.168.1.0/24', 
                    'from_peer': {
                        '0.0.0.0': {
                            'peer': '0.0.0.0',
                            'path_list': {
                                1: {
                                    'index': 1, 
                                    'path_id': '73', 
                                    'label': '1003', 
                                    'status': ['C', 'Red', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '10.1.1.1', 
                                    'color': 'green', 
                                    'encap': 'ipsec', 
                                    'preference': '-'
                                }, 
                                2: {
                                    'index': 2, 
                                    'path_id': '74', 
                                    'label': '1003', 
                                    'status': ['C', 'Red', 'R'], 
                                    'attr_type': 'installed', 
                                    'tloc_ip': '10.1.1.1', 
                                    'color': 'blue', 
                                    'encap': 'ipsec', 
                                    'preference': '-'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
