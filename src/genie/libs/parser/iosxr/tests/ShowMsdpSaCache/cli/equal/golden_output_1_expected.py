

expected_output = {
    'vrf': {
        'VRF1': {
            'sa_cache': {
                '239.1.1.1 10.1.1.10': {
                    'expire': '00:01:32',
                    'group': '239.1.1.1',
                    'origin_rp': {
                        '192.168.1.1': {
                            'rp_address': '192.168.1.1',
                        },
                    },
                    'peer_as': 200,
                    'peer_learned_from': '192.168.1.1',
                    'rpf_peer': '192.168.1.1',
                    'source_addr': '10.1.1.10',
                    'flags': {
                        'grp': ['PI'],
                        'src': ['E', 'EA', 'PI'],
                    },
                    'statistics': {
                        'received': {
                            'encapsulated_data_received': 0,
                            'sa': 2,
                        },
                    },
                    'up_time': '00:01:02',
                },
            },
        },
    },
}
