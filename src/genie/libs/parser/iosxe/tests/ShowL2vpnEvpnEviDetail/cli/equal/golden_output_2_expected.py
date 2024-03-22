# golden_output_2_expected.py
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    '1': {
        'adv_def_gateway': False,
        'adv_mcast': False,
        'bridge_domain': {
            '1': {
                'bum_label': 1002,
                'etag': 0,
                'flood_suppress': True,
                'peer': {
                    '15.15.15.15': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '20.20.20.20': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '25.25.25.25': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 2,
                        'mac_routes': 2},
                    '26.26.26.26': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '30.30.30.30': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'per_bd_label': 1003,
                'pseudo_port': {
                    'Ethernet0/1 service instance 1': {
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    'Ethernet0/2 service instance 1': {
                        'df_state': 'forwarding',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    'Ethernet0/3 service instance 1': {
                        'df_state': 'PE-to-CE BUM blocked',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'state': 'Established'
            }
        },
        'encap_type': 'mpls',
        'evi_type': 'VLAN Based',
        'export_rt': '1:1',
        'import_rt': '1:1',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '10.10.10.10:1',
        'rd_type': 'auto',
        'replication_type': 'Ingress',
        'state': 'Established'
    },
    '2': {
        'adv_def_gateway': False,
        'adv_mcast': False,
        'bridge_domain': {
            '2': {
                'bum_label': 1004,
                'etag': 0,
                'flood_suppress': True,
                'peer': {
                    '15.15.15.15': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '20.20.20.20': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '25.25.25.25': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 2,
                        'mac_routes': 2
                    },
                    '26.26.26.26': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '30.30.30.30': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'per_bd_label': 1005,
                'pseudo_port': {
                    'Ethernet0/1 service instance 2': {
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    'Ethernet0/2 service instance 2': {
                        'df_state': 'forwarding',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    'Ethernet0/3 service instance 2': {
                        'df_state': 'PE-to-CE BUM blocked',
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    }
                },
                'state': 'Established'
            }
        },
        'encap_type': 'mpls',
        'evi_type': 'VLAN Bundle',
        'export_rt': '1:2',
        'import_rt': '1:2',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '10.10.10.10:2',
        'rd_type': 'auto',
        'replication_type': 'Ingress',
        'state': 'Established'
    },
    '3': {
        'adv_def_gateway': False,
        'adv_mcast': False,
        'bridge_domain': {
            '3': {
                'bum_label': 1006,
                'etag': 3,
                'flood_suppress': True,
                'peer': {
                    '15.15.15.15': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '20.20.20.20': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '25.25.25.25': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    '26.26.26.26': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '30.30.30.30': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'per_bd_label': 1007,
                'pseudo_port': {
                    'Ethernet0/1 service instance 3': {
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    'Ethernet0/2 service instance 3': {
                        'df_state': 'blocked',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    'Ethernet0/3 service instance 3': {
                        'df_state': 'PE-to-CE BUM blocked',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'state': 'Established'
            },
            '4': {
                'bum_label': 1008,
                'etag': 4,
                'flood_suppress': True,
                'peer': {
                    '15.15.15.15': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '20.20.20.20': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '25.25.25.25': {'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    '26.26.26.26': {'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '30.30.30.30': {'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'per_bd_label': 1009,
                'pseudo_port': {
                    'Ethernet0/1 service instance 4': {
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    'Ethernet0/2 service instance 4': {
                        'df_state': 'forwarding',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    'Ethernet0/3 service instance 4': {
                        'df_state': 'PE-to-CE BUM blocked',
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    }
                },
                'state': 'Established'
            },
            '5': {
                'bum_label': 1010,
                'etag': 5,
                'flood_suppress': True,
                'peer': {
                    '15.15.15.15': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '20.20.20.20': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '25.25.25.25': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    '26.26.26.26': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    '30.30.30.30': {
                        'ead_routes': 1,
                        'imet_routes': 1,
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'per_bd_label': 1011,
                'pseudo_port': {
                    'Ethernet0/1 service instance 5': {
                        'mac_ip_routes': 1,
                        'mac_routes': 1
                    },
                    'Ethernet0/2 service instance 5': {
                        'df_state': 'blocked',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    },
                    'Ethernet0/3 service instance 5': {
                        'df_state': 'forwarding',
                        'mac_ip_routes': 0,
                        'mac_routes': 0
                    }
                },
                'state': 'Established'
            }
        },
        'encap_type': 'mpls',
        'evi_type': 'VLAN Aware',
        'export_rt': '1:3',
        'import_rt': '1:3',
        'ip_local_learn': True,
        'per_evi_label': 'none',
        'rd': '10.10.10.10:3',
        'rd_type': 'auto',
        'replication_type': 'Ingress',
        'state': 'Established'
    }
}
