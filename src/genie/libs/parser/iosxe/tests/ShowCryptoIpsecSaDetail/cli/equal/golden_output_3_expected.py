expected_output={
    "interface": {
        "Tunnel1": {
            "crypto_map_tag": "Tunnel1-head-0",
            "local_addr": "100.0.10.2",
            "ident": {
                1: {
                    "protected_vrf": "(none)",
                    "local_ident": {
                        "addr": "100.0.10.2",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "remote_ident": {
                        "addr": "51.51.51.2",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "peer_ip": "51.51.51.2",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 185,
                    "pkts_encrypt": 185,
                    "pkts_digest": 185,
                    "pkts_decaps": 185,
                    "pkts_decrypt": 185,
                    "pkts_verify": 185,
                    "pkts_compressed": 0,
                    "pkts_decompressed": 0,
                    "pkts_not_compressed": 0,
                    "pkts_compr_failed": 0,
                    "pkts_not_decompressed": 0,
                    "pkts_decompress_failed": 0,
                    "pkts_no_sa_send": 0,
                    "pkts_invalid_sa_rcv": 0,
                    "pkts_invalid_prot_recv": 0,
                    "pkts_verify_failed": 0,
                    "pkts_invalid_identity_recv": 0,
                    "pkts_replay_rollover_send": 0,
                    "pkts_replay_rollover_rcv": 0,
                    "pkts_replay_failed_rcv": 0,
                    "pkts_tagged_send": 0,
                    "pkts_untagged_rcv": 0,
                    "pkts_not_tagged_send": 0,
                    "pkts_not_untagged_rcv": 0,
                    "pkts_internal_err_send": 0,
                    "pkts_internal_err_recv": 0,
                    "local_crypto_endpt": "100.0.10.2",
                    "remote_crypto_endpt": "51.51.51.2",
                    "plaintext_mtu": 1458,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "GigabitEthernet2",
                    "current_outbound_spi": "0xF2FAF9F4(4076534260)",
                    "pfs": "Y",
                    "dh_group": "group14",
                    "ake": {
                        "AKE1": "MLKEM1024"
                    },
                    "inbound_esp_sas": {
                        "spi": {
                            "0x25AD4F0C(632114956)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "(4607999/101)",
                                "iv_size": "16 bytes",
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            }
                        }
                    },
                    "inbound_ah_sas": {},
                    "inbound_pcp_sas": {},
                    "outbound_esp_sas": {
                        "spi": {
                            "0xF2FAF9F4(4076534260)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "(4607999/101)",
                                "iv_size": "16 bytes",
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            }
                        }
                    },
                    "outbound_ah_sas": {},
                    "outbound_pcp_sas": {}
                },
                2: {
                    "protected_vrf": "(none)",
                    "local_ident": {
                        "addr": "100.0.10.2",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "remote_ident": {
                        "addr": "50.50.50.2",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "peer_ip": "50.50.50.2",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 194056,
                    "pkts_encrypt": 194056,
                    "pkts_digest": 194056,
                    "pkts_decaps": 371974,
                    "pkts_decrypt": 371974,
                    "pkts_verify": 371974,
                    "pkts_compressed": 0,
                    "pkts_decompressed": 0,
                    "pkts_not_compressed": 0,
                    "pkts_compr_failed": 0,
                    "pkts_not_decompressed": 0,
                    "pkts_decompress_failed": 0,
                    "pkts_no_sa_send": 0,
                    "pkts_invalid_sa_rcv": 0,
                    "pkts_invalid_prot_recv": 0,
                    "pkts_verify_failed": 0,
                    "pkts_invalid_identity_recv": 0,
                    "pkts_replay_rollover_send": 0,
                    "pkts_replay_rollover_rcv": 0,
                    "pkts_replay_failed_rcv": 0,
                    "pkts_tagged_send": 0,
                    "pkts_untagged_rcv": 0,
                    "pkts_not_tagged_send": 0,
                    "pkts_not_untagged_rcv": 0,
                    "pkts_internal_err_send": 0,
                    "pkts_internal_err_recv": 0,
                    "local_crypto_endpt": "100.0.10.2",
                    "remote_crypto_endpt": "50.50.50.2",
                    "plaintext_mtu": 1458,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "GigabitEthernet2",
                    "current_outbound_spi": "0xF03F6B9(251918009)",
                    "pfs": "Y",
                    "dh_group": "group14",
                    "ake": {
                        "AKE1": "MLKEM1024"
                    },
                    "inbound_esp_sas": {
                        "spi": {
                            "0x3556D99C(894884252)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "(4607999/98)",
                                "iv_size": "16 bytes",
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            }
                        }
                    },
                    "inbound_ah_sas": {},
                    "inbound_pcp_sas": {},
                    "outbound_esp_sas": {
                        "spi": {
                            "0xF03F6B9(251918009)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "(4607999/98)",
                                "iv_size": "16 bytes",
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            }
                        }
                    },
                    "outbound_ah_sas": {},
                    "outbound_pcp_sas": {}
                }
            }
        }
    }
}