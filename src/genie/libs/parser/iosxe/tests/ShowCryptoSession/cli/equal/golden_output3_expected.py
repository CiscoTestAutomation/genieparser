expected_output= {
    "interface": {
        "1": {
            "interface": "Tunnel3111",
            "peer": {
                "192.168.1.1": {
                    "port": {
                        "500": {
                            "ipsec_flow": {
                                "permit ip 100.75.0.0/255.255.255.192 192.168.25.0/255.255.255.0": {
                                    "active_sas": 0,
                                    "origin": "crypto map"
                                },
                                "permit ip 100.75.0.0/255.255.255.192 192.168.25.0/255.255.255.128": {
                                    "active_sas": 0,
                                    "origin": "crypto map"
                                },
                                "permit ip 100.75.0.0/255.255.255.192 192.168.26.0/255.255.255.0": {
                                    "active_sas": 0,
                                    "origin": "crypto map"
                                },
                                "permit ip host 100.74.10.1 192.168.25.0/255.255.255.0": {
                                    "active_sas": 0,
                                    "origin": "crypto map"
                                },
                                "permit ip host 100.74.10.1 192.168.25.0/255.255.255.128": {
                                    "active_sas": 0,
                                    "origin": "crypto map"
                                },
                                "permit ip host 100.74.10.1 192.168.26.0/255.255.255.0": {
                                    "active_sas": 0,
                                    "origin": "crypto map"
                                }
                            }
                        }
                    }
                }
            },
            "session_status": "DOWN"
        },
        "2": {
            "interface": "Tunnel3111",
            "peer": {
                "192.168.1.1": {
                    "port": {
                        "500": {
                            "ike_sa": {
                                "1": {
                                    "local": "94.140.184.80",
                                    "local_port": "500",
                                    "remote": "192.168.1.1",
                                    "remote_port": "500",
                                    "sa_status": "Inactive",
                                    "session_id": "0",
                                    "version": "IKEv1"
                                },
                                "2": {
                                    "local": "94.140.184.80",
                                    "local_port": "500",
                                    "remote": "192.168.1.1",
                                    "remote_port": "500",
                                    "sa_status": "Inactive",
                                    "session_id": "0",
                                    "version": "IKEv1"
                                }
                            }
                        }
                    }
                }
            },
            "profile": "ISAKMP-inner-LOC_A",
            "session_status": "DOWN-NEGOTIATING"
        }
    }
}