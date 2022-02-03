expected_output = {
   "vrf":{
      "default":{
         "address_family":{
            "ipv6":{
               "multicast_group":{
                  "FF05:1:1::1":{
                     "source_address":{
                        "2001:192:168:1::10":{
                           "egress_interface_list":{
                              "LISP0.1-100.154.154.154":{
                                 "egress_flags":"F ",
                                 "egress_next_hop":"100.154.154.154"
                              },
                              "LISP0.1-100.22.22.22":{
                                 "egress_flags":"F ",
                                 "egress_next_hop":"100.22.22.22"
                              },
                              "LISP0.1-100.33.33.33":{
                                 "egress_flags":"F ",
                                 "egress_next_hop":"100.33.33.33"
                              },
                              "LISP0.1-100.88.88.88":{
                                 "egress_flags":"F ",
                                 "egress_next_hop":"100.88.88.88"
                              }
                           },
                           "flags":"",
                           "incoming_interface_list":{
                              "Vlan2001":{
                                 "ingress_flags":"A ""F"
                              }
                           },
                           "rpf_nbr":"2001:192:168:1::10"
                        }
                     }
                  }
               }
            }
         }
      }
   }
}
