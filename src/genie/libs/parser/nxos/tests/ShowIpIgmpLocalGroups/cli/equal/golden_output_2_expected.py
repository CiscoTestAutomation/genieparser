

expected_output = {
    "vrfs": {
        "VRF1": {
             "interface": {
                  "Ethernet2/4": {
                       "join_group": {
                            "239.1.1.1 *": {
                                 "source": "*",
                                 "group": "239.1.1.1"
                            },
                            "239.3.3.3 10.4.1.1": {
                                 "source": "10.4.1.1",
                                 "group": "239.3.3.3"
                            },
                            "239.2.2.2 *": {
                                 "source": "*",
                                 "group": "239.2.2.2"
                            },
                            "239.4.4.4 10.4.1.2": {
                                 "source": "10.4.1.2",
                                 "group": "239.4.4.4"
                            }
                       },
                       "static_group": {
                            "239.5.5.5 *": {
                                 "source": "*",
                                 "group": "239.5.5.5"
                            },
                            "239.8.8.8 10.16.2.2": {
                                 "source": "10.16.2.2",
                                 "group": "239.8.8.8"
                            },
                            "239.6.6.6 *": {
                                 "source": "*",
                                 "group": "239.6.6.6"
                            },
                            "239.7.7.7 10.16.2.1": {
                                 "source": "10.16.2.1",
                                 "group": "239.7.7.7"
                            }
                       },
                       "group": {
                            "239.1.1.1": {
                                 "last_reporter": "00:00:50",
                                 "type": "local"
                            },
                            "239.8.8.8": {
                                 "source": {
                                      "10.16.2.2": {
                                           "last_reporter": "01:06:47",
                                           "type": "static"
                                      }
                                 },
                            },
                            "239.2.2.2": {
                                 "last_reporter": "00:00:54",
                                 "type": "local"
                            },
                            "239.4.4.4": {
                                 "source": {
                                      "10.4.1.2": {
                                           "last_reporter": "00:00:55",
                                           "type": "local"
                                      }
                                 },
                            },
                            "239.6.6.6": {
                                 "last_reporter": "01:06:47",
                                 "type": "static"
                            },
                            "239.5.5.5": {
                                 "last_reporter": "01:06:47",
                                 "type": "static"
                            },
                            "239.3.3.3": {
                                 "source": {
                                      "10.4.1.1": {
                                           "last_reporter": "00:01:01",
                                           "type": "local"
                                      }
                                 },
                            },
                            "239.7.7.7": {
                                 "source": {
                                      "10.16.2.1": {
                                           "last_reporter": "01:06:47",
                                           "type": "static"
                                      }
                                 },
                            }}}}}}
}
