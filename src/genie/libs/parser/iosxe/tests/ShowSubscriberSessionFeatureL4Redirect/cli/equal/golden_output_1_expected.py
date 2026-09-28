expected_output = {
 "sessions": {
  48: {
   "type": "DHCPv4",
   "uid": 48,
   "state": "unauthen",
   "identity": "11.11.11.4",
   "ipv4_address": "11.11.11.4",
   "session_up_time": "00:00:07",
   "last_changed": "00:00:09",
   "switch_id": 4335,
   "features": {
    "l4_redirect": {
     98: {
      "class_id": 98,
      "rule_cfg": "#1",
      "definition": "SVC  to group V4_DASHBOARD",
      "source": "L4_REDIRECT_V4"
     },
     100: {
      "class_id": 100,
      "rule_cfg": "#1",
      "definition": "SVC  to group V6_DASHBOARD",
      "source": "L4_REDIRECT_V6"
     }
    }
   }
  }
 }
}
