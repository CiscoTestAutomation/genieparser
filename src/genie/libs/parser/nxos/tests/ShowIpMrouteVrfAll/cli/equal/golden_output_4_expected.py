

expected_output = {
    "vrf":{
       "default":{
          "address_family":{
             "ipv4":{
                "multicast_group":{
                   "225.1.0.1/32":{
                      "source_address":{
                         "10.234.1.2/32":{
                            "uptime":"00:22:11",
                            "flags":"ip mrib pim",
                            "incoming_interface_list":{
                               "Ethernet1/9":{
                                  "rpf_nbr":"10.234.1.2",
                                  "internal":True
                               }
                            },
                            "oil_count":3,
                            "outgoing_interface_list":{
                               "port-channel12":{
                                  "oil_uptime":"00:10:13",
                                  "oil_flags":"pim"
                               },
                               "Vlan30":{
                                  "oil_uptime":"00:21:53",
                                  "oil_flags":"mrib"
                               },
                               "Vlan200":{
                                  "oil_uptime":"03:01:01",
                                  "oil_flags":"mrib",
                                  "flag":"bridge-only"
                               },
                               "Ethernet1/11":{
                                  "oil_uptime":"00:22:00",
                                  "oil_flags":"mrib"
                               }
                            }
                         }
                      }
                   }
                }
             }
          }
       }
    }
}
