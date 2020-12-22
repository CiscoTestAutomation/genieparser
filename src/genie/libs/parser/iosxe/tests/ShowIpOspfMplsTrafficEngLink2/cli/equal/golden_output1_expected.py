expected_output = {
       "address_family":{
          "ipv4":{
             "instance":{
                "1":{
                   "mpls":{
                      "te":{
                         "router_id":"10.4.1.1"
                      }
                   },
                   "areas":{
                      "0.0.0.0":{
                         "mpls":{
                            "te":{
                               "enable":True,
                               "total_links":2,
                               "area_instance":2,
                               "link_hash_bucket":{
                                  8:{
                                     "link_fragments":{
                                        2:{
                                           "link_instance":2,
                                           "network_type":"broadcast network",
                                           "link_id":"10.1.2.1",
                                           "interface_address":"10.1.2.1",
                                           "te_admin_metric":1,
                                           "igp_admin_metric":1,
                                           "max_bandwidth":125000000,
                                           "max_reservable_bandwidth":93750000,
                                           "total_priority":8,
                                           "unreserved_bandwidths":{
                                              "0 93750000":{
                                                 "priority":0,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "1 93750000":{
                                                 "priority":1,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "2 93750000":{
                                                 "priority":2,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "3 93750000":{
                                                 "priority":3,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "4 93750000":{
                                                 "priority":4,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "5 93750000":{
                                                 "priority":5,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "6 93750000":{
                                                 "priority":6,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "7 93750000":{
                                                 "priority":7,
                                                 "unreserved_bandwidth":93750000
                                              }
                                           },
                                           "affinity_bit":"0x0"
                                        }
                                     }
                                  },
                                  9:{
                                     "link_fragments":{
                                        1:{
                                           "link_instance":2,
                                           "network_type":"broadcast network",
                                           "link_id":"10.1.4.4",
                                           "interface_address":"10.1.4.1",
                                           "te_admin_metric":1,
                                           "igp_admin_metric":1,
                                           "max_bandwidth":125000000,
                                           "max_reservable_bandwidth":93750000,
                                           "total_priority":8,
                                           "unreserved_bandwidths":{
                                              "0 93750000":{
                                                 "priority":0,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "1 93750000":{
                                                 "priority":1,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "2 93750000":{
                                                 "priority":2,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "3 93750000":{
                                                 "priority":3,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "4 93750000":{
                                                 "priority":4,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "5 93750000":{
                                                 "priority":5,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "6 93750000":{
                                                 "priority":6,
                                                 "unreserved_bandwidth":93750000
                                              },
                                              "7 93750000":{
                                                 "priority":7,
                                                 "unreserved_bandwidth":93750000
                                              }
                                           },
                                           "affinity_bit":"0x0"
                                        }
                                     }
                                  }
                               }
                            }
                         }
                      }
                   }
                },
                "2":{
                   "mpls":{
                      "te":{
                         "router_id":"10.229.11.11"
                      }
                   },
                   "areas":{
                      "0.0.0.1":{
                         "mpls":{
                            "te":{
                               "enable":False
                            }
                         }
                      }
                   }
                }
             }
          }
       }
    }