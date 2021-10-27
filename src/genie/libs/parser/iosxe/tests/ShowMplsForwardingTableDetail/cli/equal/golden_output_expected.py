expected_output = {
    'vrf': {
        'L3VPN-0051': {
            'local_label': {
                9301: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '172.16.100.1/32[V]': {
                                    'outgoing_interface': {
                                        'Port-channel1.51': {
                                            'next_hop': '192.168.10.253',
                                            'bytes_label_switched': 0,
                                            'mac': 18,
                                            'encaps': 18,
                                            'mru': 1530,
                                            'label_stack': '',
                                            'macstr': '00002440156384B261CB1480810000330800',
                                            'vpn_route': 'L3VPN-0051',
                                            'output_feature_configured': False,
                                            'load_sharing': {
                                                'method': 'per-destination',
                                                'slots': [
                                                    '0',
                                                    '2',
                                                    '4',
                                                    '6',
                                                    '8',
                                                    '10',
                                                    '12',
                                                    '14']}}}}}}}},
                2641: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '172.16.100.100/32[V]': {
                                    'outgoing_interface': {
                                        'Port-channel1.51': {
                                            'next_hop': '192.168.10.253',
                                            'bytes_label_switched': 0,
                                            'mac': 18,
                                            'encaps': 18,
                                            'mru': 1530,
                                            'label_stack': '',
                                            'via': 'Ls0',
                                            'macstr': 'AABBCC032800AABBCC0325018847',
                                            'lstack': '00010000',
                                            'vpn_route': 'L3VPN-0051',
                                            'output_feature_configured': False}}}}}}},
                2642: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '192.168.10.0/24[V]': {
                                    'outgoing_interface': {
                                        'Aggregate/L3VPN-0051': {
                                            'bytes_label_switched': 12189672,
                                            'mac': 0,
                                            'encaps': 0,
                                            'mru': 0,
                                            'label_stack': '',
                                            'vpn_route': 'L3VPN-0051',
                                            'output_feature_configured': False,
                                            'broadcast': True}}}}}}}}}}}
