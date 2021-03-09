expected_output= {
    "interface": {
        "Tunnel13": {
            "origin": "crypto map", 
            "uptime": "6d00h", 
            "outbound_drop": 0, 
            "inbound_pkts_dec": 46, 
            "session_status": "UP-ACTIVE", 
            "phase1_id": "11.0.1.1", 
            "session_id": {
                "0": {
                    "ike_sa_conn_id": {
                        "1002": {
                            "remote": "11.0.1.1/500", 
                            "conn_status": "Active", 
                            "local": "11.0.1.2/500", 
                            "capabilities": "none", 
                            "lifetime": "23:39:38"
                        }, 
                        "1001": {
                            "remote": "11.0.1.1/500", 
                            "conn_status": "Active", 
                            "local": "11.0.1.2/500", 
                            "capabilities": "none", 
                            "lifetime": "23:39:32"
                        }
                    }
                }
            }, 
            "ivrf": "none", 
            "fvrf": "none", 
            "outbound_life_in_kb/sec": "3934761/3544", 
            "outbound_pkts_enc": 36933108, 
            "inbound_drop": 0, 
            "peer": "11.0.1.1", 
            "ipsec_flow": "permit 47 host 11.0.1.2 host 11.0.1.1", 
            "active_sa": 4, 
            "port": "500", 
            "inbound_life_in_kb/sec": "4607999/3544", 
            "desc": "none"
        }
    }
}