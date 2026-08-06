expected_output = {
 "total_sessions": 1,
 "sessions": {
  "705": {
   "type": "IPv4/IPv6",
   "uid": 705,
   "state": "authen",
   "identity": "aaaa.bbbb.cccc",
   "ipv4_address": "11.11.11.2",
   "ipv6_address": "8001::",
   "session_up_time": "00:00:18",
   "last_changed": "00:00:06",
   "switch_id": 4717,
   "policy_information": {
    "context": "7F2190EB88D0",
    "handle": "1D00041D",
    "aaa_id": "000003A9",
    "flow_handle": 0,
    "authentication_status": "authen",
    "downloaded_user_profile": {
     "excluding_services": {
      "service_type": {
       "value1": 0,
       "value2": 2,
       "description": "Framed"
      },
      "prefix": {
       "index": 0,
       "value": "00 40 80 01 00 00 00 00 00 00"
      }
     },
     "including_services": {
      "service_type": {
       "value1": 0,
       "value2": 2,
       "description": "Framed"
      },
      "prefix": {
       "index": 0,
       "value": "00 40 80 01 00 00 00 00 00 00"
      }
     }
    },
    "config_history": {
     "access_type": "IP",
     "client": "SM",
     "policy_event": "Service Selection Request",
     "profile_name": "aaaa.bbbb.cccc",
     "references": 2,
     "profile_attributes": {
      "service_type": {
       "value1": 0,
       "value2": 2,
       "description": "Framed"
      },
      "prefix": {
       "index": 0,
       "value": "00 40 80 01 00 00 00 00 00 00"
      }
     }
    },
    "rules_actions_conditions_executed": {
     "subscriber_rule_map": "TAL",
     "conditions": [
      {
       "condition": "always",
       "event": "session-start",
       "actions": [
        {
         "sequence": 10,
         "command": "authorize identifier mac-address"
        }
       ]
      }
     ]
    }
   },
   "classifiers": {
    0: {
     "direction": "In",
     "packets": 5,
     "bytes": 542,
     "priority": 0,
     "definition": "Match Any"
    },
    1: {
     "direction": "Out",
     "packets": 4,
     "bytes": 456,
     "priority": 0,
     "definition": "Match Any"
    }
   },
   "template_id": 69,
   "configuration_sources": {
    "USR": {
     "active_time": "00:00:18",
     "aaa_service_id": "-",
     "name": "Peruser"
    },
    "INT": {
     "active_time": "00:00:18",
     "aaa_service_id": "-",
     "name": "GigabitEthernet0/0/3"
    }
   }
  }
 }
}
