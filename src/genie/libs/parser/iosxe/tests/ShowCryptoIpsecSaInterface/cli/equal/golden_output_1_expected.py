expected_output={
    "interface": {
        "FiveGigabitEthernet3/0/15": {
            "crypto_map_tag": "FiveGigabitEthernet3/0/15-OSPF-MAP",
            "local_addr": "FE80::B28B:D0FF:FE8D:BA49",
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
                    "pkts_encaps": 4312,
                    "pkts_encrypt": 4312,
                    "pkts_digest": 4312,
                    "pkts_decaps": 4291,
                    "pkts_decrypt": 4291,
                    "pkts_verify": 4291,
                    "pkts_compressed": 0,
                    "pkts_decompressed": 0,
                    "pkts_not_compressed": 0,
                    "pkts_compr_failed": 0,
                    "pkts_not_decompressed": 0,
                    "pkts_decompress_failed": 0,
                    "send_errors": 0,
                    "recv_errors": 0,
                    "local_crypto_endpt": "FE80::B28B:D0FF:FE8D:BA49",
                    "remote_crypto_endpt": "FF02::5",
                    "plaintext_mtu": 1476,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "FiveGigabitEthernet3/0/15",
                    "current_outbound_spi": "0x100(256)",
                    "pfs": "N",
                    "dh_group": "none",
                    "inbound_esp_sas": {},
                    "inbound_ah_sas": {
                        "spi": {
                            "0x100(256)": {
                                "transform": "ah-md5-hmac",
                                "in_use_settings": "Transport, ",
                                "conn_id": 71,
                                "flow_id": "SW",
                                "flow_id_val": 71,
                                "sibling_flags": "FFFFFFFF80000019",
                                "crypto_map": "FiveGigabitEthernet3/0/15-OSPF-MAP",
                                "initiator_flag": "False",
                                "remaining_key_lifetime": "0",
                                "kilobyte_volume_rekey": "disabled",
                                "replay_detection_support": "N",
                                "status": "ACTIVE(ACTIVE)",
                            }
                        }
                    },
                    "inbound_pcp_sas": {},
                    "outbound_esp_sas": {},
                    "outbound_ah_sas": {
                        "spi": {
                            "0x100(256)": {
                                "transform": "ah-md5-hmac",
                                "in_use_settings": "Transport, ",
                                "conn_id": 72,
                                "flow_id": "SW",
                                "flow_id_val": 72,
                                "sibling_flags": "FFFFFFFF80000019",
                                "crypto_map": "FiveGigabitEthernet3/0/15-OSPF-MAP",
                                "initiator_flag": "False",
                                "remaining_key_lifetime": "0",
                                "kilobyte_volume_rekey": "disabled",
                                "replay_detection_support": "N",
                                "status": "ACTIVE(ACTIVE)",
                            }
                        }
                    },
                    "outbound_pcp_sas": {},
                }
            },
            "ipsecv6_policy_name": "OSPFv3-256",
        }
    }
}
