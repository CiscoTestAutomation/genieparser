

expected_output = {
    "prefix_set_name": {
        "test": {
             "entries": 6,
             "protocol": "ipv4",
             "prefix_set_name": "test",
             "prefixes": {
                  "10.169.0.0/8 16..24 permit": {
                       "masklength_range": "16..24",
                       "sequence": 25,
                       "prefix": "10.169.0.0/8",
                       "action": "permit"
                  },
                  "10.205.0.0/8 8..16 permit": {
                       "masklength_range": "8..16",
                       "sequence": 10,
                       "prefix": "10.205.0.0/8",
                       "action": "permit"
                  },
                  "10.21.0.0/8 8..16 permit": {
                       "masklength_range": "8..16",
                       "sequence": 15,
                       "prefix": "10.21.0.0/8",
                       "action": "permit"
                  },
                  "10.205.0.0/8 8..8 deny": {
                       "masklength_range": "8..8",
                       "sequence": 5,
                       "prefix": "10.205.0.0/8",
                       "action": "deny"
                  },
                  "10.94.0.0/8 24..32 permit": {
                       "masklength_range": "24..32",
                       "sequence": 20,
                       "prefix": "10.94.0.0/8",
                       "action": "permit"
                  },
                  "192.0.2.0/24 25..25 permit": {
                       "masklength_range": "25..25",
                       "sequence": 30,
                       "prefix": "192.0.2.0/24",
                       "action": "permit"
                  },
             }
        }
   }
}
