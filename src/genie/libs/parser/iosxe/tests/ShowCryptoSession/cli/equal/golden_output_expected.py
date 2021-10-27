expected_output= {
    "interface": {
        "Tunnel13": {
            "session_status": "UP-ACTIVE",
            "peer": {
                "11.0.1.1": {
                    "port": {
                        "500": {
                            "ike_sa": {
                                "1": {
                                    "local": "11.0.1.2",
                                    "local_port": "500",
                                    "remote": "11.0.1.1",
                                    "remote_port": "500",
                                    "sa_status": "Active",
                                    "session_id": "0",
                                    "version": "IKEv1"
                                }
                            },
                            "ipsec_flow": {
                                "permit 47 host 11.0.1.2 host 11.0.1.1": {
                                    "active_sas": 2,
                                    "origin": "crypto map"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}