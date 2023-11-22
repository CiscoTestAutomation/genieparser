expected_output={
   "vrf":{
      "default":{
         "address_family":{
            "ipv4":{
               "multicast_group":{
                  "225.1.1.2":{
                     "source_address":{
                        "192.168.7.10":{
                           "egress_interface_list":{
                              "LISP0.1-(100.11.11.11, 235.1.3.163)":{
                                 "egress_flags":"F ""NS ",
                                 "egress_next_hop":"(100.11.11.11, ""235.1.3.163)"
                              },
                              "Vlan2001":{
                                 "egress_flags":"F ""NS"
                              }
                           },
                           "flags":"",
                           "incoming_interface_list":{
                              "Vlan2007":{
                                 "ingress_flags":"A"
                              }
                           },
                           "rpf_nbr":"0.0.0.0"
                        }
                     }
                  }
               }
            }
         }
      }
   }
}