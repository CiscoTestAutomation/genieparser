

expected_output = {
 "multicast": {
        "vrf": {
            "default": {
                'vnid': '0',
              },
            "vxlan-1001": {
                "address_family": {
                    "ipv4": {
                        "sa_ad_routes": {
                              "gaddr": {
                                  "226.0.0.1/32": {
                                     "grp_len": 32,
                                     "saddr": {
                                         "1.1.11.3/32": {
                                             "src_len": 32,
                                             "uptime": "00:12:32",
                                             "interested_fabric_nodes": {
                                                 "This node": {
                                                     "uptime": "00:12:32",
                                                 },
                                                "100.100.100.4": {
                                                     "uptime": "00:12:32",
                                                 }

                                             }
                                        }
                                     }
                                  },
                                  "226.1.1.1/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                           "1.1.11.4/32": {
                                               "src_len": 32,
                                               "uptime": "00:12:32",
                                               "interested_fabric_nodes": {
                                                   "This node": {
                                                      "uptime": "00:12:32",
                                                   },
                                                   "100.100.100.4": {
                                                       "uptime": "00:12:32",
                                               }

                                            }
                                        }
                                    }
                                },
                            }
                         }
                    }
                },
                "vnid": '203001'
            },
        }
 }
}