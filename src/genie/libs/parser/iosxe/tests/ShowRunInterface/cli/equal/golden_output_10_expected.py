expected_output = {
   "interfaces": {
        "GigabitEthernet1/0/2": {
            "description": "test_of_parser",
            "switchport_trunk_vlans": "500,821,900-905",
            "switchport_mode": "trunk",
            "flow_monitor_input": "IPv4_NETFLOW",
            "ip_arp_inspection_trust": True,
            "ip_arp_inspection_limit_rate": "100",
            "load_interval": "30",
            "power_inline": {
                "state": "static",
                "max_watts": "30000"
                },
            "power_inline_port_priority": "high",
            "spanning_tree_portfast": True,
            "spanning_tree_bpdufilter": "disable",
            "switchport_protected": True,
            "switchport_block_unicast": True,
            "switchport_block_multicast": True,
            "ip_dhcp_snooping_trust": True,
            "ip_dhcp_snooping_limit_rate": "15",
            "channel_group": {
                "chg": 23,
                "mode": "active"
                }
        }
    }
}
