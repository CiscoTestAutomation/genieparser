expected_output = {
   'GigabitEthernet1/14': {
      'model': 'IE-4010-4S24P',
      'type': '10/100/1000BaseTX',
      'speed': [
         '10',
         '100',
         '1000',
         'auto'
      ],
      'duplex': [
         'half',
         'full',
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
         'qos_scheduling_tx': '4q3t'
      },
      'udld': True,
      'inline_power': True,
      'span': 'source/destination',
      'portsecure': True,
      'dot1x': True
   }
}