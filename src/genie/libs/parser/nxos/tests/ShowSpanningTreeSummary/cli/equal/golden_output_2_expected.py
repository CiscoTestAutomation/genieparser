

expected_output = {
    'mode': {
        'mst': {
            'MST0': {
                'blocking': 3,
                'listening': 0,
                'learning': 0,
                'forwarding': 9,
                'stp_active': 12
            },
            'MST100': {
                'blocking': 3,
                'listening': 0,
                'learning': 0,
                'forwarding': 1,
                'stp_active': 4
            }
        }
    },
    'root_bridge_for': 'MST0000',
    'mst_type': 'IEEE Standard',
    'port_type_default': False,
    'bpdu_guard': True,
    'bpdu_filter': True,
    'bridge_assurance': True,
    'loop_guard': False,
    'path_cost_method': 'long',
    'pvst_simulation': False,
    'vpc_peer_switch': True,
    'vpc_peer_switch_status': 'non-operational',
    'stp_lite': True,
    'total_statistics': {
        'blockings': 1,
        'listenings': 0,
        'learnings': 0,
        'forwardings': 0,
        'stp_actives': 1
    }
}
