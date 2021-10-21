

expected_output = {
    "vrf": {
          "default": {
               "address_family": {
                    "l2vpn evpn": {
                         "dampening_enabled": True,
                         "route_identifier": {
                              "10.16.2.101:1002": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 4,
                                   "history_paths": 0
                              },
                              "101:1000": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 4,
                                   "history_paths": 0
                              },
                              "101:10001": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 4,
                                   "history_paths": 0
                              },
                              "101:1001": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 4,
                                   "history_paths": 0
                              },
                              "201:2000": {
                                   "dampening_enabled": True,
                                   "network": {
                                        "[2]:[0]:[0]:[48]:[0201.02ff.0303]:[32]:[10.81.1.2]/248": {
                                             "duration": "00:20:58",
                                             "peer": "10.106.102.3",
                                             "best": False,
                                             "suppress_limit": 30,
                                             "pathtype": "e",
                                             "status": "d",
                                             "current_penalty": 35,
                                             "flaps": 84,
                                             "reuse_limit": 10,
                                             "reuse_time": "00:01:50"
                                        },
                                        "[5]:[0]:[0]:[24]:[10.100.1.0]:[0.0.0.0]/224": {
                                             "duration": "00:20:58",
                                             "peer": "10.106.102.3",
                                             "best": False,
                                             "suppress_limit": 30,
                                             "pathtype": "e",
                                             "status": "d",
                                             "current_penalty": 35,
                                             "flaps": 84,
                                             "reuse_limit": 10,
                                             "reuse_time": "00:01:50"
                                        },
                                        "[5]:[0]:[0]:[24]:[10.100.2.0]:[0.0.0.0]/224": {
                                             "duration": "00:20:58",
                                             "peer": "10.106.102.3",
                                             "best": False,
                                             "suppress_limit": 30,
                                             "pathtype": "e",
                                             "status": "d",
                                             "current_penalty": 35,
                                             "flaps": 84,
                                             "reuse_limit": 10,
                                             "reuse_time": "00:01:50"
                                        },
                                        "[2]:[0]:[0]:[48]:[0201.02ff.0302]:[32]:[10.81.1.1]/248": {
                                             "duration": "00:20:58",
                                             "peer": "10.106.102.3",
                                             "best": False,
                                             "suppress_limit": 30,
                                             "pathtype": "e",
                                             "status": "d",
                                             "current_penalty": 35,
                                             "flaps": 84,
                                             "reuse_limit": 10,
                                             "reuse_time": "00:01:50"
                                        }
                                   },
                                   "dampened_paths": 4,
                                   "history_paths": 0
                              }
                         },
                         "dampened_paths": 4,
                         "history_paths": 0
                    },
                    "ipv6 multicast": {
                         "dampening_enabled": True,
                         "network": {
                              "2001:db8:961::/112": {
                                   "duration": "00:21:00",
                                   "peer": "2001:db8:8d82::2002",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 34,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              },
                              "2001:db8:961::1:0/112": {
                                   "duration": "00:21:00",
                                   "peer": "2001:db8:8d82::2002",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 34,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              }
                         },
                         "dampened_paths": 2,
                         "history_paths": 0
                    },
                    "vpnv4 unicast": {
                         "dampening_enabled": True,
                         "route_identifier": {
                              "101:100": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 2,
                                   "history_paths": 0
                              },
                              "0:0": {
                                   "dampening_enabled": True,
                                   "network": {
                                        "10.25.2.0/24": {
                                             "duration": "00:20:58",
                                             "peer": "10.106.102.3",
                                             "best": False,
                                             "suppress_limit": 30,
                                             "pathtype": "e",
                                             "status": "d",
                                             "current_penalty": 35,
                                             "flaps": 84,
                                             "reuse_limit": 10,
                                             "reuse_time": "00:01:50"
                                        },
                                        "10.25.1.0/24": {
                                             "duration": "00:20:58",
                                             "peer": "10.106.102.3",
                                             "best": False,
                                             "suppress_limit": 30,
                                             "pathtype": "e",
                                             "status": "d",
                                             "current_penalty": 35,
                                             "flaps": 84,
                                             "reuse_limit": 10,
                                             "reuse_time": "00:01:50"
                                        }
                                   },
                                   "dampened_paths": 2,
                                   "history_paths": 0
                              },
                              "102:100": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 2,
                                   "history_paths": 0
                              }
                         },
                         "dampened_paths": 2,
                         "history_paths": 0
                    },
                    "ipv6 unicast": {
                         "dampening_enabled": True,
                         "network": {
                              "2001::/112": {
                                   "duration": "00:21:00",
                                   "peer": "2001:db8:8d82::2002",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 34,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              },
                              "2001::1:0/112": {
                                   "duration": "00:21:00",
                                   "peer": "2001:db8:8d82::2002",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 34,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              }
                         },
                         "dampened_paths": 2,
                         "history_paths": 0
                    },
                    "ipv4 multicast": {
                         "dampening_enabled": True,
                         "network": {
                              "10.9.1.0/24": {
                                   "duration": "00:20:58",
                                   "peer": "10.106.102.3",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 35,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              },
                              "10.9.0.0/24": {
                                   "duration": "00:20:58",
                                   "peer": "10.106.102.3",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 35,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              }
                         },
                         "dampened_paths": 2,
                         "history_paths": 0
                    },
                    "ipv4 unicast": {
                         "dampening_enabled": True,
                         "network": {
                              "10.4.0.0/24": {
                                   "duration": "00:20:58",
                                   "peer": "10.106.102.3",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 35,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              },
                              "10.4.1.0/24": {
                                   "duration": "00:20:58",
                                   "peer": "10.106.102.3",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 35,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              }
                         },
                         "dampened_paths": 2,
                         "history_paths": 0
                    },
                    "vpnv6 unicast": {
                         "dampening_enabled": True,
                         "route_identifier": {
                              "0xbb00010000000000": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 0,
                                   "history_paths": 0
                              },
                              "100:200": {
                                   "dampening_enabled": True,
                                   "dampened_paths": 0,
                                   "history_paths": 0
                              }
                         },
                         "dampened_paths": 0,
                         "history_paths": 0
                    },
                    "link-state": {
                         "dampening_enabled": True,
                         "network": {
                              "[2]:[77][7,0][10.219.39.39,1,656877351][10.70.1.1,22][10.106.102.3,10.246.1.30]/616": {
                                   "duration": "00:20:58",
                                   "peer": "10.106.102.3",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 35,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              },
                              "[2]:[77][7,0][10.219.39.39,2,656877351][10.70.1.1,22][10.106.102.3,10.246.1.31]/616": {
                                   "duration": "00:20:58",
                                   "peer": "10.106.102.3",
                                   "best": False,
                                   "suppress_limit": 30,
                                   "pathtype": "e",
                                   "status": "d",
                                   "current_penalty": 35,
                                   "flaps": 84,
                                   "reuse_limit": 10,
                                   "reuse_time": "00:01:50"
                              }
                         },
                         "dampened_paths": 2,
                         "history_paths": 0
                    }}}}}
