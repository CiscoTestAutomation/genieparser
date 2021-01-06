expected_output = {
    "system-users-information": {
        "uptime-information": {
            "active-user-count": {"#text": "2"},
            "date-time": {"#text": "11:36PM"},
            "load-average-1": "0.00",
            "load-average-15": "0.00",
            "load-average-5": "0.00",
            "up-time": {"#text": "2 days,  5 hrs"},
            "user-table": {
                "user-entry": [
                    {
                        "command": "-cli (cli)",
                        "from": "-",
                        "idle-time": {"#text": "2days"},
                        "login-time": {"#text": "Mon10PM"},
                        "tty": "d0",
                        "user": "cisco",
                    },
                    {
                        "command": "-cli (cli)",
                        "from": "255.255.255.255",
                        "idle-time": {"#text": "-"},
                        "login-time": {"#text": "11:36PM"},
                        "tty": "p0",
                        "user": "cisco",
                    },
                ]
            },
        }
    }
}
