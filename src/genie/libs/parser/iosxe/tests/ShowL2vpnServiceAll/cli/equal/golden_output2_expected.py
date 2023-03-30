# golden_output_2_expected.py
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
   "vpls_name":{
      "test_conn":{
         "state":"UP",
         "description":"TEST_LOCAL_CONN_DESCRIPTION",
         "interface":{
            "Gi0/1/0":{
               "group":"left",
               "encapsulation":"Gi0/1/0:7(Ethernet)",
               "priority":0,
               "state":"UP",
               "state_in_l2vpn_service":"UP"
            },
            "Gi0/1/3":{
               "group":"right",
               "encapsulation":"Gi0/1/3:10(Ethernet)",
               "priority":0,
               "state":"UP",
               "state_in_l2vpn_service":"UP"
            }
         }
      },
      "test_conn2":{
         "state":"DN",
         "description":"TEST_LOCAL_CONN_DESC_2",
         "interface":{
            "Gi0/1/1":{
               "group":"left",
               "encapsulation":"Gi0/1/1:8(Ethernet)",
               "priority":0,
               "state":"DN",
               "state_in_l2vpn_service":"DN"
            },
            "Gi0/1/2":{
               "group":"right",
               "encapsulation":"Gi0/1/2:9(Ethernet)",
               "priority":0,
               "state":"DN",
               "state_in_l2vpn_service":"DN"
            }
         }
      }
   }
}
