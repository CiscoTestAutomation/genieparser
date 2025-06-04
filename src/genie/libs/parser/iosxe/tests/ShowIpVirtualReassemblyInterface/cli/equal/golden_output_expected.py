expected_output = {
  "virtual_fragment_reassembly_information": {
    "interface": "GigabitEthernet4",
    "vfr_enabled": True,
    "maximum_number_of_fragments": 64,
    "maximum_packet_length_bytes": 1500,
    "timeout_seconds": 30,
    "current_number_of_reassembly_contexts": 3,
    "current_number_of_fragments": 15,
    "reassembly_timeout_events": 2,
    "reassembly_fail_events": 1,
    "reassembly_success_events": 20,
    "last_packet_dropped_due_to_vfr": {
      "fragment_count_exceeded": True,
      "packet_length_exceeded": True
    },
    "statistics_since_last_clear": {
      "total_packets_received": 1000,
      "total_fragments_received": 200,
      "total_packets_reassembled": 950,
      "total_packets_dropped_due_to_vfr": 50
    }
  }
}
