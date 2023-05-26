expected_output = { 
   "ipv6_nd_router_proxy_config":{
      "policy_name":"default",
      "proxying":"NDP",
      "targets":{
         "vlan 1100":{
            "target":"vlan 1100",
            "type":"VLAN",
            "feature":"Routing Proxy",
            "target_range":"vlan all"
         },
         "vlan 1400":{
            "target":"vlan 1400",
            "type":"VLAN",
            "feature":"Routing Proxy",
            "target_range":"vlan all"
         },
         "Vl110":{
            "target":"Vl110",
            "type":"PORT",
            "feature":"Routing Proxy",
            "target_range":"vlan all"
         }
      }
   }
}
