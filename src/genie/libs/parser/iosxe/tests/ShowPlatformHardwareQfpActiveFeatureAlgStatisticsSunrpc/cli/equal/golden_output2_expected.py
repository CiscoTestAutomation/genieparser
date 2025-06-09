expected_output = {
  "global_info": {
    "total_pkts_passed_inspection": 0,
    "call": 0,
    "reply": 0,
    "non_data": 0,
    "procedures": {
      "get_port": 0,
      "call_it": 0,
      "dump": 0,
      "other": 0
    },
    "rpcbind_v3_v4": 0,
    "duplicate_xid": 0,
    "vfred_packets": 0
  },
  "drop_counters": {
    "total_dropped": 0,
    "fatal_error": {
      "internal_sw_error": 0
    },
    "info": {
      "pkt_malformed": 0,
      "pkt_too_short": 0,
      "xid_mismatch": 0,
      "rpc_ver_not_supported": 0,
      "tcp_record_is_not_last_frag": 0
    },
    "packets_subject_to_policy_inspection": {
      "policy_not_exist": 0,
      "policy_dirty_bit_set": 0,
      "policy_mismatch": 0
    },
  },
  "counters_cleared" : True,
  "memory_management": {
    "chunk": {
      "requested": 0,
      "returned": 0
    },
    "l7_scb": {
      "allocated": 0,
      "freed": 0,
      "failed": 0
    },
    "l7_pkt": {
      "allocated": 0,
      "freed": 0,
      "failed": 0
    },
  },
"counters_cleared" : True
}
