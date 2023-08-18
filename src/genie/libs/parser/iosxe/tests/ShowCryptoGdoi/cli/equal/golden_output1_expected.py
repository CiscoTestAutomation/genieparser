expected_output={
    "group_name": {
        "cust": {
            "group_information": {
                "group_identity": "1000",
                "group_type": "G-IKEv2 (IKEv2)",
                "crypto_path": "ipv4",
                "key_management_path": "ipv4",
                "rekeys_received": 134,
                "ipsec_sa_direction": "Both",
                "group_server_list": "3.3.3.3",
                "group_member_information": {
                    "acl_received_from_ks": "gdoi_group_cust_temp_acl",
                    "rekeys_cumulative": {
                        "total_received": 134,
                        "after_latest_register": 134,
                        "rekey_acks_sents": 134,
                    },
                    "acl_download_from_ks": {
                        "3.3.3.3": {
                            "acl_list": [
                                "access-list deny eigrp any any",
                                "access-list permit ip host 23.23.23.23 any",
                                "access-list permit ip host 33.23.23.23 any",
                            ]
                        }
                    },
                },
                "group_member": {
                    "10.10.10.2": {
                        "vrf": "None",
                        "local_addr": "10.10.10.2",
                        "local_addr_port": "848",
                        "remote_addr": "3.3.3.3",
                        "remote_addr_port": 848,
                        "fvrf": "None",
                        "ivrf": "None",
                        "version": "1.0.22",
                        "registration": "Registered",
                        "server_ip": "3.3.3.3",
                        "re_register_time_sec": 589,
                        "succeeded_registration_count": 1,
                        "attempted_registration_count": 2,
                        "last_rekey_server": "3.3.3.3",
                        "last_rekey_seq_num": 2,
                        "uncicast_rekey_received": 134,
                        "rekey_acks_sent": 134,
                        "dp_error_monitoring": "OFF",
                        "ipsec_init_reg_executed": 0,
                        "ipsec_init_reg_postponed": 0,
                        "active_tek_num": 2,
                        "sa_track": "disabled",
                        "allowable_rekey_cipher": "ESP",
                    }
                },
                "kek_policy": {
                    "rekey_transport_type": "Unicast",
                    "lifetime": 1650,
                    "encrypt_algorithm": "AES",
                    "key_size": 256,
                    "sig_hash_algorithm": "HMAC_AUTH_SHA512",
                    "sig_key_length": 4400,
                },
                "tek_policy": {
                    "interfaces": {
                        "GigabitEthernet0/0/3": {
                            "ipsec_sa": {
                                "spi": {
                                    "0xBB7AA559(3145377113)": {
                                        "transform": "esp-256-aes esp-sha512-hmac",
                                        "sa_remaining_key_lifetime": 661,
                                        "tag_method": "disabled",
                                        "alg_key_size_bytes": 32,
                                        "sig_key_size_bytes": 64,
                                        "encaps": "ENCAPS_TUNNEL",
                                    },
                                    "0x1190A473(294691955)": {
                                        "transform": "esp-256-aes esp-sha512-hmac",
                                        "sa_remaining_key_lifetime": 36,
                                        "tag_method": "disabled",
                                        "alg_key_size_bytes": 32,
                                        "sig_key_size_bytes": 64,
                                        "encaps": "ENCAPS_TUNNEL",
                                    },
                                }
                            }
                        }
                    }
                },
                "kgs_policy": {"reg_gm": {"local_addr": "10.10.10.2"}},
                "p2p_policy": {"reg_gm": {"local_addr": "10.10.10.2"}},
            }
        }
    }
}

