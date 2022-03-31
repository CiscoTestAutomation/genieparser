expected_output = {
   "vrf":{
      "vrf1":{
         "address_family":{
            "ipv4":{
               "multicast_group":{
                  "225.1.1.1":{
                     "source_address":{
                        "192.168.1.10":{
                           "flags":"K HW DDE",
                           "oif_ic_count":0,
                           "oif_a_count":1,
                           "sw_packet_count":2,
                           "sw_packets_per_second":0,
                           "sw_average_packet_size":178,
                           "sw_kbits_per_second":0,
                           "sw_total":0,
                           "sw_rpf_failed":0,
                           "sw_other_drops":0,
                           "hw_packet_count":256180,
                           "hw_packets_per_second":7,
                           "hw_average_packet_size":200,
                           "hw_kbits_per_second":11,
                           "hw_total":0,
                           "hw_rpf_failed":0,
                           "hw_other_drops":0,
                           "incoming_interfaces":{
                              "Vlan2001":{
                                 "ingress_flags":"RA A MA"
                              }
                           },
                           "outgoing_interfaces":{
                              "LISP0.1":{
                                 "egress_flags":"RF F NS",
                                 "egress_rloc":"100.11.11.11",
                                 "egress_underlay_mcast":"235.1.3.167",
                                 "egress_adj_mac":"Adjacency with MAC: 450000000000400000111D2F640B0B0BEB0103A7000012B5000000000840000000000100BA25CDF4AD38BA25CDF4AD380000",
                                 "egress_hw_pkt_count":0,
                                 "egress_fs_pkt_count":0,
                                 "egress_ps_pkt_count":2,
                                 "egress_pkt_rate":0
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
