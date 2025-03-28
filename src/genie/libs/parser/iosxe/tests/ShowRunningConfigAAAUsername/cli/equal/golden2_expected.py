expected_output = {
    "username": {
        "testuser07": {
            "nopassword": True,
            "privilege": 3
        },
        "testuser08": {
            "common_criteria_policy": "Test-CC",
            "privilege": 15,
            "secret": {
                "secret": "$9$oNguEA9um9vRx.$MsDk0DOy1rzBjKAcySWdNjoKcA7GetG9YNnKOs8S67A",
                "type": 9
            }
        },
        "testuser09": {
            "autocommand": "show ip bgp summary",
            "privilege": 15,
            "secret": {
                "secret": "$9$UuxZCcqGu2IgBU$teHrzSPJK5FgLH0YAnUezoA1JwaqGBcJI4Xb6c3S7tU",
                "type": 9
            }
        },
        "testuser10": {
            "common_criteria_policy": "Test-CC",
            "password": {
                "password": "lab",
                "type": 0
            },
            "privilege": 15
        },
        "testuser11": {
            "privilege": 15
        }
    }
}
