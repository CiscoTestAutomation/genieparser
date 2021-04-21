expected_output = {
    "system-uptime-information": {
        "current-time": {"date-time": {"#text": "2021-01-06 12:31:48 EST"}},
        "system-booted-time": {
            "date-time": {"#text": "2020-12-22 12:27:02 EST"},
            "time-length": {"#text": "2w1d 00:04"},
        },
        "protocols-started-time": {
            "date-time": {"#text": "2020-12-22 12:28:48 EST"},
            "time-length": {"#text": "2w1d 00:03"},
        },
        "last-configured-time": {
            "user": "cisco",
            "date-time": {"#text": "2021-01-06 12:30:08 EST "},
            "time-length": {"#text": "00:01:40"},
        },
        "uptime-information": {
            "date-time": {"#text": "12:31PM"},
            "active-user-count": {"#text": "1"},
            "up-time": {"#text": "15 days, 5 mins", "@junos:seconds": "1296300"},
            "load-average-1": "0.07",
            "load-average-15": "0.09",
            "load-average-5": "0.04",
        },
    }
}
