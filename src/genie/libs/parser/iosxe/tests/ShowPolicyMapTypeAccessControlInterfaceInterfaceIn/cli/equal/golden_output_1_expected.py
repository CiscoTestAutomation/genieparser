expected_output = {
 "interface": {
  "GigabitEthernet0/0/0": {
   "service_policy": {
    "input": {
     "name": "access-control",
     "type": "parent",
     "classes": {
      "ip_tcp": {
       "match_type": "match-all",
       "packets": 584692,
       "bytes": 49114128,
       "offered_rate_bps_5min": 1139000,
       "matches": [
        "field IP version eq 4",
        "field IP ihl eq 5",
        "field IP protocol eq 6 next TCP"
       ],
       "child_policy": {
        "name": "access-control",
        "type": "child",
        "classes": {
         "class1": {
          "match_type": "match-all",
          "packets": 0,
          "bytes": 0,
          "offered_rate_bps_5min": 0,
          "drop_rate_bps_5min": 0,
          "matches": [
           "field TCP source-port range 5 5000",
           "field TCP dest-port eq 1",
           "field IP dest-addr eq 20.1.1.8",
           "start l3-start offset 40 size 4 regex \"ABCD\"",
           "field IP source-addr eq 10.1.1.2",
           "field IP tos lt 255",
           "field IP fragment-offset eq 00",
           "field TCP urgent-pointer eq 1"
          ],
          "action": "drop"
         },
         "class-default": {
          "match_type": "match-any",
          "packets": 584692,
          "bytes": 49114128,
          "offered_rate_bps_5min": 1139000,
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