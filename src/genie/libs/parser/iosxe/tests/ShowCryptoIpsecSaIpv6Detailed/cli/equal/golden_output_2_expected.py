expected_output = {
    "interfaces": {
        "Tunnel1": {
            "crypto_map_tag": "Tunnel1-head-0",
            "local_addr": "2001:DB8:1201::222",
            "protected_vrf": "(none)",
            "identities": {
                "2001:DB8:1201::222/128/47/0": {
                    "local_ident": "2001:DB8:1201::222/128/47/0",
                    "remote_ident": {
                        "2001:DB8:1101::222/128/47/0": {
                            "remote_ident": "2001:DB8:1101::222/128/47/0",
                            "current_peer": "2001:DB8:1101::222",
                            "port": 500,
                            "permit_flags": [
                                "origin_is_acl",
                                ""
                            ],
                            "pkts_encaps": 53613,
                            "pkts_encrypt": 53613,
                            "pkts_digest": 53613,
                            "pkts_decaps": 53620,
                            "pkts_decrypt": 53620,
                            "pkts_verify": 53620,
                            "local_crypto_endpt": "2001:DB8:1201::222",
                            "remote_crypto_endpt": "2001:DB8:1101::222",
                            "plaintext_mtu": 1446,
                            "path_mtu": 1500,
                            "ipv6_mtu": 1500,
                            "ipv6_mtu_idb": "GigabitEthernet2",
                            "current_outbound_spi": "0xD2882922(3532138786)",
                            "pfs": "Y",
                            "dh_group": "group14",
                            "ake": {
                                "AKE1": "MLKEM1024"
                            },
                            "inbound_esp_sas": {
                                "spi": "0xCEB03EB1(3467656881)",
                                "transform": "esp-256-aes esp-sha256-hmac ",
                                "in_use_settings": [
                                    "Transport",
                                    " "
                                ],
                                "conn_id": 2446,
                                "flow_id": "CSR:446",
                                "sibling_flags": "FFFFFFFF80004009",
                                "crypto_map": "Tunnel1-head-0",
                                "initiator": True,
                                "sa_timing": "remaining key lifetime (k/sec): (4607930/1277)",
                                "iv_size": 16,
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            },
                            "outbound_esp_sas": {
                                "spi": "0xD2882922(3532138786)",
                                "transform": "esp-256-aes esp-sha256-hmac ",
                                "in_use_settings": [
                                    "Transport",
                                    " "
                                ],
                                "conn_id": 2445,
                                "flow_id": "CSR:445",
                                "sibling_flags": "FFFFFFFF80004009",
                                "crypto_map": "Tunnel1-head-0",
                                "initiator": True,
                                "sa_timing": "remaining key lifetime (k/sec): (4607955/1277)",
                                "iv_size": 16,
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            }
                        }
                    }
                }
            }
        }
    }
}