

expected_output = {
    'vpc_domain_id': '1',
    'vpc_peer_status': 'peer adjacency formed ok',
    'vpc_peer_keepalive_status': 'peer is alive',
    'vpc_configuration_consistency_status': 'success',
    'vpc_per_vlan_consistency_status': 'success',
    'vpc_type_2_consistency_status': 'success',
    'vpc_role': 'primary',
    'num_of_vpcs': 1,
    'peer_gateway': 'Enabled',
    'dual_active_excluded_vlans': '-',
    'vpc_graceful_consistency_check_status': 'Enabled',
    'vpc_auto_recovery_status': 'Enabled, timer is off.(timeout = 240s)',
    'vpc_delay_restore_status': 'Timer is off.(timeout = 30s)',
    'vpc_delay_restore_svi_status': 'Timer is off.(timeout = 10s)',
    'operational_l3_peer_router': 'Disabled',
    'peer_link': {
        1: {
            'peer_link_id': 1,
            'peer_link_ifindex': 'Port-channel101',
            'peer_link_port_state': 'up',
            'peer_up_vlan_bitset': '1,100-102,200-202,300-350'
        }
    },
    'vpc': {
        1: {
            'vpc_id': 1,
            'vpc_ifindex': 'Port-channel1',
            'vpc_port_state': 'up',
            'vpc_consistency': 'success',
            'vpc_consistency_status': 'success',
            'up_vlan_bitset': '1,100-102,200-202'
        }
    }
}
