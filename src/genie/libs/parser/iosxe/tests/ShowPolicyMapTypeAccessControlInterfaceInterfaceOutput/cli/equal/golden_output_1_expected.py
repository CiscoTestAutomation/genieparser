expected_output = {
 "interface": {
  "GigabitEthernet0/0/0": {
   "service_policy": {
    "output": {
     "name": "access-control",
     "type": "parent",
     "classes": {
      "ip_tcp": {
       "match_type": "match-all",
       "packets": 1,
       "bytes": 60,
       "offered_rate_bps_5min": 0,
       "matches": [
        "field IP version eq 4",
        "field IP ihl eq 5",
        "field IP protocol eq 6 next TCP"
       ],
       "child_policy": {
        "name": "access-control",
        "type": "child",
        "classes": {
         "test": {
          "match_type": "match-any",
          "packets": 1,
          "bytes": 60,
          "offered_rate_bps_5min": 0,
          "drop_rate_bps_5min": 0,
          "matches": [
           "field TCP dest-port eq 36"
          ],
          "action": "drop"
         },
         "class-default": {
          "match_type": "match-any",
          "packets": 0,
          "bytes": 0,
          "offered_rate_bps_5min": 0,
          "drop_rate_bps_5min": 0,
          "matches": [
           "any"
          ]
         }
        }
       }
      },
      "class-default": {
       "match_type": "match-any",
       "packets": 0,
       "bytes": 0,
       "offered_rate_bps_5min": 0,
       "drop_rate_bps_5min": 0,
       "matches": [
        "any"
       ]
      }
     }
    }
   }
  }
 }
}
