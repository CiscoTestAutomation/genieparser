expected_output = {
   'interfaces': {
      'GigabitEthernet1/0/10': {
         'switchport_mode': 'access',
         'flow_monitor_input': 'IPv4_NETFLOW',
         'load_interval': '30',
         'shutdown': True,
         'speed': 'auto 10 100 1000',
         'duplex': 'full',
         'spanning_tree_portfast': True
      }
   }
}
