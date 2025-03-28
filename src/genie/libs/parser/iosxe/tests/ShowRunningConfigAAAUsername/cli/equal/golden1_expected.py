expected_output = {
    'username': {
        'lab': {
            'password': {
                'password': 'lab',
                'type': 0
            },
            'privilege': 15
        },
        'testuser1': {
            'password': {
                'password': 'lab',
                'type': 0
            }
        },
        'testuser2': {
            'common_criteria_policy': 'Test-CC',
            'password': {
                'password': 'password', 'type': 0
            }
        },
        'testuser3': {
            'secret': {
                'secret': '$9$DOm9h7QgsEREnU$.W5Hbwmwi0rqlw40XwiRSHABLSwg85DrRgKfIi8/hKM',
                'type': 9
            }
        },
        'testuser4': {
            'onetime': True,
            'password': {
                'password': 'password',
                'type': 0
            }
        },
        'testuser5': {
            'common_criteria_policy': 'Test-CC',
            'secret': {
                'secret': '$9$UuxZCcqGu2IgBU$teHrzSPJK5FgLH0YAnUezoA1JwaqGBcJI4Xb6c3S7tU',
                'type': 9
            }
        },
        'testuser6': {
            'privilege': 15,
            'secret': {
                'secret': '$9$oNguEA9um9vRx.$MsDk0DOy1rzBjKAcySWdNjoKcA7GetG9YNnKOs8S67A',
                'type': 9
            }
        }
    }
}
