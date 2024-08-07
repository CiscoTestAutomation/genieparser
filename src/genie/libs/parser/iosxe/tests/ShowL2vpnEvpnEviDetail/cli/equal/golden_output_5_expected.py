expected_output = {
    '11': {
        'adv_def_gateway': False,
        'adv_mcast': True,
        'adv_mcast_scope': 'sync-only',
        'bridge_domain': {
            '11': {
                'access_if': 'Vlan11',
                'core_vlan': 0,
                'etag': 0,
                'flood_suppress': True,
                'ipv4_irb': True,
                'ipv6_irb': True,
                'l2vni': 10011,
                'l3vni': 0,
                'nve_if': 'nve1',
                'peer': {
                    '109.0.0.1': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 7,
                        'mac_routes': 2,
                    },
                },
                'pseudo_port': {
                    'Port-channel10 service instance 11': {
                        'df_state': 'forwarding',
                        'esi': '03AA.AA00.0000.0100.0001',
                        'mac_ip_routes': 7,
                        'mac_routes': 3,
                    },
                },
                'rmac': '0000.0000.0000',
                'state': 'Established',
                'vtep_ip': '109.0.0.2',
            },
        },
        'encap_type': 'vxlan',
        'evi_type': 'VLAN Based',
        'export_rt': '1:11',
        'import_rt': '1:11',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '109.0.0.2:11',
        'rd_type': 'auto',
        're_orig_rt5': False,
        'replication_type': 'Ingress',
        'state': 'Established',
    },
}
