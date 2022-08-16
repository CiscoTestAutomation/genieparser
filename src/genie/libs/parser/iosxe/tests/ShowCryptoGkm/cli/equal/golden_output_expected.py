expected_output={
   "group_name":{
      "getvpn1":{
         "group_information":{
            "crypto_path":"ipv4",
            "group_identity":"1223",
            "group_member":{
               "3.3.1.1":{
                  "active_tek_num":2,
                  "allowable_rekey_cipher":"ESP",
                  "attempted_registration_count":1,
                  "dp_error_monitoring":"OFF",
                  "fail_close_revert":"Disabled",
                  "fvrf":"None",
                  "ipsec_init_reg_executed":0,
                  "ipsec_init_reg_postponed":0,
                  "ivrf":"None",
                  "last_rekey_seq_num":0,
                  "last_rekey_server":"1.1.1.1",
                  "local_addr":"3.3.1.1",
                  "local_addr_port":"848",
                  "pfs_rekey_received":0,
                  "re_register_time_sec":485,
                  "registration":"Registered",
                  "rekey_acks_sent":27,
                  "remote_addr":"1.1.1.1",
                  "remote_addr_port":848,
                  "sa_track":"disabled",
                  "server_ip":"1.1.1.1",
                  "succeeded_registration_count":1,
                  "uncicast_rekey_received":27,
                  "version":"1.0.26",
                  "vrf":"None"
               }
            },
            "group_member_information":{
               "acl_download_from_ks":{
                  "1.1.1.1":{
                     "acl_list":[
                        "access-list   deny ip host 11.23.33.33 host 24.54.55.55",
                        "access-list   deny ip host 41.23.32.37 host 44.58.59.55",
                        "access-list   deny esp any any",
                        "access-list   deny udp any any port = 3784",
                        "access-list   deny udp any any port = 3785",
                        "access-list   deny udp any port = 3785 any",
                        "access-list   deny tcp any any port = 179",
                        "access-list   deny tcp any port = 179 any",
                        "access-list   deny tcp any any port = 22",
                        "access-list   deny tcp any port = 22 any",
                        "access-list   deny ospf any any",
                        "access-list   deny pim any 224.0.0.0 0.0.0.255",
                        "access-list   deny udp any any port = 123",
                        "access-list   deny udp any any port = 514",
                        "access-list   deny udp any port = 500 any port = 500",
                        "access-list   deny udp any port = 848 any",
                        "access-list   deny udp any any port = 848",
                        "access-list   deny ip any 10.90.0.0 0.0.255.255",
                        "access-list   deny ip 10.90.0.0 0.0.255.255 any",
                        "access-list   permit ip 25.25.0.0 0.0.255.255 15.15.0.0 0.0.255.255",
                        "access-list   permit ip 15.15.0.0 0.0.255.255 25.25.0.0 0.0.255.255",
                        "access-list   permit ip 16.16.0.0 0.0.255.255 26.26.0.0 0.0.255.255",
                     ]
                  }
               },
               "acl_received_from_ks":"gdoi_group_getvpn1_temp_acl",
               "rekeys_cumulative":{
                  "after_latest_register":27,
                  "rekey_acks_sents":27,
                  "total_received":27
               }
            },
            "group_server_list":"1.1.1.1",
            "group_type":"GDOI (ISAKMP)",
            "ipsec_sa_direction":"Both",
            "kek_policy":{
               "encrypt_algorithm":"AES",
               "key_size":256,
               "lifetime":1148,
               "rekey_transport_type":"Unicast",
               "sig_hash_algorithm":"HMAC_AUTH_SHA",
               "sig_key_length":4400
            },
            "key_management_path":"ipv4",
            "kgs_policy":{
               "reg_gm":{
                  "local_addr":"3.3.1.1"
               }
            },
            "p2p_policy":{
               "reg_gm":{
                  "local_addr":"3.3.1.1"
               }
            },
            "rekeys_received":27,
            "tek_policy":{
               "interfaces":{
                  "GigabitEthernet0/0/1":{
                     "ipsec_sa":{
                        "spi":{
                           "0x3A14695B(974416219)":{
                              "alg_key_size_bytes":32,
                              "sig_key_size_bytes":32,
                              "anti_replay_count":64,
                              "encaps":"ENCAPS_TUNNEL",
                              "sa_remaining_key_lifetime":74,
                              "tag_method":"disabled",
                              "transform":"esp-256-aes esp-sha256-hmac"
                           },
                           "0xEE021924(3993114916)":{
                              "alg_key_size_bytes":32,
                              "sig_key_size_bytes":32,
                              "anti_replay_count":64,
                              "encaps":"ENCAPS_TUNNEL",
                              "sa_remaining_key_lifetime":549,
                              "tag_method":"disabled",
                              "transform":"esp-256-aes esp-sha256-hmac"
                           }
                        }
                     }
                  }
               }
            }
         }
      }
   }
}