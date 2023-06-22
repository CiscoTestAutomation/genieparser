expected_output = {
    'bridge_domain': 11,
    'flood_list_info': {
        'olist': 1,
        'ports': 4,
    },
    'ip_multicast_prefix_table_size': 0,
    'port_info': {
        'Et0/1:11': {
            'description': 'Et0/1:11',
            'description_values': {
                'interface': 'Et0/1',
                'service_instance': 11,
            },
            'is_pathlist': False,
            'type': 'BD_PORT',
        },
        'Et0/2:11': {
            'description': 'Et0/2:11',
            'description_values': {
                'interface': 'Et0/2',
                'service_instance': 11,
            },
            'is_pathlist': False,
            'type': 'BD_PORT',
        },
        '[IR]20011:ABCD:2::2': {
            'description': '[IR]20011:ABCD:2::2',
            'description_values': {
                'address': 'ABCD:2::2',
                'port': 20011,
                'type': 'IR',
            },
            'is_pathlist': True,
            'path_list_count': 1,
            'path_list_id': 6,
            'path_list_type': 'VXLAN_REP',
            'type': 'VXLAN_REP',
        },
        '[IR]20011:ABCD:3::2': {
            'description': '[IR]20011:ABCD:3::2',
            'description_values': {
                'address': 'ABCD:3::2',
                'port': 20011,
                'type': 'IR',
            },
            'is_pathlist': True,
            'path_list_count': 1,
            'path_list_id': 2,
            'path_list_type': 'VXLAN_REP',
            'type': 'VXLAN_REP',
        },
    },
    'reference_count': 11,
    'replication_ports_count': 4,
    'unicast_addr_table_info': {
        'aabb.0000.0021': {
            'is_pathlist': True,
            'type': 'VXLAN_UC',
            'unicast_path_list': {
                'unicast_description': '[MAC]20011:ABCD:2::2',
                'unicast_description_values': {
                    'address': 'ABCD:2::2',
                    'port': 20011,
                    'type': 'MAC',
                },
                'unicast_id': 4,
                'unicast_path_count': 1,
                'unicast_type': 'VXLAN_UC',
            },
        },
        'aabb.0000.0031': {
            'is_pathlist': True,
            'type': 'VXLAN_UC',
            'unicast_path_list': {
                'unicast_description': '[MAC]20011:ABCD:3::2',
                'unicast_description_values': {
                    'address': 'ABCD:3::2',
                    'port': 20011,
                    'type': 'MAC',
                },
                'unicast_id': 1,
                'unicast_path_count': 1,
                'unicast_type': 'VXLAN_UC',
            },
        },
    },
    'unicast_addr_table_size': 2,
}
