

expected_output = {
    'vpc_domain_id': '10',
    'vpc_peer_status': 'peer adjacency formed ok',
    'vpc_peer_keepalive_status': 'peer is alive',
    'vpc_configuration_consistency_status': 'success',
    'vpc_role': 'primary',
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
            'vpc_consistency': 'success',
            'vpc_consistency_status': 'success',
            'up_vlan_bitset': '1-100'
        }
    }
}
