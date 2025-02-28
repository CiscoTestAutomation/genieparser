expected_output = {
    'vrf': {
        'default': {
            'backup_paths': {
            },
            'best_paths': {
                'direct': 2,
                'discard': 2,
                'local': 3,
            },
            'num_routes_per_mask': {
                '/10': 1,
                '/112': 3,
                '/127': 1,
                '/128': 11,
                '/8': 1,
            },
            'total_paths': 17,
            'total_routes': 17,
        },
        'management': {
            'backup_paths': {
            },
            'best_paths': {
                'am': 1,
                'direct': 1,
                'discard': 2,
                'local': 2,
                'static': 1,
            },
            'num_routes_per_mask': {
                '/0': 1,
                '/10': 1,
                '/112': 1,
                '/127': 1,
                '/128': 2,
                '/8': 1,
            },
            'total_paths': 7,
            'total_routes': 7,
        },
    },
}
