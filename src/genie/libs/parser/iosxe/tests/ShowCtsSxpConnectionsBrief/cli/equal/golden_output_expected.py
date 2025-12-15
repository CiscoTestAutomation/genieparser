expected_output={
  'sxp_connections': {
    'status': {
      'sxp_status': 'Enabled',
      'highest_version': 5,
      'default_pw': 'Set',
      'key_chain': 'Not Set',
      'key_chain_name': 'Not Applicable',
      'source_ip': 'Not Set',
      'conn_retry': 10,
      'reconcile_secs': 30,
      'retry_timer': 'running',
      'peer_sequence_traverse_limit_for_export': 'Not Set',
      'peer_sequence_traverse_limit_for_import': 'Not Set'
    },
    'sxp_peers': {
      '33.1.1.1': {
        'source_ip': '33.1.1.2',
        'conn_status': 'Off(Speaker)::Pending_On(Listener)',
        'duration': '0:02:44:45'
      },
      '1100:1:1::1': {
        'source_ip': '2200:1:1::1',
        'conn_status': 'Off(Speaker)::Off(Listener)',
        'duration': '0:02:44:45'
      },
      '1133:1:1::1': {
        'source_ip': '1133:1:1::2',
        'conn_status': 'Off(Speaker)::Off(Listener)',
        'duration': '0:02:44:45'
      }
    },
    'total_sxp_connections': 2,
    'total_sxp_ipv4_connections': 1
  }
}
