expected_output= {
   "group_name":{
      "bw-suiteB":{
         "configured_acl":[
            "access-list bw600-crypto-policy  deny udp any port = 16384 any",
            "access-list bw600-crypto-policy  deny tcp any any port = 179",
            "access-list bw600-crypto-policy  deny tcp any port = 179 any",
            "access-list bw600-crypto-policy  permit ip 190.0.0.0 0.255.255.255 115.0.0.0 0.255.255.255",
            "access-list bw600-crypto-policy  permit ip 115.0.0.0 0.255.255.255 190.0.0.0 0.255.255.255"
         ]
      },
      "bw-suiteB-v6":{
         "configured_acl":[
            "access-list bw600-v6-crypto-policy  deny udp any any eq 20001",
            "access-list bw600-v6-crypto-policy  deny udp any any eq 20002",
            "access-list bw600-v6-crypto-policy  deny udp any any eq 20003",
            "access-list bw600-v6-crypto-policy  permit ipv6 1900::/16 1150::/16",
            "access-list bw600-v6-crypto-policy  permit ipv6 1150::/16 1900::/16"
         ]
      },
      "bw600-IPV6":{
         "configured_acl":[
            "access-list bw600-v6-crypto-policy  deny udp any any eq 20001",
            "access-list bw600-v6-crypto-policy  deny udp any any eq 20002",
            "access-list bw600-v6-crypto-policy  deny udp any any eq 20003",
            "access-list bw600-v6-crypto-policy  permit ipv6 1900::/16 1150::/16",
            "access-list bw600-v6-crypto-policy  permit ipv6 1150::/16 1900::/16"
         ]
      },
      "bw600-IPV6_eft":{
         "configured_acl":[
            "access-list bw600-v6-crypto-policy_eft  deny udp any any eq 20001",
            "access-list bw600-v6-crypto-policy_eft  deny udp any any eq 20002",
            "access-list bw600-v6-crypto-policy_eft  deny udp any any eq 20003",
            "access-list bw600-v6-crypto-policy_eft  permit ipv6 2100::/16 3100::/16",
            "access-list bw600-v6-crypto-policy_eft  permit ipv6 3100::/16 2100::/16"
         ]
      },
      "bw6000":{
         "configured_acl":[
            "access-list bw600-crypto-policy  deny udp any port = 16384 any",
            "access-list bw600-crypto-policy  deny tcp any any port = 179",
            "access-list bw600-crypto-policy  deny tcp any port = 179 any",
            "access-list bw600-crypto-policy  permit ip 190.0.0.0 0.255.255.255 115.0.0.0 0.255.255.255",
            "access-list bw600-crypto-policy  permit ip 115.0.0.0 0.255.255.255 190.0.0.0 0.255.255.255"
         ]
      },
      "bw6000_eft":{
         "configured_acl":[
            "access-list bw600-crypto-policy_eft  deny udp any port = 16384 any",
            "access-list bw600-crypto-policy_eft  deny tcp any any port = 179",
            "access-list bw600-crypto-policy_eft  deny tcp any port = 179 any",
            "access-list bw600-crypto-policy_eft  permit ip 21.0.0.0 0.255.255.255 31.0.0.0 0.255.255.255",
            "access-list bw600-crypto-policy_eft  permit ip 31.0.0.0 0.255.255.255 21.0.0.0 0.255.255.255"
         ]
      }
   }
}