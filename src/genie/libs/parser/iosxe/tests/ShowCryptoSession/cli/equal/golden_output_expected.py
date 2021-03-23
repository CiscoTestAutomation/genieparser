expected_output= {
    "interface": {
        "Tunnel13": {
            "profile": "GS-GRE:ISAKMP", 
            "peer": {
                "11.0.2.1": {
                    "port": {
                        "500": {
                            "phase1_id": "11.0.2.1", 
                            "fvrf": "none", 
                            "ikev1_sa": {
                                "1": {
                                    "remote": "11.0.2.1", 
                                    "remote_port": "500", 
                                    "local": "11.0.2.2", 
                                    "local_port": "500", 
                                    "conn_id": "1042", 
                                    "session_id": "0", 
                                    "capabilities": "D", 
                                    "lifetime": "05:50:03", 
                                    "sa_status": "Active"
                                }
                            }, 
                            "ipsec_flow": {
                                "permit 47 host 11.0.2.2 host 11.0.2.1 ": {
                                    "origin": "crypto map", 
                                    "outbound_pkts_drop": 0, 
                                    "inbound_pkts_drop": 0, 
                                    "outbound_pkts_encrypted": 772730, 
                                    "active_sas": 2, 
                                    "outbound_life_secs": "3060", 
                                    "inbound_life_secs": "3060", 
                                    "inbound_pkts_decrypted": 449282, 
                                    "inbound_life_kb": "KB Vol Rekey Disabled", 
                                    "outbound_life_kb": "KB Vol Rekey Disabled"
                                }
                            }, 
                            "ivrf": "none", 
                            "desc": "none"
                        }
                    }
                }
            }, 
            "uptime": "3d18h", 
            "session_status": "UP-ACTIVE"
        }
    }
}