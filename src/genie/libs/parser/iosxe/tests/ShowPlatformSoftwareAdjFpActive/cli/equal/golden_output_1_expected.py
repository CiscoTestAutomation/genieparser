expected_output = {
 "number_of_adjacency_objects": 4,
 "adjacencies": {
  "0xe": {
   "id": {
    "hex": "0xe",
    "dec": 14
   },
   "interface": "GigabitEthernet0/0/3",
   "if_index": 10,
   "link_type": "MCP_LINK_IP",
   "encap": "0:50:56:8b:7b:52:c4:b2:39:fb:dc:43:8:0",
   "encap_length": 14,
   "encap_type": "MCP_ET_ARPA",
   "mtu": 1500,
   "flags": ["no-l3-inject"],
   "incomplete_behavior_type": "None",
   "fixup": "unknown",
   "fixup_flags_2": "unknown",
   "nexthop_addr": "172.100.0.2",
   "ip_frr": {
    "mode": "MCP_ADJ_IPFRR_NONE",
    "value": 0
   },
   "aom_id": 14879,
   "hw_handle": "0x55a9a5b76d50",
   "hw_handle_state": "created"
  },
  "0x15": {
   "id": {
    "hex": "0x15",
    "dec": 21
   },
   "interface": "NVI0",
   "if_index": 16,
   "link_type": "MCP_LINK_IP",
   "encap": "ca:fe:ba:be",
   "encap_length": 4,
   "encap_type": "MCP_ET_NULL",
   "mtu": 9216,
   "flags": ["no-l3-inject", "is-nvi"],
   "incomplete_behavior_type": "None",
   "fixup": "unknown",
   "fixup_flags_2": "unknown",
   "nexthop_addr": "100.0.0.2",
   "ip_frr": {
    "mode": "MCP_ADJ_IPFRR_NONE",
    "value": 0
   },
   "aom_id": 106,
   "hw_handle": "0x55a9a578bb50",
   "hw_handle_state": "created"
  },
  "0x30": {
   "id": {
    "hex": "0x30",
    "dec": 48
   },
   "interface": "GigabitEthernet0/0/3",
   "if_index": 10,
   "link_type": "MCP_LINK_IP",
   "encap": "8:96:ad:8d:71:0:c4:b2:39:fb:dc:43:8:0",
   "encap_length": 14,
   "encap_type": "MCP_ET_ARPA",
   "mtu": 1500,
   "flags": ["no-l3-inject"],
   "incomplete_behavior_type": "None",
   "fixup": "unknown",
   "fixup_flags_2": "unknown",
   "nexthop_addr": "172.100.0.1",
   "ip_frr": {
    "mode": "MCP_ADJ_IPFRR_NONE",
    "value": 0
   },
   "aom_id": 14872,
   "hw_handle": "0x55a9a5b75960",
   "hw_handle_state": "created"
  },
  "0xf80000a4": {
   "id": {
    "hex": "0xf80000a4",
    "dec": 4160749732
   },
   "interface": "GigabitEthernet0/0/3",
   "if_index": 10,
   "link_type": "MCP_LINK_IP",
   "encap": "1:0:5e:0:0:0:c4:b2:39:fb:dc:43:8:0",
   "encap_length": 14,
   "encap_type": "MCP_ET_ARPA",
   "mtu": 1500,
   "flags": ["p2mp-type"],
   "incomplete_behavior_type": "None",
   "fixup": "unknown",
   "fixup_flags_2": "unknown",
   "nexthop_addr": "227.0.0.0",
   "ip_frr": {
    "mode": "MCP_ADJ_IPFRR_NONE",
    "value": 0
   },
   "aom_id": 604,
   "hw_handle": "0x55a9a5b5d110",
   "hw_handle_state": "created"
  }
 }
}