expected_output={
    "interface": {
        "Tunnel1": {
            "crypto_map_tag": "Tunnel1-head-0",
            "local_addr": "11.0.10.131",
            "ident": {
                1: {
                    "protected_vrf": "(none)",
                    "local_ident": {
                        "addr": "11.0.10.131",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "remote_ident": {
                        "addr": "22.51.51.123",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "peer_ip": "22.51.51.123",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 410,
                    "pkts_encrypt": 410,
                    "pkts_digest": 410,
                    "pkts_decaps": 349,
                    "pkts_decrypt": 349,
                    "pkts_verify": 349,
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
                    "local_crypto_endpt": "11.0.10.131",
                    "remote_crypto_endpt": "22.51.51.123",
                    "plaintext_mtu": 1458,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "TenGigabitEthernet0/0/1",
                    "current_outbound_spi": "0x746D481C(1953318940)",
                    "pfs": "Y",
                    "dh_group": "none",
                    "pqc": "ML-KEM-1024",
                    "inbound_esp_sas": {
                        "spi": {
                            "0xAF2C1743(2938902339)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "94",
                                "kilobyte_volume_rekey": "disabled",
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
                            "0x746D481C(1953318940)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "94",
                                "kilobyte_volume_rekey": "disabled",
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
                        "addr": "11.0.10.131",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "remote_ident": {
                        "addr": "21.50.50.122",
                        "mask": "255.255.255.255",
                        "prot": "47",
                        "port": "0"
                    },
                    "peer_ip": "21.50.50.122",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 39798,
                    "pkts_encrypt": 39798,
                    "pkts_digest": 39798,
                    "pkts_decaps": 76359,
                    "pkts_decrypt": 76359,
                    "pkts_verify": 76359,
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
                    "local_crypto_endpt": "11.0.10.131",
                    "remote_crypto_endpt": "21.50.50.122",
                    "plaintext_mtu": 1458,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "TenGigabitEthernet0/0/1",
                    "current_outbound_spi": "0x31CA189(52208009)",
                    "pfs": "Y",
                    "dh_group": "none",
                    "pqc": "ML-KEM-1024",
                    "inbound_esp_sas": {
                        "spi": {
                            "0xD3345E5F(3543424607)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "100",
                                "kilobyte_volume_rekey": "disabled",
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
                            "0x31CA189(52208009)": {
                                "transform": "esp-256-aes esp-sha256-hmac",
                                "in_use_settings": "Transport, ",
                                "remaining_key_lifetime": "100",
                                "kilobyte_volume_rekey": "disabled",
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