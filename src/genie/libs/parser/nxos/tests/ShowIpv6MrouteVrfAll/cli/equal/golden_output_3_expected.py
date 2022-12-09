

expected_output = {
    "vrf":{
       "default":{
          "address_family":{
             "ipv6":{
                "multicast_group":{
                   "ff1e:1111::1:0/128":{
                      "source_address":{
                         "2001::222:1:1:1234/128":{
                            
                            "flags":"ipv6 m6rib pim6",
                            "incoming_interface_list":{
                               "Ethernet1/33.10":{
                                  "rpf_nbr":"2001::222:1:1:1234",
                                  "internal":True
                               }
                            },
                            "oil_count":'2',
                            "outgoing_interface_list":{
                               "Ethernet1/26":{
                                  "oil_flags":"pim6",
                                  "oil_uptime":"00:02:58"
                                  
                               },
                               
                               "Vlan200":{
                                  "oil_flags":"m6rib",
                                  "oil_uptime":"00:02:58",
                                  "oif_rpf":"bridge-only"
                               }
                            },
                            "uptime":"00:04:03",
                         }
                      }
                   }
                }
             }
          }
       }
    }
}
