expected_output = {
    'alarm_facility': {
         'hsr': {
             'actions': {
                 'enable': {
                     'enabled': False,
                 },
                 'notifies': {
                     'enabled': False,
                 },
                 'relay_major': {
                     'enabled': False,
                 },
                 'syslog': {
                     'enabled': False,
                 },
             },
         },
         'input-alarm 1': {
             'actions': {
                 'notifies': {
                     'enabled': False,
                 },
                 'relay_major': {
                     'enabled': False,
                 },
                 'syslog': {
                     'enabled': True,
                 },
             },
         },
         'input-alarm 2': {
             'actions': {
                 'notifies': {
                     'enabled': False,
                 },
                 'relay_major': {
                     'enabled': False,
                 },
                 'syslog': {
                     'enabled': True,
                 },
             },
         },
         'input-alarm 3': {
             'actions': {
                 'notifies': {
                     'enabled': False,
                 },
                 'relay_major': {
                     'enabled': False,
                 },
                 'syslog': {
                     'enabled': True,
                 },
             },
         },
         'input-alarm 4': {
             'actions': {
                 'notifies': {
                     'enabled': False,
                 },
                 'relay_major': {
                     'enabled': False,
                 },
                 'syslog': {
                     'enabled': True,
                 },
             },
         },
         'power-supply': {
             'actions': {
                 'syslog': {
                     'enabled': False,
                 },
             },
         },
         'temperature primary': {
             'actions': {
                 'notifies': {
                     'enabled': False,
                 },
                 'relay_major': {
                     'enabled': False,
                 },
                 'syslog': {
                     'enabled': False,
                 },
             },
             'thresholds': {
                 'high': 80,
                 'low': 0,
             },
         },
         'temperature secondary': {
             'thresholds': {
                 'high': 80,
                 'low': 0,
             },
         },
     },
     'alarm_profile': {
         'alarm': 'not-operating',
         'name': 'defaultPort',
         'notifies': 'not-operating',
         'syslog': 'not-operating',
     },
     'logging': {
         'alarm': False,
     },
     'snmp': {
         'mib': {
             'flowmon': {
                 'alarmhistorysize': 500,
             },
         },
     },
 }
