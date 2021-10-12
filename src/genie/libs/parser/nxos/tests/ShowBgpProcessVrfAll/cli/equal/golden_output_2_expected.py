

expected_output = {
    'bgp_as_path_entries': 0,
    'bgp_asformat': 'asplain',
    'bgp_isolate_mode': 'Yes',
    'bgp_memory_state': 'ok',
    'bgp_mmode': 'Initialized',
    'bgp_paths_per_hwm_attr': 3,
    'bgp_performance_mode': 'No',
    'bgp_pid': 26549,
    'bgp_protocol_started_reason': 'configuration',
    'bgp_protocol_state': 'running (isolate)',
    'bgp_tag': '333',
    'bytes_used': 784,
    'bytes_used_as_path_entries': 0,
    'entries_pending_delete': 0,
    'hwm_attr_entries': 8,
    'hwm_entries_pending_delete': 0,
    'num_attr_entries': 7,
    'segment_routing_global_block': '10000-25000',
    'vrf':
        {'VRF1':
            {'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'num_conf_peers': 2,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '0.0.0.0',
            'vrf_id': '3',
            'vrf_rd': 'not configured',
            'vrf_state': 'up'},
        'ac':
            {'address_family':
                {'ipv4 unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {1:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'table_id': '0x4',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'table_id': '0x80000004',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'num_conf_peers': 1,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '0.0.0.0',
            'vrf_id': '4',
            'vrf_rd': 'not configured',
            'vrf_state': 'up'},
        'default':
            {'address_family':
                {'ipv4 label unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 7,
                            'routes': 4}},
                    'table_id': '0x1',
                    'table_state': 'up'},
                'ipv4 multicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {3:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 3,
                            'routes': 3}},
                    'redistribution':
                        {'static':
                            {'route_map': 'PERMIT_ALL_RM'}},
                    'route_reflector': True,
                    'table_id': '0x1',
                    'table_state': 'up'},
                'ipv4 unicast':
                    {'label_mode': 'per-prefix',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {5:
                            {'active_peers': 0,
                            'aggregates': 1,
                            'networks': 1,
                            'paths': 7,
                            'routes': 4}},
                    'redistribution':
                        {'static':
                            {'route_map': 'ADD_RT_400_400'}},
                    'route_reflector': True,
                    'table_id': '0x1',
                    'table_state': 'up'},
                'ipv6 multicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {4:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 3,
                            'routes': 3}},
                    'redistribution':
                        {'static':
                            {'route_map': 'PERMIT_ALL_RM'}},
                    'route_reflector': True,
                    'table_id': '0x80000001',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {4:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 5,
                            'routes': 3}},
                    'redistribution':
                        {'static':
                            {'route_map': 'PERMIT_ALL_RM'}},
                    'route_reflector': True,
                    'table_id': '0x80000001',
                    'table_state': 'up'},
                'link-state':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {4:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'route_reflector': True,
                    'table_id': '0x1',
                    'table_state': 'up'},
                'vpnv4 unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 4,
                        'non_critical': 5},
                    'peers':
                        {3:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 7,
                            'routes': 5}},
                    'route_reflector': True,
                    'table_id': '0x1',
                    'table_state': 'up'},
                'vpnv6 unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {3:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 7,
                            'routes': 5}},
                    'route_reflector': True,
                    'table_id': '0x80000001',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.3',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'num_conf_peers': 6,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.36.3.3',
            'vrf_id': '1',
            'vrf_rd': 'not configured',
            'vrf_state': 'up'},
        'management':
            {'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'num_conf_peers': 1,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '0.0.0.0',
            'vrf_id': '2',
            'vrf_rd': 'not configured',
            'vrf_state': 'up'},
        'vpn1':
            {'address_family':
                {'ipv4 multicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 2,
                            'routes': 2}},
                    'redistribution':
                        {'static': {'route_map': 'PERMIT_ALL_RM'}},
                    'table_id': '0x5',
                    'table_state': 'up'},
                'ipv4 unicast':
                    {'aggregate_label': '492287',
                    'export_default_map': 'PERMIT_ALL_RM',
                    'export_default_prefix_count': 2,
                    'export_default_prefix_limit': 1000,
                    'export_rt_list': '100:1 400:400',
                    'import_default_map': 'PERMIT_ALL_RM',
                    'import_default_prefix_count': 3,
                    'import_default_prefix_limit': 1000,
                    'import_rt_list': '100:1',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {2:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 5,
                            'routes': 3}},
                    'redistribution':
                        {'static': {'route_map': 'PERMIT_ALL_RM'}},
                    'table_id': '0x5',
                    'table_state': 'up'},
                'ipv6 multicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 2,
                            'routes': 2}},
                    'redistribution':
                        {'static': {'route_map': 'PERMIT_ALL_RM'}},
                    'table_id': '0x80000005',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'aggregate_label': '492288',
                    'export_default_map': 'PERMIT_ALL_RM',
                    'export_default_prefix_count': 2,
                    'export_default_prefix_limit': 1000,
                    'export_rt_list': '1:100 600:600',
                    'import_default_map': 'PERMIT_ALL_RM',
                    'import_default_prefix_count': 3,
                    'import_default_prefix_limit': 1000,
                    'import_rt_list': '1:100',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {2:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 5,
                            'routes': 3}},
                    'redistribution':
                        {'static': {'route_map': 'PERMIT_ALL_RM'}},
                    'table_id': '0x80000005',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'num_conf_peers': 2,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.21.33.33',
            'vrf_id': '5',
            'vrf_rd': '1:100',
            'vrf_evpn_rd': '1:100',
            'vrf_state': 'up'},
        'vpn2':
            {'address_family':
                {'ipv4 unicast':
                    {'import_rt_list': '400:400',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 2,
                            'routes': 2}},
                    'table_id': '0x6',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'import_rt_list': '600:600',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 2,
                            'routes': 2}},
                    'table_id': '0x80000006',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'num_conf_peers': 0,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '0.0.0.0',
            'vrf_id': '6',
            'vrf_rd': '2:100',
            'vrf_evpn_rd': '2:100',
            'vrf_state': 'up'}}}
