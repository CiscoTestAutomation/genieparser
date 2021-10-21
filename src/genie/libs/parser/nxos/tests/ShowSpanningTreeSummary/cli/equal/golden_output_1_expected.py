

expected_output = {
    'mode': {
        'mst': {
            'MST0000': {
                'blocking': 1,
                'listening': 0,
                'learning': 0,
                'forwarding': 0,
                'stp_active': 1
            }
        }
    },
    'root_bridge_for': 'MST0000',
    'mst_type': 'IEEE Standard',
    'port_type_default': False,
    'bpdu_guard': False,
    'bpdu_filter': False,
    'bridge_assurance': True,
    'loop_guard': False,
    'path_cost_method': 'long',
    'pvst_simulation': True,
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
