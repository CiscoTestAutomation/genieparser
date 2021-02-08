expected_output = {
    'lsps': {
        'mlx8.1_to_ces.2': {
            'destination': '1.1.1.1',
            'admin': 'UP',
            'operational': 'UP',
            'flap_count': 1,
            'retry_count': 0,
            'tunnel_interface': 'tunnel0'
        },
        'mlx8.1_to_ces.1': {
            'destination': '2.2.2.2',
            'admin': 'UP',
            'operational': 'UP',
            'flap_count': 1,
            'retry_count': 0,
            'tunnel_interface': 'tunnel56'
        },
        'mlx8.1_to_mlx8.2': {
            'destination': '3.3.3.3',
            'admin': 'UP',
            'operational': 'UP',
            'flap_count': 1,
            'retry_count': 0,
            'tunnel_interface': 'tunnel63'
        },
        'mlx8.1_to_mlx8.3': {
            'destination': '4.4.4.4',
            'admin': 'DOWN',
            'operational': 'DOWN',
            'flap_count': 0,
            'retry_count': 0
        }
    }
}
