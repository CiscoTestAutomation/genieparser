expected_output = {
    'oce': {
        'adjacency': {
            'adj_flag_2': True,
            'adj_flags': '0x0000',
            'adj_gre': True,
            'adj_type': 'IPV4 Adjacency',
            'encap': '45 00 00 00 00 00 00 00 ff 11 ed 5e 63 63 03 64 63 63 04 64 12 b5 12 b5 00 00 00 00',
            'encap_len': 28,
            'fixup_flags': '0x0001',
            'fixup_flags_2': '0xd0000',
            'interface_name': 'Tunnel0',
            'l3_mtu': 9216,
            'lisp_fixup_hw_ptr': '0x4966a3a0',
            'next_hop_address': '99.99.4.100',
            'next_hw_oce_ptr': '00000000',
            'number_of_children': 0,
            'output_uidb': 262090
            },
        'evpn_encap_oce': {
            'atom_flags': '0000',
            'efi_name': 'nve1.VNI301700',
            'flags': '0x02',
            'next_hop': '99.99.4.100',
            'next_hw_oce_ptr': '0x4a2bffe0',
            'number_of_children': 1
            },
        'vxlan_header_oce': {
            'encap_str': '8000000 6212400',
            'next_hw_oce_ptr': '0x49700740',
            'number_of_children': 1
            }
        }
}
