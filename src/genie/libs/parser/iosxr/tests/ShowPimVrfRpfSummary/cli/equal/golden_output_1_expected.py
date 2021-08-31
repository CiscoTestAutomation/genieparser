

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'default_rpf_table': 'IPv4-Unicast-default',
                    'isis_mcast_topology': False,
                    'mo_frr_flow_based': False,
                    'mo_frr_rib': False,
                    'multipath': True,
                    'pim_rpfs_registered': 'Unicast RIB table',
                    'rib_convergence_time_left': '00:00:00',
                    'rib_convergence_timeout': '00:30:00',
                    'rump_mu_rib': False,
                    'table':
                        {'IPv4-Unicast-default':
                            {'pim_rpf_registrations': 1,
                            'rib_table_converged': True}}}}}}}
