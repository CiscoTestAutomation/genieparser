expected_output = {
    "system-uptime-information": {
        "current-time": {"date-time": {"#text": "2020-03-26 08:16:41 UTC"}},
        "last-configured-time": {
            "date-time": {"#text": "2020-03-05 16:04:34 UTC "},
            "time-length": {"#text": "2w6d 16:12"},
            "user": "cisco",
        },
        "protocols-started-time": {
            "date-time": {"#text": "2019-08-29 09:03:25 UTC"},
            "time-length": {"#text": "29w6d 23:13"},
        },
        "system-booted-time": {
            "date-time": {"#text": "2019-08-29 09:02:22 UTC"},
            "time-length": {"#text": "29w6d 23:14"},
        },
        "time-source": "LOCAL CLOCK",
        "uptime-information": {
            "active-user-count": {"#text": "5"},
            "date-time": {"#text": "8:16AM"},
            "load-average-1": "0.43",
            "load-average-15": "0.43",
            "load-average-5": "0.42",
            "up-time": {"#text": "209 days, 23:14 mins,", "@junos:seconds": "18141240"},
        },
    }
}
