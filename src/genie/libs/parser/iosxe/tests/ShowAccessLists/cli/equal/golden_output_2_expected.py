expected_output = {
   "1":{
      "name":"1",
      "type":"ipv4-acl-type",
      "acl_type": "standard",
      "aces":{
         "10":{
            "name":"10",
            "actions":{
               "forwarding":"deny",
               "logging":"log-syslog"
            },
            "matches":{
               "l3":{
                  "ipv4":{
                     "protocol":"ipv4",
                     "source_network":{
                        "10.9.3.4 0.0.0.0":{
                           "source_network":"10.9.3.4 0.0.0.0"
                        }
                     }
                  }
               }
            },
            "statistics":{
               "matched_packets":"18"
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
                        "any":{
                           "source_network":"any"
                        }
                     }
                  }
               }
            },
            "statistics":{
               "matched_packets":"58"
            }
         }
      }
   },
   "meraki-fqdn-dns":{
      "name":"meraki-fqdn-dns",
      "type":"ipv4-acl-type",
      "acl_type": "extended",
   }
}