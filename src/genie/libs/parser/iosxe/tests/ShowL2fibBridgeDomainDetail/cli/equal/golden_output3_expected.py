expected_output = {
    'bridge_domain': 101,
    'flood_list_info': {
        'olist': 9,
        'ports': 6,
    },
    'ip_multicast_prefix_table_info': {
        '224.0.0.0/24': {
            'adjacency': ' ',
            'group': '224.0.0.0/24',
            'iif': 'Null',
            'olist': 9,
            'port_count': 6,
            'source': '*',
        },
        '224.0.1.39': {
            'adjacency': ' ',
            'group': '224.0.1.39',
            'iif': 'Null',
            'olist': 9,
            'port_count': 6,
            'source': '*',
        },
        '224.0.1.40': {
            'adjacency': ' ',
            'group': '224.0.1.40',
            'iif': 'Null',
            'olist': 9,
            'port_count': 6,
            'source': '*',
        },
    },
    'ip_multicast_prefix_table_size': 3,
    'port_info': {
        'Et0/0:101': {
            'description': 'Et0/0:101',
            'description_values': {
                'interface': 'Et0/0',
                'service_instance': 101,
            },
            'is_pathlist': False,
            'type': 'BD_PORT',
        },
        'Et1/1:101': {
            'description': 'Et1/1:101',
            'description_values': {
                'interface': 'Et1/1',
                'service_instance': 101,
            },
            'is_pathlist': False,
            'type': 'BD_PORT',
        },
        '[IR]42@1.1.1.1': {
            'description': '[IR]42@1.1.1.1',
            'description_values': {
                'address': '1.1.1.1',
                'label': '42',
                'type': 'IR',
            },
            'is_pathlist': True,
            'path_list_count': 1,
            'path_list_id': 37,
            'path_list_type': 'MPLS_IR',
            'type': 'MPLS_IR',
        },
        '[IR]42@3.3.3.1': {
            'description': '[IR]42@3.3.3.1',
            'description_values': {
                'address': '3.3.3.1',
                'label': '42',
                'type': 'IR',
            },
            'is_pathlist': True,
            'path_list_count': 1,
            'path_list_id': 25,
            'path_list_type': 'MPLS_IR',
            'type': 'MPLS_IR',
        },
        '[IR]42@4.4.4.1': {
            'description': '[IR]42@4.4.4.1',
            'description_values': {
                'address': '4.4.4.1',
                'label': '42',
                'type': 'IR',
            },
            'is_pathlist': True,
            'path_list_count': 1,
            'path_list_id': 1,
            'path_list_type': 'MPLS_IR',
            'type': 'MPLS_IR',
        },
        '[IR]42@5.5.5.1': {
            'description': '[IR]42@5.5.5.1',
            'description_values': {
                'address': '5.5.5.1',
                'label': '42',
                'type': 'IR',
            },
            'is_pathlist': True,
            'path_list_count': 1,
            'path_list_id': 2,
            'path_list_type': 'MPLS_IR',
            'type': 'MPLS_IR',
        },
    },
    'reference_count': 16,
    'replication_ports_count': 6,
    'unicast_addr_table_info': {
        'ffff.ffff.fffd': {
            'is_pathlist': False,
            'type': 'Olist',
            'unicast_path_list': {
                'output_list_id': 11,
                'ports': 2,
            },
        },
        'ffff.ffff.fffe': {
            'is_pathlist': False,
            'type': 'Olist',
            'unicast_path_list': {
                'output_list_id': 10,
                'ports': 6,
            },
        },
    },
    'unicast_addr_table_size': 2,
}
