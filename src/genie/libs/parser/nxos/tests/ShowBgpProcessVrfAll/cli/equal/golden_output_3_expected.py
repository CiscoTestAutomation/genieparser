

expected_output = {
    'bgp_as_path_entries': 1,
    'bgp_asformat': 'asplain',
    'bgp_isolate_mode': 'No',
    'bgp_memory_state': 'ok',
    'bgp_mmode': 'Initialized',
    'bgp_paths_per_hwm_attr': 6,
    'bgp_performance_mode': 'No',
    'bgp_pid': 6308,
    'bgp_protocol_started_reason': 'configuration',
    'bgp_protocol_state': 'running',
    'bgp_tag': '100',
    'bytes_used': 1276,
    'bytes_used_as_path_entries': 26,
    'entries_pending_delete': 0,
    'hwm_attr_entries': 11,
    'hwm_entries_pending_delete': 0,
    'num_attr_entries': 11,
    'vrf':
        {'default':
            {'address_family':
                {'ipv4 unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3333,
                        'non_critical': 11111},
                    'peers':
                        {1:
                            {'active_peers': 1,
                            'aggregates': 1,
                            'networks': 0,
                            'paths': 12,
                            'routes': 12}},
                    'redistribution':
                        {'direct':
                            {'route_map': 'RMAP_Lo0'},
                        'ospf':
                            {'route_map': 'RMAP_OSPF'},
                        'static':
                            {'route_map': 'ALL'}},
                    'route_reflector': True,
                    'table_id': '0x1',
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
                    'table_id': '0x80000001',
                    'table_state': 'up'},
                'l2vpn evpn':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {1:
                            {'active_peers': 1,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 6,
                            'routes': 5}},
                    'table_id': '0x1',
                    'table_state': 'up'},
                'vpnv4 unicast':
                    {'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 4,
                            'routes': 3}},
                    'table_id': '0x1',
                    'table_state': 'up'},
                'vpnv6 unicast':
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
                    'table_id': '0x80000001',
                    'table_state': 'up'}},
            'cluster_id': '10.4.1.1',
            'conf_router_id': '0.0.0.0',
            'confed_id': 100,
            'vnid': '0',
            'num_conf_peers': 1,
            'num_established_peers': 1,
            'num_pending_conf_peers': 0,
            'router_id': '10.49.1.0',
            'vrf_id': '1',
            'vrf_rd': 'not configured',
            'vrf_state': 'up'},
        'vrf-9100':
            {'address_family':
                {'ipv4 unicast':
                    {'export_rt_list': '100:9100',
                    'import_rt_list': '100:9100',
                    'evpn_export_rt_list': '100:9100',
                    'evpn_import_rt_list': '100:9100',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 4,
                            'routes': 3}},
                    'redistribution':
                        {'direct':
                            {'route_map': 'permitall'},
                        'hmm':
                            {'route_map': 'permitall'}},
                    'table_id': '0x3',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'export_rt_list': '100:9100',
                    'import_rt_list': '100:9100',
                    'evpn_export_rt_list': '100:9100',
                    'evpn_import_rt_list': '100:9100',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'table_id': '0x80000003',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'encap_type': 'VXLAN',
            'router_mac': '000c.29ff.a329',
            'topo_id': '1000',
            'vip_derived_mac': '000c.29ff.a329',
            'vnid': '9100',
            'vtep_ip': '10.49.1.1',
            'vtep_vip_r': '10.49.2.1',
            'vtep_virtual_ip': '10.49.2.1',
            'num_conf_peers': 0,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.220.11.1',
            'vrf_id': '3',
            'vrf_rd': '10.49.1.0:3',
            'vrf_evpn_rd': '10.49.1.0:3',
            'vrf_state': 'up'},
        'vrf-9105':
            {'address_family':
                {'ipv4 unicast':
                    {'export_rt_list': '100:9105',
                    'import_rt_list': '100:9105',
                    'evpn_export_rt_list': '100:9105',
                    'evpn_import_rt_list': '100:9105',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'redistribution':
                        {'hmm':
                            {'route_map': 'permitall'}},
                    'table_id': '0x4',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'export_rt_list': '100:9105',
                    'import_rt_list': '100:9105',
                    'evpn_export_rt_list': '100:9105',
                    'evpn_import_rt_list': '100:9105',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
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
            'encap_type': 'VXLAN',
            'router_mac': '000c.29ff.a329',
            'topo_id': '1005',
            'vip_derived_mac': '000c.29ff.a329',
            'vnid': '9105',
            'vtep_ip': '10.49.1.1',
            'vtep_vip_r': '10.49.2.1',
            'vtep_virtual_ip': '10.49.2.1',
            'num_conf_peers': 0,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.220.16.1',
            'vrf_id': '4',
            'vrf_rd': '10.49.1.0:4',
            'vrf_evpn_rd': '10.49.1.0:4',
            'vrf_state': 'up'},
        'vrf-9106':
            {'address_family':
                {'ipv4 unicast':
                    {'export_rt_list': '100:9106',
                    'import_rt_list': '100:9106',
                    'evpn_export_rt_list': '100:9106',
                    'evpn_import_rt_list': '100:9106',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'redistribution':
                        {'hmm':
                            {'route_map': 'permitall'}},
                    'table_id': '0x5',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'export_rt_list': '100:9106',
                    'import_rt_list': '100:9106',
                    'evpn_export_rt_list': '100:9106',
                    'evpn_import_rt_list': '100:9106',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'table_id': '0x80000005',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'encap_type': 'VXLAN',
            'router_mac': '000c.29ff.a329',
            'topo_id': '1006',
            'vip_derived_mac': '000c.29ff.a329',
            'vnid': '9106',
            'vtep_ip': '10.49.1.1',
            'vtep_vip_r': '10.49.2.1',
            'vtep_virtual_ip': '10.49.2.1',
            'num_conf_peers': 0,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.220.17.1',
            'vrf_id': '5',
            'vrf_rd': '10.49.1.0:5',
            'vrf_evpn_rd': '10.49.1.0:5',
            'vrf_state': 'up'},
        'vrf-9107':
            {'address_family':
                {'ipv4 unicast':
                    {'export_rt_list': '100:9107',
                    'import_rt_list': '100:9107',
                    'evpn_export_rt_list': '100:9107',
                    'evpn_import_rt_list': '100:9107',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'redistribution':
                        {'hmm':
                            {'route_map': 'permitall'}},
                    'table_id': '0x6',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'export_rt_list': '100:9107',
                    'import_rt_list': '100:9107',
                    'evpn_export_rt_list': '100:9107',
                    'evpn_import_rt_list': '100:9107',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'table_id': '0x80000006',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'encap_type': 'VXLAN',
            'router_mac': '000c.29ff.a329',
            'topo_id': '1007',
            'vip_derived_mac': '000c.29ff.a329',
            'vnid': '9107',
            'vtep_ip': '10.49.1.1',
            'vtep_vip_r': '10.49.2.1',
            'vtep_virtual_ip': '10.49.2.1',
            'num_conf_peers': 0,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.220.18.1',
            'vrf_id': '6',
            'vrf_rd': '10.49.1.0:6',
            'vrf_evpn_rd': '10.49.1.0:6',
            'vrf_state': 'up'},
        'vrf-9108':
            {'address_family':
                {'ipv4 unicast':
                    {'export_rt_list': '100:9108',
                    'import_rt_list': '100:9108',
                    'evpn_export_rt_list': '100:9108',
                    'evpn_import_rt_list': '100:9108',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'redistribution':
                        {'hmm':
                            {'route_map': 'permitall'}},
                    'table_id': '0x7',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'export_rt_list': '100:9108',
                    'import_rt_list': '100:9108',
                    'evpn_export_rt_list': '100:9108',
                    'evpn_import_rt_list': '100:9108',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'table_id': '0x80000007',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'encap_type': 'VXLAN',
            'router_mac': '000c.29ff.a329',
            'topo_id': '1008',
            'vip_derived_mac': '000c.29ff.a329',
            'vnid': '9108',
            'vtep_ip': '10.49.1.1',
            'vtep_vip_r': '10.49.2.1',
            'vtep_virtual_ip': '10.49.2.1',
            'num_conf_peers': 0,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.220.19.1',
            'vrf_id': '7',
            'vrf_rd': '10.49.1.0:7',
            'vrf_evpn_rd': '10.49.1.0:7',
            'vrf_state': 'up'},
        'vrf-9109':
            {'address_family':
                {'ipv4 unicast':
                    {'export_rt_list': '100:9109',
                    'import_rt_list': '100:9109',
                    'evpn_export_rt_list': '100:9109',
                    'evpn_import_rt_list': '100:9109',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'redistribution':
                        {'hmm':
                            {'route_map': 'permitall'}},
                    'table_id': '0x8',
                    'table_state': 'up'},
                'ipv6 unicast':
                    {'export_rt_list': '100:9109',
                    'import_rt_list': '100:9109',
                    'evpn_export_rt_list': '100:9109',
                    'evpn_import_rt_list': '100:9109',
                    'label_mode': 'per-vrf',
                    'next_hop_trigger_delay':
                        {'critical': 3000,
                        'non_critical': 10000},
                    'peers':
                        {0:
                            {'active_peers': 0,
                            'aggregates': 0,
                            'networks': 0,
                            'paths': 0,
                            'routes': 0}},
                    'table_id': '0x80000008',
                    'table_state': 'up'}},
            'cluster_id': '0.0.0.0',
            'conf_router_id': '0.0.0.0',
            'confed_id': 0,
            'encap_type': 'VXLAN',
            'router_mac': '000c.29ff.a329',
            'topo_id': '1009',
            'vip_derived_mac': '000c.29ff.a329',
            'vnid': '9109',
            'vtep_ip': '10.49.1.1',
            'vtep_vip_r': '10.49.2.1',
            'vtep_virtual_ip': '10.49.2.1',
            'num_conf_peers': 0,
            'num_established_peers': 0,
            'num_pending_conf_peers': 0,
            'router_id': '10.220.20.1',
            'vrf_id': '8',
            'vrf_rd': '10.49.1.0:8',
            'vrf_evpn_rd': '10.49.1.0:8',
            'vrf_state': 'up'}}}
