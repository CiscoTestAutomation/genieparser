expected_output = {
    'group_members': {
        12345: {
            'members': {
                1: {
                    'l2_dest_gid': 54321,
                    'l2_dest_type': 'DENSE_AC',
                    'l3_port_type': 'NONE',
                    'member_gid': 0,
                    'next_hop_gid': 0,
                    'stack_port_oid': 0,
                    'sysport_gid': 128,
                    'type': 'L3_AC',
                },
                2: {
                    'l2_dest_gid': 0,
                    'l2_dest_type': 'NONE',
                    'l3_port_type': 'NONE',
                    'member_gid': 65535,
                    'next_hop_gid': 0,
                    'stack_port_oid': 0,
                    'sysport_gid': 0,
                    'type': 'L3_MCG',
                },
            },
        },
    },
}