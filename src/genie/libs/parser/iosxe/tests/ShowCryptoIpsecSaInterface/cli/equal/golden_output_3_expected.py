expected_output={
    "interface": {
        "Virtual-Access1": {
            "crypto_map_tag": "Virtual-Access1-head-0",
            "local_addr": "17.17.17.2",
            "ident": {
                1: {
                    "protected_vrf": "none",
                    "local_ident": {
                        "addr": "0.0.0.0",
                        "mask": "0.0.0.0",
                        "prot": "0",
                        "port": "0"
                    },
                    "remote_ident": {
                        "addr": "0.0.0.0",
                        "mask": "0.0.0.0",
                        "prot": "0",
                        "port": "0"
                    },
                    "peer_ip": "27.27.27.2",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 5490,
                    "pkts_encrypt": 5490,
                    "pkts_digest": 5490,
                    "pkts_decaps": 5481,
                    "pkts_decrypt": 5481,
                    "pkts_verify": 5481,
                    "pkts_compressed": 0,
                    "pkts_decompressed": 0,
                    "pkts_not_compressed": 0,
                    "pkts_compr_failed": 0,
                    "pkts_not_decompressed": 0,
                    "pkts_decompress_failed": 0,
                    "send_errors": 0,
                    "recv_errors": 0,
                    "local_crypto_endpt": "17.17.17.2",
                    "remote_crypto_endpt": "27.27.27.2",
                    "plaintext_mtu": 1438,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "GigabitEthernet2",
                    "current_outbound_spi": "0xC5F471E5(3321131493)",
                    "pfs": "Y",
                    "dh_group": "MLKEM512",
                    "inbound_esp_sas": {
                        "spi": {
                            "0x59B12F13(1504784147)": {
                                "transform": "esp-aes",
                                "in_use_settings": "Tunnel, ",
                                "conn_id": 6316,
                                "flow_id": "CSR",
                                "flow_id_val": 4316,
                                "sibling_flags": "FFFFFFFF80004048",
                                "crypto_map": "Virtual-Access1-head-0",
                                "initiator_flag": "True",
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
                            "0xC5F471E5(3321131493)": {
                                "transform": "esp-aes",
                                "in_use_settings": "Tunnel, ",
                                "conn_id": 6315,
                                "flow_id": "CSR",
                                "flow_id_val": 4315,
                                "sibling_flags": "FFFFFFFF80004048",
                                "crypto_map": "Virtual-Access1-head-0",
                                "initiator_flag": "True",
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