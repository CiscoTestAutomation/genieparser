

expected_output = {
'vrf': {
    'default': {
        'backup_paths': {
        },
        'best_paths': {
            'am': 1,
            'broadcast': 5,
            'bgp-100': 1000,
            'direct': 4,
            'local': 4,
            'ospf-1': 6,
            'ospf-2': 6,
        },
        'num_routes_per_mask': {
            '/24': 4,
            '/32': 12,
            '/8': 1,
        },
        'total_paths': 20,
        'total_routes': 17,
    },
    'evpn-tenant-0002': {
        'backup_paths': {
        },
        'best_paths': {
            'broadcast': 7,
            'direct': 2,
            'local': 2,
        },
        'num_routes_per_mask': {
            '/16': 2,
            '/32': 8,
            '/8': 1,
        },
        'total_paths': 11,
        'total_routes': 11,
    },
    'evpn-t-0003': {
        'backup_paths': {
        },
        'best_paths': {
            'broadcast': 7,
            'direct': 2,
            'local': 2,
        },
        'num_routes_per_mask': {
            '/16': 2,
            '/32': 8,
            '/8': 1,
        },
        'total_paths': 11,
        'total_routes': 11,
    },
    'management': {
        'backup_paths': {
        },
        'best_paths': {
            'am': 3,
            'broadcast': 5,
            'direct': 1,
            'local': 1,
            'static': 1,
        },
        'num_routes_per_mask': {
            '/0': 1,
            '/24': 1,
            '/32': 8,
            '/8': 1,
        },
        'total_paths': 11,
        'total_routes': 11,
    },
},
}
