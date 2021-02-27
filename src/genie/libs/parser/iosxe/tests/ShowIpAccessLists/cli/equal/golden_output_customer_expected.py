expected_output = {
   "43":{
      "name":"43",
      "type":"ipv4-acl-type",
      "acl_type": "standard",
      "aces":{
         "10":{
            "name":"10",
            "actions":{
               "forwarding":"permit"
            },
            "matches":{
               "l3":{
                  "ipv4":{
                     "protocol":"ipv4",
                     "source_network":{
                        "10.1.0.2 0.0.0.0":{
                           "source_network":"10.1.0.2 0.0.0.0"
                        }
                     }
                  }
               }
            },
            "statistics":{
               "matched_packets":"1168716"
            }
         },
         "20":{
            "name":"20",
            "actions":{
               "forwarding":"permit"
            },
            "matches":{
               "l3":{
                  "ipv4":{
                     "protocol":"ipv4",
                     "source_network":{
                        "10.144.0.9 0.0.0.0":{
                           "source_network":"10.144.0.9 0.0.0.0"
                        }
                     }
                  }
               }
            }
         },
         "30":{
            "name":"30",
            "actions":{
               "forwarding":"permit"
            },
            "matches":{
               "l3":{
                  "ipv4":{
                     "protocol":"ipv4",
                     "source_network":{
                        "10.70.10.0 0.0.10.255":{
                           "source_network":"10.70.10.0 0.0.10.255"
                        }
                     }
                  }
               }
            }
         },
         "40":{
            "name":"40",
            "actions":{
               "forwarding":"permit"
            },
            "matches":{
               "l3":{
                  "ipv4":{
                     "protocol":"ipv4",
                     "source_network":{
                        "10.196.0.0 0.0.255.255":{
                           "source_network":"10.196.0.0 0.0.255.255"
                        }
                     }
                  }
               }
            },
            "statistics":{
               "matched_packets":"8353358"
            }
         }
      }
   }
}