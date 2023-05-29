expected_output={
    "interface": {
        "FiveGigabitEthernet3/0/16": {
            "crypto_map_tag": "FiveGigabitEthernet3/0/16-OSPF-MAP",
            "local_addr": "FE80::B28B:D0FF:FE8D:BA75",
            "ident": {
                1: {
                    "protected_vrf": "none",
                    "local_ident": {
                        "addr": "FE80::",
                        "mask": "10",
                        "prot": "89",
                        "port": "0",
                    },
                    "remote_ident": {
                        "addr": "::",
                        "mask": "0",
                        "prot": "89",
                        "port": "0",
                    },
                    "peer_ip": "FF02::5",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 703,
                    "pkts_encrypt": 703,
                    "pkts_digest": 703,
                    "pkts_decaps": 682,
                    "pkts_decrypt": 682,
                    "pkts_verify": 682,
                    "pkts_compressed": 0,
                    "pkts_decompressed": 0,
                    "pkts_not_compressed": 0,
                    "pkts_compr_failed": 0,
                    "pkts_not_decompressed": 0,
                    "pkts_decompress_failed": 0,
                    "send_errors": 0,
                    "recv_errors": 0,
                    "local_crypto_endpt": "FE80::B28B:D0FF:FE8D:BA75",
                    "remote_crypto_endpt": "FF02::5",
                    "plaintext_mtu": 1470,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "FiveGigabitEthernet3/0/16",
                    "current_outbound_spi": "0x9F8(2552)",
                    "pfs": "N",
                    "dh_group": "none",
                    "inbound_esp_sas": {
                        "spi": {
                            "0x9F8(2552)": {
                                "transform": "esp-3des",
                                "in_use_settings": "Transport, ",
                                "conn_id": 73,
                                "flow_id": "SW",
                                "flow_id_val": 73,
                                "sibling_flags": "FFFFFFFF80000009",
                                "crypto_map": "FiveGigabitEthernet3/0/16-OSPF-MAP",
                                "initiator_flag": "False",
                                "remaining_key_lifetime": "0",
                                "kilobyte_volume_rekey": "disabled",
                                "iv_size": "8 bytes",
                                "replay_detection_support": "N",
                                "status": "ACTIVE(ACTIVE)",
                            }
                        }
                    },
                    "inbound_ah_sas": {},
                    "inbound_pcp_sas": {},
                    "outbound_esp_sas": {
                        "spi": {
                            "0x9F8(2552)": {
                                "transform": "esp-3des",
                                "in_use_settings": "Transport, ",
                                "conn_id": 74,
                                "flow_id": "SW",
                                "flow_id_val": 74,
                                "sibling_flags": "FFFFFFFF80000009",
                                "crypto_map": "FiveGigabitEthernet3/0/16-OSPF-MAP",
                                "initiator_flag": "False",
                                "remaining_key_lifetime": "0",
                                "kilobyte_volume_rekey": "disabled",
                                "iv_size": "8 bytes",
                                "replay_detection_support": "N",
                                "status": "ACTIVE(ACTIVE)",
                            }
                        }
                    },
                    "outbound_ah_sas": {},
                    "outbound_pcp_sas": {},
                }
            },
            "ipsecv6_policy_name": "OSPFv3-2552",
        }
    }
}
