expected_output = {
  'flow_monitor_name': {
    'FLow-1': {
      'description': 'User defined',
      'record_name': 'not configured',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 50,
        'active_timeout': 30
      }
    },
    'FLow-4': {
      'description': 'User defined',
      'record_name': 'not configured',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 50,
        'active_timeout': 30
      }
    },
    'FLow-5': {
      'description': 'User defined',
      'record_name': 'not configured',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 50,
        'active_timeout': 30
      }
    },
    'LIVEACTION-FLOWMONITOR-INGRESS': {
      'description': 'DO NOT MODIFY. USED BY LIVEACTION.',
      'record_name': 'LIVEACTION-FLOWRECORD-INGRESS',
      'exporter_name': 'LIVEACTION-FLOWEXPORTER',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 10,
        'active_timeout': 30
      }
    },
    'LIVEACTION-FLOWMONITOR-EGRESS': {
      'description': 'DO NOT MODIFY. USED BY LIVEACTION.',
      'record_name': 'LIVEACTION-FLOWRECORD-EGRESS',
      'exporter_name': 'LIVEACTION-FLOWEXPORTER',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 10,
        'active_timeout': 60
      }
    },
    'STEALTHWATCH_IN_FLOW_MONITOR': {
      'description': 'User defined',
      'record_name': 'STEALTHWATCH_IN',
      'exporter_name': 'STEALTHWATCH_FLOW_EXPORTER',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 15,
        'active_timeout': 60
      }
    },
    'STEALTHWATCH_OUT_FLOW_MONITOR': {
      'description': 'User defined',
      'record_name': 'STEALTHWATCH_OUT',
      'exporter_name': 'STEALTHWATCH_FLOW_EXPORTER',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 15,
        'active_timeout': 60
      }
    },
    'fnf-mon': {
      'description': 'ETTA',
      'record_name': 'fnf-rec',
      'exporter_name': 'FLOW-COLLECTOR1',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'not allocated',
        'size': 10000,
        'inactive_timeout': 10,
        'active_timeout': 30
      }
    },
    'monitor_ipv4_in': {
      'description': 'User defined',
      'record_name': 'record_ipv4_in',
      'exporter_name': 'export_prime_nf10',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'allocated',
        'size': 10000,
        'inactive_timeout': 15,
        'active_timeout': 30
      }
    },
    'monitor_ipv4_out': {
      'description': 'User defined',
      'record_name': 'record_ipv4_out',
      'exporter_name': 'export_prime_nf10',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'allocated',
        'size': 10000,
        'inactive_timeout': 15,
        'active_timeout': 30
      }
    },
    'dnacmonitor': {
      'description': 'User defined',
      'record_name': 'dnacrecord',
      'exporter_name': 'dnacexporter',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'allocated',
        'size': 10000,
        'inactive_timeout': 10,
        'active_timeout': 60
      }
    },
    'dnacmonitor_v6': {
      'description': 'User defined',
      'record_name': 'dnacrecord_v6',
      'exporter_name': 'dnacexporter',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'allocated',
        'size': 10000,
        'inactive_timeout': 10,
        'active_timeout': 60
      }
    },
    'monitor_ipv6_in': {
      'description': 'User defined',
      'record_name': 'record_ipv6_in',
      'exporter_name': 'export_prime_nf10',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'allocated',
        'size': 10000,
        'inactive_timeout': 15,
        'active_timeout': 30
      }
    },
    'monitor_ipv6_out': {
      'description': 'User defined',
      'record_name': 'record_ipv6_out',
      'exporter_name': 'export_prime_nf10',
      'cache': {
        'type': 'normal (Platform cache)',
        'status': 'allocated',
        'size': 10000,
        'inactive_timeout': 15,
        'active_timeout': 30
      }
    }
  }
}
