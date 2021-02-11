expected_output = {
  'zp_name': {
    'ZP_LAN_ZONE_vpn20_LAN__968352866': {
      'src-zone-name': 'LAN_ZONE_vpn20',
      'dst-zone-name': 'LAN_ZONE_vpn20',
      'policy-name': 'ZBFW',
      'class_entry': {
        'ZBFW-seq-1-cm_': {
          'zonepair-name': 'ZP_LAN_ZONE_vpn20_LAN__968352866',
          'class-action': 'Inspect',
          'pkts-counter': 1230841471742,
          'bytes-counter': 902658477086649,
          'attempted-conn': 50000,
          'current-active-conn': 10000,
          'max-active-conn': 10000,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 1060419,
          'match_entry': {
            'ZBFW-sRule_1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'ZBFW-seq-Rule_1-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'proto_entry': {
            '2': {
              'protocol-name': 'udp',
              'byte-counters': 2380355513,
              'pkt-counters': 2480825086
            }
          },
          'l7-policy-name': 'my_aoo-pm_'
        },
        'class-default': {
          'zonepair-name': 'ZP_LAN_ZONE_vpn20_LAN__968352866',
          'class-action': 'Inspect Drop',
          'pkts-counter': 20003,
          'bytes-counter': 13926178,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'l7-policy-name': 'NONE'
        }
      },
      'l7_class_entry': {
        'my_aoo-cm0_': {
          'parent-class-name': 'ZBFW-seq-1-cm_',
          'child-class-action': 'Inspect AVC Deny',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'l7_match_entry': {
            'apple-app-store': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'ftp': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'gmail': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'google-play': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'itunes': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'netflix': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'whatsapp': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'yahoo-messenger': {
              'byte-counters': 0,
              'pkt-counters': 0
            },
            'zoom-meetings': {
              'byte-counters': 0,
              'pkt-counters': 0
            }
          }
        },
        'class-default': {
          'parent-class-name': 'ZBFW-seq-1-cm_',
          'child-class-action': 'Inspect Data',
          'pkts-counter': 1230838599565,
          'bytes-counter': 902656354954242,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0
        }
      }
    }
  }
}