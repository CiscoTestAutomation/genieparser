expected_output={
   "interface":{
      "GigabitEthernet3":{
         "crypto_map_tag":"vpn-crypto-map",
         "ident":{
            1:{
               "acl":"origin_is_acl,",
               "action":"PERMIT",
               "current_outbound_spi":"0x397C36EE(964441838)",
               "dh_group":"none",
               "inbound_ah_sas":{
                  
               },
               "inbound_esp_sas":{
                  "spi":{
                     "0x658F7C11(1703902225)":{
                        "conn_id":2076,
                        "crypto_map":"vpn-crypto-map",
                        "flow_id":"CSR",
                        "flow_id_val":76,
                        "transform":"esp-256-aes esp-sha256-hmac",
                        "in_use_settings":"Tunnel, ",
                        "iv_size":"16 bytes",
                        "remaining_key_lifetime":"(4607999/83191)",
                        "replay_detection_support":"Y",
                        "sibling_flags":"FFFFFFFF80000048",
                        "status":"ACTIVE(ACTIVE)"
                     }
                  }
               },
               "inbound_pcp_sas":{
                  
               },
               "ip_mtu_idb":"GigabitEthernet3",
               "local_crypto_endpt":"1.1.1.2",
               "local_ident":{
                  "addr":"20.20.20.0",
                  "mask":"255.255.255.0",
                  "port":"0",
                  "prot":"0"
               },
               "outbound_ah_sas":{
                  
               },
               "outbound_esp_sas":{
                  "spi":{
                     "0x397C36EE(964441838)":{
                        "conn_id":2075,
                        "crypto_map":"vpn-crypto-map",
                        "flow_id":"CSR",
                        "flow_id_val":75,
                        "transform":"esp-256-aes esp-sha256-hmac",
                        "in_use_settings":"Tunnel, ",
                        "iv_size":"16 bytes",
                        "remaining_key_lifetime":"(4607999/83191)",
                        "replay_detection_support":"Y",
                        "sibling_flags":"FFFFFFFF80000048",
                        "status":"ACTIVE(ACTIVE)"
                     }
                  }
               },
               "outbound_pcp_sas":{
                  
               },
               "path_mtu":1500,
               "peer_ip":"1.1.1.1",
               "pfs":"N",
               "pkts_compr_failed":0,
               "pkts_compressed":0,
               "pkts_decaps":4,
               "pkts_decompress_failed":0,
               "pkts_decompressed":0,
               "pkts_decrypt":4,
               "pkts_encaps":4,
               "pkts_encrypt":4,
               "pkts_digest":4,
               "pkts_not_compressed":0,
               "pkts_not_decompressed":0,
               "pkts_verify":4,
               "plaintext_mtu":1438,
               "ip_mtu":1500,
               "port":500,
               "protected_vrf":"(none)",
               "recv_errors":0,
               "remote_crypto_endpt":"1.1.1.1",
               "remote_ident":{
                  "addr":"10.10.10.0",
                  "mask":"255.255.255.0",
                  "port":"0",
                  "prot":"0"
               },
               "send_errors":0
            },
            2:{
               "acl":"origin_is_acl,",
               "action":"PERMIT",
               "current_outbound_spi":"0x0(0)",
               "dh_group":"none",
               "inbound_ah_sas":{
                  
               },
               "inbound_esp_sas":{
                  
               },
               "inbound_pcp_sas":{
                  
               },
               "ip_mtu_idb":"GigabitEthernet3",
               "local_crypto_endpt":"1.1.1.2",
               "local_ident":{
                  "addr":"40.40.40.0",
                  "mask":"255.255.255.0",
                  "port":"0",
                  "prot":"0"
               },
               "outbound_ah_sas":{
                  
               },
               "outbound_esp_sas":{
                  
               },
               "outbound_pcp_sas":{
                  
               },
               "path_mtu":1500,
               "peer_ip":"1.1.1.1",
               "pfs":"N",
               "pkts_compr_failed":0,
               "pkts_compressed":0,
               "pkts_decaps":0,
               "pkts_decompress_failed":0,
               "pkts_decompressed":0,
               "pkts_decrypt":0,
               "pkts_encaps":0,
               "pkts_encrypt":0,
               "pkts_digest":0,
               "pkts_not_compressed":0,
               "pkts_not_decompressed":0,
               "pkts_verify":0,
               "plaintext_mtu":1500,
               "ip_mtu":1500,
               "port":500,
               "protected_vrf":"(none)",
               "recv_errors":0,
               "remote_crypto_endpt":"1.1.1.1",
               "remote_ident":{
                  "addr":"30.30.30.0",
                  "mask":"255.255.255.0",
                  "port":"0",
                  "prot":"0"
               },
               "send_errors":0
            }
         },
         "local_addr":"1.1.1.2"
      },
      "Tunnel0":{
         "crypto_map_tag":"Tunnel0-head-0",
         "ident":{
            1:{
               "acl":"origin_is_acl,",
               "action":"PERMIT",
               "current_outbound_spi":"0x2E8482F8(780436216)",
               "dh_group":"none",
               "inbound_ah_sas":{
                  
               },
               "inbound_esp_sas":{
                  "spi":{
                     "0xA54D38A4(2773301412)":{
                        "conn_id":2077,
                        "crypto_map":"Tunnel0-head-0",
                        "flow_id":"CSR",
                        "flow_id_val":77,
                        "transform":"esp-256-aes esp-sha256-hmac",
                        "in_use_settings":"Tunnel, ",
                        "iv_size":"16 bytes",
                        "remaining_key_lifetime":"(4608000/3237)",
                        "replay_detection_support":"Y",
                        "sibling_flags":"FFFFFFFF80004048",
                        "status":"ACTIVE(ACTIVE)"
                     }
                  }
               },
               "inbound_pcp_sas":{
                  
               },
               "ip_mtu_idb":"GigabitEthernet5",
               "local_crypto_endpt":"2.2.2.2",
               "local_ident":{
                  "addr":"0.0.0.0",
                  "mask":"0.0.0.0",
                  "port":"0",
                  "prot":"0"
               },
               "outbound_ah_sas":{
                  
               },
               "outbound_esp_sas":{
                  "spi":{
                     "0x2E8482F8(780436216)":{
                        "conn_id":2078,
                        "crypto_map":"Tunnel0-head-0",
                        "flow_id":"CSR",
                        "flow_id_val":78,
                        "transform":"esp-256-aes esp-sha256-hmac",
                        "in_use_settings":"Tunnel, ",
                        "iv_size":"16 bytes",
                        "remaining_key_lifetime":"(4608000/3237)",
                        "replay_detection_support":"Y",
                        "sibling_flags":"FFFFFFFF80004048",
                        "status":"ACTIVE(ACTIVE)"
                     }
                  }
               },
               "outbound_pcp_sas":{
                  
               },
               "path_mtu":1500,
               "peer_ip":"2.2.2.1",
               "pfs":"N",
               "pkts_compr_failed":0,
               "pkts_compressed":0,
               "pkts_decaps":0,
               "pkts_decompress_failed":0,
               "pkts_decompressed":0,
               "pkts_decrypt":0,
               "pkts_encrypt":0,
               "pkts_encaps":0,
               "pkts_digest":0,
               "pkts_not_compressed":0,
               "pkts_not_decompressed":0,
               "pkts_verify":0,
               "plaintext_mtu":1438,
               "port":500,
               "ip_mtu":1500,
               "protected_vrf":"(none)",
               "recv_errors":0,
               "remote_crypto_endpt":"2.2.2.1",
               "remote_ident":{
                  "addr":"0.0.0.0",
                  "mask":"0.0.0.0",
                  "port":"0",
                  "prot":"0"
               },
               "send_errors":0
            }
         },
         "local_addr":"2.2.2.2"
      }
   }
}
