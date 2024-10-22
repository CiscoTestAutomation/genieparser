expected_output =  {
    "interface": {
        "Tunnel1": {
            "profile": "CLIV6-IKEV2-PROFILE",
            "session_status": "UP-ACTIVE",
            "peer": {
                "2001:DB8:ACAD:1::2": {
                    "port": {
                        "500": {
                            "ike_sa": {
                                "1": {
                                    "local": "2001:DB8:ACAD:1::1",
                                    "local_port": "500",
                                    "version": "IKEv2",
                                    "session_id": "15",
                                    "remote": "2001:DB8:ACAD:1::2",
                                    "remote_port": "500",
                                    "sa_status": "Active"
                                }
                            },
                            "ipsec_flow": {
                                "permit ipv6 ::/0 ::/0": {
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

