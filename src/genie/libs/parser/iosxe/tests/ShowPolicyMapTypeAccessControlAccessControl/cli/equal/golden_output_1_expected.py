expected_output = {
 "policy_map": {
  "type": "access-control parent",
  "name": "",
  "class": {
   "ip_udp": {
    "actions": {
     "service_policy": "child"
    }
   },
   "attack4": {
    "actions": {
     "drop": True,
     "send_response": "icmp-unreachable"
    }
   },
   "attack1": {
    "actions": {
     "drop": True
    }
   },
   "attack2": {
    "actions": {
     "log": True
    }
   }
  }
 }
}