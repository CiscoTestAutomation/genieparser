expected_output = {
    "system-uptime-information": {
        "current-time": {"date-time": {"#text": "2020-08-13 14:08:16 UTC"}},
        "last-configured-time": {
            "date-time": {"#text": "2020-08-13 14:08:16 UTC "},
            "time-length": {"#text": "00:00:00"},
            "user": "genie",
        },
        "protocols-started-time": {
            "date-time": {"#text": "2020-08-13 13:37:06 UTC"},
            "time-length": {"#text": "00:31:10"},
        },
        "system-booted-time": {
            "date-time": {"#text": "2020-08-13 03:05:11 UTC"},
            "time-length": {"#text": "11:03:05"},
        },
        "time-source": "LOCAL CLOCK",
        "uptime-information": {
            "active-user-count": {"#text": "1"},
            "date-time": {"#text": "2:08PM"},
            "load-average-1": "0.31",
            "load-average-15": "0.48",
            "load-average-5": "0.50",
            "up-time": {"#text": "11:03 mins,", "@junos:seconds": "39780"},
        },
    }
}
