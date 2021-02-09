expected_output = {
    "system-uptime-information": {
        "current-time": {"date-time": {"#text": "2020-03-25 09:38:14 UTC"}},
        "last-configured-time": {
            "date-time": {"#text": "2020-03-05 16:04:34 UTC "},
            "time-length": {"#text": "2w5d 17:33"},
            "user": "cisco",
        },
        "protocols-started-time": {
            "date-time": {"#text": "2019-08-29 09:03:25 UTC"},
            "time-length": {"#text": "29w6d 00:34"},
        },
        "system-booted-time": {
            "date-time": {"#text": "2019-08-29 09:02:22 UTC"},
            "time-length": {"#text": "29w6d 00:35"},
        },
        "time-source": "LOCAL CLOCK",
        "uptime-information": {
            "active-user-count": {"#text": "3"},
            "date-time": {"#text": "9:38AM"},
            "load-average-1": "0.29",
            "load-average-15": "0.41",
            "load-average-5": "0.38",
            "up-time": {"#text": "209 days, 36 mins", "@junos:seconds": "18059760"},
        },
    }
}
