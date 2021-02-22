expected_output = {
  'zonepair_name': {
    'ZP_LAN_ZONE_vpn20_LAN__968352866': {
      'src_zone_name': 'LAN_ZONE_vpn20',
      'dst_zone_name': 'LAN_ZONE_vpn20',
      'policy_name': 'ZBFW',
      'class_entry': {
        'ZBFW-seq-1-cm_': {
          'zonepair_name': 'ZP_LAN_ZONE_vpn20_LAN__968352866',
          'class_action': 'Inspect',
          'pkts_counter': 1230841471742,
          'bytes_counter': 902658477086649,
          'attempted_conn': 50000,
          'current_active_conn': 10000,
          'max_active_conn': 10000,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 1060419,
          'match_entry': {
            'ZBFW-sRule_1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'ZBFW-seq-Rule_1-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'proto_entry': {
            2: {
              'protocol_name': 'udp',
              'byte_counters': 2380355513,
              'pkt_counters': 2480825086
            }
          },
          'l7_policy_name': 'my_aoo-pm_'
        },
        'class-default': {
          'zonepair_name': 'ZP_LAN_ZONE_vpn20_LAN__968352866',
          'class_action': 'Inspect Drop',
          'pkts_counter': 20003,
          'bytes_counter': 13926178,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'l7_policy_name': 'NONE'
        }
      },
      'l7_class_entry': {
        'my_aoo-cm0_': {
          'parent_class_name': 'ZBFW-seq-1-cm_',
          'child_class_action': 'Inspect AVC Deny',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'l7_match_entry': {
            'apple-app-store': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'ftp': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'gmail': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'google-play': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'itunes': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'netflix': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'whatsapp': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'yahoo-messenger': {
              'byte_counters': 0,
              'pkt_counters': 0
            },
            'zoom-meetings': {
              'byte_counters': 0,
              'pkt_counters': 0
            }
          }
        },
        'class-default': {
          'parent_class_name': 'ZBFW-seq-1-cm_',
          'child_class_action': 'Inspect Data',
          'pkts_counter': 1230838599565,
          'bytes_counter': 902656354954242,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0
        }
      }
    }
  }
}