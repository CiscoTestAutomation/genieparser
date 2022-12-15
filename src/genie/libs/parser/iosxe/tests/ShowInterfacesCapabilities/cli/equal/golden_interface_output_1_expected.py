expected_output = {
   'TenGigabitEthernet1/1/4': {
      'model': 'WS-C3850-48P',
      'type': 'SFP-10GBase-CX1',
      'speed': [
         '10',
         '100',
         '1000',
         'auto'
      ],
      'duplex': [
         'full',
         'half',
         'auto'
      ],
      'trunk_encap_type': '802.1Q',
      'trunk_mode': [
         'on',
         'off',
         'desirable',
         'nonegotiate'
      ],
      'channel': True,
      'broadcast_suppression': 'percentage(0-100)',
      'unicast_suppression': 'percentage(0-100)',
      'multicast_suppression': 'percentage(0-100)',
      'flowcontrol': {
         'flowcontrol_rx': [
            'off',
            'on',
            'desired'
         ],
         'flowcontrol_tx': [
            'none'
         ]
      },
      'fast_start': True,
      'qos_scheduling': {
         'qos_scheduling_rx': 'not configurable on per port basis',
         'qos_scheduling_tx': '2p6q3t'
      },
      'udld': True,
      'inline_power': False,
      'span': 'source/destination',
      'portsecure': True,
      'dot1x': True,
      'breakout_support': 'not applicable',
      'media_types': [
         'rj45',
         'sfp',
         'auto-select'
      ]
   }
}