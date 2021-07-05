expected_output = {
    "key_chains": {
        "bla": {
            "keys": {
                1: {
                    "accept_lifetime": {
                        "end": "always valid",
                        "is_valid": True,
                        "start": "always valid",
                    },
                    "key_string": "cisco123",
                    "send_lifetime": {
                        "end": "always valid",
                        "is_valid": True,
                        "start": "always valid",
                    },
                },
                2: {
                    "accept_lifetime": {
                        "end": "06:01:00 UTC Jan 1 2010",
                        "is_valid": False,
                        "start": "10:10:10 UTC Jan 1 2002",
                    },
                    "key_string": "blabla",
                    "send_lifetime": {
                        "end": "06:01:00 UTC Jan 1 2010",
                        "is_valid": False,
                        "start": "10:10:10 UTC Jan 1 2002",
                    },
                },
            },
        },
        "cisco": {
            "keys": {
                1: {
                    "accept_lifetime": {
                        "end": "infinite",
                        "is_valid": True,
                        "start": "11:11:11 UTC Mar 1 2001",
                    },
                    "key_string": "cisco123",
                    "send_lifetime": {
                        "end": "infinite",
                        "is_valid": True,
                        "start": "11:11:11 UTC Mar 1 2001",
                    },
                },
                2: {
                    "accept_lifetime": {
                        "end": "22:11:11 UTC Dec 20 2030",
                        "is_valid": True,
                        "start": "11:22:11 UTC Jan 1 2001",
                    },
                    "key_string": "cisco234",
                    "send_lifetime": {
                        "end": "always valid",
                        "is_valid": True,
                        "start": "always valid",
                    },
                },
                3: {
                    "accept_lifetime": {
                        "end": "always valid",
                        "is_valid": True,
                        "start": "always valid",
                    },
                    "key_string": "cisco",
                    "send_lifetime": {
                        "end": "always valid",
                        "is_valid": True,
                        "start": "always valid",
                    },
                },
            },
        },
    },
}
