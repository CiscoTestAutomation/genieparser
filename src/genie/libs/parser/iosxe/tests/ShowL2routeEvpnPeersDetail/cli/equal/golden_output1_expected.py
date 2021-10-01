# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {"evi": {
                       0: {
                           "eth_tag": {
                               0: {
                                   "peer_ip": {
                                       "3.3.3.1": {
                                           "encap": "MPLS",
                                           "number_of_routes": {
                                               "ead_es": 1,
                                               "es": 1
                                           },
                                           "top_id": "FFFFFFFE00000000",
                                           "top_name": "GLOBAL",
                                           "up_time": "3d02h"
                                       }
                                   }
                               }
                           }
                       },
                       2: {
                           "eth_tag": {
                               0: {
                                   "peer_ip": {
                                       "2.2.2.1": {
                                           "encap": "MPLS",
                                           "number_of_routes": {
                                               "ead_evi": 0,
                                               "imet": 1,
                                               "mac": 2,
                                               "mac_ip": 4
                                           },
                                           "top_id": "200000000",
                                           "top_name": "BD-12",
                                           "up_time": "3d02h"
                                       },
                                       "3.3.3.1": {
                                           "encap": "MPLS",
                                           "number_of_routes": {
                                               "ead_evi": 1,
                                               "imet": 1,
                                               "mac": 1,
                                               "mac_ip": 1
                                           },
                                           "top_id": "200000000",
                                           "top_name": "BD-12",
                                           "up_time": "3d02h"
                                       }
                                   }
                               }
                           }
                       }

             }

}
