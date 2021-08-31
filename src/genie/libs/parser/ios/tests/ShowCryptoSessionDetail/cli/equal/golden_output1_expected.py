expected_output= {
    "interface": {
        "Tunnel0": {
            "session_status": "UP-ACTIVE",
            "peer": {
                "10.1.1.3": {
                    "port": {
                        "500": {
                            "fvrf": "none",
                            "ivrf": "none",
                            "desc": "this is my peer at 10",
                            "phase1_id": "10.1.1.3",
                            "ikev1_sa": {
                                "1": {
                                    "local": "10.1.1.4",
                                    "local_port": "500",
                                    "remote": "10.1.1.3",
                                    "remote_port": "500",
                                    "sa_status": "Active",
                                    "conn_id": "3",
                                    "capabilities": "none",
                                    "lifetime": "22:03:24"
                                }
                            },
                            "ipsec_flow": {
                                "permit 47 host 10.1.1.4 host 10.1.1.3": {
                                    "active_sas": 0,
                                    "origin": "crypto map",
                                    "inbound_pkts_decrypted": 0,
                                    "inbound_pkts_drop": 0,
                                    "inbound_life_kb": "0",
                                    "inbound_life_secs": "0",
                                    "outbound_pkts_encrypted": 0,
                                    "outbound_pkts_drop": 0,
                                    "outbound_life_kb": "0",
                                    "outbound_life_secs": "0"
                                },
                                "permit ip host 10.1.1.4 host 10.1.1.3": {
                                    "active_sas": 4,
                                    "origin": "crypto map",
                                    "inbound_pkts_decrypted": 4,
                                    "inbound_pkts_drop": 0,
                                    "inbound_life_kb": "4605665",
                                    "inbound_life_secs": "2949",
                                    "outbound_pkts_encrypted": 4,
                                    "outbound_pkts_drop": 1,
                                    "outbound_life_kb": "4605665",
                                    "outbound_life_secs": "2949"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}