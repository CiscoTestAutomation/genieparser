expected_output = {
      "track": {
           "1": {
               "type": "Interface", 
               "instance": "Ethernet1/4", 
               "subtrack": "IP Routing",
               "state": "DOWN", 
               "change_count": 1,
               "last_change": "3w5d", 
               "tracked_by": {
                    1: {
                      "name": "HSRP", 
                      "interface": "Vlan2",
                      "group_id": "2"
                    },
                    2: {
                      "name": "HSRP", 
                      "interface": "Ethernet1/1", 
                      "group_id": "1"
                    },
                    3: {
                      "name": "VRRPV3",
                      "interface": "Vlan2",
                      "group_id": "2"
                    },
                    4: {
                      "name": "Track", 
                      "interface": "List", 
                      "group_id": "10"
                    }, 
                    5: {
                      "name": "Track",
                      "interface": "List",
                      "group_id": "11"
                    }, 
                    6: {
                      "name": "Track",
                      "interface": "List",
                      "group_id": "12"
                    }
               },
               "delay_up_secs": 20.0
           },
           "12": {
               "type": "List", 
               "sublist": "weight",
               "state": "DOWN", 
               "change_count": 1, 
               "last_change": "3w3d", 
               "threshold_down": "10", 
               "threshold_up": "20", 
               "track_list_members": {
                    1: {
                      "object_id": "10",
                      "weight": "10", 
                      "obj_state": "UP"}, 
                    2: {
                      "object_id": "1", 
                      "weight": "100", 
                      "obj_state": "DOWN"
                    }
               }
           },
           "13": {
               "type": "Interface",
               "instance": "loopback1", 
               "subtrack": "Line Protocol",
               "state": "DOWN", 
               "change_count": 2,
               "last_change": "3w3d",
               "delay_up_secs": 23.0, 
               "delay_down_secs": 24.0
           },
      }
}
