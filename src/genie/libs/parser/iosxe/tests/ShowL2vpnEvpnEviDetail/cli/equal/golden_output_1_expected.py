# golden_output_1_expected.py
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    '1': {
        'adv_def_gateway': False,
        'adv_mcast': True,
        'bridge_domain': {
            '100': {
                'access_if': 'Vlan100',
                'core_vlan': 0,
                'etag': 0,
                'flood_suppress': True,
                'ipv4_irb': True,
                'ipv6_irb': False,
                'l2vni': 10000,
                'l3vni': 0,
                'mcast_ip': '227.0.0.1',
                'nve_if': 'nve1',
                'pseudo_port': {
                    'AppGigabitEthernet4/0/1 service instance 100': {
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    }
                },
                'rmac': '0000.0000.0000',
                'state': 'Established',
                'vtep_ip': '1.20.20.20'
            }
        },
        'encap_type': 'vxlan',
        'evi_type': 'VLAN Based',
        'export_rt': '1:1',
        'import_rt': '1:1',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '20.20.20.20:1',
        'rd_type': 'auto',
        're_orig_rt5': False,
        'replication_type': 'Static',
        'state': 'Established'
    }
}
