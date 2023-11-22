
expected_output = {
   "vpc_domain_id":"200",
   "vpc_peer_status":"peer adjacency formed ok",
   "vpc_peer_keepalive_status":"peer is alive",
   "vpc_configuration_consistency_status":"success",
   "vpc_per_vlan_consistency_status":"success",
   "vpc_type_2_consistency_status":"success",
   "vpc_role":"primary",
   "num_of_vpcs":2,
   "peer_gateway":"Enabled",
   "dual_active_excluded_vlans":"-",
   "vpc_graceful_consistency_check_status":"Enabled",
   "vpc_auto_recovery_status":"Disabled",
   "vpc_delay_restore_status":"Timer is off.(timeout = 30s)",
   "vpc_delay_restore_svi_status":"Timer is off.(timeout = 10s)",
   "operational_l3_peer_router":"Disabled",
   "virtual_peerlink_mode":"Enabled",
   "peer_link":{
      1:{
         "peer_link_id":1,
         "peer_link_ifindex":"Port-channel101",
         "peer_link_port_state":"up",
         "peer_up_vlan_bitset":"1-5,10-15,21-25,31-35,41-45,51-55,61-65,71-75,81-85,91-95,101-105,111-115,121-125,131-135,141-145,151-155,161-165,171-175,181-185,191-195,201-205,501,1006-1010,1016-1020"
      }
   },
   "vpc":{
      102:{
         "vpc_id":102,
         "vpc_ifindex":"Port-channel102",
         "vpc_port_state":"up",
         "vpc_consistency":"success",
         "vpc_consistency_status":"success",
         "up_vlan_bitset":"10"
      },
      103:{
         "vpc_id":103,
         "vpc_ifindex":"Port-channel103",
         "vpc_port_state":"up",
         "vpc_consistency":"success",
         "vpc_consistency_status":"success",
         "up_vlan_bitset":"2-5,11-15,21-25,31-35,41-45,51-55,61-65,71-75,81-85,91-95,101-105,111-115,121-125,"
      }
   }
}
