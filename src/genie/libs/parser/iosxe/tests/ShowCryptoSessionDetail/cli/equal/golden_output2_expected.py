expected_output= {
    "interface": {
        "Tunnel0": {
            "profile": "polaris-test",
            "uptime": "00:27:42",
            "session_status": "UP-ACTIVE",
            "peer": {
                "1.1.1.1": {
                    "port": {
                        "500": {
                            "fvrf": "myf-vrf",
                            "ivrf": "myi-vrf",
                            "phase1_id": "polaris-test.polaris-test",
                            "desc": "none",
                            "ike_sa": {
                                "1": {
                                    "local": "2.2.2.2",
                                    "local_port": "500",
                                    "remote": "1.1.1.1",
                                    "remote_port": "500",
                                    "sa_status": "Active",
                                    "version": "IKEv2",
                                    "session_id": "3",
                                    "conn_id": "1",
                                    "capabilities": "U",
                                    "lifetime": "23:32:18"
                                }
                            },
                            "ipsec_flow": {
                                "permit 47 host 2.2.2.2 host 1.1.1.1": {
                                    "active_sas": 2,
                                    "origin": "crypto map",
                                    "inbound_pkts_decrypted": 0,
                                    "inbound_pkts_drop": 0,
                                    "inbound_life_kb": "4319919",
                                    "inbound_life_secs": "1937",
                                    "outbound_pkts_encrypted": 0,
                                    "outbound_pkts_drop": 0,
                                    "outbound_life_kb": "4319919",
                                    "outbound_life_secs": "1937"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}