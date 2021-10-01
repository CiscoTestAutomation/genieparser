

expected_output = {
    'bgp_as_path_entries': 0,
    'bgp_asformat': 'asplain',
    'bgp_isolate_mode': 'No',
    'bgp_memory_state': 'ok',
    'bgp_mmode': 'Initialized',
    'bgp_paths_per_hwm_attr': 1,
    'bgp_performance_mode': 'No',
    'bgp_pid': 29474,
    'bgp_protocol_started_reason': 'configuration',
    'bgp_protocol_state': 'running',
    'bgp_tag': '100',
    'bytes_used': 368,
    'bytes_used_as_path_entries': 0,
    'entries_pending_delete': 0,
    'hwm_attr_entries': 5,
    'hwm_entries_pending_delete': 0,
    'num_attr_entries': 4,
    'segment_routing_global_block': '10000-25000',
    'vrf':
        {'VRF1': {
            'address_family':
                {'ipv4 unicast':
                    {'aggregate_label': '492287',
                    'export_rt_list': '100:100',
                    'import_rt_list': '100:100',
                    'label_mode': 'per-prefix',
                    'peers':
                        {1:
                            {'active_peers': 0,
                             'aggregates': 2,
                             'networks': 1,
                             'paths': 5,
                             'routes': 5}},
                    'redistribution':
                        {'direct':
                            {'route_map': 'genie_redistribution'},
                         'eigrp':
                            {'route_map': 'test-map'},
                         'static':
                            {'route_map': 'genie_redistribution'}},
                    'table_id': '0x10',
                    'table_state': 'up'},
                'ipv6 unicast': {
                    'aggregate_label': '492288',
                    'export_rt_list': '100:100',
                    'import_rt_list': '100:100',
                    'label_mode': 'per-prefix',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                         'non_critical': 10000,
                        },
                    'peers':
                        {0:
                            {'active_peers': 0,
                             'aggregates': 1,
                             'networks': 1,
                             'paths': 4,
                             'routes': 4}},
                    'redistribution':
                        {'direct':
                            {'route_map': 'genie_redistribution'},
                         'static':
                            {'route_map': 'genie_redistribution'}},
                    'table_id': '0x80000010',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'num_conf_peers': 1,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.229.11.11',
            'vrf_id': '3',
            'vrf_rd': '100:100',
            'vrf_state': 'up'},
         'default':
            {'address_family':
                {'ipv4 unicast':
                    {'peers':
                        {1:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                     'table_id': '0x1',
                     'table_state': 'up'},
                'ipv6 label unicast':
                    {'peers':
                        {0:
                            {'active_peers': 0,
                             'aggregates': 0,
                             'networks': 0,
                             'paths': 0,
                             'routes': 0}},
                     'table_id': '0x80000001',
                     'table_state': 'up'},
                'ipv6 unicast':
                    {'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                     'table_id': '0x80000001',
                     'table_state': 'up'},
                'vpnv4 unicast':
                    {'peers':
                        {1:
                            {'active_peers': 1,
                             'aggregates': 0,
                             'networks': 0,
                             'paths': 5,
                             'routes': 5}},
                     'table_id': '0x1',
                     'table_state': 'up'},
                'vpnv6 unicast':
                    {'peers':
                        {1:
                            {'active_peers': 1,
                            'aggregates': 0,
                             'networks': 0,
                             'paths': 4,
                             'routes': 4}},
                     'table_id': '0x80000001',
                     'table_state': 'up'}},
             'cluster_id': '0.0.0.0',
             'conf_router_id': '10.4.1.1',
             'confed_id': 0,
             'num_conf_peers': 3,
             'num_established_peers': 1,
             'num_pending_conf_peers': 0,
             'router_id': '10.4.1.1',
             'vrf_id': '1',
             'vrf_rd': 'not configured',
             'vrf_state': 'up'}}}
