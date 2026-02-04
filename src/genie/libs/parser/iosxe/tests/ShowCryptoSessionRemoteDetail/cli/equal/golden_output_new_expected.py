expected_output = {
            "interfaces": {
                "Virtual-Access1": {
                    "profile": "IKEV2_PROFILE",
                    "uptime": "00:00:10",
                    "session_status": "UP-ACTIVE",
                    "peer_ip": "27.27.27.2",
                    "peer_port": 500,
                    "fvrf": "none",
                    "ivrf": "none",
                    "phase_id": "27.27.27.2",
                    "session_id": 1,
                    "IKEv2": {
                        "local_ip": "17.17.17.2",
                        "local_port": 500,
                        "remote_ip": "27.27.27.2",
                        "remote_port": 500,
                        "capabilities": "DU",
                        "connid": 1,
                        "lifetime": "00:08:10"
                    },
                    "ipsec_flow": {
                        1: {
                            "flow": "permit ip   0.0.0.0/0.0.0.0 0.0.0.0/0.0.0.0",
                            "active_sa": 2,
                            "origin": "crypto map",
                            "inbound": {
                                "decrypted": 6,
                                "dropped": 0,
                                "life_in_kb": "KB Vol Rekey Disabled",
                                "life_in_sec": 239
                            },
                            "outbound": {
                                "encrypted": 6,
                                "dropped": 0,
                                "life_in_kb": "KB Vol Rekey Disabled",
                                "life_in_sec": 239
                            }
                        }
                    }
                }
            }
        }