expected_output = {
   "interfaces": {
      "GigabitEthernet1/0/5": {
         "switchport_mode": "trunk",
         "flow_monitor_input": "IPv4_NETFLOW",
         "ip_arp_inspection_limit_rate": "100",
         "load_interval": "30",
         "output_policy": "UPLINK-EGRESS-QUEUING",
         "spanning_tree_portfast_trunk": True,
         "ip_dhcp_snooping_limit_rate": "20"
      }
   }
}