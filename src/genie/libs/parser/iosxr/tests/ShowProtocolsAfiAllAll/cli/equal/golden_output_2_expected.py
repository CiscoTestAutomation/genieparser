

expected_output = {
    "protocols": {
          "ospf": {
               "vrf": {
                    "default": {
                         "address_family": {
                              "ipv4": {
                                   "instance": {
                                        "1": {
                                             "preference": {
                                                  "single_value": {
                                                       "all": 110
                                                  }
                                             },
                                             "router_id": "192.168.205.1",
                                             "nsf": True,
                                             "areas": {
                                                  "0.0.0.1": {
                                                       "mpls": {
                                                            "te": {
                                                                 "enable": True
                                                            }
                                                       },
                                                       "interfaces": [
                                                            "Loopback5"
                                                       ]
                                                  },
                                                  "0.0.0.0": {
                                                       "interfaces": [
                                                            "Loopback0"
                                                       ]
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    }
               }
          },
          "ospfv3": {
               "vrf": {
                    "default": {
                         "address_family": {
                              "ipv4": {
                                   "instance": {
                                        "1": {
                                             "preference": {
                                                  "single_value": {
                                                       "all": 110
                                                  }
                                             },
                                             "router_id": "0.0.0.0"
                                        }
                                   }
                              }
                         }
                    }
               }
          },
          "bgp": {
               "bgp_pid": 100,
               "nsr": {
                    "enable": True,
                    "current_state": "tcp initial sync"
               },
               "address_family": {
                    "vpnv6 unicast": {
                         "distance": {
                              "internal": 200,
                              "local": 200,
                              "external": 20
                         }
                    },
                    "vpnv4 unicast": {
                         "distance": {
                              "internal": 200,
                              "local": 200,
                              "external": 20
                         }
                    }
               }
          }
     }
 }
