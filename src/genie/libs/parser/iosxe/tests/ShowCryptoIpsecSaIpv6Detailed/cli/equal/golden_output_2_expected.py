expected_output = {
    "interfaces": {
        "Tunnel1": {
            "crypto_map_tag": "Tunnel1-head-0",
            "local_addr": "2001:DB8:1101::131",
            "protected_vrf": "(none)",
            "identities": {
                "2001:DB8:1101::131/128/47/0": {
                    "local_ident": "2001:DB8:1101::131/128/47/0",
                    "remote_ident": {
                        "2001:DB8:1202::123/128/47/0": {
                            "remote_ident": "2001:DB8:1202::123/128/47/0",
                            "current_peer": "2001:DB8:1202::123",
                            "port": 500,
                            "permit_flags": [
                                "origin_is_acl",
                                ""
                            ],
                            "pkts_encaps": 196,
                            "pkts_encrypt": 196,
                            "pkts_digest": 196,
                            "pkts_decaps": 196,
                            "pkts_decrypt": 196,
                            "pkts_verify": 196,
                            "local_crypto_endpt": "2001:DB8:1101::131",
                            "remote_crypto_endpt": "2001:DB8:1202::123",
                            "plaintext_mtu": 1446,
                            "path_mtu": 1500,
                            "ipv6_mtu": 1500,
                            "ipv6_mtu_idb": "TenGigabitEthernet0/0/1",
                            "current_outbound_spi": "0x6064CAD7(1617218263)",
                            "pfs": "Y",
                            "dh_group": "none",
                            "pqc": "ML-KEM-1024",
                            "inbound_esp_sas": {
                                "spi": "0x7D6FAAB9(2104470201)",
                                "transform": "esp-256-aes esp-sha256-hmac ",
                                "in_use_settings": [
                                    "Transport",
                                    " "
                                ],
                                "conn_id": 2063,
                                "flow_id": "HW:63",
                                "sibling_flags": "FFFFFFFF80000009",
                                "crypto_map": "Tunnel1-head-0",
                                "initiator": False,
                                "sa_timing": "remaining key lifetime (sec): 148",
                                "iv_size": 16,
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            },
                            "outbound_esp_sas": {
                                "spi": "0x6064CAD7(1617218263)",
                                "transform": "esp-256-aes esp-sha256-hmac ",
                                "in_use_settings": [
                                    "Transport",
                                    " "
                                ],
                                "conn_id": 2064,
                                "flow_id": "HW:64",
                                "sibling_flags": "FFFFFFFF80000009",
                                "crypto_map": "Tunnel1-head-0",
                                "initiator": False,
                                "sa_timing": "remaining key lifetime (sec): 148",
                                "iv_size": 16,
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            }
                        },
                        "2001:DB8:1201::122/128/47/0": {
                            "remote_ident": "2001:DB8:1201::122/128/47/0",
                            "current_peer": "2001:DB8:1201::122",
                            "port": 500,
                            "permit_flags": [
                                "origin_is_acl",
                                ""
                            ],
                            "pkts_encaps": 51402,
                            "pkts_encrypt": 51402,
                            "pkts_digest": 51402,
                            "pkts_decaps": 51442,
                            "pkts_decrypt": 51442,
                            "pkts_verify": 51442,
                            "local_crypto_endpt": "2001:DB8:1101::131",
                            "remote_crypto_endpt": "2001:DB8:1201::122",
                            "plaintext_mtu": 1446,
                            "path_mtu": 1500,
                            "ipv6_mtu": 1500,
                            "ipv6_mtu_idb": "TenGigabitEthernet0/0/1",
                            "current_outbound_spi": "0x3F4B6DE0(1061907936)",
                            "pfs": "Y",
                            "dh_group": "none",
                            "pqc": "ML-KEM-1024",
                            "inbound_esp_sas": {
                                "spi": "0x6236E68(102985320)",
                                "transform": "esp-256-aes esp-sha256-hmac ",
                                "in_use_settings": [
                                    "Transport",
                                    " "
                                ],
                                "conn_id": 2061,
                                "flow_id": "HW:61",
                                "sibling_flags": "FFFFFFFF80000009",
                                "crypto_map": "Tunnel1-head-0",
                                "initiator": False,
                                "sa_timing": "remaining key lifetime (sec): 117",
                                "iv_size": 16,
                                "replay_detection_support": "Y",
                                "status": "ACTIVE(ACTIVE)"
                            },
                            "outbound_esp_sas": {
                                "spi": "0x3F4B6DE0(1061907936)",
                                "transform": "esp-256-aes esp-sha256-hmac ",
                                "in_use_settings": [
                                    "Transport",
                                    " "
                                ],
                                "conn_id": 2062,
                                "flow_id": "HW:62",
                                "sibling_flags": "FFFFFFFF80000009",
                                "crypto_map": "Tunnel1-head-0",
                                "initiator": False,
                                "sa_timing": "remaining key lifetime (sec): 117",
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