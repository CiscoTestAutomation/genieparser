expected_output = {
    'OSPF2202BGP': {
        'statements': {
            10: {
                'actions': {
                    'set_community_list': 'DCBQ_VOZ',
                    'set_next_hop': '10.20.96.53',
                    'set_local_pref': 330
                },
                'conditions': {

                }
            },
            20: {
                'actions': {
                    'set_community_list': 'DCBQ_VOZ',
                    'set_next_hop': '10.20.96.53',
                    'set_local_pref': 310
                },
                'conditions': {

                }
            }
        }
    }
}
