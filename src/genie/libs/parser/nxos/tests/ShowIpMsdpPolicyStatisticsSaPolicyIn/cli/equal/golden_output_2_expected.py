

expected_output = {
    "vrf": {
        "default": {
           "peer": {
                "10.144.6.6": {
                     "in": {
                         "total_accept_count": 0,
                         "total_reject_count": 1,
                          "pfxlista": {
                               "ip prefix-list pfxlista seq 10 permit 224.0.0.0/4 le 32": {
                                    "num_of_matches": 0,
                                    "match": "ip prefix-list pfxlista seq 10 permit 224.0.0.0/4 le 32"
                               },
                               "ip prefix-list pfxlista seq 5 permit 224.0.0.0/4": {
                                    "num_of_matches": 0,
                                    "match": "ip prefix-list pfxlista seq 5 permit 224.0.0.0/4",
                               }
                          }
                     },
                }
           }
        }
    }
}
