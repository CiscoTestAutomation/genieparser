

expected_output = {
    'vpc_domain_id': '10',
    'vpc_peer_status': 'peer adjacency formed ok',
    'vpc_peer_keepalive_status': 'peer is alive',
    'vpc_configuration_consistency_status': 'failed',
    'vpc_configuration_consistency_reason': 'vPC type-1 configuration incompatible - STP interface port type inconsistent',
    'vpc_role': 'secondary',
    'num_of_vpcs': 1,
    'peer_link': {
        1: {
            'peer_link_id': 1,
            'peer_link_ifindex': 'Port-channel10',
            'peer_link_port_state': 'up',
            'peer_up_vlan_bitset': '1-100'
        }
    },
    'vpc': {
        20: {
            'vpc_id': 20,
            'vpc_ifindex': 'Port-channel20',
            'vpc_port_state': 'up',
            'vpc_consistency': 'failed',
            'vpc_consistency_status': 'vPC type-1 configuration',
            'up_vlan_bitset': '-'
        }
    }
}
