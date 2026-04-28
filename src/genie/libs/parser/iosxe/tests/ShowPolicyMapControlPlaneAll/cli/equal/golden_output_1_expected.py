expected_output = {
 "control_plane": {
  "service_policy": {
   "output": {
    "copp": {
     "class": {
      "copp": {
       "packets": 44266,
       "bytes": 3452858,
       "rate": {
        "interval": 300,
        "offered_rate_bps": 91000,
        "drop_rate_bps": 0
       },
       "match_evaluated": "match-all",
       "match": [
        "access-group name copp"
       ],
       "qos_set": {
        "ip": {
         "dscp": {
          "default": {
           "marker_statistics": "Disabled"
          }
         }
        }
       }
      },
      "class-default": {
       "packets": 176,
       "bytes": 13800,
       "rate": {
        "interval": 300,
        "offered_rate_bps": 1000,
        "drop_rate_bps": 0
       },
       "match_evaluated": "match-any",
       "match": [
        "any"
       ]
      }
     }
    }
   }
  }
 }
}