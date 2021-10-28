# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.
expected_output = {"evi": {
                       0: {
                           "eth_tag": {
                               0: {
                                   "peer_ip": {
                                       "3.3.3.1": {
                                           "encap": "MPLS",
                                           "num_rtes": 2,
                                           "top_name": "GLOBAL",
                                           "up_time": "2d22h"
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
                                           "num_rtes": 7,
                                           "top_name": "BD-12",
                                           "up_time": "2d22h"
                                       },
                                       "2.2.2.3": {
                                           "encap": "VxLAN",
                                           "num_rtes": 1,
                                           "top_name": "BD-101",
                                           "up_time": "00:02:07"
                                       },
                                       "3.3.3.1": {
                                           "encap": "MPLS",
                                           "num_rtes": 4,
                                           "top_name": "BD-12",
                                           "up_time": "2d22h"
                                       }
                                   }
                               },
                               1: {
                                   "peer_ip": {
                                       "AABB:BBCC:AABB:BBCC:AABB:BBCC:AABB:BBCC": {
                                           "encap": "MPLS",
                                           "num_rtes": 24,
                                           "top_name": "BD-20",
                                           "up_time": "2d22h"
                                       }
                                   }
                               }
                           }
                       }    
    }
    }
