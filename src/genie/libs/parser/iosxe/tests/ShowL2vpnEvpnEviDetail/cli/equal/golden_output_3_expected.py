# golden_output_3_expected.py
#
# Copyright (c) 2021-2022 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    '7': {
        'adv_def_gateway': False,
        'adv_mcast': True,
        'bridge_domain': {
            '107': {
                'core_vlan': 0,
                'etag': 0,
                'flood_suppress': True,
                'l2vni': 20107,
                'l3vni': 0,
                'mcast_ip': 'UNKNOWN',
                'pseudo_port': {
                    'Ethernet0/0 service instance 107': {
                        'mac_ip_routes': 3,
                        'mac_routes': 1,
                    },
                    'Ethernet0/3 service instance 107': {
                        'mac_ip_routes': 0,
                        'mac_routes': 1,
                    },
                    'Ethernet1/0 service instance 107': {
                        'mac_ip_routes': 0,
                        'mac_routes': 0,
                    },
                },
                'rmac': '0000.0000.0000',
                'state': 'Established',
                'vtep_ip': 'UNKNOWN',
                'vtep_ip_sec': 'UNKNOWN',
            },
        },
        'encap_type': 'vxlan',
        'evi_type': 'VLAN Based',
        'export_rt': '1:7',
        'import_rt': '1:7',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '1.1.1.2:7',
        'rd_type': 'auto',
        're_orig_rt5': False,
        'replication_type': 'Static',
        'state': 'Established',
    },
    '10': {
        'adv_def_gateway': False,
        'adv_mcast': False,
        'bridge_domain': {
            '10': {
                'core_vlan': 0,
                'etag': 0,
                'flood_suppress': True,
                'l2vni': 39100,
                'l3vni': 0,
                'nve_if': 'nve1',
                'peer': {
                    '1.20.20.20': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '1.30.30.30': {
                        'ead_routes': 0,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'pseudo_port': {
                    'pseudowire100002': {
                        'access_vfi': 'VFI10',
                        'df_state': 'forwarding',
                        'mac_ip_routes': 0,
                        'mac_routes': 0,
                        'peer': '5.5.5.5',
                        'vc': 10
                    },
                    'pseudowire100003': {
                        'access_vfi': 'VFI10',
                        'df_state': 'forwarding',
                        'mac_ip_routes': 0,
                        'mac_routes': 0,
                        'peer': '15.15.15.15',
                        'vc': 10
                    }
                },
                'rmac': '0000.0000.0000',
                'state': 'Established',
                'vtep_ip': '1.10.10.10'
            }
        },
        'encap_type': 'vxlan',
        'evi_type': 'VLAN Based',
        'export_rt': '1:10',
        'import_rt': '1:10',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '10.10.10.10:10',
        'rd_type': 'auto',
        're_orig_rt5': False,
        'replication_type': 'Ingress',
        'state': 'Established'
    },
        '20': {
            'adv_def_gateway': False,
            'adv_mcast': False,
            'bridge_domain': {
                '20': {
                    'core_vlan': 0,
                    'etag': 0,
                    'flood_suppress': True,
                    'l2vni': 39200,
                    'l3vni': 0,
                    'nve_if': 'nve1',
                    'peer': {
                        '1.20.20.20': {
                            'ead_routes': 1,
                            'imet_routes': 1,
                            'mac_ip_routes': 0,
                            'mac_routes': 0
                        },
                        '1.30.30.30': {
                            'ead_routes': 0,
                            'imet_routes': 1,
                            'mac_ip_routes': 0,
                            'mac_routes': 0
                        }
                    },
                    'pseudo_port': {
                        'pseudowire100005': {
                            'access_vfi': 'VFI20',
                            'df_state': 'forwarding',
                            'mac_ip_routes': 0,
                            'mac_routes': 0,
                            'peer': '5.5.5.5',
                            'vc': 20
                        },
                        'pseudowire100006': {
                            'access_vfi': 'VFI20',
                            'df_state': 'forwarding',
                            'mac_ip_routes': 0,
                            'mac_routes': 0,
                            'peer': '15.15.15.15',
                            'vc': 20
                        }
                    },
                    'rmac': '0000.0000.0000',
                    'state': 'Established',
                    'vtep_ip': '1.10.10.10'
                }
            },
            'encap_type': 'vxlan',
            'evi_type': 'VLAN Based',
            'export_rt': '1:20',
            'import_rt': '1:20',
            'ip_local_learn': True,
            'per_evi_label': 'none',
            'rd': '10.10.10.10:20',
            'rd_type': 'auto',
            're_orig_rt5': False,
            'replication_type': 'Ingress',
            'state': 'Established'
        }
}
