expected_output = {
  "ip_slas_configuration": {
    1: {
      "entry_number": 1,
      "owner": "-",
      "tag": "-",
      "type_of_operation_to_perform": "icmp-echo",
      "target_address": "192.168.1.1",
      "source_address": "192.168.1.2",
      "request_size_arr_data_bytes": 28,
      "timeout_milliseconds": 5000,
      "frequency_seconds": 60,
      "verify_data": "No",
      "status_of_entry_snmp_rowstatus": "Active",
      "threshold_milliseconds": 2000,
      "distribution_statistics": {
        "number_of_statistics_hours_kept": 2,
        "number_of_statistics_distributions_buckets_kept": 1,
        "statistic_distribution_interval_milliseconds": 20
      },
      "enhanced_history": {
        "number_of_history_lives_kept": 0,
        "number_of_history_buckets_kept": 15,
        "history_filter_type": "None"
      }
    },
    2: {
      "entry_number": 2,
      "owner": "-",
      "tag": "-",
      "type_of_operation_to_perform": "udp-jitter",
      "target_address": "192.168.2.1",
      "source_address": "192.168.2.2",
      "request_size_arr_data_bytes": 32,
      "timeout_milliseconds": 3000,
      "frequency_seconds": 30,
      "status_of_entry_snmp_rowstatus": "Active",
      "threshold_milliseconds": 1000,
      "distribution_statistics": {
        "number_of_statistics_hours_kept": 4,
        "number_of_statistics_distributions_buckets_kept": 2,
        "statistic_distribution_interval_milliseconds": 10
      },
      "enhanced_history": {
        "number_of_history_lives_kept": 0,
        "number_of_history_buckets_kept": 20,
        "history_filter_type": "None"
      }
    }
  }
}
