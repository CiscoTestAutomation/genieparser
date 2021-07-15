expected_output = { 
   "flooding_supression_policy_config":{
      "policy_name":"fspol1",
      "suppressing":"NDP",
      "mode":"Proxy all resolution requests",
      "targets":{
         "vlan 1":{
            "target":"vlan 1",
            "type":"VLAN",
            "feature":"Flooding Suppress",
            "target_range":"vlan all"
         }
      }
   }
}