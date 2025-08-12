expected_output={
    "interface": {
        "GigabitEthernet0/0/0": {
            "crypto_map_tag": "testtag",
            "local_addr": "17.0.0.2",
            "ident": {
                1: {
                    "protected_vrf": "(none)",
                    "local_ident": {
                        "addr": "15.0.0.5",
                        "mask": "255.255.255.255",
                        "prot": "0",
                        "port": "0"
                    },
                    "remote_ident": {
                        "addr": "14.0.0.6",
                        "mask": "255.255.255.255",
                        "prot": "0",
                        "port": "0"
                    },
                    "peer_ip": "17.0.0.1",
                    "port": 500,
                    "action": "PERMIT",
                    "acl": "origin_is_acl,",
                    "pkts_encaps": 0,
                    "pkts_encrypt": 0,
                    "pkts_digest": 0,
                    "pkts_decaps": 0,
                    "pkts_decrypt": 0,
                    "pkts_verify": 0,
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
                    "local_crypto_endpt": "17.0.0.2",
                    "remote_crypto_endpt": "17.0.0.1",
                    "plaintext_mtu": 1438,
                    "path_mtu": 1500,
                    "ip_mtu": 1500,
                    "ip_mtu_idb": "GigabitEthernet0/0/0",
                    "current_outbound_spi": "0x0(0)",
                    "pfs": "N",
                    "dh_group": "none",
                    "inbound_esp_sas": {},
                    "inbound_ah_sas": {},
                    "inbound_pcp_sas": {},
                    "outbound_esp_sas": {},
                    "outbound_ah_sas": {},
                    "outbound_pcp_sas": {}
                }
            }
        }
    }
}