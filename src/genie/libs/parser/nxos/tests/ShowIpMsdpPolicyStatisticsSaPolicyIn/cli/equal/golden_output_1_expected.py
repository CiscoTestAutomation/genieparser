

expected_output = {
    "vrf": {
        "default": {
           "peer": {
                "10.144.6.6": {
                     "in": {
                         "total_accept_count": 0,
                         "total_reject_count": 0,
                          "filtera": {
                               "route-map filtera permit 10 match ip address mcast-all-groups": {
                                    "match": "route-map filtera permit 10 match ip address mcast-all-groups",
                                    "num_of_matches": 0,
                                    "num_of_comparison": 0
                               },
                               "route-map filtera permit 20 match ip address mcast-all-groups2": {
                                    "match": "route-map filtera permit 20 match ip address mcast-all-groups2",
                                    "num_of_matches": 0,
                                    "num_of_comparison": 0
                               }
                          }
                     },
                }
           }
        }
    }
}
