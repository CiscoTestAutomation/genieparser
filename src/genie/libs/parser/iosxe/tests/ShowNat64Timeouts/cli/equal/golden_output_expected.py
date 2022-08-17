expected_output = {
    'nat64_timeout': {
        'all flows': {
            'cli_cfg': 'FALSE',
            'seconds': 86400,
            'uses_all': 'FALSE'
        },
        'bind': {
            'cli_cfg': 'FALSE',
            'seconds': 3600,
            'uses_all': 'TRUE'
        },
        'icmp': {
            'cli_cfg': 'FALSE',
            'seconds': 120,
            'uses_all': 'TRUE'
        },
        'tcp': {
            'cli_cfg': 'FALSE',
            'seconds': 7200,
            'uses_all': 'TRUE'
        },
        'tcp-transient': {
            'cli_cfg': 'FALSE',
            'seconds': 240,
            'uses_all': 'FALSE'
        },
        'udp': {
            'cli_cfg': 'FALSE',
            'seconds': 300,
            'uses_all': 'TRUE'
        }
    }
}
