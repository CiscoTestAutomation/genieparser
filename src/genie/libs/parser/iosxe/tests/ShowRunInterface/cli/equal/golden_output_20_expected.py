expected_output = {
  'interfaces': {
    'TenGigabitEthernet2/0/1': {
      'switchport_trunk_vlans': '302-311,2400-2419',
      'switchport_mode': 'trunk',
      'flow_monitor_input': 'monitor_ipv4_in',
      'flow_monitor_output': 'monitor_ipv4_out',
      'load_interval': '60',
      'flow_monitor_input_v6': 'monitor_ipv6_in',
      'flow_monitor_output_v6': 'monitor_ipv6_out',
      'spanning_tree_portfast': True
    }
  }
}

