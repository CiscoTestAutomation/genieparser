expected_output = {
   "issu_proceed_status": "ISSU Cannot Proceed",    
   "criteria1": {
         "status": "PASSED",
         "value": "No Topology change must be active in any STP instance"
   },
   "criteria2": {
         "status": "PASSED",
         "value": "Bridge assurance(BA) should not be active on any port"
   },
   "criteria3": {
         "non_edge_port": {
             "Ethernet1/20": {
                 "instance": "0",
                 "role": "Desg",
                 "sts": "FWD",
                 "tree_type": "MST",
                 "vlan": 1
             },
             "Ethernet1/21": {
                 "instance": "0",
                 "role": "Desg",
                 "sts": "FWD",
                 "tree_type": "MST",
                 "vlan": 1
             }
         },
         "status": "FAILED",        
         "value": "There should not be any Non Edge Designated Forwarding port"

   }
}
