expected_output =  {
 "cg_name": {
  "racl_permitv4_egress": {
   "cg_id": 21,
   "feature": "Racl",
   "prot": "IPv4",
   "region": "0x1006c0b8",
   "dir": "Egress",
   "sdk_handles": [
    {
     "asic": 0,
     "oid": "0xA62"
    }
   ],
   "seq": {
    "10": {
     "ipv4_src_value": "0x00000002",
     "ipv4_src_mask": "0x000000ff",
     "ipv4_dst_value": "0x00000002",
     "ipv4_dst_mask": "0x000000ff",
     "proto": {
      "value": "0x0",
      "mask": "0x0",
      "tcp_flg": "0x0",
      "tcp_op": "0x0",
      "src_port": "0x0",
      "dst_port": "0x0"
     },
     "tos": {
      "value": "0x0",
      "mask": "0x0",
      "ttl": "0x0",
      "cos": "0x0",
      "v4_opt": "0x0",
      "src_obj": "0x0",
      "dst_obj": "0x0"
     },
     "action": "PERMIT",
     "logging": "NO_LOG"
    },
    "4294967295": {
     "ipv4_src_value": "0x00000000",
     "ipv4_src_mask": "0x00000000",
     "ipv4_dst_value": "0x00000000",
     "ipv4_dst_mask": "0x00000000",
     "proto": {
      "value": "0x0",
      "mask": "0x0",
      "tcp_flg": "0x0",
      "tcp_op": "0x0",
      "src_port": "0x0",
      "dst_port": "0x0"
     },
     "tos": {
      "value": "0x0",
      "mask": "0x0",
      "ttl": "0x0",
      "cos": "0x0",
      "v4_opt": "0x0",
      "src_obj": "0x0",
      "dst_obj": "0x0"
     },
     "counter_handles": [
      {
       "asic": 0,
       "oid": "0xA63"
      }
     ],
     "action": "DENY",
     "logging": "NONE"
    }
   }
  },
  "racl_permitv6_egress": {
   "cg_id": 22,
   "feature": "Racl",
   "prot": "IPv6",
   "region": "0x1005b4f8",
   "dir": "Egress",
   "sdk_handles": [
    {
     "asic": 0,
     "oid": "0xA55"
    }
   ],
   "seq": {
    "50": {
     "ipv6_src_value": "0x00100000.0x00000000.0x00000000.0x00000000",
     "ipv6_src_mask": "0xffffffff.0xffffffff.0xffffffff.0xffffff00",
     "ipv6_dst_value": "0x00300000.0x00000000.0x00000000.0x00000000",
     "proto": {
      "value": "0x0",
      "mask": "0x0",
      "tcp_flg": "0x0",
      "tcp_op": "0x0",
      "src_port": "0x0",
      "dst_port": "0x0"
     },
     "tos": {
      "value": "0x0",
      "mask": "0x0",
      "ttl": "0x0",
      "cos": "0x0",
      "v4_opt": "0x0",
      "src_obj": "0x0",
      "dst_obj": "0x0"
     },
     "action": "PERMIT",
     "logging": "NO_LOG"
    },
    "60": {
     "ipv6_src_value": "0x00100000.0x00000000.0x00000000.0x00010000",
     "ipv6_src_mask": "0xffffffff.0xffffffff.0xffffffff.0xffffff00",
     "ipv6_dst_value": "0x00300000.0x00000000.0x00000000.0x00010000",
     "proto": {
      "value": "0x0",
      "mask": "0x0",
      "tcp_flg": "0x0",
      "tcp_op": "0x0",
      "src_port": "0x0",
      "dst_port": "0x0"
     },
     "tos": {
      "value": "0x0",
      "mask": "0x0",
      "ttl": "0x0",
      "cos": "0x0",
      "v4_opt": "0x0",
      "src_obj": "0x0",
      "dst_obj": "0x0"
     },
     "counter_handles": [
      {
       "asic": 0,
       "oid": "0xA5D"
      }
     ],
     "action": "DENY",
     "logging": "NO_LOG"
    },
    "70": {
     "ipv6_src_value": "0x00000000.0x00000000.0x00000000.0x00000000",
     "ipv6_src_mask": "0x00000000.0x00000000.0x00000000.0x00000000",
     "ipv6_dst_value": "0x00000000.0x00000000.0x00000000.0x00000000",
     "proto": {
      "value": "0xff",
      "mask": "0x0",
      "tcp_flg": "0x0",
      "tcp_op": "0x0",
      "src_port": "0x0",
      "dst_port": "0x0"
     },
     "tos": {
      "value": "0x0",
      "mask": "0x0",
      "ttl": "0x0",
      "cos": "0x0",
      "v4_opt": "0x0",
      "src_obj": "0x0",
      "dst_obj": "0x0"
     },
     "action": "PERMIT",
     "logging": "NO_LOG"
    },
    "4294967295": {
     "ipv6_src_value": "0x00000000.0x00000000.0x00000000.0x00000000",
     "ipv6_src_mask": "0x00000000.0x00000000.0x00000000.0x00000000",
     "ipv6_dst_value": "0x00000000.0x00000000.0x00000000.0x00000000",
     "proto": {
      "value": "0x0",
      "mask": "0x0",
      "tcp_flg": "0x0",
      "tcp_op": "0x0",
      "src_port": "0x0",
      "dst_port": "0x0"
     },
     "tos": {
      "value": "0x0",
      "mask": "0x0",
      "ttl": "0x0",
      "cos": "0x0",
      "v4_opt": "0x0",
      "src_obj": "0x0",
      "dst_obj": "0x0"
     },
     "counter_handles": [
      {
       "asic": 0,
       "oid": "0xA60"
      }
     ],
     "action": "DENY",
     "logging": "NONE"
    }
   }
  }
 }
}
