expected_output = {
  'flow_monitor': {
    'FLow-1': {
      'description': 'User defined',
      'flow_record': 'not configured',
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
      'flow_record': 'not configured',
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
      'flow_record': 'not configured',
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
      'flow_record': 'LIVEACTION-FLOWRECORD-INGRESS',
      'flow_exporter': 'LIVEACTION-FLOWEXPORTER',
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
      'flow_record': 'LIVEACTION-FLOWRECORD-EGRESS',
      'flow_exporter': 'LIVEACTION-FLOWEXPORTER',
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
      'flow_record': 'STEALTHWATCH_IN',
      'flow_exporter': 'STEALTHWATCH_FLOW_EXPORTER',
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
      'flow_record': 'STEALTHWATCH_OUT',
      'flow_exporter': 'STEALTHWATCH_FLOW_EXPORTER',
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
      'flow_record': 'fnf-rec',
      'flow_exporter': 'FLOW-COLLECTOR1',
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
      'flow_record': 'record_ipv4_in',
      'flow_exporter': 'export_prime_nf10',
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
      'flow_record': 'record_ipv4_out',
      'flow_exporter': 'export_prime_nf10',
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
      'flow_record': 'dnacrecord',
      'flow_exporter': 'dnacexporter',
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
      'flow_record': 'dnacrecord_v6',
      'flow_exporter': 'dnacexporter',
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
      'flow_record': 'record_ipv6_in',
      'flow_exporter': 'export_prime_nf10',
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
      'flow_record': 'record_ipv6_out',
      'flow_exporter': 'export_prime_nf10',
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
