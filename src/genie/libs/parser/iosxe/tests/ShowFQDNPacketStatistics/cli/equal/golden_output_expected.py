expected_output = {
  'fqdn_statistics': {
    'pkts_received': {
      'total_dns_pkts_rcvd': 226,
      'ipv4_dns_pkts_rcvd': 226,
      'ipv6_dns_pkts_rcvd': 0
    },
    'total_registered_fqdn': 6,
    'total_induced_latency': 6,
    'dns_pkt_latency': {
      'min_latency': 12,
      'max_latency': 3001,
      'avg_latency': 1506
    },
    'pkts_injected': {
      'total_pkts_injected': 226,
      'pkts_injected_by_ack': 6,
      'pkts_with_parse_error': 0,
      'pkts_with_no_answer': 220,
      'pkts_with_no_aaaa_record': 0,
      'fqdn_not_registered': 0,
      'fqdn_already_cached': 0
    },
    'total_pkts_dropped_nack': 0,
    'avg_input_rate_1_min': 3,
    'avg_input_rate_5_min': 3,
    'avg_input_rate_1_hr': 3
  }
}

