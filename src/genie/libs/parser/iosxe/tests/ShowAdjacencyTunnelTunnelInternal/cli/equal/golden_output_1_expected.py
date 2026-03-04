expected_output = {
 "interface": {
  "Tunnel{tunnel}": {
   "protocol": "IP",
   "interface": "Tunnel1",
   "address": "point2point",
   "adjacency_id": 19,
   "packets": 1998,
   "bytes": 1581880,
   "epoch": 0,
   "sourced_in_sev_epoch": 1110,
   "encap_length": 40,
   "encap": [
    "60000000000004FF0100010000010000",
    "00000000000000010300030000010000",
    "0000000000000001"
   ],
   "adjacency_type": "P2P-ADJ",
   "next_chain_element": {
    "protocol": "IPV6",
    "out_interface": "GigabitEthernet0/0/1",
    "addr": "FE80::C6B2:39FF:FEFB:DC41",
    "pointer": "78EE054686C8",
    "parent_oce": "0x78EE05468788",
    "frame_origin": "frame originated locally (Null0)"
   },
   "l3_mtu": 1460,
   "mtu_update_suppressed": True,
   "flags": "0x4928E4",
   "fixup": {
    "enabled": True,
    "value": "0x80000",
    "note": "IPv6 in IPv6 tunnel"
   },
   "hwidb_pointer": "0x78EDFF532770",
   "idb_pointer": "0x78EE0541C910",
   "ip_redirect_disabled": True,
   "switching_vector": "IPv4 midchain adj oce",
   "next_hop_inferred": False,
   "ip_tunnel_stack": {
    "to": "300:300:1::1",
    "vrf": "Default",
    "vrf_id": "0x0"
   },
   "nh_tracking": {
    "enabled": True,
    "prefix": "300:300:1::1/128",
    "adjacency": {
     "protocol": "IPV6",
     "out_interface": "GigabitEthernet0/0/1",
     "addr": "FE80::C6B2:39FF:FEFB:DC41"
    }
   },
   "platform": {
    "adj_id": "0xF8000216",
    "adj_id2": "0x0",
    "tun_qos_dpidx": 0
   },
   "adjacency_pointer": "0x78EE05468F88",
   "next_hop": "unknown"
  }
 }
}