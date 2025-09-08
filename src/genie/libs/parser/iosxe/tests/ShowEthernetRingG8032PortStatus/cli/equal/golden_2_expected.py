expected_output = {
  "ethernet_ring_ports": {
    "GigabitEthernet1/3": {
      "block_vlan_list": "1-9,11-4095",
      "instance": "1",
      "req/ack": "0/0",
      "ring": "g8032_ring",
      "state": "Blocked",
      "unblock_vlan_list": "10"
    },
    "GigabitEthernet1/4": {
      "block_vlan_list": "1-9,11-99,201-4095",
      "instance": "1",
      "req/ack": "0/0",
      "ring": "g8032_ring",
      "state": "Unblocked",
      "unblock_vlan_list": "10,100-200"
    }
  }
} 
