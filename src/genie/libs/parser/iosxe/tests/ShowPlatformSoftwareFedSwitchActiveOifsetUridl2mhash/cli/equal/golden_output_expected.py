expected_output={
        'type': 'oif_vp_handles',
        'state': 'allocated',
        'md5': '99661bffcb26f8db:c644c3f264bb9bec',
        'fset_urid': '0x20000000000009b3',
        'parent_urid': '0x20000000000009af',
        'users_count': 1,
        'vp_oif_count': 2,
        'vp_interface_details': {
            1: {
            'vp_interface': 'Gi3/0/18Vlan3300',
            'interface': 'GigabitEthernet3/0/18',
            'physical_interface': 'GigabitEthernet3/0/18',
            'flags': 'oif_port mrouter ',
            'hw_flags': 'InHw  remote ',
            'asic': {
                'asic_num': 0,
                'l2_ac_oid': 0
            }
            },
            2: {
            'vp_interface': 'Gi4/0/18Vlan3300',
            'interface': 'GigabitEthernet4/0/18',
            'physical_interface': 'GigabitEthernet4/0/18',
            'flags': 'mrouter ',
            'hw_flags': 'InHw  remote ',
            'asic': {
                'asic_num': 0,
                'l2_ac_oid': 0
            }
            }
        },
        'fset_gid': 10618,
        'asic_mcid_oid': 9172,
        'hw_l2_mcg_info': '',
        'users': {
            '0x6000000000004c92': {
            'l2m_grp': {
                'vlan': '3300',
                'group_ip': '225.1.1.1'
            }
            }
        }
        }