

expected_output = {
    "vrfs": {
        "default": {
             "groups_count": 2,
             "interface": {
                  "Ethernet2/1": {
                       "group": {
                            "ff30::2": {
                                 "source": {
                                      "2001:db8:0:abcd::2": {
                                           "last_reporter": "2001:db8:8404:907f::1",
                                           "expire": "never",
                                           "type": "static",
                                           "up_time": "00:26:28"
                                      }
                                 }
                            },
                            "fffe::2": {
                                 "last_reporter": "2001:db8:8404:907f::1",
                                 "expire": "never",
                                 "type": "static",
                                 "up_time": "00:26:05"
                            }
                       }
                  }
             }
        },
        "VRF1": {
             "groups_count": 2,
             "interface": {
                  "Ethernet2/2": {
                       "group": {
                            "ff30::2": {
                                 "source": {
                                      "2001:db8:0:abcd::2": {
                                           "last_reporter": "2001:db8:8404:751c::1",
                                           "expire": "never",
                                           "type": "static",
                                           "up_time": "00:25:49"
                                      }
                                 }
                            },
                            "fffe::2": {
                                 "last_reporter": "2001:db8:8404:751c::1",
                                 "expire": "never",
                                 "type": "static",
                                 "up_time": "00:25:49"
                            }
                       }
                  }
             }
        }
    }
}
