expected_output = {
    "username": {
        "lab": {
            "privilege": 15,
            "password": {
                "type": 0,
                "password": "lab"
            }
        },
        "testuser1": {
            "password": {
                "type": 0,
                "password": "lab"
            }
        },
        "testuser2": {
            "common_criteria_policy": "Test-CC",
            "password": {
                "type": 0,
                "password": "password"
            }
        },
        "testuser3": {
            "secret": {
                "type": 9,
                "secret": "$9$DOm9h7QgsEREnU$.W5Hbwmwi0rqlw40XwiRSHABLSwg85DrRgKfIi8/hKM"
            }
        },
        "testuser4": {
            "onetime": True,
            "password": {
                "type": 0,
                "password": "password"
            }
        },
        "testuser5": {
            "common_criteria_policy": "Test-CC",
            "secret": {
                "type": 9,
                "secret": "$9$UuxZCcqGu2IgBU$teHrzSPJK5FgLH0YAnUezoA1JwaqGBcJI4Xb6c3S7tU"
            }
        },
        "testuser6": {
            "privilege": 15,
            "secret": {
                "type": 9,
                "secret": "$9$oNguEA9um9vRx.$MsDk0DOy1rzBjKAcySWdNjoKcA7GetG9YNnKOs8S67A"
            }
        },
        "testuser7": {
            "privilege": 3,
            "nopassword": True
        },
        "testuser8": {
            "privilege": 15,
            "common_criteria_policy": "Test-CC",
            "secret": {
                "type": 9,
                "secret": "$9$oNguEA9um9vRx.$MsDk0DOy1rzBjKAcySWdNjoKcA7GetG9YNnKOs8S67A"
            }
        },
        "testuser9": {
            "privilege": 15,
            "secret": {
                "type": 9,
                "secret": "$9$UuxZCcqGu2IgBU$teHrzSPJK5FgLH0YAnUezoA1JwaqGBcJI4Xb6c3S7tU"
            },
            "autocommand": "show ip bgp summary"
        },
        "testuser10": {
            "privilege": 15,
            "common_criteria_policy": "Test-CC",
            "password": {
                "type": 0,
                "password": "lab"
            }
        },
        "testuser11": {
            "privilege": 15
        }
    }
}
