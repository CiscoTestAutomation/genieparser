expected_output = {
    "system-storage-information": {
        "filesystem": [
            {
                "available-blocks": {"junos:format": "17G"},
                "filesystem-name": "/dev/gpt/junos",
                "mounted-on": "/.mount",
                "total-blocks": {"junos:format": "20G"},
                "used-blocks": {"junos:format": "1.2G"},
                "used-percent": "7%",
            },
            {
                "available-blocks": {"junos:format": "730M"},
                "filesystem-name": "/dev/gpt/config",
                "mounted-on": "/.mount/config",
                "total-blocks": {"junos:format": "793M"},
                "used-blocks": {"junos:format": "60K"},
                "used-percent": "0%",
            },
            {
                "available-blocks": {"junos:format": "6.3G"},
                "filesystem-name": "/dev/gpt/var",
                "mounted-on": "/.mount/var",
                "total-blocks": {"junos:format": "7.0G"},
                "used-blocks": {"junos:format": "117M"},
                "used-percent": "2%",
            },
            {
                "available-blocks": {"junos:format": "3.2G"},
                "filesystem-name": "tmpfs",
                "mounted-on": "/.mount/tmp",
                "total-blocks": {"junos:format": "3.2G"},
                "used-blocks": {"junos:format": "196K"},
                "used-percent": "0%",
            },
            {
                "available-blocks": {"junos:format": "333M"},
                "filesystem-name": "tmpfs",
                "mounted-on": "/.mount/mfs",
                "total-blocks": {"junos:format": "334M"},
                "used-blocks": {"junos:format": "748K"},
                "used-percent": "0%",
            },
        ]
    }
}
