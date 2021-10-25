expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                40: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '65536/1[TE-Bind]': {
                                    'outgoing_interface': {
                                        'Tunnel65536': {
                                            'next_hop': 'point2point',
                                            'bytes_label_switched': 0,
                                            'mac': 14,
                                            'encaps': 26,
                                            'mru': 1492,
                                            'label_stack': '16052 16062 16063',
                                            'via': 'GigabitEthernet0/1/7',
                                            'macstr': '0050568DA282BC16652F3A178847',
                                            'lstack': '03EB400003EBE00003EBF000',
                                            'output_feature_configured': False}}}}}}}}}}}
