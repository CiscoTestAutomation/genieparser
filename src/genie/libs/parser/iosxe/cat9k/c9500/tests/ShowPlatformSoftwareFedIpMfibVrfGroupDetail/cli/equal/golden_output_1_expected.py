expected_output = {
    'mvrf_table': {
        1: {
            'mcast_table': {
                'cpu_credit': 1,
                'fset_aux_urid': '0x0',
                'fset_urid': '0x3000000000000004',
                'gid': 8195,
                'group_ip': '227.0.0.1',
                'hardware_info_asic': {
                    'cookie_urid': '0x30::4',
                    'enable_rpf_check': 1,
                    'ip_mcid_oid': 2113,
                    'punt_and_forward': 1,
                    'punt_on_rpf_fail': 1,
                    'rpf_port_oid': 660,
                    'rpfid': 0,
                    'use_rpfid': 0
                },
                'hw_flag': 'InHw',
                'mcid_oid_asic': 2113,
                'mlist_handle': '0x118807d8e78',
                'mlist_urid': '0x1000000000000017',
                'npi_mroute_ent': '0x118825a0178',
                'oif_details': {
                    1: {
                        'adj_id': '0xf80054d6',
                        'flags': 'A',
                        'hw_flag': 'Cpu',
                        'interface': 'Tu0',
                        'intf_type': '--------',
                        'msg_type': 'NORMAL',
                        'parent_if': '--------'
                    },
                    2: {
                        'adj_id': '0xf8005551',
                        'flags': 'F NS',
                        'hw_flag': '---',
                        'interface': 'Hu1/0/23',
                        'intf_type': '--------',
                        'msg_type': 'NORMAL',
                        'parent_if': '--------'
                    }
                },
                'rpf_adjancency_id': '0xf80054d6',
                'source_ip': '*',
                'svi_fwd_ifs': 0,
                'total_packets': 0}},
        2: {
            'mcast_table': {
                'cpu_credit': 0,
                'fset_aux_urid': '0x0',
                'fset_urid': '0x3000000000000046',
                'gid': 8259,
                'group_ip': '227.0.0.1',
                'hardware_info_asic': {
                    'cookie_urid': '0x30::46',
                    'enable_rpf_check': 1,
                    'ip_mcid_oid': 2256,
                    'punt_and_forward': 0,
                    'punt_on_rpf_fail': 1,
                    'rpf_port_oid': 2116,
                    'rpfid': 0,
                    'use_rpfid': 0
                },
                'hw_flag': 'InHw',
                'mcid_oid_asic': 2256,
                'mlist_handle': '0x1188334c298',
                'mlist_urid': '0x1000000000001fbf',
                'npi_mroute_ent': '0x118833ccf78',
                'oif_details': {
                    1: {
                        'adj_id': '0xf8005501',
                        'flags': 'A',
                        'hw_flag': '---',
                        'interface': 'Hu1/0/9',
                        'intf_type': '--------',
                        'msg_type': 'NORMAL',
                        'parent_if': '--------'
                    },
                    2: {
                        'adj_id': '0xf8005551',
                        'flags': 'F NS',
                        'hw_flag': '---',
                        'interface': 'Hu1/0/23',
                        'intf_type': '--------',
                        'msg_type': 'NORMAL',
                        'parent_if': '--------'
                    }
                },
                'rpf_adjancency_id': '0xf8005501',
                'source_ip': '11.11.11.2',
                'svi_fwd_ifs': 0,
                'total_packets': 0
            }
        }
    }
}