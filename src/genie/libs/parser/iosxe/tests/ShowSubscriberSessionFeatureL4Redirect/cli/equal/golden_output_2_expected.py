expected_output = {
 "sessions": {
  642: {
   "type": "IPv4/IPv6",
   "uid": 642,
   "state": "unauthen",
   "identity": "11.11.11.2",
   "ipv4_address": "11.11.11.2",
   "ipv6_address": "5001:0:0:1::",
   "session_up_time": "00:00:28",
   "last_changed": "00:00:11",
   "switch_id": 31205,
   "features": {
    "l4_redirect": {
     184: {
      "class_id": 184,
      "rule_cfg": "#1",
      "definition": "SVC  to group V6_DASHBOARD",
      "source": "L4_REDIRECT_V6"
     },
     186: {
      "class_id": 186,
      "rule_cfg": "#1",
      "definition": "SVC  to group V4_DASHBOARD",
      "source": "L4_REDIRECT_V4"
     }
    }
   }
  }
 }
}
