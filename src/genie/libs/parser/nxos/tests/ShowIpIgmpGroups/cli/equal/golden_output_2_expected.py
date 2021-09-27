

expected_output = {
    "vrfs": {
        "default": {
             "interface": {
                  "Ethernet2/1": {
                       "group": {
                            "239.6.6.6": {
                                 "expire": "never",
                                 "type": "S",
                                 "last_reporter": "10.1.2.1",
                                 "up_time": "00:20:53"
                            },
                            "239.8.8.8": {
                                 "source": {
                                      "10.16.2.2": {
                                           "expire": "never",
                                           "type": "S",
                                           "last_reporter": "10.1.2.1",
                                           "up_time": "00:20:34"
                                      }
                                 },
                            },
                            "239.5.5.5": {
                                 "expire": "never",
                                 "type": "S",
                                 "last_reporter": "10.1.2.1",
                                 "up_time": "00:21:00"
                            },
                            "239.7.7.7": {
                                 "source": {
                                      "10.16.2.1": {
                                           "expire": "never",
                                           "type": "S",
                                           "last_reporter": "10.1.2.1",
                                           "up_time": "00:20:42"
                                      }
                                 },
                            }
                       }
                  }
             },
             "total_entries": 4
        }
    }
}
