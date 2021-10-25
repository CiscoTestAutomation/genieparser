expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                16: {
                    'outgoing_label_or_vc': {
                        '16': {
                            'prefix_or_tunnel_id': {
                                '10.0.0.1 1 [19]': {
                                    'outgoing_interface': {
                                        'Ethernet1/0': {
                                            'next_hop': '10.0.1.30',
                                            'bytes_label_switched': 0,
                                            'mac': 14,
                                            'encaps': 18,
                                            'mru': 1500,
                                            'label_stack': '16',
                                            'macstr': 'AABBCC032800AABBCC0325018847',
                                            'lstack': '00010000',
                                            'output_feature_configured': False,
                                            'broadcast': True}}}}}}},
                17: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '10.0.0.1 1 [19]': {
                                    'outgoing_interface': {
                                        'aggregate': {
                                            'bytes_label_switched': 342,
                                            'mac': 0,
                                            'encaps': 0,
                                            'mru': 0,
                                            'label_stack': '',
                                            'via': 'Ls0'}}}}}}}}}}}
