expected_output = {
   "instance":{
      "default":{
         "interface":{
            "Bundle-Ether10":{
               "state":"Enabled",
               "adjacency_formation":"Enabled",
               "prefix_advertisement":"Enabled",
               "ipv4_bfd":False,
               "ipv6_bfd":False,
               "bfd_min_interval":100,
               "bfd_multiplier":3,
               "rsi_srlg":"Registered",
               "bandwidth":2000000,
               "total_bandwidth":2000000,
               "circuit_type":"level-2-only",
               "media_type":"P2P",
               "circuit_number":0,
               'measured_delay': {
                  'min': '-',
                  'avg': '-',
                  'max': '-'
               },
               'delay_normalization': {
                  'interval': 0,
                  'offset': 0
               },
               'normalized_delay': {
                  'min': '-',
                  'avg': '-',
                  'max': '-'
               },
               "link_loss":"-",
               "extended_circuit_number":0,
               "next_p2p_iih_in":4,
               "lsp_rexmit_queue_size":0,
               "level":{
                  2:{
                    "adjacency_count":0,
                    "lsp_pacing_interval_ms":33,
                    "psnp_entry_queue_size":0,
                    "hello_interval_sec":10,
                    "hello_multiplier":3
                  }
               },
               "clns_io":{
                  "protocol_state":"Up",
                  "mtu":1497,
                  "snpa":"5087.890d.27c4",
                  "layer2_mcast_groups_membership":{
                     "all_level_1_iss":"Yes",
                     "all_level_2_iss":"Yes"
                  }
               },
               "topology":{
                  "ipv4 unicast":{
                     "state":"Enabled",
                     "adjacency_formation":"Running",
                     "prefix_advertisement":"Running",
                     "metric":{
                        "level":{
                           1:0,
                           2:55
                        }
                     },
                     "metric_fallback":{
                        "bandwidth":{
                           "level":{
                              1:"Inactive",
                              2:"Inactive"
                           }
                        },
                        "anomaly":{
                           "level":{
                              1:"Inactive",
                              2:"Inactive"
                           }
                        }
                     },
                     "weight":{
                        "level":{
                           1:0,
                           2:0
                        }
                     },
                     "mpls":{
                        "mpls_max_label_stack":"1/3/10/10 (PRI/BKP/SRTE/SRAT)",
                        "ldp_sync":{
                           "level":{
                              1:"Enabled",
                              2:"Enabled"
                           },
                           "status":"Achieved"
                        }
                     },
                     "frr":{
                        "level":{
                           1:{
                            "state":"Not Enabled",
                            "type":"None"
                           },
                           2:{
                            "state":"Not Enabled",
                            "type":"None"
                           }
                        }
                     }
                  },
                  "ipv6 unicast":{
                     "state":"Enabled",
                     "adjacency_formation":"Running",
                     "prefix_advertisement":"Running",
                     "metric":{
                        "level":{
                           1:0,
                           2:55
                        }
                     },
                     "metric_fallback":{
                        "bandwidth":{
                           "level":{
                              1:"Inactive",
                              2:"Inactive"
                           }
                        },
                        "anomaly":{
                           "level":{
                              1:"Inactive",
                              2:"Inactive"
                           }
                        }
                     },
                     "weight":{
                        "level":{
                           1:0,
                           2:0
                        }
                     },
                     "mpls":{
                        "mpls_max_label_stack":"1/3/10/10 (PRI/BKP/SRTE/SRAT)",
                        "ldp_sync":{
                           "level":{
                              1:"Enabled",
                              2:"Enabled"
                           },
                           "status":"Not Achieved"
                        }
                     },
                     "frr":{
                        "level":{
                           1:{
                            "state":"Not Enabled",
                            "type":"None"
                           },
                           2:{
                            "state":"Not Enabled",
                            "type":"None"
                           }
                        }
                     }
                  }
               },
               "address_family":{
                  "IPv4":{
                     "state":"Enabled",
                     "protocol_state":"Up",
                     "forwarding_address":[
                        "1.1.1.1"
                     ],
                     "global_prefix":[
                        "1.1.1.0/24"
                     ]
                  },
                  "IPv6":{
                     "state":"Enabled",
                     "protocol_state":"Up",
                     "forwarding_address":[
                        "fe80::5287:89ff:fe0d:27c4"
                     ],
                     "global_prefix":[
                        "2001:506::/64"
                     ]
                  }
               },
               "lsp":{
                  "transmit_timer_expires_ms":0,
                  "transmission_state":"idle",
                  "lsp_transmit_back_to_back_limit_window_msec":0,
                  "lsp_transmit_back_to_back_limit":10
               },
               "underlying_interface":{
                  "GigabitEthernet0/0/0/10":{
                     "index":"0x2a"
                  },
                  "GigabitEthernet0/0/0/6":{
                     "index":"0x26"
                  }
               }
            }
         }
      }
   }
}