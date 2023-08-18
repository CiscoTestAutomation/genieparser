expected_output = {
   "bridge_domain":101,
   "reference_count":10,
   "replication_ports_count":2,
   "unicast_addr_table_size":1,
   "ip_multicast_prefix_table_size":3,
   "flood_list_info":{
      "olist":1125,
      "ports":2
   },
   "port_info":{
      "Gi1/0/10:101":{
         "type":"BD_PORT",
         "description":"Gi1/0/10:101",
         "description_values":{
             "interface": "Gi1/0/10",
             "service_instance": 101,
         },
         "is_pathlist":False
      },
      "[IR]10101:172.16.254.2":{
         "type":"VXLAN_REP",
         "path_list_id":25,
         "path_list_count":1,
         "path_list_type":"VXLAN_REP",
         "description":"[IR]10101:172.16.254.2",
         "description_values":{
             "type": "IR",
             "port": 10101,
             "address": "172.16.254.2",
         },
         "is_pathlist":True
      }
   },
   "unicast_addr_table_info":{
      "44d3.ca28.6cc2":{
         "type":"VXLAN_UC",
         "is_pathlist":True,
         "unicast_path_list":{
            "unicast_id":24,
            "unicast_path_count":1,
            "unicast_type":"VXLAN_UC",
            "unicast_description":"[MAC]10101:172.16.254.2",
            "unicast_description_values":{
                "type": "MAC",
                "port": 10101,
                "address":"172.16.254.2", 
            },
         }
      },
   },
   "ip_multicast_prefix_table_info":{
      "224.0.0.0/24":{
         "source":"*",
         "group":"224.0.0.0/24",
         "iif":"Null",
         "adjacency":" ",
         "olist":1125,
         "port_count":2
      },
      "224.0.1.39":{
         "source":"*",
         "group":"224.0.1.39",
         "iif":"Null",
         "adjacency":" ",
         "olist":1125,
         "port_count":2
      },
      "224.0.1.40":{
         "source":"*",
         "group":"224.0.1.40",
         "iif":"Null",
         "adjacency":" ",
         "olist":1125,
         "port_count":2
      }
   }
}
