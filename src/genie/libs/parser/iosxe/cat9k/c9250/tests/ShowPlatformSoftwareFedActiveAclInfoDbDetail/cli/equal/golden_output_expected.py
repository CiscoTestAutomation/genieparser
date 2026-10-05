expected_output =  {
 "cg_name": {
  "racl_ingress": {
   "cg_id": 8,
   "feature": "Racl",
   "prot": "IPv4",
   "region": "0x2c0603d8",
   "dir": "Ingress",
   "sdk_handles": [
    {
     "asic": 0,
     "oid": "0x44D"
    },
    {
     "asic": 1,
     "oid": "0x4BC"
    },
    {
     "asic": 2,
     "oid": "0x49A"
    },
    {
     "asic": 3,
     "oid": "0x470"
    }
   ],
   "seq": {
    "10": {
     "ipv4_src_value": "0x78010500",
     "ipv4_src_mask": "0xffffff00",
     "ipv4_dst_value": "0x7a010502",
     "ipv4_dst_mask": "0xffffffff",
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
       "oid": "0x577"
      },
      {
       "asic": 1,
       "oid": "0x5D2"
      },
      {
       "asic": 2,
       "oid": "0x5D2"
      },
      {
       "asic": 3,
       "oid": "0x570"
      }
     ],
     "action": "DENY",
     "logging": "NO_LOG"
    },
    "20": {
     "ipv4_src_value": "0x78010100",
     "ipv4_src_mask": "0xffffff00",
     "ipv4_dst_value": "0x7a010100",
     "ipv4_dst_mask": "0xffffff00",
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
       "oid": "0x578"
      },
      {
       "asic": 1,
       "oid": "0x5D3"
      },
      {
       "asic": 2,
       "oid": "0x5D3"
      },
      {
       "asic": 3,
       "oid": "0x571"
      }
     ],
     "action": "DENY",
     "logging": "NONE"
    }
   }
  }
 }
}
