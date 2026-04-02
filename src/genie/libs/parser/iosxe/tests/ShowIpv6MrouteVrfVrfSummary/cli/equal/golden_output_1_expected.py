expected_output = {
 "vrf": {
  "vrf2": {
   "address_family": {
    "ipv6": {
     "multicast_group": {
      "FF08:4000::1": {
       "source_address": {
        "*": {
         "uptime": "00:03:45",
         "expires": "never",
         "rp_address": "2001:2310::3",
         "oif_count": 1,
         "flags": "SCJ"
        },
        "2001:2410::42": {
         "uptime": "00:01:31",
         "expires": "00:01:58",
         "oif_count": 1,
         "flags": "SJT"
        },
        "2001:2410::43": {
         "uptime": "00:01:31",
         "expires": "00:01:58",
         "oif_count": 1,
         "flags": "SJT"
        }
       }
      }
     }
    }
   }
  }
 }
}