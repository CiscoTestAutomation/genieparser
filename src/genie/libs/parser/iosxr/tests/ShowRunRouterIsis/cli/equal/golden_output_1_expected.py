

expected_output = {
    'isis': {
        'test': {
            'address_family': {
                'ipv4_unicast': {
                    'fast_reroute': {
                        'per_prefix': {
                            'tiebreaker': {
                                'srlg_disjoint': 'index 255'}}},
                    'mpls': {
                        'traffic_eng': ['level-2-only spf-interval maximum-wait 8000 initial-wait 300 secondary-wait 500']},
                    'segment_routing': {
                        'mpls': 'sr-prefer'},
                    'spf_prefix_priority': {
                        'critical_tag': '1000'}}},
            'segment_routing': {
                'global_block': '160000 167999'},
            'interfaces': {
                'Bundle-Ether2': {
                    'other': ['passive']}},
            'lsp_gen_interval': {
                'maximum_wait': '8000',
                'initial_wait': '1',
                'secondary_wait': '250'}}}}
