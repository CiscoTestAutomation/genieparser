expected_output = {
    "interface":{
      "GigabitEthernet0/0/0/2":{
         "interface":"GigabitEthernet0/0/0/2",
         "port_number":"1",
         "address_family":{
            "IPv4":{
               "address_family":"IPv4",
               "ip_address":"192.168.254.1",
               "priority":"None (128)",
               "clock_class":"None",
               "delay_asymmetry":"None",
               "announce_messages":{
                  "Announce granted":{
                     "rate_limit":"8 per-second",
                     "duration":"300 seconds"
                  },
                  "Sync granted":{
                     "rate_limit":"64 per-second",
                     "duration":"300 seconds"
                  },
                  "Delay-resp granted":{
                     "rate_limit":"64 per-second",
                     "duration":"300 seconds"
                  }
               },
               "qualified_period":"8 hours, 26 minutes, 9 seconds",
               "clock_id":"b0aefffe04cc9b",
               "received_clk_properties":{
                  "domain":"44",
                  "priority1":"128",
                  "priority2":"128",
                  "class":"6",
                  "accuracy":"0x21",
                  "offset_scaled_log_variance":"0x4e5d",
                  "steps_removed":"1",
                  "time_source":"GPS",
                  "time_scale":"PTP",
                  "frequency":"Frequency-traceable",
                  "time":"Time-traceable",
                  "current_utc_offset":"37 seconds (valid"
               }
            }
         }
      }
   }
}