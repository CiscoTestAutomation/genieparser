expected_output = {
 "vpdn": {
  "group_select": {
   "default": {
    "default_group": "L2TP_GROUP",
    "current_default_group": "DEFAULT_L2TP",
    "state": "Active",
    "group_info": {
     "L2TP_GROUP": {
      "protocol": "l2tp",
      "domain_handling": "enabled",
      "priority": 1
     }
    },
    "protocols": {
     "l2tp": {
      "default_group": "vgdefault"
     },
     "pptp": {
      "default_group": None
     }
    }
   }
  }
 }
}
