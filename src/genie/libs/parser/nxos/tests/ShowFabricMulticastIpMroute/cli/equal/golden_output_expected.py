

expected_output = {
 "multicast": {
        "vrf": {
            "default": {
                'vnid': '0',
              },
            "vxlan-1001": {
                "address_family": {
                    "ipv4": {
                        "fabric_mroutes": {
                              "gaddr": {
                                  "227.1.1.1/32": {
                                     "grp_len": 32,
                                     "saddr": {
                                         "*": {
                                             "uptime": "22:15:41",
                                             "interested_fabric_nodes": {
                                                 "This node": {
                                                     "uptime": "22:15:41",
                                                     "rpfneighbor": "102.1.1.1",
                                             }
                                         }
                                     }
                                  }
                                  },
                                  "225.4.1.1/32": {
                                     "grp_len": 32,
                                     "saddr": {
                                         "181.1.11.44/32": {
                                              "src_len": 32,
                                              "uptime": "22:15:41",
                                              "rd_rt_ext_vri": "0b 64 64 64 04 03 e9 00 01 5a 5a 5a 04 00 03 e8 03 00 00",
                                              "interested_fabric_nodes": {
                                                   "This node": {
                                                       "uptime": "22:15:41",
                                                       "rpfneighbor": "100.100.100.4",
                                              }
                                        }
                                     }
                                  }
                                 }

                             }
                        }
                    }
               },
                "vnid": '201001'
            },
            "vxlan-1002": {

                "address_family": {
                    "ipv4": {
                        "fabric_mroutes": {
                            "gaddr": {
                                "227.1.1.1/32": {
                                    "grp_len": 32,
                                    "saddr": {
                                        "*": {
                                            "uptime": "22:15:41",
                                            "interested_fabric_nodes": {
                                                "100.100.100.2": {
                                                    "uptime": "22:15:41",
                                                    "rpfneighbor": "102.1.1.1",
                                                    "loc": "core"
                                                }
                                            }
                                        }
                                    }
                                },
                                "225.4.1.1/32": {
                                    "grp_len": 32,
                                    "saddr": {
                                        "181.1.11.44/32": {
                                            "src_len": 32,
                                            "uptime": "22:15:41",
                                            "rd_rt_ext_vri": "0b 64 64 64 04 03 e9 00 01 5a 5a 5a 04 00 03 e8 03 00 00",
                                            "interested_fabric_nodes": {
                                                "100.100.100.2": {
                                                    "uptime": "22:15:41",
                                                    "rpfneighbor": "100.100.100.4",
                                                    "loc": "fabric",
                                                }
                                            }
                                        }
                                    }
                                }

                            }
                        }
                    }
                },
                "vnid": '201002'
            }
        }
    }
}
