expected_output = {
   "bootup_breakout_config":{
      "port":0,
      "slot":0
   },
   "events_log":[
      {
         "timestamp":"2026/02/10 22:45:20.532",
         "event":"Created"
      },
      {
         "timestamp":"2026/02/10 22:45:20.532",
         "event":"STP Block"
      },
      {
         "timestamp":"2026/02/10 22:45:20.534",
         "event":"Enable Mac Learning"
      },
      {
         "timestamp":"2026/02/10 22:45:35.533",
         "event":"STP Learn"
      },
      {
         "timestamp":"2026/02/10 22:45:35.533",
         "event":"Enable Mac Learning"
      },
      {
         "timestamp":"2026/02/10 22:45:50.534",
         "event":"STP Forward"
      }
   ],
   "interface_block_pointer":"0x7b463af04658",
   "interface_block_state":"Ready",
   "interface_if_id":"0x000500000198029a",
   "interface_name":"Gi3/0/24_V666",
   "interface_ref_cnt":1,
   "interface_state":"Enabled",
   "interface_status":"ADD,",
   "interface_type":"*UNKNOWN*",
   "port_cts_subblock":{
      "disable_sgacl":"0x0",
      "port_sgt":"0xffff",
      "propagate":"0x0",
      "trust":"0x0"
   },
   "port_vp_subblock":{
      "default_vlan":666,
      "dense_mode_vp":"Yes",
      "if_id":"0x000500000198029a",
      "mac_learning_enable":"Yes",
      "match_vlan":0,
      "parent_if_id":"0x00000000000004a1",
      "port_mode":"port_mode_access",
      "port_mode_set":"No",
      "port_tagging":"PORT_TAG_NATIVE",
      "rx_span_enabled":"No",
      "service_port_gid":"0x1e0c0(123072)",
      "service_port_gid_punt":"0x9e0c0(647360)",
      "service_port_oid_asic_0":"0xca3(3235)",
      "span_dest_gpn":0,
      "stp_state":"STP_FORWARDING",
      "stp_state_set":"No",
      "tx_span_enabled":"No",
      "untagged":"Yes",
      "vlan_id":666
   },
   "ref_count":1
}