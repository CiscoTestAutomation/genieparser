expected_output = {
    "system-users-information": {
        "uptime-information": {
            "active-user-count": {"#text": "3"},
            "date-time": {"#text": "9:38AM"},
            "load-average-1": "0.28",
            "load-average-15": "0.39",
            "load-average-5": "0.37",
            "up-time": {"#text": "209 days, 37 mins"},
            "user-table": {
                "user-entry": [
                    {
                        "command": "-cl",
                        "from": "10.1.0.1",
                        "idle-time": {"#text": "-"},
                        "login-time": {"#text": "2:35AM"},
                        "tty": "pts/0",
                        "user": "cisco",
                    },
                    {
                        "command": "-cl",
                        "from": "10.1.0.1",
                        "idle-time": {"#text": "56"},
                        "login-time": {"#text": "8:31AM"},
                        "tty": "pts/1",
                        "user": "cisco",
                    },
                    {
                        "command": "-cl",
                        "from": "10.1.0.1",
                        "idle-time": {"#text": "3"},
                        "login-time": {"#text": "7:45AM"},
                        "tty": "pts/2",
                        "user": "cisco",
                    },
                ]
            },
        }
    }
}
