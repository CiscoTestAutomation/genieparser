expected_output={
    "interface": {
        "Tunnel10": {
            "crypto_map_tag": "Tunnel10-head-0",
            "local_addr": "101.1.1.1",
            "ident": {
                1: {
                    "protected_vrf": "none",
                    "local_ident": {
                        "addr": "0.0.0.0",
                        "mask": "0.0.0.0",
                        "prot": "0",
                        "port": "0",
                    },
                    "remote_ident": {
                        "addr": "0.0.0.0",
                        "mask": "0.0.0.0",
                        "prot": "0",
                        "port": "0",
                    },
                    "peer_ip": "101.1.1.2",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 144,
                    "pkts_encrypt": 144,
                    "pkts_digest": 144,
                    "pkts_decaps": 131,
                    "pkts_decrypt": 131,
                    "pkts_verify": 131,
                    "pkts_compressed": 0,
                    "pkts_decompressed": 0,
                    "pkts_not_compressed": 0,
                    "pkts_compr_failed": 0,
                    "pkts_not_decompressed": 0,
                    "pkts_decompress_failed": 0,
                    "send_errors": 0,
                    "recv_errors": 0,
                    "local_crypto_endpt": "101.1.1.1",
                    "remote_crypto_endpt": "101.1.1.2",
                    "plaintext_mtu": 1446,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "FiveGigabitEthernet3/0/15",
                    "current_outbound_spi": "0x6976013A(1769341242)",
                    "pfs": "N",
                    "dh_group": "none",
                    "inbound_esp_sas": {
                        "spi": {
                            "0x76DC8A9A(1994164890)": {
                                "transform": "esp-gcm",
                                "in_use_settings": "Tunnel, ",
                                "conn_id": 2093,
                                "flow_id": "CAT9K",
                                "flow_id_val": 93,
                                "sibling_flags": "FFFFFFFF80000048",
                                "crypto_map": "Tunnel10-head-0",
                                "initiator_flag": "False",
                                "ekey_status": "disabled",
                                "iv_size": "8 bytes",
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)",
                            }
                        }
                    },
                    "inbound_ah_sas": {},
                    "inbound_pcp_sas": {},
                    "outbound_esp_sas": {
                        "spi": {
                            "0x6976013A(1769341242)": {
                                "transform": "esp-gcm",
                                "in_use_settings": "Tunnel, ",
                                "conn_id": 2094,
                                "flow_id": "CAT9K",
                                "flow_id_val": 94,
                                "sibling_flags": "FFFFFFFF80000048",
                                "crypto_map": "Tunnel10-head-0",
                                "initiator_flag": "False",
                                "remaining_key_lifetime": "4 hours, 2 mins",
                                "kilobyte_volume_rekey": "disabled",
                                "iv_size": "8 bytes",
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)",
                            }
                        }
                    },
                    "outbound_ah_sas": {},
                    "outbound_pcp_sas": {},
                }
            },
        }
    }
}
